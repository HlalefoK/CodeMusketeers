import tabula
from tabula import read_pdf

dfs = read_pdf("C:/Users/asus/umnothoAI/statement.pdf", pages="all")
tabula.convert_into("C:/Users/asus/umnothoAI/statement.pdf", "output.csv", output_format="csv", pages="all")
