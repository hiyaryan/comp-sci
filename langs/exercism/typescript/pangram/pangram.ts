const NUM_LETTERS_IN_ALPHABET: number = 26;

function getAlphabetMap(): { [key: string]: boolean } {
  const alphabetMap: { [key: string]: boolean } = {};

  for (let char of "abcdefghijklmnopqrstuvwxyz") {
    alphabetMap[char] = false;
  }

  return alphabetMap;
}

export function isPangram(sentence: string): boolean {
  const alphabetMap = getAlphabetMap();

  let count = 0;
  for (let letter of sentence.toLocaleLowerCase().split("")) {
    if (letter.match(/^[a-z]+$/) && !alphabetMap[letter]) {
      alphabetMap[letter] = true;
      count++;
    }
  }

  return count == NUM_LETTERS_IN_ALPHABET;
}
