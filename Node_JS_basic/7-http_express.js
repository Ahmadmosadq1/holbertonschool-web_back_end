const express = require('express');
const fs = require('fs');

function countStudents(path) {
  return new Promise((resolve, reject) => {
    fs.readFile(path, 'utf8', (err, data) => {
      if (err) {
        reject(new Error('Cannot load the database'));
        return;
      }

      const lines = data.split('\n').filter((l) => l.trim() !== '');
      const students = lines.slice(1);

      let output = `Number of students: ${students.length}\n`;

      const fields = {};
      for (const row of students) {
        const parts = row.split(',');
        const firstname = parts[0];
        const field = parts[3];
        if (field) {
          if (!fields[field]) fields[field] = [];
          fields[field].push(firstname);
        }
      }

      for (const [field, names] of Object.entries(fields)) {
        output += `Number of students in ${field}: ${names.length}. List: ${names.join(', ')}\n`;
      }

      resolve(output.trim());
    });
  });
}

const app = express();

app.get('/', (req, res) => {
  res.type('text/plain').send('Hello Holberton School!');
});

app.get('/students', async (req, res) => {
  res.type('text/plain');
  const dbPath = process.argv[2];

  try {
    const summary = await countStudents(dbPath);
    res.send(`This is the list of our students\n${summary}`);
  } catch (e) {
    res.send(`This is the list of our students\n${e.message}`);
  }
});

app.listen(1245);

module.exports = app;
