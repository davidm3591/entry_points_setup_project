import sys

# Local app import
from extraction_tool import extract_open


def main(args=None):
    """The main routine."""
    if args is None:
        args = sys.argv[1:]

    extract_open()


if __name__ == "__main__":
    main()
