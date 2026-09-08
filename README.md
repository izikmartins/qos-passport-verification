# QOS Passport Verification

This repository contains a **Passport MRZ Extraction and Validation Proof of Concept (PoC)** developed as part of the QOSPAY identity verification solution.

The purpose of this project is to automatically read the **Machine Readable Zone (MRZ)** found on international passports and convert the information into structured data that can be used during customer onboarding and identity verification.

The solution uses:

* **FastMRZ** for detecting, reading, and parsing passport MRZ data
* **Tesseract OCR** as the OCR engine
* **Python** for processing the passport image and returning structured JSON data

---

## What Does This Project Do?

International passports contain a **Machine Readable Zone (MRZ)** at the bottom of the passport identity page.

For a standard TD3 passport, the MRZ contains information such as:

* Passport holder's surname
* Given names
* Passport/document number
* Issuing country
* Nationality
* Date of birth
* Sex
* Passport expiry date
* MRZ check digits

Instead of manually entering these details, this prototype accepts a passport image and attempts to automatically extract the information.

For example:

```bash
python passport_mrz.py data/passport_uk.jpg
```

The application processes the passport and returns structured information such as:

```json
{
    "mrz_type": "TD3",
    "document_code": "P",
    "issuer_code": "GBR",
    "surname": "PUDARSAN",
    "given_name": "HENERT",
    "document_number": "707797979",
    "nationality_code": "GBR",
    "birth_date": "1995-05-20",
    "sex": "M",
    "expiry_date": "2017-04-22",
    "status": "SUCCESS"
}
```

---

# How It Works

The basic processing flow is:

```text
Passport Image
      |
      v
FastMRZ detects the MRZ
      |
      v
Tesseract OCR reads the MRZ characters
      |
      v
FastMRZ parses the MRZ
      |
      v
Passport Fields Extracted
      |
      v
Structured JSON Result
```

### Step 1 — Passport Image

The program receives the path to a passport image.

Example:

```bash
python passport_mrz.py data/passport_uk.jpg
```

### Step 2 — MRZ Detection

FastMRZ attempts to locate the Machine Readable Zone on the passport.

For standard TD3 passports, this is normally the two machine-readable lines at the bottom of the passport identity page.

### Step 3 — OCR

Tesseract OCR reads the characters contained in the detected MRZ.

### Step 4 — MRZ Parsing

FastMRZ converts the OCR result into individual fields such as:

* Passport number
* Name
* Nationality
* Date of birth
* Sex
* Expiry date
* Check digits

### Step 5 — Structured Result

The extracted information is returned as structured JSON that can later be passed to other components of the QOSPAY identity verification system.

---

# Project Structure

```text
qos-passport-verification/
│
├── passport_mrz.py
├── requirements.txt
├── README.md
├── .gitignore
│
└── data/
    └── passport_uk.jpg
```

The `data/passport_uk.jpg` file is a sample passport image used for testing the installation.

Real customer or personal passport images should not be committed to the repository.

---

# Installation

## 1. Install Python

Python must be installed on the computer.

Check whether Python is already installed:

```bash
python --version
```

You should receive a Python version number.

If Python is not installed, install Python before continuing.

---

## 2. Clone the Repository

Clone the QOS Passport Verification repository:

```bash
git clone <repository-url>
```

Enter the project directory:

```bash
cd qos-passport-verification
```

---

## 3. Create a Python Virtual Environment

Create a virtual environment:

```bash
python -m venv .venv
```

### Windows — Git Bash

Activate it with:

```bash
source .venv/Scripts/activate
```

### Windows — Command Prompt

Use:

```cmd
.venv\Scripts\activate
```

### Windows — PowerShell

Use:

```powershell
.venv\Scripts\Activate.ps1
```

After activation, the terminal should show something similar to:

```text
(.venv)
```

---

## 4. Install Python Dependencies

With the virtual environment activated, run:

```bash
pip install -r requirements.txt
```

The requirements include the Python packages used by the prototype, including:

* FastMRZ
* NumPy
* OpenCV
* Pillow
* pytesseract

---

# Installing Tesseract OCR

Tesseract is an external OCR application and is **not installed automatically by `pip install -r requirements.txt`**.

It must be installed separately.

The official Tesseract installation documentation recommends the UB Mannheim Windows builds for Windows users.

Tesseract Installation Documentation:
https://tesseract-ocr.github.io/tessdoc/Installation.html

Windows Installer (UB Mannheim):
https://github.com/UB-Mannheim/tesseract/wiki

Download the appropriate Windows installer and run it.

## Windows Installation

### Step 1 — Install Tesseract

Install a Windows build of Tesseract OCR.

Tesseract's documentation notes that the project itself does not provide an official current Windows installer and points Windows users to third-party Windows installers.

During installation, the normal installation location used by this prototype is:

```text
C:\Program Files\Tesseract-OCR\
```

After installation, the executable should normally be located at:

```text
C:\Program Files\Tesseract-OCR\tesseract.exe
```

### Step 2 — Check the Installation

Open a new terminal and run:

```bash
tesseract --version
```

If Tesseract is correctly installed and available through PATH, the terminal should display the installed Tesseract version.

