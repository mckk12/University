var pg = require('pg');

(async function main() {
    var pool = new pg.Pool({
        host: 'localhost',
        database: 'postgres',
        user: 'postgres',
        password: 'pass'
    });
    try {
        var result = await pool.query('select * from osoba');
        result.rows.forEach( r => {
        console.log( `${r.id} ${r.imie} ${r.nazwisko}`);
        });
    }
    catch ( err ) {
        console.log( err ); 
    }
        pool.query('insert into osoba (imie, nazwisko) values ($1, $2)', ['Jan', 'Kowalski']);
        try {
            var result = await pool.query('select * from osoba');
            result.rows.forEach( r => {
            console.log( `${r.id} ${r.imie} ${r.nazwisko}`);
            });
        }
        catch ( err ) {
            console.log( err ); 
        }
    pool.query('delete from osoba where id = 6');
    pool.query('delete from osoba where id = 7');
    
    })();

