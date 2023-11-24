import sys


def containpunct(string):
    """return false if contain punctuation"""

    punc = r'''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    for ch in string:
        # print(ch)
        if ch in punc:
            return True
    return False


def main():
    """Converts string and print as morse code"""
    NESTED_MORSE = {
        'A': '.- ', 'B': '-... ', 'C': '-.-. ', 'D': '-.. ',
        'E': '. ', 'F': '..-. ', 'G': '--. ', 'H': '.... ',
        'I': '.. ', 'J': '.--- ', 'K': '-.- ', 'L': '.-.. ',
        'M': '-- ', 'N': '-. ', 'O': '--- ', 'P': '.--. ',
        'Q': '--.- ', 'R': '.-. ', 'S': '... ', 'T': '- ',
        'U': '..- ', 'V': '...- ', 'W': '.-- ', 'X': '-..- ',
        'Y': '-.-- ', 'Z': '--.. ', '0': '----- ', '1': '.---- ',
        '2': '..--- ', '3': '...-- ', '4': '....- ', '5':
        '..... ', '6': '-.... ', '7': '--... ',
        '8': '---.. ', '9': '----. ', ' ': '/ '
        }
    # NESTED_MORSE =  {
    #     'A': '.-A', 'B': '-...B', 'C': '-.-.C', 'D': '-..D',
    #     'E': '.E', 'F': '..-.F', 'G': '--.G', 'H': '....H',
    #     'I': '..I', 'J': '.---J', 'K': '-.-K', 'L': '.-..L',
    #     'M': '--M', 'N': '-.N', 'O': '---O', 'P': '.--.P',
    #     'Q': '--.-Q', 'R': '.-.R', 'S': '...S', 'T': '-T',
    #     'U': '..-U', 'V': '...-V', 'W': '.--W', 'X': '-..-X',
    #     'Y': '-.--Y', 'Z': '--..Z', '0': '-----0', '1': '.----1',
    #     '2': '..---2', '3': '...--3', '4': '....-4', '5':
    #     '.....5', '6': '-....6', '7': '--...7',
    #     '8': '---..8', '9': '----.9', ' ': '/ '
    #     }
    try:
        argc = len(sys.argv)
        assert argc == 2, "the arguments are bad"
        arg = str(sys.argv[1])
        flag = False
        if (containpunct(arg) is False):
            flag = True
        assert flag is True, "the arguments are bad"
        return_string = ""
        for ch in arg:
            if ch.upper() in NESTED_MORSE:
                return_string = return_string + NESTED_MORSE[ch.upper()]
        print(return_string.strip())

    except AssertionError as msg:
        print("AssertionError:", msg)


if __name__ == "__main__":
    """Testing"""
    main()
