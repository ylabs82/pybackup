#!/usr/bin/env python3

"""Python Backup
   Arguments Module

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

import argparse
import os

from pb_mods import pybackup_aux as pb_aux
from pb_mods import pybackup_help as pb_hlp


def process_arguments():
    """Processes the arguments given to the program. Returns the parsed
       arguments and the exit code if any error is found. If no error
       is found, exit code is None."""

    # Prepare the argument parser.
    argument_parser = argparse.ArgumentParser(
        add_help=False, exit_on_error=False)

    argument_parser.add_argument("-c", "--configuration")
    argument_parser.add_argument("-r", "--rotations")
    argument_parser.add_argument("-e", "--errorlog")
    argument_parser.add_argument(
        "-h", "--help", const="none", dest="help_category", nargs="?", type=str.lower)

    return __parse_arguments(argument_parser)


def __parse_arguments(argument_parser):
    """Parses the program arguments. Returns the parsed arguments and
       the exit code if any error is found. If no error is found, exit
       code is None."""
    arguments = None
    exit_code = None
    exceptions = []

    # Parse the arguments.
    try:
        arguments = argument_parser.parse_args()

        # If asking for help, print it and exit.
        if arguments.help_category is not None:
            return None, pb_hlp.category_help(arguments.help_category)

        # Configuration file is mandatory. If not provided, use the default.
        if arguments.configuration is None:
            arguments.configuration = os.path.join(pb_aux.get_config_dir(), "configuration")

        if not os.path.isfile(arguments.configuration):
            exceptions.append("Configuration file does not exist or is not a file")
            exit_code = 1

        # Rotations file is mandatory. If not provided, use the default.
        if arguments.rotations is None:
            arguments.rotations = os.path.join(pb_aux.get_config_dir(), "rotations")

        if not os.path.isfile(arguments.rotations):
            exceptions.append("Rotations file does not exist or is not a file")
            exit_code = 1

        if arguments.errorlog is not None:
            if os.path.isdir(arguments.errorlog):
                exceptions.append("Error log file is a directory")
                exit_code = 1

            if os.path.isfile(arguments.errorlog):
                print("Error log file already exists")
                answer = input("Do you want to overwrite it? [y/N] ")
                if answer.lower() != "y":
                    exceptions.append("Error log file already exists")
                    exit_code = 1

    except argparse.ArgumentError as exception:
        exceptions.append(exception)
        exit_code = 1

    if exceptions:
        pb_hlp.help_with_exceptions(exceptions)
        exit_code = 1

    return arguments, exit_code


if __name__ == '__main__':
    print("PYBACKUP Arguments Module")
