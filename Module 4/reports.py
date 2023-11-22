#!/usr/bin/env python3
import os
from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer, Table, Image
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors


def generate_report_table(attachment, title, paragraph):
    styles = getSampleStyleSheet()
    report = SimpleDocTemplate(attachment)
    report_title = Paragraph(title, styles["h1"])
    empty_line = Spacer(1, 20)

    table_data = []
    for fruit in paragraph:
        # table_data.append([])
        for k, v in fruit.items():
            table_data.append([k, v])

    report_table = Table(data=table_data, hAlign="LEFT")

    if not os.path.exists('./tmp'):
        os.makedirs('./tmp')

    report.build([report_title, empty_line, report_table])


def generate_report(attachment, title, paragraph):
    styles = getSampleStyleSheet()
    report = SimpleDocTemplate(attachment)
    report_title = Paragraph(title, styles["h1"])
    report_info = Paragraph(paragraph, styles["BodyText"])
    empty_line = Spacer(1, 20)

    if not os.path.exists('./tmp'):
        os.makedirs('./tmp')

    report.build([report_title, empty_line, report_info])
