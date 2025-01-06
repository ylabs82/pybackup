#!/usr/bin/env python3

"""Python Backup
   Main Module

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
import subprocess
import sys

from pb_mods import pybackup_arguments as pb_args
from pb_mods import pybackup_aux as pb_aux


def main():
    """Program entry point."""

    # Perform initial checks and exit if any error is found.
    checks_result, exit_code = pb_aux.initial_checks()
    if not checks_result:
        sys.exit(exit_code)

    # Parse the arguments and exit if any error is found.
    arguments, exit_code = pb_args.process_arguments()
    if exit_code is not None:
        sys.exit(exit_code)

    sources = pb_aux.get_file_lines(arguments.configuration)
    rotations = pb_aux.get_file_lines(arguments.rotations)

    # Check if there are any sources.
    if not sources:
        print("No backup sources found.")
        print("Exiting...")
        sys.exit(1)

    # Check if there are any destinations.
    if not rotations:
        print("No backup destinations found.")
        print("Exiting...")
        sys.exit(1)

    # If there is only one destination, warn the user.
    if len(rotations) == 1:
        print("There is only one destination. You should consider adding more.")
        print()

    # Get the first destination.
    current_dest = rotations[0].strip()

    # Check if the destination directory exists.
    if not os.path.exists(current_dest):
        print(f"Destination directory '{current_dest}' does not exist.")
        print("Maybe you have connected the wrong device or the device is not mounted.")
        print("Exiting...")
        sys.exit(1)

    # Prepare the rsync command.
    rsync_command = "rsync -av --delete"

    # Loop through the sources and add them to the rsync command.
    for source in sources:
        rsync_command += f" {pb_aux.clean_source(source)}"

    # Add the destination to the rsync command.
    rsync_command += f" {current_dest}"

    # Execute the rsync command.
    p = subprocess.Popen(rsync_command, shell=True, stderr=subprocess.PIPE)

    # Print the output of the rsync command, realtime.
    while True:
        out = p.stderr.read(1)
        if out == b'' and p.poll() is not None:
            break
        if out != b'':
            sys.stdout.write(out.decode('utf-8'))
            sys.stdout.flush()

    print()

    # Check the return code of the process and rotate the backups if successful.
    if p.returncode == 0:
        if len(rotations) > 1:
            print("Backup successful. Rotating backup destinations...")
            rotations = pb_aux.rotate_backups(rotations)
            pb_aux.save_rotations(rotations, arguments.rotations)
        else:
            print("Backup successful. Consider adding more destinations.")
    else:
        print("An error occurred during the backup.")
        print("Exiting...")
        sys.exit(1)


if __name__ == '__main__':
    main()
