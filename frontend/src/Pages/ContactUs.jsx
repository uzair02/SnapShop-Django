import React from 'react';

const ContactUs = () => {
    return (
        <div className="container my-3 py-3">
            <h1 className="text-center">Contact Us</h1>
            <hr />
            <div className="row my-4 h-100">
                <div className="col-md-4 col-lg-4 col-sm-8 mx-auto">
                    <form>
                        <div className="form my-3">
                            <label htmlFor="Name">Name</label>
                            <input
                                type="text"  
                                className="form-control"
                                id="Name"
                                placeholder="Enter your name"
                            />
                        </div>
                        <div className="form my-3">
                            <label htmlFor="Email">Email</label>
                            <input
                                type="email"
                                className="form-control"
                                id="Email"
                                placeholder="name@example.com"
                            />
                        </div>
                        <div className="form my-3">
                            <label htmlFor="Message">Message</label>
                            <textarea
                                rows={5}
                                className="form-control"
                                id="Message"
                                placeholder="Enter your message"
                            />
                        </div>
                        <div className="text-center">
                            <button
                                className="my-2 px-4 mx-auto btn btn-danger"
                                type="submit"
                            >
                                Send
                            </button>
                        </div>
                    </form>
                </div>
            </div>
        </div>
    );
};

export default ContactUs;
