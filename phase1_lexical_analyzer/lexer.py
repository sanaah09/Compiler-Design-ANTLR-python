# lexer.py
# Simple Lexical Analyzer in Python (Compiler Design)

import re

# Token patterns
KEYWORDS = {
    "int", "float", "char", "double", "if", "else", "while",
    "for", "return", "break", "continue", "void"
}

OPERATORS = {
    "==", "!=", "<=", ">=", "=", "+", "-", "*", "/", "<", ">"
}

SYMBOLS = {
    ";", ",", "(", ")", "{", "}", "[", "]"
}

# Regular expressions
token_specification = [
    ("NUMBER",   r"\d+"),
    ("ID",       r"[A-Za-z_]\w*"),
    ("OPERATOR", r"==|!=|<=|>=|[=+\-*/<>]"),
    ("SYMBOL",   r"[;,()\{\}\[\]]"),
    ("SKIP",     r"[ \t]+"),
    ("NEWLINE",  r"\n"),
    ("MISMATCH", r"."),
]

token_regex = "|".join(
    f"(?P<{name}>{pattern})" for name, pattern in token_specification)


def lexical_analyzer(code):
    tokens = []

    for match in re.finditer(token_regex, code):
        kind = match.lastgroup
        value = match.group()

        if kind == "NUMBER":
            tokens.append(("INTEGER", value))

        elif kind == "ID":
            if value in KEYWORDS:
                tokens.append(("KEYWORD", value))
            else:
                tokens.append(("IDENTIFIER", value))

        elif kind == "OPERATOR":
            tokens.append(("OPERATOR", value))

        elif kind == "SYMBOL":
            tokens.append(("SYMBOL", value))

        elif kind == "SKIP" or kind == "NEWLINE":
            continue

        elif kind == "MISMATCH":
            tokens.append(("UNKNOWN", value))

    return tokens


# -------- MAIN PROGRAM --------
input_file = "input.txt"   # VERY IMPORTANT

try:
    with open(input_file, "r") as f:
        source_code = f.read()

    result = lexical_analyzer(source_code)

    print("TOKENS:")
    for token in result:
        print(f"{token[0]} : {token[1]}")

except FileNotFoundError:
    print("ERROR: input.txt file not found!")
    print("Make sure input.txt is in the SAME folder as lexer.py")
