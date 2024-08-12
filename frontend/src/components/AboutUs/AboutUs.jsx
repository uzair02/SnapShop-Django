import React from 'react'
import image from '../Assets/Image.png'
import Image1 from '../Assets/Image1.png'
import image3 from '../Assets/image3.png'
import image4 from '../Assets/image4.png'
import image5 from '../Assets/image5.png'
import image6 from '../Assets/image6.png'
import Skeleton from "react-loading-skeleton";
import "react-loading-skeleton/dist/skeleton.css";
import "../../Pages/login.css";

const AboutUs = () => {
  return (
    <div >
              <div className="container my-3 py-3">
                <div className="row">
                  <div className="col-12">
                  <h2 className="display-7 text-center text-2xl font-weight-bolder">How it Works?</h2>
                    <hr />
                  </div>
                </div>
              </div>

            <div className="container my-3 py-3">
            <div className="row">
              
              <div className="col-md-4 col-sm-6 col-xs-8 col-12 mb-10">
                <div className="card text-center h-100">
                  <img className="card-img-top p-3" src={image} alt="Card" height={300}  />
                  <ul className="list-group list-group-flush">
                    <li className="list-group-item lead"></li>
                  </ul>
                  <div className="card-body fw-bold my-0 pm-0">
                    Step 1
                    <p className="fw-normal">Find the product you want. Upload a picture or type in the name to get started.</p>
                  </div>
                </div>
              </div>


              <div className="col-md-4 col-sm-6 col-xs-8 col-12 mb-10">
                <div className="card text-center h-100">
                  <img className="card-img-top p-3" src={image3} alt="Card" height={300} />
                  <ul className="list-group list-group-flush">
                    <li className="list-group-item lead"></li>
                  </ul>
                  <div className="card-body fw-bold my-0 pm-0">
                    Step 2
                    <p className="fw-normal">  Compare prices and select the best option. We'll redirect you to the e-commerce website to
                        complete your purchase.</p>
                  </div>
                </div>
              </div>


              <div className="col-md-4 col-sm-6 col-xs-8 col-12 mb-10">
                <div className="card text-center h-100">
                  <img className="card-img-top p-3" src={image4} alt="Card" height={300} />
                  <ul className="list-group list-group-flush">
                    <li className="list-group-item lead"></li>
                  </ul>
                  <div className="card-body fw-bold my-0 pm-0">
                    Step 3
                    <p className="fw-normal"> Complete your purchase. Enjoy your new product!</p>
                  </div>
                </div>
              </div>
            </div>
            </div>

          
            <div className="container my-3 py-3">
                <div className="row">
                  <div className="col-12">
                  <h2 className="display-7 text-center text-2xl font-weight-bolder">Work with SnapShop</h2>
                    <hr />
                  </div>
                </div>
              </div>

          <div className="container">
              <div className="row py-3 g-3 align-items-center">
                  <div className="col-md-6 d-flex justify-content-center">
                      <img src={Image1} alt="" class="img-fluid w-50"/>
                  </div>
                  <div className="col-md-6 d-flex flex-column align-items-end">
                      <div className="w-50">
                          <h2 className="display-7 fw-bolder mb-3">
                              As a Partner
                          </h2>
                          <p>
                              Earn money by partnering with SnapShop.
                              Help users find the best deals and earn commissions.
                          </p>
                          <button className="btn btn-dark mt-3 px-4 py-2  w-10">Partner with Us</button>
                      </div>
                  </div>

                  <div className="col-12 border-top border-2"></div>

                  <div className="col-md-6 d-flex justify-content-center">
                      <img src={image5} alt="" className="img-fluid w-50"/>
                  </div>
                  <div className="col-md-6 d-flex flex-column align-items-end">
                      <div className="w-50">
                          <h2 className="display-7 fw-bolder mb-3">
                            As a retailer
                          </h2>
                          <p>
                          SnapShop helps retailers
                          reach more customers with our platform.
                          Increase your sales and visibility.
                          </p>
                          <button className="btn btn-dark mt-3 px-4 py-2  w-10">Sell with Us</button>
                      </div>
                  </div>

                  <div className="col-12 border-top border-2"></div>

                  <div className="col-md-6 d-flex justify-content-center">
                      <img src={image6} alt="" className="img-fluid w-50"/>
                  </div>
                  <div className="col-md-6 d-flex flex-column align-items-end">
                      <div className="w-50">
                          <h2 className="display-7 fw-bolder mb-3">
                            As a Colleague
                          </h2>
                          <p>
                          Join our team and be part of
                          an innovative company that's
                          revolutionizing online shopping.
                          </p>
                          <button className="btn btn-dark mt-3 px-4 py-2  w-10">Work with Us</button>
                      </div>
                  </div>

                  <div className="col-12 border-top border-2"></div>
              </div>
          </div>
    </div>
  )
}

export default AboutUs
