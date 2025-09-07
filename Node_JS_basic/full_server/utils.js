import fs from 'fs';

export default function readDatabase(filePath) {
  return new Promise((resolve, reject) => {
    fs.readFile(filePath, 'utf8', (err, data = '') => {
      if (err) {
        reject(new Error('Cannot load the database'));
        return;
      }

      const lines = data.split('\n').filter((l) => l.trim() !== '');
      // remove header
      const rows = lines.slice(1);

      const result = {};
      for (const row of rows) {
        const parts = row.split(',');
        if (parts.length >= 4) {
          const firstname = parts[0];
          const field = parts[3];
          if (field) {
            if (!result[field]) result[field] = [];
            result[field].push(firstname);
          }
        }
      }
      resolve(result);
    });
  });
}
