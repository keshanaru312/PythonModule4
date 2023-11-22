#!/usr/bin/env python3
import os


def generate_report(attachment, title, paragraph):

  from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, Image
  report = SimpleDocTemplate(attachment)

  # from reportlab.platypus import Paragraph, Spacer, Table, Image
  from reportlab.lib.styles import getSampleStyleSheet
  styles = getSampleStyleSheet()

  table_data = []
  for fruit in paragraph:
    table_data.append([])
    for k, v in fruit.items():
      table_data.append([k, v])

  report_title = Paragraph(title, styles["h1"])
  report_table = Table(data=table_data, hAlign="LEFT")

  if not os.path.exists('../tmp'):
    os.makedirs('../tmp')
  report.build([report_title, report_table])

  # print(fruit["name:"])
  # table_data.append("name: {}<br/>weight: {}\n".format(fruit["name:"], fruit["weight:"]))
  # print(table_data)