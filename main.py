from fpdf import FPDF
import pandas as pd

# creating pdfs

pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)

df = pd.read_csv("topics.csv")  # make a pandas file

# use a for-loop to iterate through all the rows of the topic.csv file
# use two variables to get to the elements as it separates the index of the rows and the actual rows themselves
for index, row in df.iterrows():
    # adds a page
    pdf.add_page()

    # add header
    pdf.set_font(family="Times", style="B", size=24)  # this font is inherited by all lines below this line of code
    pdf.cell(w=0, h=12, txt=row["Topic"], align="L", ln=1)
    pdf.line(10.0, 21.0, 200.0, 21.0)

    x = 0
    for i in range(26):
        x = x + 10
        pdf.line(10.0, 21.0 + x, 200.0, 21.0 + x)
        pdf.ln(1)

    # add footer
    pdf.ln(235)
    pdf.set_font(family="Times", style="I", size=12)
    pdf.cell(w=0, h=8, txt=row["Topic"], align="R")

    for i in range(row["Pages"] - 1):
        pdf.add_page()

        y = 0
        for j in range(26):
            y = y + 10
            pdf.line(10.0, 21.0 + y, 200.0, 21.0 + y)
            pdf.ln(1)

        # add footer
        pdf.ln(248)
        pdf.set_font(family="Times", style="I", size=12)
        pdf.cell(w=0, h=8, txt=row["Topic"], align="R")


pdf.output("output.pdf")
