import os
# from camel_tools.utils.transliterate import Transliterator
# from camel_tools.utils.charmap import CharMapper

# # Initialize the Buckwalter transliterator
# bw2ar = CharMapper.builtin_mapper("bw2ar")
# bt = Transliterator(bw2ar)

# Set your dataset paths (update these paths as needed)
dataset_path = './arabic-speech-corpus'  # Replace with your dataset root directory
wav_dir = os.path.join(dataset_path, 'wav')
transcript_file = os.path.join(dataset_path, 'phonetic-transcipt.txt')

# Output directory for Kaldi-style files (e.g., for training)
kaldi_data_dir = './arabic-speech-corpus/kaldi_data/train'  # Update this as needed
os.makedirs(kaldi_data_dir, exist_ok=True)

# Open output files for Kaldi-style directory
wav_scp = open(os.path.join(kaldi_data_dir, 'wav.scp'), 'w', encoding='utf-8')
text_f = open(os.path.join(kaldi_data_dir, 'text'), 'w', encoding='utf-8')
utt2spk = open(os.path.join(kaldi_data_dir, 'utt2spk'), 'w', encoding='utf-8')

# Set a default speaker ID (adjust if you have multiple speakers)
default_spk = "arabic"

with open(transcript_file, 'r', encoding='utf-8') as f:
    for line in f:
        # Remove extra quotes and split the line into fields
        # Expected format: "ARA NORM  0002.wav" "buckwalter transcription"
        parts = line.strip().split('" "')
        if len(parts) < 2:
            continue
        # Clean up the fields (remove any remaining quotes)
        utt_field = parts[0].replace('"', '').strip()
        buckwalter_transcription = parts[1].replace('"', '').strip()

        # Extract the filename from utt_field. Example: "ARA NORM  0002.wav"
        utt_filename = utt_field.split()[-1]
        # Remove the file extension to create an utterance ID (e.g., "0002")
        utt_id = os.path.splitext(utt_filename)[0]

        # Convert the Buckwalter transcription to standard Arabic script
        # arabic_transcription = bt.transliterate(buckwalter_transcription)

        # Write to wav.scp (assumes the wav files are in the wav/ directory)
        wav_path = os.path.join(wav_dir, utt_filename)
        wav_scp.write(f"{utt_id} {wav_path}\n")

        # Write the converted Arabic transcript to the text file
        text_f.write(f"{utt_id} {buckwalter_transcription}\n")

        # Write to utt2spk (assign default speaker)
        utt2spk.write(f"{utt_id} {default_spk}\n")

# Close the files
wav_scp.close()
text_f.close()
utt2spk.close()

print("Kaldi-style training data files have been created in:", kaldi_data_dir)