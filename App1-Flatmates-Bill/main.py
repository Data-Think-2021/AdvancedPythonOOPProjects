from flat import Bill, Flatmate
from reports import PdfReport, FileSharer

the_bill = Bill(float(input("The total bill: ")), input("Period: "))

flatmate1 = Flatmate(input("Your name: "), float(input("days in house: ")))
flatmate2 = Flatmate(input("Your flatmate: "), float(input("days in house: ")))

pdf_report = PdfReport(filename=f"{the_bill.period}.pdf")
pdf_report.generate(flatmate1, flatmate2, the_bill)

file_sharer = FileSharer(filepath=pdf_report.filename)
print(file_sharer.share())
