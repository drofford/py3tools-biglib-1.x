import os
import os.path
import re
import sys

#
# option keys
#
JUST = "JUST"
JOIN = "JOIN"
SPACING = "SPACING"
COMMENT = "COMMENT"
BOXCHAR = "BOXCHAR"

#
# option values
#
LEFT = "L"
CENTER = "C"
RIGHT = "R"
SINGLE = "S"
DOUBLE = "D"
SLASHES = "// "
HASHES = "# "
NONE = ""
MINUS = "-"
EQUAL = "="
STAR = "*"


################################################################################
### function : _double_space()
### params   : words_in
################################################################################
def _double_space(words_in):
    words_out = list()
    for word_in in words_in:
        word_out = ""
        for ch in word_in:
            word_out += ch + " "
        words_out.append(word_out.rstrip())
    return words_out


################################################################################
### function : boxit()
### params   : options
###          : words
################################################################################
def boxit(options, words):
    if type(words) is list or type(words) == tuple:
        if JOIN in options and options[JOIN]:
            words = [" ".join(words)]
    else:
        words = [words]

    pad = " "
    if SPACING in options and options[SPACING] == DOUBLE:
        words = _double_space(words)
        pad = "   "

    max_width = 0
    for word in words:
        max_width = max(max_width, len(word))

    if JUST not in options:
        dirn = "<"
    elif options[JUST] == LEFT:
        dirn = "<"
    elif options[JUST] == RIGHT:
        dirn = ">"
    elif options[JUST] == CENTER:
        dirn = "^"
    else:
        print("INTERNAL ERROR: justification option is invalid:", options[JUST])
        exit(1)
    fmt = "{:" + dirn + str(max_width) + "}"

    boxchar = options[BOXCHAR] if BOXCHAR in options else "* "
    comment = options[COMMENT] if COMMENT in options else "# "

    puff = boxchar * 3
    tot_width = len(puff) + len(pad) + max_width + len(pad) + len(puff)

    result = comment + boxchar * tot_width + "\n"
    for word in words:
        result += comment + puff + pad + fmt.format(word) + pad + puff + "\n"
    result += comment + boxchar * tot_width

    return result
