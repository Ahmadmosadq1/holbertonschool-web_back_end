export default class Car {
  constructor(brand, motor, color) {
    this._brand = brand;
    this._motor = motor;
    this._color = color;
  }

  // Use Symbol.species so subclasses can control what gets cloned
  static get [Symbol.species]() {
    return this;
  }

  cloneCar() {
    const Species = this.constructor[Symbol.species];
    return new Species();
  }
}
