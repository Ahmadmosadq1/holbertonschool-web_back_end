export default class AppController {
  static getHomepage(_req, res) {
    res.status(200).send('Hello Holberton School!');
  }
}
