import sys
from extract_startup import extract_open


def main(args=None):
    """The main routine."""
    if args is None:
        args = sys.argv[1:]

    print("This is the main routine.")
    print("It should do something interesting.")

    # Do argument parsing here (e.g. with argparse)
    # and anything else you want your projet to do.
    extract_open()


if __name__ == "__main__":
    main()
