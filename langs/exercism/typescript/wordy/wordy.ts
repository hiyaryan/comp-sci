const operations: { [key: string]: (a: number, b: number) => number } = {
  is: (a: number, b: number) => b,
  plus: (a: number, b: number) => a + b,
  minus: (a: number, b: number) => a - b,
  multiplied: (a: number, b: number) => a * b,
  divided: (a: number, b: number) => a / b,
};

const solvable: { [key: string]: boolean } = {
  what: true,
  who: false,
};

export const answer = (problem: string): number => {
  let words: string[] = problem.split(" ");

  if (!solvable[words[0].toLocaleLowerCase()])
    throw new Error("Unknown operation");
  else {
    words = words.slice(1);
    words[words.length - 1] = words[words.length - 1].split("?")[0];
    words = words.filter((word) => word !== "by");
  }

  let isNum = false;
  let isOp = false;
  let answer = 0;
  let operator = "";
  for (let word of words) {
    if (parseInt(word)) {
      if (isNum) {
        throw new Error("Syntax error");
      }

      isNum = true;
      isOp = false;
    } else {
      if (isOp) {
        throw new Error("Syntax error");
      } else {
        isNum = false;
        isOp = true;

        if (operations[word]) {
          operator = word;
        } else {
          throw new Error("Unknown operation");
        }
      }
    }

    if (isNum) {
      answer = operations[operator](answer, parseInt(word));
    }
  }

  if (isNum) return answer;
  else throw new Error("Syntax error");
};
