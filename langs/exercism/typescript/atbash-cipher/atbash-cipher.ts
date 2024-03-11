const encodings: { [key: string]: string } = {
  a: "z",
  b: "y",
  c: "x",
  d: "w",
  e: "v",
  f: "u",
  g: "t",
  h: "s",
  i: "r",
  j: "q",
  k: "p",
  l: "o",
  m: "n",
  n: "m",
  o: "l",
  p: "k",
  q: "j",
  r: "i",
  s: "h",
  t: "g",
  u: "f",
  v: "e",
  w: "d",
  x: "c",
  y: "b",
  z: "a",
  " ": "",
};

const regex = /^[a-zA-Z0-9]+$/;
const numbers = /^[0-9]+$/;

export function encode(plainText: string): string {
  const chars = plainText.split("");

  let cipher = "";
  let count = 0;
  chars.forEach((char) => {
    if (regex.test(char)) {
      cipher += numbers.test(char) ? char : encodings[char.toLowerCase()];
      count += 1;
    }

    if (count === 5) {
      count = 0;
      cipher += " ";
    }
  });

  return cipher.trim();
}

export function decode(cipherText: string): string {
  const chars = cipherText.split("");

  let decipher = "";
  chars.forEach((char) => {
    decipher += numbers.test(char) ? char : encodings[char];
  });

  return decipher;
}
