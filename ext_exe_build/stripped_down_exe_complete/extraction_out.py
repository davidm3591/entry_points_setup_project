# Simulate extraction_out.py for exe build
import sys
import time


def ppt_stuff_out(start):
    pptx_stuff = [
        "\nPowerPoint Content Simulation:\n"
        "\tMain page content",
        "\tStart note slide content",
        "\tMore note slide content",
        "\tEnd note slide content\n"
    ]
    for slide in pptx_stuff:
        print(slide)

    end = time.time()
    print(f"Execution time: {end - start}")
    time.sleep(4)
    sys.exit()