You can also check that this file exists:

```text
C:\Program Files\Tesseract-OCR\tesseract.exe
```

### Step 3 — Check the Python Configuration

The current `passport_mrz.py` contains:

```python
TESSERACT_PATH = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
```

If Tesseract was installed somewhere else, change `TESSERACT_PATH` to the correct location.

For example:

```python
TESSERACT_PATH = r"C:\Your\Tesseract\Path\tesseract.exe"
```

---

# Running the Project

The repository contains a sample British passport image for testing the installation.

Make sure the virtual environment is active:

```bash
source .venv/Scripts/activate
```

Then run:

```bash
python passport_mrz.py data/passport_uk.jpg
```

If everything is installed correctly, you should see:

```text
QOSPAY PASSPORT MRZ EXTRACTION
============================================================
```

followed by the extracted passport information.

Example:

```json
{
    "mrz_type": "TD3",
    "document_code": "P",
    "issuer_code": "GBR",
    "surname": "PUDARSAN",
    "given_name": "HENERT",
    "document_number": "707797979",
    "document_number_checkdigit": "2",
    "nationality_code": "GBR",
    "birth_date": "1995-05-20",
    "birth_date_checkdigit": "9",
    "sex": "M",
    "expiry_date": "2017-04-22",
    "expiry_date_checkdigit": "4",
    "optional_data": "",
    "optional_data_checkdigit": "0",
    "final_checkdigit": "0",
    "status": "SUCCESS"
}
```

---

# Testing Another Passport Image

The Python script accepts the passport image path from the command line.

For example:

```bash
python passport_mrz.py passport1.png
```

You can also provide a path to an image in another directory:

```bash
python passport_mrz.py path/to/passport.jpg
```

The general command is:

```bash
python passport_mrz.py <passport-image-path>
```

---

# Quick Setup

For someone cloning the project on a Windows computer, the main Python setup is:

```bash
git clone <repository-url>
cd qos-passport-verification

python -m venv .venv
source .venv/Scripts/activate

pip install -r requirements.txt

python passport_mrz.py data/passport_uk.jpg
```

Remember that **Tesseract OCR must also be installed separately** before running the final command.

---

# MRZ Validation

Passport MRZs contain check digits that help identify inconsistencies in fields such as the document number, birth date, and expiry date.

FastMRZ returns these values as part of the extraction result.

However:

> **Successful MRZ extraction or internally consistent MRZ data does not prove that a passport is genuine.**

This PoC primarily demonstrates **passport MRZ extraction and validation**, not complete physical passport authentication.

A forged or manipulated document could potentially contain structurally valid MRZ information.

---

# Role in the QOSPAY Identity Verification System

This repository represents one component of the broader identity verification solution.

The planned architecture includes:

```text
                Identity Document
                       |
          +------------+------------+
          |                         |
          v                         v
 Passport MRZ Processing      NIN OCR Processing
 FastMRZ + Tesseract             PaddleOCR
          |                         |
          +------------+------------+
                       |
                       v
              Identity Information
                       |
                       v
               Liveness Detection
                       |
                       v
                Face Verification
                       |
                       v
              Verification Result
```

The components are maintained as separate PoCs so they can be tested independently before integration.

---

# Related QOSPAY Identity PoCs

### QOS Passport Verification

This repository.

Responsible for:

* Passport MRZ detection
* OCR
* Passport field extraction
* MRZ parsing and validation

### QOS NIN Verification

Responsible for:

* Nigerian NIN document OCR
* NIN field extraction
* Structured identity information

### QOS Liveness Detection

Responsible for active and passive liveness checks, including:

* Randomized challenges
* Blink detection
* Mouth-open detection
* Head movement
* MiniFASNet passive anti-spoofing

### QOS Face Verification

Responsible for comparing the identity-document photograph with a selfie using:

* DeepFace
* GhostFaceNet
* RetinaFace
* Cosine-distance face comparison

---

# Current Limitations

This project is currently a **Proof of Concept / R&D implementation**.

Performance may be affected by:

* Poor image quality
* Blur
* Glare
* Low lighting
* Camera quality
* Passport positioning
* Cropped MRZ regions
* Damaged passports
* OCR errors

Broader testing should be performed across passports from different countries, cameras, devices, lighting conditions and image qualities before production deployment.

A production passport-verification system may also require additional controls such as:

* Document authenticity analysis
* Tamper detection
* Security-feature verification
* NFC/ePassport chip verification
* Face verification
* Liveness detection
* Fraud monitoring

---

# Privacy and Security

Passport information is sensitive identity information.

Do **not** commit:

* Real customer passport images
* Personal passport scans
* NIN documents
* Customer selfies
* Biometric information
* API keys
* Credentials
* Production customer information

The repository's `.gitignore` is configured to ignore common image/document formats except for the approved sample passport used for testing.

---

# Third-Party Dependency

This project uses **FastMRZ** as a third-party dependency.

FastMRZ and associated resources remain subject to their respective copyright and licensing terms.

---

# Project Status

**Status:** Proof of Concept / Research & Development

The current implementation demonstrates the extraction of structured identity information from the Machine Readable Zone of international passports for potential use within the QOSPAY identity verification workflow.
