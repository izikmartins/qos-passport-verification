from fastmrz import FastMRZ
import json
import os
import sys


TESSERACT_PATH = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


def main():
    if len(sys.argv) < 2:
        print("Usage:")
        print("python passport_mrz.py <passport_image>")
        print()
        print("Example:")
        print("python passport_mrz.py passport.jpg")
        return

    image_path = sys.argv[1]

    if not os.path.exists(image_path):
        print(f"Image not found: {image_path}")
        return

    fast_mrz = FastMRZ(
        tesseract_path=TESSERACT_PATH
    )

    print("\nQOSPAY PASSPORT MRZ EXTRACTION")
    print("=" * 60)

    try:
        result = fast_mrz.get_details(image_path)

        print(json.dumps(result, indent=4))

    except Exception as e:
        print("\nERROR:")
        print(type(e).__name__)
        print(str(e))


if __name__ == "__main__":
    main()