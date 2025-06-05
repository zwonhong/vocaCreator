from fpdf import FPDF
import random

FONT_PATH = "NotoSansKR-Regular.ttf"

class PDF(FPDF):
    def header(self):
        self.set_font("Noto", "", 14)
        self.cell(0, 10, "영어 단어 시험지", ln=True, align="C")
        self.ln(10)

    def footer(self):
        self.set_y(-15)
        self.set_font("Noto", "", 10)
        self.cell(0, 10, f"Page {self.page_no()}", align="C")

with open("vocab.txt", "r", encoding="utf-8") as f:
    lines = [line.strip() for line in f if line.strip()]
random.shuffle(lines)

pdf = PDF()
pdf.add_font("Noto", "", FONT_PATH, uni=True)

pdf.add_page()
pdf.set_font("Noto", "", 12)

pdf.set_fill_color(200, 220, 255)
pdf.cell(60, 10, "English", border=1, align="C", fill=True)
pdf.cell(130, 10, "뜻", border=1, align="C", fill=True)
pdf.ln()

for idx, line in enumerate(lines, 1):
    try:
        eng, kor = line.split(maxsplit=1)
    except ValueError:
        continue
    pdf.cell(60, 10, f"{idx}.", border=1)
    pdf.cell(130, 10, kor, border=1)
    pdf.ln()

pdf.add_page()
pdf.set_font("Noto", "", 12)
pdf.cell(60, 10, "English", border=1, align="C", fill=True)
pdf.cell(130, 10, "뜻", border=1, align="C", fill=True)
pdf.ln()

for idx, line in enumerate(lines, 1):
    try:
        eng, kor = line.split(maxsplit=1)
    except ValueError:
        continue
    pdf.cell(60, 10, f"{idx}. {eng}", border=1)
    pdf.cell(130, 10, kor, border=1)
    pdf.ln()

pdf.output("단어시험지한글버전.pdf")
