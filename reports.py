import os
import webbrowser
from filestack import Client
from fpdf import FPDF


class PdfReport:
    """
    Create a Pdf file that contains data about the flatmates such their name,
    due amount and the period of the bill.
    """

    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatmate1, flatmate2, bill):
        pdf = FPDF(orientation="P", unit="pt", format="A4")
        pdf.add_page()

        # Insert logo
        pdf.image("files/house.png", w=30, h=30)

        # Insert title
        pdf.set_font(family="Times", size=24, style="B")
        pdf.cell(w=0, h=88, txt="Flatmates Bill", border=0, align="C", ln=1)

        # Insert Period label and value
        pdf.set_font(family="Times", size=14, style="B")
        pdf.cell(w=100, h=40, txt="Period:", border=0)
        pdf.cell(w=150, h=40, txt=bill.period, border=0, ln=1)

        # Insert name and due amount of the first flatmate
        pdf.set_font(family="Times", size=14)
        pdf.cell(w=100, h=40, txt=flatmate1.name, border=0)
        pdf.cell(w=150, h=40, txt=str(round(flatmate1.pays(flatmate2, bill), 2)), border=0, ln=1)

        # Insert name and due amount of the second flatmate
        pdf.cell(w=100, h=40, txt=flatmate2.name, border=0)
        pdf.cell(w=150, h=40, txt=str(round(flatmate2.pays(flatmate1, bill), 2)), border=0, ln=1)

        os.chdir("files")
        pdf.output(self.filename)
        webbrowser.open("file:" + os.path.realpath(self.filename))   # In mac "file:" should add before the path


class FileSharer:

    def __init__(self, filepath, api_key="AVuHTCgQkRNSOgPn16okvz"):
        self.filepath = filepath
        self.api_key = api_key

    def share(self):
        client = Client(self.api_key)
        new_filelink = client.upload(filepath=self.filepath)
        return new_filelink.url

