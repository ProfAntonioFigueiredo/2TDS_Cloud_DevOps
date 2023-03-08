const express = require('express');
const app = express();

const port = process.env.PORT || 3030;

const mysql = require('mysql');
const db = mysql.createConnection({
  host: process.env.DB,
  user: process.env.ROOT,
  password: process.env.Fiap2tds2023,
  database: process.env.db_portalweb ,
});

db.connect((err) => {
  if (err) {
    console.log(err);
    return;
  }
  console.log('Connected to database');
});

app.use(express.json());
app.use(express.urlencoded({ extended: true }));

app.get('/', (req, res) => {
  res.send('Hello World!');
});

app.listen(port, () => {
  console.log(`App listening at http://localhost:${port}`);
});
