const colors: { [key: string]: string } = {
  black: "0",
  brown: "1",
  red: "2",
  orange: "3",
  yellow: "4",
  green: "5",
  blue: "6",
  violet: "7",
  grey: "8",
  white: "9",
};

export function decodedValue(colorList: string[]): number {
  if (!colorList.length) return -1;

  if (colorList.length > 2) colorList.splice(2);

  let resistorColor = "";
  for (let color of colorList) {
    resistorColor += colors[color];
  }

  return parseInt(resistorColor);
}
