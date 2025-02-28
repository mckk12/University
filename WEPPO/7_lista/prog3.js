var fs = require('fs');
var http = require('http');
const express = require('express');

const app = express();

(async function () {
    var html = await fs.promises.readFile('index.html', 'utf-8');
    var server = http.createServer(
    (req, res) => {
        res.setHeader('Content-type', 'text/html; charset=utf-8');
        if ( req.method == 'GET' ) {
            res.end(html.replace("{{error}}", ''));
        } else {
            var postdata = '';
            req.on('data', function(data) { postdata += data });
            req.on('end', () => {
                // w body jest komplet zapostowanych
                // danych w postaci klucz=wartosc&klucz2=wartosc2
                // można np. zamienic na obiekt
                // { klucz:wartosc, klucz2: wartosc2 } (reduce!)
                var body = Object.fromEntries(postdata.split('&').map( kv => kv.split('=') ));

                if (!body.name || !body.surname || !body.class) {
                    res.end(html.replace("{{error}}", 'Prosze uzupełnić wszystkie pola'));
                } else {
                    
                    var printable = `Imie: ${body.name}<br>Nazwisko: ${body.surname}<br>Zajęcia: ${body.class}<br>`;
                    for (var i = 1; i <= 10; i++) {
                        printable += `Zadanie ${i}: ${body['task' + i] || 0}<br>`;
                    }
                res.end(printable);
                }
            });
        }
    });
    server.listen(3000);
    console.log('started');
})();