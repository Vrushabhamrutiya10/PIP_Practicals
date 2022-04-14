from fpdf import FPDF

pdf = FPDF()
pdf.add_page()

pdf.set_font("Arial", size=15)

pdf.cell(200, 10, txt="Name: VRUSHABH AMRUTIYA", ln=1, align='C')
pdf.cell(200, 10, txt="ID: 20CS004", ln=2, align='C')
pdf.cell(200, 10, txt="Practical 10", ln=4, align='C')
pdf.cell(200, 10, txt="RESULT", ln=6, align='C')
pdf.cell(200, 10, txt="CA224 INTRODUCTION TO WEB DESIGNING                AA", ln=7, align='C')
pdf.cell(200, 10, txt="CE244 SGP-I                                        AB", ln=8, align='C')
pdf.cell(200, 10, txt="CE251 Java Programming                             AB", ln=9, align='C')
pdf.cell(200, 10, txt="CE251 Java Programming(Practical)                  BB", ln=10, align='C')
pdf.cell(200, 10, txt="CE252 Digital Electronics                          AB", ln=11, align='C')
pdf.cell(200, 10, txt="CE252 Digital Electronics(Practical)               AB", ln=12, align='C')
pdf.cell(200, 10, txt="CE257 Data Communicatons & Networking              AB", ln=13, align='C')
pdf.cell(200, 10, txt="CE257 Data Communicatons & Networking(Practical)   AA", ln=14, align='C')
pdf.cell(200, 10, txt="HS121 Creativity,Problem Solving & Innovative      AA", ln=15, align='C')
pdf.cell(200, 10, txt="MA253 Discrete Mathematics & Algebra               AA", ln=16, align='C')
pdf.cell(200, 10, txt="CGPA: 9.05         SGPA:9.29", ln=18, align='C')


pdf.output("20CS004_Practical_10.pdf")
