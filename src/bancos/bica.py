import pdfplumber
import re
def formato_monto(valor):
    return "{:,.2f}".format(valor).replace(",", "X").replace(".", ",").replace("X", ".")

def extract_tables_from_pdf(pdf_files):
    for pdf_file in pdf_files:
        with pdfplumber.open(pdf_file) as pdf:
            total = {}
            for page in pdf.pages:
            # Ajusta la estrategia de extracción (ej: "text" o "lines")
                table = page.extract_table({
                    "vertical_strategy": "lines",  # o   "lines" si hay bordes visibles
                    "horizontal_strategy": "lines",
                    "snap_tolerance": 20,          # Tolerancia para alinear texto
                })
                if table:
                    table = table[1:]
                    for row in table:
                        montoString = row[5]
                        monto = float(montoString.replace(",", "").replace("+", ""))
                        if row[3] not in total:
                            total[row[3]] = monto
                        else:
                            total[row[3]] += monto
   
    mensaje = "📊 RESUMEN DE TOTALES\n\n"
    for key, value in total.items():
        key_limpio = key.replace('\n', ' ') if '\n' in key else key
        mensaje += f"💰 {key_limpio}\n"
        mensaje += f"${formato_monto(value)}\n\n"
     

    return mensaje

    
   
