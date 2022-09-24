import fpdf


def main():
    get_pdf(input("Name: "))


def get_pdf(name):
    pdf = fpdf.FPDF(orientation="portrait", format="A4")
    pdf.add_page()
    pdf.set_y(pdf.eph/6)
    pdf.set_font("Helvetica", size=48)
    pdf.cell(0, 0 ,txt="CS50 Shirtificate", align="C", new_x="LMARGIN", new_y="NEXT")
    pdf.image("shirtificate.png", w=pdf.epw, y=pdf.eph/4)
    pdf.set_y(pdf.eph/2)
    pdf.set_font("Helvetica", size=24)
    pdf.set_text_color(255, 255 , 255)
    pdf.cell(0, 0, txt=f"{name} took CS50", align = "C")
    pdf.output("shirtificate.pdf")


if __name__ == "__main__":
    main()