const fs = require("fs");
const readline = require("readline");

const input_path = "logi.txt";

const inputStream = fs.createReadStream(input_path);

var ip_values = {};
var lineReader = readline.createInterface(inputStream, ip_values);

lineReader.on("line", function (line) {
    let ip = line.split(" ")[1];
    if (ip_values[ip]) {
        ip_values[ip] += 1;
    } else {
        ip_values[ip] = 1;
    }
});

lineReader.on("close", function () {
    biggest = [0, 0, 0];
    ips = [];
    for (let ip in ip_values) {
        if (ip_values[ip] > biggest[0]) {
            [biggest[2], biggest[1]]= [biggest[1],biggest[0]];
            [ips[2], ips[1]] = [ips[1], ips[0]];
            biggest[0] = ip_values[ip];
            ips[0] = ip;
            
        }
        else if (ip_values[ip] > biggest[1]) {
            biggest[2] = biggest[1];
            ips[2] = ips[1];
            biggest[1] = ip_values[ip];
            ips[1] = ip;
        }
        else if (ip_values[ip] > biggest[2]) {
            biggest[2] = ip_values[ip];
            ips[2] = ip;
        }
    }
    for(let i = 0; i<3;i++){
        console.log(ips[i],biggest[i]);
    }
});
