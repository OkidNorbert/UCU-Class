const express = require("express");

const app = express();
const port = 8080;

//Logging middleware 
function requestLogger(request, response, next) {
    console.log(`Request method: $(request.method) - Request URL: $(request.url)`);
    next(); // passing control to the next middlewares/route handler

app.use(requesttogger); // we then apply the middleware to all routes

app.get('/', (req, res) => {
    res.send('Hello World!');
})

app.listen(port, () => {
    console.log(`the server is running on ${port}`)
})
