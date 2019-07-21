# Build sim for extraction_pptx.py
from extraction_out import ppt_stuff_out


def read_file():
    """Build simulated extraction_pptx.py
       for entry script build
    """
    print("\nPowerPoint Loaded\n")

    slide_info = "Processing..."
    for i in range(10):
        print(f"\t{slide_info}")

    ppt_stuff_out()
