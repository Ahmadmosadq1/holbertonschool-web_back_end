export default class Building {
  constructor(sqft) {
    if (typeof sqft !== 'number') {
      throw new TypeError('Square feet must be a number');
    }

    this._sqft = sqft;

    // Ensure subclass overrides evacuationWarningMessage
    if (this.constructor !== Building &&
        this.evacuationWarningMessage === Building.prototype.evacuationWarningMessage) {
      throw new Error('Class extending Building must override evacuationWarningMessage');
    }
  }

  // Getter
  get sqft() {
    return this._sqft;
  }

  // Abstract method placeholder
  evacuationWarningMessage() {
    return 'Override me!';
  }
}
