import curses
import os
import sys

term_width = -1


################################################################################
### function : termwidth()
################################################################################
def termwidth():
    global term_width

    try:
        if term_width < 0:
            if os.isatty(1):
                # interactive, query curses for screen width
                #sys.stderr.write("We are writing to an interactive terminal\n")
                win = curses.initscr()
                dim = win.getmaxyx()
                curses.endwin()
                term_width = dim[1]
            else:
                # not interactive, prob redirected to a file
                #sys.stderr.write("We are writing to a non-interactive terminal\n")
                term_width = 32767
    except Exception as ex:
        sys.stderr.write("Exception: " + str(ex) + "\n")


    return term_width


################################################################################
### function : dash()
### params   : wid=-1
################################################################################
def dash(wid=-1):
    return linebar("-", wid)


################################################################################
### function : dbldash()
### params   : wid=-1
################################################################################
def dbldash(wid=-1):
    return linebar("=", wid)


################################################################################
### function : linebar()
### params   : char
###          : num
################################################################################
def linebar(char, num=-1):
    if num < 0:
        num = termwidth()
    return char * num
    # return '+' + (char * (num-2)) + '+'


################################################################################
### function : print2()
### params   : val
################################################################################
def print2(val):
    line1 = ""
    line2 = ""
    for ch in val:
        ch2 = ch if ord(ch) > 31 and ord(ch) < 127 else "."
        line1 += "  %1s" % ch2
        line2 += " %02x" % ord(ch)
    print("txt:" + line1)
    print("hex:" + line2)


################################################################################
### function : print4()
### params   : val
################################################################################
def print4(val):
    line1 = ""
    line2 = ""
    for ch in val:
        ch2 = ch if ord(ch) > 31 and ord(ch) < 127 else "."
        line1 += "    %1s" % (ch2)
        line2 += " %04x" % (ord(ch))
    print("txt:" + line1)
    print("hex:" + line2)
