const express = require('express')
const app = express()

const port = process.env.PORT || 9000;

app.get('/', (req, res) => res.send('Hello from Container - Parabéns bem Vindo ao Time FIAP Turma Devops & Cloud Computing!!'))

app.listen(port, (err) => {
    if (err) {
      console.log('Error::', err);
    }
      console.log(`App listening on port ${port}`);
  });
