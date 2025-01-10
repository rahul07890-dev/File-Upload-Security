import os
from werkzeug.utils import secure_filename
from flask import Flask, request, jsonify, render_template

# Flask application setup
app = Flask(__name__)

# Configure upload settings
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'pdf', 'txt'}
MAX_FILE_SIZE = 5 * 1024 * 1024  # 5 MB

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = MAX_FILE_SIZE

# Ensure the upload folder exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def allowed_file(filename):
    """Check if the file has an allowed extension."""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def home():
    """Render the home page."""
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    """Handle file upload securely."""
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    if not allowed_file(file.filename):
        return jsonify({"error": "File type not allowed"}), 400

    # Secure the filename and save the file
    filename = secure_filename(file.filename)
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    
    try:
        file.save(file_path)
        return jsonify({"message": f"File {filename} uploaded successfully!"}), 200
    except Exception as e:
        return jsonify({"error": f"File upload failed: {str(e)}"}), 500

# Mitigation Strategies
@app.route('/mitigation', methods=['GET'])
def mitigation_strategies():
    """List potential mitigation strategies for file upload vulnerabilities."""
    strategies = {
        "allowed_file_types": "Validate file extensions and MIME types.",
        "file_size_limit": "Set maximum allowed file size.",
        "filename_sanitization": "Use secure_filename to sanitize filenames.",
        "store_outside_webroot": "Save uploaded files in non-public directories.",
        "scan_for_malware": "Perform antivirus or malware scans on uploaded files.",
        "check_content_type": "Verify the file's actual content matches its claimed type."
    }
    return jsonify(strategies), 200

# Exploitation simulation
@app.route('/test_upload', methods=['POST'])
def test_upload():
    """Test upload endpoint for vulnerabilities."""
    test_files = [
        ("malicious.php", "echo '<?php echo shell_exec($_GET['cmd']); ?>';"),
        ("safe_image.png", b"\x89PNG\r\n\x1a\n"),
    ]
    responses = {}
    for filename, content in test_files:
        with open(os.path.join(UPLOAD_FOLDER, filename), 'wb') as f:
            f.write(content if isinstance(content, bytes) else content.encode())
        responses[filename] = f"Saved as {UPLOAD_FOLDER}/{filename}."

    return jsonify(responses), 200

if __name__ == '__main__':
    print("Starting Flask application...")
    app.run(debug=True)
