const express = require('express');
const session = require('express-session');
const bodyParser = require('body-parser');

const app = express();

app.set('view engine', 'ejs');
app.set('views', './views');
app.use(bodyParser.urlencoded({ extended: true }));

//ustawienia sesji
app.use(session({
  secret: 'key',
  resave: true,
  saveUninitialized: true
}));

app.get('/', (req, res) => {
  res.render('form', { error: req.session.error, formData: req.session.formData });
});

app.post('/submit', (req, res) => {
  const { firstName, lastName, course, task1, task2, task3, task4, task5, task6, task7, task8, task9, task10} = req.body;

  if (!firstName || !lastName || !course) {
    req.session.error = 'Wypełnij wszystkie pola formularza.';
    req.session.formData = { firstName, lastName, course, task1, task2, task3, task4, task5, task6, task7, task8, task9, task10 };
    res.redirect('/');
  } else {
    
    req.session.submittedData = { firstName, lastName, course, task1, task2, task3, task4, task5, task6, task7, task8, task9, task10 };
    req.session.error = null;
    req.session.formData = null;
    res.redirect('/print');
  }
});

app.get('/print', (req, res) => {
  const data = req.session.submittedData;
  if (!data) {
    res.redirect('/');
  } else {
    res.render('print', { data });
  }
});

app.listen(3000, () => {
  console.log('started');
});
