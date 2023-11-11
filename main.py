import os
import tabula
from tabula import read_pdf

directory = "C:\Users\asus\CodeMusketeers"

for filename in os.listdir(directory):
    if filename.endswith(".pdf"):
        file_path = os.path.join(directory, filename)

        dfs = read_pdf(file_path, pages="all")
        tabula.convert_into(file_path, "output.csv", output_format="csv", pages="all")
