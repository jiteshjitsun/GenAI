const express = require("express");

const PORT = process.env.PORT ? process.env.PORT : 8000;

const app = express();

app.get('/', (req, res) => {
    res.json({
        status: "successful", 
        message: "Hello Pune!"
    })
})


app.listen(PORT, () => {
    console.log(`App is running on port ${PORT}`);
})