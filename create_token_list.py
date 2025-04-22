import os

kaldi_data_dir = "./arabic-speech-corpus/kaldi_data/train"

token_set = set()
text_path = os.path.join(kaldi_data_dir, 'text')
with open(text_path, 'r', encoding='utf-8') as f:
    for line in f:
        parts = line.strip().split(maxsplit=1)
        if len(parts) == 2:
            transcript = parts[1]
            token_set.update(list(transcript))

# Write token list
token_list_path = os.path.join(kaldi_data_dir, 'token_list.txt')
with open(token_list_path, 'w', encoding='utf-8') as f:
    for token in sorted(token_set):
        f.write(token + "\n")
print("Token list created at:", token_list_path)