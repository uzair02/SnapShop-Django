// PrivateRoute.js
import React from 'react';
import { Route, Navigate } from 'react-router-dom';

const PrivateRoute = ({ element: Element, isAuthenticated, ...rest }) => (
  <Route
    {...rest}
    element={
      isAuthenticated ? (
        <Element />
      ) : (
        <Navigate to="/login" replace />
      )
    }
  />
);

export default PrivateRoute;
