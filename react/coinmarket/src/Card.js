function Card() {
  return (
    <>
      <div className="row">
        <div className="col-sm-6 col-xl-3">
          <div className="p-3 bg-primary-300 rounded overflow-hidden position-relative text-white mb-g">
            <div className="">
              <h3 className="display-4 d-block l-h-n m-0 fw-500">
                <p id=""> 100 </p>
                <small className="m-0 l-h-n"> Total Cryptocurrency Found </small>
              </h3>
            </div>
            <i className="fa fa-user position-absolute pos-right pos-bottom opacity-15 mb-n1 mr-n1">
              
            </i>
          </div>
        </div>
      </div>
    </>
  );
}

export default Card;
