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

function decodedValue(colorList: string[]): number {
  let resistorColor = "";

  for (let color of colorList) {
    resistorColor += colors[color];
  }

  return parseInt(resistorColor);
}

function applyZeros(resistorValue: number, zeroColor: string): number {
  return resistorValue * 10 ** parseInt(colors[zeroColor]);
}

function applyDimensionalAnalysis(resistorValue: number): string {
  const units = ["ohms", "kiloohms", "megaohms", "gigaohms"];
  let index = 0;

  while (resistorValue >= 1000 && index < units.length - 1) {
    resistorValue /= 1000;
    index++;
  }

  return `${resistorValue} ${units[index]}`;
}

export function decodedResistorValue(colorList: string[]): string {
  if (!colorList.length) return "";

  if (colorList.length > 2) colorList.splice(3);

  // determine the initial value
  let resistorValue: number = decodedValue(colorList.slice(0, 2));

  // apply zeros
  resistorValue = applyZeros(resistorValue, colorList[2]);

  // apply dimensional analysis and return value
  return applyDimensionalAnalysis(resistorValue);
}
