const actions: string[] = [
  "wink", // 0
  "double blink", // 1
  "close your eyes", // 2
  "jump", // 3
  "reverse", // 4
];

/**
 * Convert number to binary array.
 */
function numberToBinaries(num: number): string[] {
  return (num >>> 0).toString(2).split("");
}

export function commands(action: number): string[] {
  // reverse because 0 starts at the right for a binary digit
  const binaries = numberToBinaries(action).reverse();

  const secret: string[] = [];
  binaries.forEach((binary, i) => {
    // insert action for binary value of "1"
    if (binary === "1" && i !== 4) secret.push(actions[i]);
  });

  // reverse if not undefined
  if (binaries[4]) {
    secret.reverse();
  }

  return secret;
}
