export class SimpleCipher {
  key: string;
  constructor(key: string = "") {
    this.key = key ? key : this.generateKey();
  }

  generateKey(): string {
    let key = "";
    for (let i = 0; i < 100; i++) {
      key += String.fromCharCode(Math.floor(Math.random() * 26) + 97);
    }
    return key;
  }

  encode(input: string): string {
    let output = "";
    for (let i = 0; i < input.length; i++) {
      const charCode = input.charCodeAt(i) - 97;
      const keyCharCode = this.key.charCodeAt(i % this.key.length) - 97;
      output += String.fromCharCode(((charCode + keyCharCode) % 26) + 97);
    }
    return output;
  }

  decode(cipher: string): string {
    let output = "";
    for (let i = 0; i < cipher.length; i++) {
      const cipherCharCode = cipher.charCodeAt(i) - 97;
      const keyCharCode = this.key.charCodeAt(i % this.key.length) - 97;
      ``;
      output += String.fromCharCode(
        ((cipherCharCode - keyCharCode + 26) % 26) + 97
      );
    }
    return output;
  }
}
