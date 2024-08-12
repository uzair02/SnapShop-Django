import React, { useEffect } from 'react';

const Chatbot = () => {
  useEffect(() => {
    const botpressScript = document.createElement('script');
    botpressScript.src = 'https://cdn.botpress.cloud/webchat/v1/inject.js';
    botpressScript.async = true;
    document.body.appendChild(botpressScript);


    const configScript = document.createElement('script');
    configScript.src = 'https://mediafiles.botpress.cloud/670d8f01-30bf-4fd8-9f17-48122010e26e/webchat/config.js';
    configScript.defer = true;
    document.body.appendChild(configScript);

    return () => {
      document.body.removeChild(botpressScript);
      document.body.removeChild(configScript);
    };
  }, []);

  return <div id="webchat" />;
};

export default Chatbot;
