from flask import Flask, render_template, request, redirect, url_for, flash
import os
from werkzeug.utils import secure_filename
from metadata_extractor import extract_metadata
from steganography_checker import check_steganography
from file_integrity import hash_file

app = Flask(__name__)
app.secret_key = "supersecretkey"

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "pdf"}

def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/upload", methods=["POST"])
def upload_file():
    if "file" not in request.files:
        flash("No file part")
        return redirect(url_for("index"))

    file = request.files["file"]

    if file.filename == "":
        flash("No selected file")
        return redirect(url_for("index"))

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config["UPLOAD_FOLDER"], filename)
        file.save(file_path)

        return redirect(url_for("analyze_file", filename=filename))
    
    flash("Invalid file type")
    return redirect(url_for("index"))

@app.route("/analyze/<filename>")
def analyze_file(filename):
    file_path = os.path.join(app.config["UPLOAD_FOLDER"], filename)

    # Extract metadata
    metadata = extract_metadata(file_path) if filename.endswith(("png", "jpg", "jpeg")) else "Not an image file"

    # Check steganography (for images only)
    stego_result = check_steganography(file_path) if filename.endswith(("png", "jpg", "jpeg")) else "Not an image file"

    # File integrity check
    md5_hash = hash_file(file_path, "md5")
    sha1_hash = hash_file(file_path, "sha1")
    sha256_hash = hash_file(file_path, "sha256")

    return render_template("results.html", filename=filename, metadata=metadata, stego_result=stego_result, 
                           md5_hash=md5_hash, sha1_hash=sha1_hash, sha256_hash=sha256_hash)

if __name__ == "__main__":
    app.run(debug=True)
