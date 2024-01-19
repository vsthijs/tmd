import sys
import os
from rich import print
from rich.console import Console
from rich.markdown import Markdown
from rich.syntax import Syntax
from rich.tree import Tree

console = Console()
force_code = False


def print_markdown(src:str) -> None:
    with open(src) as f:
        console.print(Markdown(f.read()))


def index_dir(d: str, t: Tree) -> None:
    for ii in os.listdir(d):
        n = t.add(ii)
        if os.path.isdir(os.path.join(d, ii)):
            index_dir(os.path.join(d, ii), n)


def print_file(f:str) -> None:
    if f.endswith(".md") and not force_code:
        return print_markdown(f)
    else:
        console.print(Syntax.from_path(f, theme="ansi_dark"))


def print_help() -> None:
    print("""tmd reads files to the terminal like cat, but highlights the syntax.

Usage: tmd [-h|--help] [-v|--version] [flags] files

Flags:
          --force-code          Do not apply special style for markdown files.
          --disable-markdown    Does the same as --force-code.""")


def main(argv:list[str]) -> int:
    global force_code
    last_file:str = ""
    files = []
    for ii in argv[1:]:
        if ii.startswith("-"):
            if ii in ["-h", "--help"]:
                print_help()
                return 0
            elif ii in ["-v", "--version"]:
                print("tmd 0.1.1")
                return 0
            elif ii in ["--force-code", "--disable-markdown"]:
                force_code = True
            else:
                print(f"tmd: [red]err:[/red] unrecognized option '{ii}'", file=sys.stderr)
                return 1
        else:
            files.append(ii)

    try:
        for infile in files:
            last_file = infile
            print_file(infile)

    except PermissionError:
        print(f"tmd: [red]err:[/red] could not open {last_file}.", file=sys.stderr)
        return 1
    except FileNotFoundError:
        print(f"tmd: [red]err:[/red] {last_file} does not exist.", file=sys.stderr)
        return 1
    except IsADirectoryError:
        print(f"tmd: [red]err:[/red] {last_file} is a directory.", file=sys.stderr)
        return 1
    except Exception as e:
        print(f"[white]tmd:[/white] unhandled err: {e}. Please report to the developers", file=sys.stderr)
        return 1

if __name__ == "__main__":
    exit(main(sys.argv))
