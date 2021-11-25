from pathlib import Path
import os
import tqdm

# the folder 'text' contains all the files
paths = [str(x) for x in Path("./ar_corpus/").glob("**/*.txt")]
single_string = ""
for filename in tqdm.tqdm(paths):
    with open(filename, "r", encoding="utf-8") as f:
        x = f.read()
    single_string += x
with open("data.txt", "w") as file_handle:
    file_handle.write(single_string)

