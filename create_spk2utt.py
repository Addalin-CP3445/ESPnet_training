import os

# Define the function to convert utt2spk to spk2utt
def generate_spk2utt(utt2spk_path, spk2utt_path, label):
    speaker_dict = {}

    # Read utt2spk file
    with open(utt2spk_path, 'r', encoding='utf-8') as f:
        for line in f:
            parts = line.strip().split()
            if len(parts) != 2:
                continue  # Skip malformed lines
            utt, spk = parts
            speaker_dict.setdefault(spk, []).append(utt)

    # Write spk2utt file
    with open(spk2utt_path, 'w', encoding='utf-8') as f:
        for spk, utt_list in speaker_dict.items():
            f.write(f"{spk} {' '.join(utt_list)}\n")

    print(f"{label} spk2utt file has been created at: {spk2utt_path}")

# Define file paths for both train and test sets
paths = {
    "train": {
        "utt2spk": './arabic-speech-corpus/kaldi_data/train/utt2spk',
        "spk2utt": './arabic-speech-corpus/kaldi_data/train/spk2utt'
    },
    "test": {
        "utt2spk": './arabic-speech-corpus/kaldi_data/test/utt2spk',
        "spk2utt": './arabic-speech-corpus/kaldi_data/test/spk2utt'
    }
}

# Process both train and test sets
for label, path_set in paths.items():
    generate_spk2utt(path_set["utt2spk"], path_set["spk2utt"], label)
