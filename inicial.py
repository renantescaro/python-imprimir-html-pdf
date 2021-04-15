import os    
import pdfkit

# pdfkit.from_string('teste sla o que Renan K Digital','relatorio.pdf')
pdfkit.from_file('teste.html','relatorio.pdf')

#os.startfile('relatorio.pdf', 'print')