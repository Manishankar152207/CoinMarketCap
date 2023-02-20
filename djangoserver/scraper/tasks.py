from __future__ import absolute_import, unicode_literals
from celery import shared_task
from datetime import datetime
from time import sleep
import os
from unittest import result
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from fake_useragent import UserAgent
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (NoSuchElementException,ElementClickInterceptedException,ElementNotInteractableException)
import json
import ast
from bs4 import BeautifulSoup
from api.models import MarketFeed
from api.serializers import MarketFeedSerializer
import redis
from contextlib import contextmanager

# @shared_task(name = "print_time")
# def print_time():
#     now = datetime.now()
#     current_time = now.strftime("%H:%M:%S")
#     print(f"Current Time is {current_time}")


redis_client = redis.Redis(host='localhost', port=6379)


@contextmanager
def redis_lock(lock_name):
    """Yield 1 if specified lock_name is not already set in redis. Otherwise returns 0.

    Enables sort of lock functionality.
    """
    status = redis_client.set(lock_name, 'lock', nx=True)
    try:
        yield status
    finally:
        redis_client.delete(lock_name)


@shared_task(name="scraper_bot")
def scraper_bot():
    with redis_lock('my_lock_name') as acquired:
        my_scraper.delay()

@shared_task(name="my_scraper_fn")
def my_scraper():
    Options = webdriver.ChromeOptions()
    Options.add_argument("--headless")
    Options.add_argument("--no-sandbox")
    Options.add_argument("--disable-extensions")
    Options.add_experimental_option('excludeSwitches', ['enable-logging'])
    Options.add_argument("--disable-dev-shm-usage")
    Options.add_argument("--window-size=1920x1080")
    Options.add_argument("start-maximised")
    s = Service(ChromeDriverManager().install())
    try:
        while(True):
            driver = webdriver.Chrome(service=s, options=Options)
            driver.get('https://coinmarketcap.com/')
            driver.maximize_window()
            try:
                WebDriverWait(driver,20).until(EC.presence_of_element_located((By.CLASS_NAME, "sc-f7a61dda-3")))
            except:
                driver.quit()
                return "Something went wrong. Please try again."
            else:
                sleep(2)
                last_height = driver.execute_script("return document.body.scrollHeight")
                current_height = 1750
                result = []
                while(True):
                    driver.execute_script('''
                        window.scrollTo(0, '''+str(current_height)+''')
                    ''')
                    sleep(.2)                    
                    if current_height == 8750:
                        content = driver.page_source
                        soup = BeautifulSoup(content, "html.parser")
                        trlist = soup.find("table").find("tbody").find_all("tr")
                        for tr in trlist:
                            resultSet = {}
                            tdlist = tr.find_all("td")
                            if tdlist[1].text != '':
                                resultSet["id"] = tdlist[1].text 
                                resultSet["symbol"] = tdlist[2].text 
                                resultSet["price"] = tdlist[3].text 
                                resultSet["onehrper"] = tdlist[4].text 
                                resultSet["twentyfourhrper"] = tdlist[5].text 
                                resultSet["sevendayper"] = tdlist[6].text 
                                resultSet["marketcap"] = tdlist[7].find("span" , attrs={"class":"sc-edc9a476-1"}).text 
                                resultSet["volume24h"] = tdlist[8].find("p", attrs={"class":"gLNGkf"}).text
                                resultSet["volume24h1"] = tdlist[8].find("p", attrs={"class":"hHLLiH"}).text
                                resultSet["circulatingsupply"] = tdlist[9].text 
                            result.append(resultSet)
                        save_data(result)
                    if current_height + 1750 <= last_height:
                        current_height = current_height + 1750 
                    else:
                        current_height = 1750
                        break 
                driver.quit()
    except Exception as e:
        print(e)
        driver.quit()
        print("Something went wrong. Please check.")

def save_data(data):
    try:
        for item in data:
            # import ipdb;ipdb.set_trace()
            ins = MarketFeed.objects.filter(id=item["id"]).last()
            if ins:
                id = item.pop("id")
                update(ins, item)
            else:
                serializer = MarketFeedSerializer(data=item)
                serializer.is_valid(raise_exception=True)
                MarketFeed.objects.create(serializer.data)
    except:
        print("Something went wrong while saving data.")
    else:
        print("Data saved successfully.")

def update(instance, validated_data):
    instance.price = validated_data.get('price',instance.price)
    instance.onehrper = validated_data.get('onehrper', instance.onehrper)
    instance.twentyfourhrper = validated_data.get('twentyfourhrper', instance.twentyfourhrper)
    instance.sevendayper = validated_data.get('sevendayper',instance.sevendayper)
    instance.marketcap = validated_data.get('marketcap', instance.marketcap)
    instance.volume24h = validated_data.get('volume24h', instance.volume24h)
    instance.volume24h1 = validated_data.get('volume24h1',instance.volume24h1)
    instance.circulatingsupply = validated_data.get('circulatingsupply', instance.circulatingsupply)
    instance.save()
    return instance

  
