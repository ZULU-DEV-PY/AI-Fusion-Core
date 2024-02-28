import re
from enum import Enum, auto

# Definición de la clase Token y TokenType
class TokenType(Enum):
  EOF = auto()
  IDENTIFIER = auto()
  NUMBER = auto()
  STRING = auto()
  KEYWORD = auto()
  OPERATOR = auto()
  PUNCTUATION = auto()

class Token:
  def __init__(self, type, value, position):
    self.type = type
    self.value = value
    self.position = position

  def __str__(self):
    return f"Token({self.type}, {repr(self.value)}, Posición: {self.position})"

# Definición de las palabras clave, operadores y símbolos de puntuación
KEYWORDS = {"def", "if", "else", "while", "for", "return", "break", "continue"}
OPERATORS = {"+", "-", "*", "/", "%", "==", "!=", "<", ">", "<=", ">=", "&&", "||", "!", "^"}
PUNCTUATION = {";", ",", "(", ")", "{", "}", "[", "]", "."}

# Excepción personalizada para errores léxicos
from enum import Enum, auto
import re

# Definición de la clase Token y TokenType
class TokenType(Enum):
  EOF = auto()
  IDENTIFIER = auto()
  NUMBER = auto()
  STRING = auto()
  KEYWORD = auto()
  OPERATOR = auto()
  PUNCTUATION = auto()

class Token:
  def __init__(self, type, value, position):
    self.type = type
    self.value = value
    self.position = position

  def __str__(self):
    return f"Token({self.type}, {repr(self.value)}, Posición: {self.position})"

# Definición de las palabras clave, operadores y símbolos de puntuación
KEYWORDS = {"def", "if", "else", "while", "for", "return", "break", "continue"}
OPERATORS = {"+", "-", "*", "/", "%", "==", "!=", "<", ">", "<=", ">=", "&&", "||", "!", "^"}
PUNCTUATION = {";", ",", "(", ")", "{", "}", "[", "]", "."}

# Excepción personalizada para errores léxicos
class LexicalError(Exception):
  pass

# Función principal del lexer
def lex(source_code):
  tokens = []
  index = 0
  while index < len(source_code):
    current_char = source_code[index]
    # Saltarse comentarios de una sola línea
    if current_char == "#" and index + 1 < len(source_code) and source_code[index + 1] != "\n":
      index = source_code.find("\n", index) + 1
      continue
    # Identificar identificadores
    match = re.match(r"[a-zA-Z_][a-zA-Z0-9_]*", source_code[index:])
    if match:
      identifier = match.group(0)
      token_type = TokenType.KEYWORD if identifier in KEYWORDS else TokenType.IDENTIFIER
      tokens.append(Token(token_type, identifier, index))
      index += len(match.group(0))
      continue
    # Identificar números
    match = re.match(r"[0-9]+", source_code[index:])
    if match:
      number = match.group(0)
      tokens.append(Token(TokenType.NUMBER, number, index))
      index += len(match.group(0))
      continue
    # Identificar cadenas
    match = re.match(r'\"(.*?)\"', source_code[index:])
    if match:
      string = match.group(1)
      tokens.append(Token(TokenType.STRING, string, index))
      index += len(match.group(0))
      continue
    # Identificar operadores y símbolos de puntuación
    if current_char in OPERATORS or current_char in PUNCTUATION:
      tokens.append(Token(TokenType.OPERATOR if current_char in OPERATORS else TokenType.PUNCTUATION, current_char, index))
      index += 1
      continue
    # Manejar caracteres desconocidos
    raise LexicalError(f"Caracter desconocido '{current_char}' en la posición {index}")
  tokens.append(Token(TokenType.EOF, None, index))
  return tokens

# Ejemplo de uso
source_code = """
def factorial(n):
  if n == 0:
    return 1
  else:
    return n * factorial(n - 1)

print(factorial(5))
"""

tokens = lex(source_code)
for token in tokens:
  print(token)
