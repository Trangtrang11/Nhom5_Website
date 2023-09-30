class Car {
  constructor(name, color) {
    this.name = name;
    this.color = color;
  }
  getName = () => {
    return this.name;
  };
  getColor = () => {
    return this.color;
  };
}
class SuperCar extends Car {
  constructor(name, color, signature) {
    super(name, color);
    this.signature = signature;
  }
}
const fera = new SuperCar("Ferari", "Green", "signature Ferari");
const bmw = new Car("BMW", "Black");
const toyota = new Car("Mer", "White");
console.log(JSON.stringify(fera.getColor()));
// console.log(JSON.stringify(bmw));
