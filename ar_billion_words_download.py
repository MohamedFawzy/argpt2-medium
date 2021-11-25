from datasets import load_dataset
import datasets

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

for src in src_lst:
    load_dataset("arabic_billion_words", src)

# dataset_Alittihad = load_dataset("arabic_billion_words", "Alittihad")

# print(dataset_Alittihad["train"]["text"][0])
