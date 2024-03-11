export class Rational {
  public numerator: number;
  public denominator: number;

  constructor(numerator: number, denominator: number) {
    this.numerator = numerator;
    this.denominator = denominator;
  }

  add(rational: Rational) {
    if (Math.abs(this.denominator) !== Math.abs(rational.denominator)) {
      const denominator = this.denominator;

      this.denominator = this.denominator * rational.denominator;
      this.numerator = this.numerator * rational.denominator;

      rational.denominator = rational.denominator * denominator;
      rational.numerator = rational.numerator * denominator;
    }

    this.numerator = this.numerator + rational.numerator;

    return this.reduce();
  }

  sub(rational: Rational) {
    if (Math.abs(this.denominator) !== Math.abs(rational.denominator)) {
      const denominator = this.denominator;

      this.denominator = this.denominator * rational.denominator;
      this.numerator = this.numerator * rational.denominator;

      rational.denominator = rational.denominator * denominator;
      rational.numerator = rational.numerator * denominator;
    }

    this.numerator = this.numerator - rational.numerator;

    return this.reduce();
  }

  mul(rational: Rational) {
    this.numerator = this.numerator * rational.numerator;
    this.denominator = this.denominator * rational.denominator;

    return this.reduce();
  }

  div(rational: Rational) {
    this.numerator = this.numerator * rational.denominator;
    this.denominator = this.denominator * rational.numerator;

    return this.reduce();
  }

  abs() {
    if (this.numerator < 0) this.numerator *= -1;
    if (this.denominator < 0) this.denominator *= -1;

    return this.reduce();
  }

  exprational(exponent: number) {
    this.numerator = this.numerator ** Math.abs(exponent);
    this.denominator = this.denominator ** Math.abs(exponent);

    if (exponent < 0) {
      const numerator = this.numerator;

      this.numerator = this.denominator;
      this.denominator = numerator;
    }

    return this.reduce();
  }

  expreal(real: number): number {
    return (real ** this.numerator) ** (1 / this.denominator);
  }

  reduce(): Rational {
    if (this.numerator === 0) {
      this.denominator = 1;
      return this;
    }

    let gcd =
      Math.abs(this.numerator) > Math.abs(this.denominator)
        ? Math.abs(this.denominator)
        : Math.abs(this.numerator);

    while (this.numerator % gcd !== 0 || this.denominator % gcd !== 0) gcd--;

    this.numerator = this.numerator / gcd;
    this.denominator = this.denominator / gcd;

    if (this.denominator < 0) {
      this.numerator *= -1;
      this.denominator *= -1;
    }

    return this;
  }
}
