# tmd

`tmd` is a tool for pretty-printing files to the terminal. It uses the
`python3-rich` library for syntax-highlighting and markdown viewing.

## Installing

The `tmd.py` is the only required file. The repository is a
[take](https://github.com/vsthijs/take) project, so, if `take` is installed, you can install it with
`take this install`. This will copy the `tmd.py` file in the same directory as
the `take` executable. The installer is almost the same.

> Before using tmd, make sure that the `rich` library is installed.
> It can be installed by `sudo apt install python3-rich`, or
> `pip install rich`. For more details on this library, go to the
> [source code](https://github.com/Textualize/rich)

## Usage

Like `cat`, you can pass multiple files to `tmd`. All files will be printed to the terminal in order. The following options are allowed:
- `-h` or `--help`:                         print a help message and return
- `-v` or `--version`:                      print the version, and return
- `--disable-markdown` or `--force-code`:   view all files as source code, and
                                            do not apply special styles to
                                            markdown files.
