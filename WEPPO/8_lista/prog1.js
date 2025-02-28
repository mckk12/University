var http = require('http');
const express = require('express')
const multer  = require('multer')
const upload = multer({ dest: 'pliki/' })

var app = express();

app.set('view engine', 'ejs');
app.set('views', './views');

app.use( (req, res) => {
    res.render('index');
});

app.post(upload.single('plik'), function (req, res, next) {
    res.send('Dziękujemy za przesłanie pliku');
})

http.createServer(app).listen(3000);