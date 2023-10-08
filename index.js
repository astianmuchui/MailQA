const express = require('express');
const app = express();

app.get('/auth/google/callback', (req, res) => {
  const authorizationCode = req.query.code;

  // Now, you can use this authorization code to exchange it for access tokens
  // and user information on your server.
});

app.listen(5500)