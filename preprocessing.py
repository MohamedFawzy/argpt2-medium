from pathlib import Path
import os
import tqdm

tokenizer_tokens = {
    "eos_token": "</s>",
    "bos_token": "<s>",
    "unk_token": "<unk>",
    "pad_token": "<pad>",
    "mask_token": "<mask>",
}
# the folder 'text' contains all the files
paths = [str(x) for x in Path("./ar_corpus/").glob("**/*.txt")]
single_string = ""
for filename in tqdm.tqdm(paths):
    with open(filename, "r", encoding="utf-8") as f:
        x = f.read()
    single_string += x + tokenizer_tokens.get("eos_token")
with open("data.txt", "w") as file_handle:
    file_handle.write(single_string)

