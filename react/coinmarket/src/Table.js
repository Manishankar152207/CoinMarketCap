import "./App.css";
// import Card from "./Card.js";
import { useEffect } from "react";
import { useState } from "react";
import axios from 'axios';
import "bootstrap/dist/css/bootstrap.min.css";

function Table() {
  const [data, setData] = useState([]);

  useEffect(() => {
      const fetchData = async () => {
      const result = await axios("http://127.0.0.1:8000/marketfeed/");

      setData(result.data);
      };
      setInterval(fetchData, 3000);
  }, []);
  return (
    <>
    <div className="row">
        <div className="col-sm-6 col-xl-3">
          <div className="p-3 bg-primary-300 rounded overflow-hidden position-relative text-white mb-g">
            <div className="">
              <h3 className="display-4 d-block l-h-n m-0 fw-500">
                <p id=""> {data.length} </p>
                <small className="m-0 l-h-n"> Total Cryptocurrency Recieved </small>
              </h3>
            </div>
            <i className="fa fa-user position-absolute pos-right pos-bottom opacity-15 mb-n1 mr-n1">
              
            </i>
          </div>
        </div>
      </div>
      <div className="row">
        <div className="col-lg-12">
          <div className="panel-container show">
            <div className="panel-content">
              <table
                id=""
                className="table table-bordered table-hover table-striped w-100"
              >
                <thead className="bg-warning-200">
                  <tr>
                    <th>ID</th>
                    <th>Symbol</th>
                    <th>Price</th>
                    <th>1h%</th>
                    <th>24h%</th>
                    <th>7d%</th>
                    <th>Market Cap</th>
                    <th>Volume(24h)</th>
                    <th>Circulating Supply</th>
                  </tr>
                </thead>
                <tbody>
                  {data.map((list) => (
                    <tr key={list.id}>
                      <td> {list.id} </td>
                      <td> {list.symbol} </td>
                      <td> {list.price} </td>
                      <td> {list.onehrper} </td>
                      <td> {list.twentyfourhrper} </td>
                      <td> {list.sevendayper} </td>
                      <td> {list.marketcap} </td>
                      <td> {list.volume24h} </td>
                      <td> {list.circulatingsupply} </td>
                      {/* <td> {list.volume24h1} </td> */}
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
          </div>
        </div>
      </div>
    </>
  );
}
// setInterval(Table, 60000);
export default Table;
