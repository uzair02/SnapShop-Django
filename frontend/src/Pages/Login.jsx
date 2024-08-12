import React, { useContext } from 'react';
import AuthContext from '../context/AuthContext'
import { Link } from 'react-router-dom'




const Login = () => {

  const {loginUser} = useContext(AuthContext)
  const handleSubmit = e => {
    e.preventDefault()
    const email = e.target.email.value
    const password = e.target.password.value

    email.length > 0 && loginUser(email, password)

    console.log(email)
    console.log(password)
   
  }
  return (
    <div className="container mt-4">
      <div className='col-md-9 card mx-auto d-flex flex-row px-0'>
        <div className="img-left d-md-flex d-none"></div>
        <div className="card-body d-flex flex-column justify-content-center">
          <h4 className="title text-center mt-4 pb-3">Login into account</h4>
          <form className='col-sm-10 col-12 mx-auto' onSubmit={handleSubmit}>
            <div className='form-group'>
              <input type="email" className="form-control" placeholder='Enter Email' name='email' />
            </div>
            <div className='form-group py-3'>
              <input type="password" className="form-control" placeholder='********' name='password' />
            </div>
            <div>
              <input type="submit" className="btn btn-outline-danger d-block w-100" />
            </div>
            <p className="mt-3 mb-4 pb-lg-2" style={{ color: "#393f81" }}>
              Don't have an account?{" "}
              <Link to="/register" style={{ color: "#393f81" }}>
                Register Now 
              </Link>
            </p>
            <a href="#!" className="small text-muted">
              Terms of use.
            </a>
            <a href="#!" className="small text-muted">
              Privacy policy
            </a>
            {/* {error && <p className="text-danger mt-2">{error}</p>} */}
          </form>
        </div>
      </div>
    </div>
  );
};

export default Login;
