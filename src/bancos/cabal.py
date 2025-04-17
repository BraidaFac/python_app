import pdfplumber
import re

def formato_monto(valor):
    return "{:,.2f}".format(valor).replace(",", "X").replace(".", ",").replace("X", ".")

def extract_tables_from_pdf_cabal(pdf_files):
    movimientos = {}

    for pdf_file in pdf_files:
        with pdfplumber.open(pdf_file) as pdf:
            for page in pdf.pages:
                text = page.extract_text()
                if not text:
                    continue
                lineas = text.split('\n')
                procesar = False
                for linea in lineas:
                    if "TOT. FEC. PAGO" in linea:
                        procesar = True

                    if procesar:
                        # Buscar todos los importes (positivo o negativo)
                        importes = re.findall(r'(\d[\d.]*,\d{2})(?:−|-)?', linea)
                        signo_negativo = bool(re.search(r'(\d[\d.]*,\d{2})(?:−|-)\s*$', linea))

                        if importes:
                            # Último importe = el que importa
                            monto_raw = importes[-1]
                            monto = float(monto_raw.replace('.', '').replace(',', '.'))
                            if signo_negativo:
                                monto = -monto

                            # Concepto = texto antes del primer importe
                            primera_pos = linea.find(importes[0])
                            concepto = linea[:primera_pos].strip()
                            
                            
                            if "TOT. FEC. PAGO" in linea:
                                concepto = "TOTAL DE VENTAS"
                            else:
                                concepto = concepto.split(".")[0]
                            

                            if concepto in movimientos:
                                movimientos[concepto] += monto
                            else:
                                movimientos[concepto] = monto
                                                  
                        if "IMPORTE NETO FINAL A LIQUIDAR" in linea:
                            procesar = False
                            continue

    
    movimientos = dict(sorted(movimientos.items(), key=lambda x: x[1], reverse=True))
    
    movimientos_consolidados = {}
    for key, value in movimientos.items():
        if key in ["−IVA", "IVA S/ARANCEL + COSTO FINANCIERO"]:
            if "IVA" not in movimientos_consolidados:
                movimientos_consolidados["IVA"] = value
            else:
                movimientos_consolidados["IVA"] += value
        else:
            movimientos_consolidados[key] = value
    # Generar mensaje
    mensaje = "📊 RESUMEN DE LIQUIDACIÓN\n\n"
    
    for concepto, valor in movimientos_consolidados.items():
        emoji = "💸" if valor < 0 else "💰"
        mensaje += f"{emoji} {concepto}\n"
        mensaje += f"${formato_monto(valor)}\n\n"

    return mensaje