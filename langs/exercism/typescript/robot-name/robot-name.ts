export class Robot {
  private _name: string;
  private static names: { [key: string]: Robot } = {};

  constructor() {
    this._name = this.getUniqueName();
  }

  public get name(): string {
    return this._name;
  }

  public getUniqueName(): string {
    while (true) {
      const name = Robot.generateName();

      if (!Robot.names[name]) {
        Robot.names[name] = this;
        return name;
      }
    }
  }

  public resetName(): void {
    this._name = this.getUniqueName();
  }

  public static releaseNames(): void {
    Robot.names = {};
  }

  public static generateName(): string {
    // Random UTF-16 65-90 A-Z Capital Letter
    const letter1 = String.fromCharCode(
      Math.floor(Math.random() * (91 - 65) + 65)
    );
    const letter2 = String.fromCharCode(
      Math.floor(Math.random() * (91 - 65) + 65)
    );

    // Random Number 0-9
    const digit1 = String(Math.floor(Math.random() * 10));
    const digit2 = String(Math.floor(Math.random() * 10));
    const digit3 = String(Math.floor(Math.random() * 10));

    return letter1 + letter2 + digit1 + digit2 + digit3;
  }
}
