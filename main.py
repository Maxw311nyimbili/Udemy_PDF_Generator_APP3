from fpdf import FPDF
import pandas as pd

# creating pdfs

pdf = FPDF(orientation="P", unit="mm", format="A4")

df = pd.read_csv("topics.csv")  # make a pandas file

# use a for-loop to iterate through all the rows of the topic.csv file
# use two variables to get to the elements as it separates the index of the rows and the actual rows themselves
for index, row in df.iterrows():
    # adds a page
    pdf.add_page()

    pdf.set_font(family="Times", style="B", size=24)  # this font is inherited by all lines below this line of code
    pdf.cell(w=0, h=12, txt=row["Topic"], align="L", ln=1)
    pdf.line(10.0, 21.0, 200.0, 21.0)

pdf.output("output.pdf")
