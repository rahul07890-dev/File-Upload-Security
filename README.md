Secure File Upload System with Flask

This project demonstrates a Secure File Upload System using Flask, designed with robust measures to handle file uploads securely and mitigate common vulnerabilities. It allows users to upload various file types while ensuring safety, scalability, and ease of use.

Features
Secure File Uploads:

Allows files with extensions: .png, .jpg, .jpeg, .gif, .pdf, .txt.
Sets a file size limit of 5 MB to prevent overloading the server.
Uses secure_filename from Werkzeug to sanitize filenames.
Robust Security Measures:

Validates file extensions and MIME types to prevent malicious uploads.
Saves files in a non-public directory to avoid direct access.
Includes antivirus/malware scan placeholders for enhanced security.
Verifies that file content matches its claimed type.
Simulation of Exploitation and Mitigation:

A test_upload endpoint simulates potential vulnerabilities with test files (e.g., malicious PHP script).
A mitigation endpoint provides details on strategies used to mitigate file upload vulnerabilities.
User-Friendly Web Interface:

A simple web page (index.html) for file uploads.
Informative JSON responses to guide users in case of errors.
Endpoints
/: Renders the homepage for file uploads.
/upload: Handles secure file uploads via POST.
/mitigation: Lists mitigation strategies for file upload vulnerabilities.
/test_upload: Simulates the upload of malicious and safe files for testing purposes.
Technologies Used
Flask: Backend framework for handling HTTP requests and rendering templates.
Werkzeug: For secure filename sanitization.
Python: For server-side logic and validations.
Setup Instructions
Clone the repository:
bash
Copy code
git clone https://github.com/your-username/secure-file-upload.git
Navigate to the project directory:
bash
Copy code
cd secure-file-upload
Install the required dependencies:
bash
Copy code
pip install -r requirements.txt
Run the Flask application:
bash
Copy code
python app.py
Access the application at http://127.0.0.1:5000.
