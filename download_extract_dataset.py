import os
import zipfile
import urllib.request

# Define the URL and output path
url = "https://en.arabicspeechcorpus.com/arabic-speech-corpus.zip"
zip_path = "./arabic-speech-corpus.zip"
extract_path = "./"

# Download the dataset
print("Downloading dataset...")
urllib.request.urlretrieve(url, zip_path)
print("Download complete.")

# Unzip the dataset
print("Extracting files...")
with zipfile.ZipFile(zip_path, 'r') as zip_ref:
    zip_ref.extractall(extract_path)

print("Extraction complete.")

# List extracted files
print(os.listdir(extract_path))

# Remove the zip file
os.remove(zip_path)
print(f"Removed {zip_path}")