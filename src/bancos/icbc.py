import pdfplumber
import re

def formato_monto(valor):
    return "{:,.2f}".format(valor).replace(",", "X").replace(".", ",").replace("X", ".")

def extract_tables_from_pdf_icbc(pdf_files):
    movimientos = {}
    for pdf_file in pdf_files:
        with pdfplumber.open(pdf_file) as pdf:
            for page in pdf.pages:
                text = page.extract_text_simple()
                # Buscar líneas que contengan movimientos
                lineas = text.split('\n')
                for linea in lineas:
                    # Buscar patrones de fecha (ej: 02-12)
                    if re.match(r'\d{2}-\d{2}', linea.strip()):
                        # Extraer concepto (después de la fecha y antes del primer número)
                        concepto_match = re.search(r'^\d{2}-\d{2}\s+(.*?)(?=\s+\d)', linea)
                        concepto = concepto_match.group(1).strip() if concepto_match else ""
                        
                        # Si el concepto comienza con TR. seguido de uno o más números, lo cambiamos a CHEQUES
                        if re.match(r'TR\.\d+', concepto):
                            concepto = "TRANSFERENCIAS"
                        
                        # Extraer importes de débito y crédito
                        debito = re.search(r'(\d[\d.]*,\d{2})-', linea)
                        credito = re.search(r'(\d[\d.]*,\d{2})(?!-)', linea)
                        
                        
                        debito_valor = float(debito.group(1).replace('.', '').replace(',', '.')) if debito else 0.0
                        credito_valor = float(credito.group(1).replace('.', '').replace(',', '.')) if credito else 0.0
                        
                       

                        if debito_valor != 0 and credito_valor == 0:
                            if concepto not in movimientos:
                                movimientos[concepto] = -debito_valor
                            else:
                                movimientos[concepto] += -debito_valor
                                
                        if debito_valor == 0 and credito_valor != 0:
                            if concepto not in movimientos:
                                movimientos[concepto] = credito_valor
                            else:
                                movimientos[concepto] += credito_valor
    
    # Generar mensaje con los movimientos
    mensaje = "📊 RESUMEN DE TOTALES\n\n"
    
    # Crear un nuevo diccionario para almacenar los movimientos consolidados
    movimientos_consolidados = {}
    
    for key, value in movimientos.items():
        if key in ["TRANSFERENCIA PUSH", "TRANS PAG PROV", "TRANSF. E/BCOS-ONLINE", "TRANSFERENCIAS"]:
            if "TRANSFERENCIAS" not in movimientos_consolidados:
                movimientos_consolidados["TRANSFERENCIAS"] = value
            else:
                movimientos_consolidados["TRANSFERENCIAS"] += value
        elif key in ["TRANS DN MTITU"]:
            if "TRANSFERENCIAS MISMO TITULAR" not in movimientos_consolidados:
                movimientos_consolidados["TRANSFERENCIAS MISMO TITULAR"] = value
            else:
                movimientos_consolidados["TRANSFERENCIAS MISMO TITULAR"] += value
        elif key in ["IVA RG"]:
            movimientos_consolidados["RETENCION DE IVA"] = value
            
        elif  key in ["I V A", "IMPUESTO AL VALOR AGREGADO"]:
            if "IVA" not in movimientos_consolidados:
                movimientos_consolidados["IVA"] = value
            else:
                movimientos_consolidados["IVA"] += value
        elif key in ["COM MVO EFVO O"]:
                movimientos_consolidados["COMISION MOVIMIENTO EFECTIVO"] = value
        else:
            movimientos_consolidados[key] = value
    
    
    #ordenar los items por el valor de mayor a menor
    movimientos_consolidados = dict(sorted(movimientos_consolidados.items(), key=lambda x: x[1], reverse=True))
    
    for key, value in movimientos_consolidados.items():
        emoji = "💸" if value < 0 else "💰"
        mensaje += f"{emoji} {key}\n"
        mensaje += f"${formato_monto(value)}\n\n"

    return mensaje

    
   
