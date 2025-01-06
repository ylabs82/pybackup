# PyBackup

PyBackup is a Python-based backup utility that allows users to back up files
and directories to multiple destinations. It supports rotation of backup
destinations to ensure data redundancy and reliability.

PyBackup needs the program `rsync` to work. Make sure you have it installed.

## Features

- Backup files and directories to multiple destinations.
- Rotate backup destinations after each backup.
- Simple configuration through text files.
- Detailed help and usage instructions.

## Usage

To run the backup utility, use the following command:

```sh
python pybackup.py -c <configuration_file> -r <rotations_file>
```

If no files are provided, the program will use the default configuration and
rotations files. The default configuration file is `configuration` and the
default rotations file is `rotations`. Both files must be located in the
configuration directory: `~/.config/pybackup/`.

## Configuration File

The configuration file is a text file that contains the sources to back up.
Each line of the file must contain the path of a source to back up.
The sources can be files or directories.
The configuration file must have at least one line with a source.

Example:

```text
/home/user/Documents/
/home/user/Pictures/
/home/user/Downloads/
/home/user/.bash_history
```

## Rotations File

The rotations file is a text file that contains the destinations for the backup.
Each line of the file must contain the path of a destination.
The destinations must be directories.
The rotations file must have at least one line with a destination.
If there's more than one destination, the program will rotate them after each backup.

Example:

```text
/run/media/user/backup_drive1
/run/media/user/backup_drive2
/run/media/user/backup_drive3
/run/media/user/backup_drive4
```

## Help

To get help on how to use the program, run:

```sh
python pybackup.py --help
```

To get help on a specific category, run:

```sh
python pybackup.py --help <category>
```

Available categories:
- configuration
- rotations

## License

This project is licensed under the MIT License. 

```text
The MIT License (MIT)
Copyright (c) 2024 Yago Mouriño Mendaña

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the “Software”), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies
of the Software, and to permit persons to whom the Software is furnished to do
so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```