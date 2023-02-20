function Head() {
  return (
    <>
      <ol className="breadcrumb page-breadcrumb">
        <li className="breadcrumb-item">
          <a href="javascript:void(0);"> Home </a>
        </li>
        <li className="breadcrumb-item active"> MyCoinMarket Dashboard </li>
        <li className="position-absolute pos-top pos-right d-none d-sm-block">
          
          <span className="js-get-date"> </span>
        </li>
      </ol>
      <div className="subheader">
        <h1 className="subheader-title">
          <i className="subheader-icon fa fa-chart-area"> </i>MyCoinMarket<span className="fw-300"> Dashboard</span>
        </h1>
      </div>
    </>
  );
}

export default Head;
