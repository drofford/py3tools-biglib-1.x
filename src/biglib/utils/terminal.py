import curses
import os
import sys

term_width = -1


def termwidth():
    global term_width

    try:
        if term_width < 0:
            if os.isatty(1):
                # interactive, query curses for screen width
                # sys.stderr.write("We are writing to an interactive terminal\n")
                win = curses.initscr()
                dim = win.getmaxyx()
                curses.endwin()
                term_width = dim[1]
            else:
                # not interactive, prob redirected to a file
                # sys.stderr.write("We are writing to a non-interactive terminal\n")
                term_width = 32767
    except Exception as ex:
        sys.stderr.write("Exception: " + str(ex) + "\n")

    return term_width
