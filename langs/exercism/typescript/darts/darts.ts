export function score(x: number, y: number): number {
  const radius = (x ** 2 + y ** 2) ** 0.5;

  if (radius > 10) {
    return 0; // missed target
  } else if (radius > 5) {
    return 1; // outer circle
  } else if (radius > 1) {
    return 5; // middle circle
  } else {
    return 10; // inner circle
  }
}
