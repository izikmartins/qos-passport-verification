cat > README.md <<'EOF'
# QOS Passport Verification

Passport MRZ extraction prototype developed for the QOSPAY identity verification workflow.

The system uses **FastMRZ** with **Tesseract OCR** to detect, read, and parse the Machine Readable Zone (MRZ) of international passports.

## Features

- Passport MRZ detection
- Tesseract-based OCR
- TD3 passport MRZ parsing
- Passport number extraction
- Surname and given-name extraction
- Issuing country extraction
- Nationality extraction
- Date of birth extraction
- Sex extraction
- Passport expiry-date extraction
- MRZ check-digit extraction and validation
- Structured JSON output

## Identity Verification Flow

```text
Passport Image
      |
      v
MRZ Detection
      |
      v
Tesseract OCR
      |
      v
FastMRZ
      |
      v
Structured Passport Data
      |
      +--------------------+
      |                    |
      v                    v
Liveness Detection    Face Verification