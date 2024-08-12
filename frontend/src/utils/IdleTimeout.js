import React, { useEffect, useState, useCallback } from 'react';

const IdleTimeout = ({ timeoutInMinutes, logoutUser, isLoggedIn }) => {
  const [timeoutId, setTimeoutId] = useState(null);

  const resetTimeout = useCallback(() => {
    if (timeoutId) {
      clearTimeout(timeoutId);
    }

    const newTimeoutId = setTimeout(() => {
      logoutUser();
    }, timeoutInMinutes * 60 * 1000);

    setTimeoutId(newTimeoutId);
  }, [timeoutId, logoutUser, timeoutInMinutes]);

  useEffect(() => {
    const events = ['mousedown', 'keydown', 'mousemove', 'scroll'];

    const handleUserActivity = () => {
      resetTimeout();
    };

    events.forEach(event => {
      document.addEventListener(event, handleUserActivity);
    });

    // Initial setup
    if (isLoggedIn) {
      resetTimeout();
    }

    return () => {
      events.forEach(event => {
        document.removeEventListener(event, handleUserActivity);
      });

      if (timeoutId) {
        clearTimeout(timeoutId);
      }
    };
  }, [resetTimeout, isLoggedIn]);

  return <></>;
};

export default IdleTimeout;
