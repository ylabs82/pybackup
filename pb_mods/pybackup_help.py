#!/usr/bin/env python3

"""Python Backup
   Help Module

   MIT License

   Copyright 2025 Yago Mouriño Mendaña <ylabs82@gmail.com>

   Permission is hereby granted, free of charge, to any person obtaining a copy
   of this software and associated documentation files (the “Software”), to
   deal in the Software without restriction, including without limitation the
   rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
   sell copies of the Software, and to permit persons to whom the Software is
   furnished to do so, subject to the following conditions:

   The above copyright notice and this permission notice shall be included in
   all copies or substantial portions of the Software.

   THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
   IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
   FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
   AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
   LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
   FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
   IN THE SOFTWARE.

"""

from pb_mods import pybackup_consts as bp_c

CATEGORY_CONFIGURATION = """\
CONFIGURATION FILE
==================
The configuration file is a text file that contains the sources to back up.
Each line of the file must contain the path of a source to back up.
The sources can be files or directories.
The configuration file must have at least one line with a source.
The default configuration file must be located at ~/.config/pybackup/configuration.

Example:
/home/user/Documents/
/home/user/Pictures/
/home/user/Downloads/
/home/user/.bash_history
"""

CATEGORY_ROTATIONS = """\
ROTATIONS FILE
==============
The rotations file is a text file that contains the destinations for the backup.
Each line of the file must contain the path of a destination.
The destinations must be directories.
The rotations file must have at least one line with a destination.
If there's more than one destination, the program will rotate them after each backup.
The default rotations file must be located at ~/.config/pybackup/rotations.

Example:
/run/media/user/backup_drive1
/run/media/user/backup_drive2
/run/media/user/backup_drive3
/run/media/user/backup_drive4
"""


def basic_help():
    """Prints the program usage."""
    __help_title()
    __help_body()
    __help_footer()


def category_help(category):
    """Prints the help of the given category. Returns 0 if the category is
       valid, 1 otherwise."""
    toret = 0

    if category == "none":
        basic_help()
    elif category == "category":
        __help_title()
        __show_categories()
    elif category == "configuration":
        __help_title()
        print(CATEGORY_CONFIGURATION)
    elif category == "rotations":
        __help_title()
        print(CATEGORY_ROTATIONS)
    else:
        __help_title()
        print(" Invalid help category")
        toret = 1

    return toret


def help_with_exceptions(exceptions_messages):
    """Prints the help of the program with the given exception
       messages. Returns nothing."""
    __help_title()

    # Print the exception messages.
    for exception_message in exceptions_messages:
        print(exception_message)
    print()

    __help_body()


def __help_title():
    """Prints the title of the help. Returns nothing."""
    print(f"{bp_c.PROG_NAME}, v{bp_c.PROG_VERSION}")
    print(f"Copyright (c) {bp_c.PROG_YEAR}, {bp_c.PROG_COMPANY}")
    print("Original author: Yago Mouriño Mendaña <ylabs82@gmail.com>")
    print()


def __help_body():
    """Prints the body of the help. Returns nothing."""
    print(f"Usage: {bp_c.EXECUTABLE} [options...]")
    print("   -c, --configuration <configuration file> Configuration file")
    print("   -r, --rotations <rotations file>         Rotations file")
    print("   -e, --errorlog <rsync error log file>    rsync error log file")
    print("   -h, --help <category>                    Get full help")


def __help_footer():
    """Prints the footer of the help. Returns nothing."""
    print()
    print("This is not the full help, use \"--help category\" to get a list of")
    print("all categories.")


def __show_categories():
    """Prints the help categories. Returns nothing."""
    print(" configuration  Get configuration file help")
    print(" rotations      Get rotations file help")
    print()


if __name__ == '__main__':
    print("PYBACKUP Help Module")
