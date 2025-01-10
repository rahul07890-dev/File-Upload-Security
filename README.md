# Secure File Upload System with Flask

## Overview
This project demonstrates a **Secure File Upload System** built using Flask. It provides a safe and user-friendly way to upload files while implementing robust security measures to mitigate vulnerabilities. Key features include file validation, secure storage, and vulnerability testing.

---

## Features

### Secure File Handling
- **Supported File Types**: `.png`, `.jpg`, `.jpeg`, `.gif`, `.pdf`, `.txt`.
- **File Size Limit**: Restricts uploads to a maximum of **5 MB**.
- **Filename Sanitization**: Utilizes `secure_filename` to prevent path traversal attacks.

### Security Measures
- **File Type Validation**: Ensures uploaded files have allowed extensions.
- **Content Verification**: Placeholder for validating that file content matches the claimed type (e.g., MIME type).
- **Storage Location**: Stores files in a non-public directory (`uploads/`) to prevent unauthorized access.
- **Malware Scanning**: Placeholder for implementing antivirus or malware scans.

### Exploitation and Mitigation
- Simulates vulnerabilities by testing with malicious and safe files.
- Includes mitigation strategies to prevent file upload attacks:
  - Validate file extensions and MIME types.
  - Limit file sizes.
  - Store files outside the web root.
  - Sanitize filenames.
  - Perform malware scans on uploaded files.

### Web Interface
- Provides a simple web page (`index.html`) for uploading files.
- Returns informative JSON responses for errors or successful uploads.

---

## Endpoints

### `/`
Renders the homepage for file uploads.

### `/upload`
Handles secure file uploads via POST requests and returns success or error messages in JSON format.

### `/mitigation`
Lists mitigation strategies for file upload vulnerabilities and provides guidance for secure file handling practices.

### `/test_upload`
Simulates uploads of test files (malicious and safe) for vulnerability testing to demonstrate the system's behavior.

---

## Technologies Used
- **Flask**: Backend framework for HTTP request handling and rendering templates.
- **Werkzeug**: Provides utilities for secure filename handling.
- **Python**: Implements server-side logic and validations.

---

## Setup Instructions

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/secure-file-upload.git
   cd secure-file-upload
   ```
2. **Install Dependencies**:
```bash
pip install -r requirements.txt
```
3. **Run the Application**:
```bash
python app.py
```

---

## Directory Structure
```
secure-file-upload/
|
├── app.py               # Main Flask application
├── uploads/             # Directory for storing uploaded files
├── templates/           # HTML templates
|    └── index.html      # Frontend template for file uploads
├── requirements.txt     # Python dependencies
└── README.md            # Project documentation
```
---

## Future Enhancements
- **Real-Time Malware Scanning**: Integrate a malware detection system.
- **Logging and Monitoring**: Track suspicious file uploads.
- **Cloud Integration**: Add support for uploading files to cloud storage (e.g., AWS S3, Google Cloud Storage).
- **Improved Frontend**: Enhance the user interface for better user experience.
- 
---

## Contribution
Contributions are welcome! Feel free to fork this repository, create a branch, and submit a pull request with your improvements or new features.

---

## License
This project is licensed under the Apache License 2.0. See the LICENSE file for details.

---

## Acknowledgments
- **Flask Documentation**: For guidance on secure file handling.
- **Open-Source Community**: For inspiration and tools to build secure web applications.
