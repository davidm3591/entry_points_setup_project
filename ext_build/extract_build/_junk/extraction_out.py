# Simulate extraction_out.py for exe build
import sys


def ppt_stuff_out():
    pptx_stuff = [
        "\nPowerPoint Content output Simulation:\n"
        "\tMain page content",
        "\tStart note slide content",
        "\tMore note slide content",
        "\tEnd note slide content\n"
    ]
    for slide in pptx_stuff:
        print(slide)

    sys.exit()
