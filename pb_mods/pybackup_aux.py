#!/usr/bin/env python3

"""Python Backup
   Auxiliary Module

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

import os
import shutil

from pb_mods import pybackup_help as pb_hlp


def initial_checks():
    """Performs the initial checks for the program. Returns a tuple with the
       result of the checks and the exit code if the checks fail."""
    checks_results = True
    exit_code = None

    # Check if needed programs are installed.
    if not __exists_commands("rsync"):
        pb_hlp.help_with_exceptions(
            ["This program needs the following programs to function properly:" +
             os.linesep + " - rsync" +
             os.linesep +
             os.linesep + "Please, make sure you have installed these programs and try again."])
        checks_results = False
        exit_code = 1

    return checks_results, exit_code


def get_config_dir():
    """Returns the configuration directory."""
    return os.path.join(os.path.expanduser("~"), ".config/pybackup/")


def get_file_lines(file):
    """Given a text file, read each line and return an array with those lines."""
    try:
        with open(file, "r") as f:
            lines = f.readlines()
    except FileNotFoundError:
        lines = []

    return lines


def clean_source(source):
    """Given a backup source string, clean it and return it."""
    toret = source.strip()

    # If the source ends with a slash, remove it.
    if toret.endswith("/"):
        toret = toret[:-1]

    return toret


def rotate_backups(rotations):
    """Given an array of strings, pass the first element to the end of the array."""
    if len(rotations) > 0:
        rotations.append(rotations.pop(0))

    return rotations


def save_rotations(rotations, rotations_file):
    """Given an array of strings, save each string in a text file."""
    try:
        with open(rotations_file, "w") as file:
            try:
                for rotation in rotations:
                    file.write(rotation)
            except (IOError, OSError):
                print("Error writing the rotations file")
    except (FileNotFoundError, PermissionError, OSError):
        print("Error opening the rotations file")


def __exists_commands(*commands):
    """Checks whether the given commands exist in the system. Returns True if
       all the commands exists, False otherwise."""
    toret = True

    for command in commands:
        if command != "" and command is not None:
            toret = toret and shutil.which(command) is not None
            if not toret:
                break

    return toret


if __name__ == '__main__':
    print("PYBACKUP Auxiliary Module")
