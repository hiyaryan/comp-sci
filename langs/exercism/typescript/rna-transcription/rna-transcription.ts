const dnaRnaComplements: { [key: string]: string } = {
  G: "C",
  C: "G",
  T: "A",
  A: "U",
};

export function toRna(dna: string): string {
  let rna = "";

  const nucleotides = dna.split("");
  for (let nucleotide of nucleotides) {
    if (dnaRnaComplements[nucleotide]) rna += dnaRnaComplements[nucleotide];
    else throw "Invalid input DNA.";
  }

  return rna;
}
