const expressions: { [key: string]: RegExp } = {
  inquiring: /\?$/,
  yelling: /^(?=.*[A-Z])[^a-z]*$/,
  questioning: /^(?=.*[A-Z])[^a-z]*\?$/,
  ignoring: /^\s*$/,
};

export function hey(message: string): string {
  message = message.trim();

  if (expressions.ignoring.test(message)) {
    return "Fine. Be that way!";
  } else if (expressions.questioning.test(message)) {
    return "Calm down, I know what I'm doing!";
  } else if (expressions.yelling.test(message)) {
    return "Whoa, chill out!";
  } else if (expressions.inquiring.test(message)) {
    return "Sure.";
  } else {
    return "Whatever.";
  }
}
