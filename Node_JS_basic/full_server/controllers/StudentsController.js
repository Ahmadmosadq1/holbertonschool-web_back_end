import readDatabase from '../utils.js';

export default class StudentsController {
  static getAllStudents(_req, res) {
    const dbPath = process.argv[2];

    readDatabase(dbPath)
      .then((map) => {
        const fields = Object.keys(map).sort((a, b) =>
          a.toLowerCase().localeCompare(b.toLowerCase())
        );

        const lines = ['This is the list of our students'];
        for (const field of fields) {
          const names = map[field] || [];
          lines.push(
            `Number of students in ${field}: ${names.length}. List: ${names.join(', ')}`
          );
        }

        res.status(200).type('text/plain').send(lines.join('\n'));
      })
      .catch(() => {
        res.status(500).type('text/plain').send('Cannot load the database');
      });
  }

  static getAllStudentsByMajor(req, res) {
    const dbPath = process.argv[2];
    const { major } = req.params;

    if (major !== 'CS' && major !== 'SWE') {
      res.status(500).type('text/plain').send('Major parameter must be CS or SWE');
      return;
    }

    readDatabase(dbPath)
      .then((map) => {
        const names = map[major] || [];
        res.status(200).type('text/plain').send(`List: ${names.join(', ')}`);
      })
      .catch(() => {
        res.status(500).type('text/plain').send('Cannot load the database');
      });
  }
}
