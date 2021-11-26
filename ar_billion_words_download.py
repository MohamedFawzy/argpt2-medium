from datasets import load_dataset
from tqdm import tqdm

"""
Download 1.5 billion words dataset from different news websites datasource using huggingface library
"""

"""
Alittihad	349342
Almasryalyoum	291723
Almustaqbal	446873
Alqabas	817274
Echoroukonline	139732
Ryiadh	858188
Sabanews	92149
SaudiYoum	888068
Techreen	314597
Youm7	1172136
"""

src_lst = [
    "Alittihad",
    "Almasryalyoum",
    "Almustaqbal",
    "Alqabas",
    "Echoroukonline",
    "Ryiadh",
    "Sabanews",
    "SaudiYoum",
    "Techreen",
    "Youm7",
]

single_string = ""
for src in src_lst:
    dataset = load_dataset("arabic_billion_words", src)
    for row in tqdm(dataset["train"]["text"]):
        single_string = row.strip()
        with open("data.txt", "a") as file_handle:
            file_handle.write(single_string)
            file_handle.write("\n")
