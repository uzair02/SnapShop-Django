import React, { useContext } from 'react';
import { Link } from 'react-router-dom';
import { jwtDecode } from 'jwt-decode';
import AuthContext from '../../context/AuthContext';
import logo from '../Assets/logo.png';
import './Navbar.css';

const Navbar = () => {
    const { user, logoutUser } = useContext(AuthContext);
    const token = localStorage.getItem("authTokens");
    let username = "";

    if (token) {
        const decoded = jwtDecode(token);
        username = decoded.username;
    }

    return (
        <nav className="navbar navbar-expand-lg navbar-light bg-light py-3 sticky-top">
            <div className="container">
                <img src={logo} alt="" />
                <Link className="navbar-brand fw-bold fs-4 px-2" to="/">Snap <br/>Shop</Link>
                <button className="navbar-toggler mx-2" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
                    <span className="navbar-toggler-icon"></span>
                </button>

                <div className="collapse navbar-collapse" id="navbarSupportedContent">
                    <ul className="navbar-nav m-auto my-2 text-center">
                        <li className="nav-item">
                            <Link className="nav-link" to="/">Home </Link>
                        </li>
                        <li className="nav-item">
                            <Link className="nav-link" to="/ProductPage">Products</Link>
                        </li>
                        <li className="nav-item">
                            <Link className="nav-link" to="/AboutUs">About</Link>
                        </li>
                        <li className="nav-item dropdown">
                            <a className="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                                Ratings
                            </a>
                            <div className="dropdown-menu" aria-labelledby="navbarDropdown">
                                <Link className="dropdown-item" to="/RatingsPage">Check Store Ratings</Link>
                                {token !== null &&
                                    <>
                                    <Link className="dropdown-item" to="/RatingForm">Rate Web Stores</Link>
                                    <Link className="dropdown-item" to="/Recommend">Recommeded Products</Link>
                                    </>
                                }
                            </div>
                        </li>
                    </ul>

                    <div className="buttons text-center">
                        {token === null ?
                            <>
                                <Link to="/login" className="btn btn-outline-danger m-2"><i className="fa fa-sign-in-alt mr-1"></i> Login</Link>
                                <Link to="/Register" className="btn btn-outline-warning m-2"><i className="fa fa-user-plus mr-1"></i> Register</Link>
                            </>
                            :
                            <>
                                <Link to="/ProfilePage" className="mx-3" style={{ textDecoration: 'none', color: 'black' }}>
                                    <h7 className="h7">Hello {username}</h7>
                                </Link>
                                <Link onClick={logoutUser} style={{ cursor: "pointer" }} className="btn btn-outline-secondary m-2"><i className="fa fa-sign-out-alt mr-1"></i> Logout</Link>
                            </>
                        }
                    </div>
                </div>
            </div>
        </nav>
    );
}

export default Navbar;
