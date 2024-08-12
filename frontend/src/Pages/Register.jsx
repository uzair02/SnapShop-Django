import React, { useState, useContext } from 'react';
import { Link } from 'react-router-dom';
import AuthContext from '../context/AuthContext';


const Register = () => {

  const [email, setEmail] = useState("")
  const [username, setUsername] = useState("")
  const [password, setPassword] = useState("")
  const [password2, setPassword2] = useState("")

  const {registerUser} = useContext(AuthContext)

  console.log(email);
  console.log(username);
  console.log(password);
  console.log(password2);


  const handleSubmit = async e => {
    e.preventDefault()
    registerUser(email, username, password, password2)
  }
  

  return (
    <div className="container mt-4">
      <div className='col-md-9 card mx-auto d-flex flex-row px-0'>
        <div className="img-left d-md-flex d-none"></div>
        <div className="card-body d-flex flex-column justify-content-center">
          <h4 className="title text-center mt-4 pb-3">Register Here!</h4>
          <form onSubmit={handleSubmit} className='col-sm-10 col-12 mx-auto'>
            <div className='form-group  py-2  '>
              <input type="text" className="form-control" placeholder="Username" onChange={e => setUsername(e.target.value)} />
            </div>
            <div className='form-group py-2 '>
              <input type="email" className="form-control" placeholder="Email Address" onChange={e => setEmail(e.target.value)} />
            </div>
            <div className='form-group py-2 ' >
              <input type="password" className="form-control" placeholder="Password" onChange={e => setPassword(e.target.value)} />
            </div>
            <div className='form-group py-2 ' >
              <input type="password" className="form-control" placeholder="Confirm Password" onChange={e => setPassword2(e.target.value)} />
            </div>
            {/* {errorMessage && <div className='text-danger'>{errorMessage}</div>} */}
            <div className='form-group py-2 ' >
              <input type="submit" className="btn btn-outline-warning d-block w-100" />
            </div>
            <p className="mt-3 mb-4 pb-lg-2" style={{ color: "#393f81" }}>
              Already have an account?{" "}
              <Link to="/login" style={{ color: "#393f81" }}>
                Login Now
              </Link>
            </p>
            <a href="#!" className="small text-muted">
              Terms of use.
            </a>
            <a href="#!" className="small text-muted">
              Privacy policy
            </a>
          </form>
        </div>
      </div>
    </div>
  );
}

export default Register;
