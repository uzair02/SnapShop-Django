import React, { useState, useEffect } from 'react';
import { jwtDecode } from 'jwt-decode';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';


const EditProfile = () => {
   
    const token = localStorage.getItem("authTokens");
    let user_id = null;

    if (token){
      const decoded = jwtDecode(token);
      user_id = decoded.user_id;
    }
    const navigate = useNavigate();
    const [fullName, setFullName] = useState('');
    const [bio, setBio] = useState('');
    const [userInfo, setUserInfo] = useState(null); // State to store user information

    useEffect(() => {
        const fetchUserInfo = async () => {
            try {
                const response = await axios.get('http://127.0.0.1:8000/api/get_profile/', {
                    params: { userId: user_id }
                });
                setUserInfo(response.data);
            } catch (error) {
                console.error('Error fetching user info:', error);
            }
        };

        fetchUserInfo();
    }, [user_id]); // Dependency added to trigger fetchUserInfo when user_id changes

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            const response = await axios.post('http://127.0.0.1:8000/api/update_profile/', {
                user_id,
                fullName,
                bio,
                userId: user_id
            });
            console.log('Profile updated successfully:', response.data);
            navigate('/ProfilePage');
            // You can handle success behavior here, like showing a success message
        } catch (error) {
            console.error('Error updating profile:', error);
            // Handle error, show error message to the user, etc.
        }
    };

    const handleChange = (e) => {
        const { name, value } = e.target;
        if (name === 'fullName') {
            // console.log(value); 
            setFullName(value);  // Update fullName state with the new value
        } else if (name === 'bio') {
            setBio(value);  // Update bio state with the new value
        }
    };
    
    return (
        <div className="container mt-4">
            <div className='col-md-9 card mx-auto d-flex flex-row px-0'>
                <div className="card-body d-flex flex-column justify-content-center">
                    <h4 className="title text-center mt-4 pb-3">Edit Profile</h4>
                    {userInfo && (
                        <form className='col-sm-10 col-12 mx-auto' onSubmit={handleSubmit}>
                            <div className='form-group pb-2'>
                                <input type="text" className="form-control" name="fullName" value={fullName} onChange={handleChange} placeholder="Full Name" />
                            </div>
                            <div className='form-group py-2 px-2'>
                                <textarea className="form-control" name="bio" value={bio} onChange={handleChange} placeholder="Bio (optional)"></textarea>
                            </div>
                            <div className='pt-1'>
                                <input type="submit" className="btn btn-secondary d-block w-100" value="Update Profile" />
                            </div>
                        </form>
                    )}
                </div>
            </div>
        </div>
    );
};

export default EditProfile;
