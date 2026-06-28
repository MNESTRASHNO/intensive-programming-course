const express = require("express");
const cors = require("cors");

const app = express();

app.use(cors());
app.use(express.json());

app.post("/api/calc", function(req, res) {
    const first = Number(req.body.first);
    const second = Number(req.body.second);
    var result;
    if (req.body.operation === "plus"){
        result = first + second;
    } else {
        result = first - second;
    }
    console.log(req.body);
    console.log(result);
    res.json({
        result
    });
});

app.listen(3000, function(){
    console.log('work');
});
