import re

# util functions of the application 
NUM_OR_DOT_REGEX = re.compile(r'^[0-9.]$')

def isNumOrDot(string: str):
    return bool(NUM_OR_DOT_REGEX.search(string))

def convertTypeNumber(string: str):
    text = float(string)

    if text.is_integer():
        text = int(text)

    return text

def isACorrectNumber(string: str):
    valid = False
    try:
        float(string)
        valid = True
    except ValueError:
        valid = False
    return valid

def isEmpty(string: str):
    return len(string) == 0