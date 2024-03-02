export class Matrix {
  matrix: number[][];

  constructor(matrix: string) {
    const strRows: string[] = matrix.split("\n");
    this.matrix = strRows.map((strRow) => strRow.split(" ").map(Number));
  }

  get rows(): number[][] {
    return this.matrix;
  }

  get columns(): number[][] {
    const transpose: number[][] = new Array(this.matrix[0].length)
      .fill(null)
      .map(() => new Array(this.matrix.length).fill(0));

    for (let row = 0; row < this.matrix.length; row++) {
      for (let col = 0; col < this.matrix[row].length; col++) {
        transpose[col][row] = this.matrix[row][col];
      }
    }

    return transpose;
  }
}
