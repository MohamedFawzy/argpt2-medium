from pathlib import Path
import os

# the folder 'text' contains all the files
paths = [str(x) for x in Path("./ar_corpus/").glob("**/*.txt")]
