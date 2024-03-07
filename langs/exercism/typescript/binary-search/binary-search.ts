export function find(haystack: number[], needle: number): number | never {
  let start = 0;
  let end = haystack.length - 1;

  while (start <= end) {
    const mid = Math.floor((start + end) / 2);

    if (haystack[mid] === needle) {
      return mid;
    } else if (haystack[mid] < needle) {
      start = mid + 1;
    } else {
      end = mid - 1;
    }
  }

  throw new Error("Value not in array");
}
