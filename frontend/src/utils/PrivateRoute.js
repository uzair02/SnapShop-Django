import React, { useContext } from 'react';
import { Navigate } from 'react-router-dom';
import AuthContext from '../context/AuthContext';
import IdleTimeout from './IdleTimeout';

const PrivateRoute = ({ children }) => {
  const { user } = useContext(AuthContext);
  if (!user) {
    return <Navigate to="/login" />;
  }
  return (
    <>
      <IdleTimeout timeoutInMinutes={90} /> 
      {children}
    </>
  );
};
export default PrivateRoute;















// const PrivateRoute = ({ element: Element, ...rest }) => {
//   const { user } = useContext(AuthContext);

//   return user ? (
//     <Routes>
//       <Route {...rest} element={<Element />} />
//     </Routes>
//   ) : (
//     <Navigate to="/login" />
//   );
// };

// export default PrivateRoute;