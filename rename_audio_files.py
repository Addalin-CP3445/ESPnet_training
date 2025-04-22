import os

# Set the directory where your wav files are stored
test_wav_directory = './arabic-speech-corpus/test set/wav'  
train_wav_directory = './arabic-speech-corpus/wav'

# Define the prefix to remove
prefix = "ARA NORM  "

# Function to rename files in a given directory
def rename_wav_files(directory):
    for filename in os.listdir(directory):
        if filename.startswith(prefix):
            # Remove the prefix
            new_filename = filename[len(prefix):]
            old_filepath = os.path.join(directory, filename)
            new_filepath = os.path.join(directory, new_filename)
            print(f"Renaming: {old_filepath} -> {new_filepath}")
            os.rename(old_filepath, new_filepath)

# Rename files in both directories
rename_wav_files(test_wav_directory)
rename_wav_files(train_wav_directory)

print("Renaming of testing and training audio files complete!")