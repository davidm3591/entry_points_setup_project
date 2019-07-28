# Build sim for extraction_pptx.py
from extraction_out import ppt_stuff_out
import time


def read_file():
    """Build simulated extraction_pptx.py
       for entry script build
    """
    start = time.time()
    print("\nPowerPoint Loaded\n")

    slide_info = "Processing..."
    for i in range(10):
        print(f"\t{slide_info}")

    ppt_stuff_out(start)
