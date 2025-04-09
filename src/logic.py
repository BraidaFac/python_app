import pdfplumber
import re
def formato_monto(valor):
    return "{:,.2f}".format(valor).replace(",", "X").replace(".", ",").replace("X", ".")

def extract_and_sum_amounts(pdf_files):
    total_importe_neto_de_pagos = 0
    total_arancel = 0
    total_ventas_c_dto_financiamiento = 0
    total_promo_cuota = 0
    total_retencion = 0
    total_iva_promo_cuota = 0
    total_iva_cred_fisc = 0
    total_cargo_sistema_cuotas = 0
    total_iva_ri_sist_cuotas = 0
    total_iva_ri_cred_fisc = 0
    total_iva_ri_cred_sobre_arancel = 0
    total_ventas_c_dto_contado = 0
    total_desc_financ_otorg = 0
    # Patrón para capturar el monto después de "IMPORTE NETO DE PAGOS"
    pattern_importe_neto_de_pagos = r"IMPORTE NETO DE PAGOS\s+\$\s*(?:\d{1,3}(?:,\d{3})*|\d+)(?:\.|\,)\d{2}"
    pattern_arancel = r"ARANCEL\s+\$\s*(?:\d{1,3}(?:,\d{3})*|\d+)(?:\.|\,)\d{2}"
    pattern_ventas_c_dto_financiamiento = r"VENTAS C/DTO CUOTAS FINANC. OTORG.\s+\$\s*(?:\d{1,3}(?:,\d{3})*|\d+)(?:\.|\,)\d{2}"
    pattern_promo_cuota = r"PROMO CUOTA AHORA/SIMPLE\s+\$\s*(?:\d{1,3}(?:,\d{3})*|\d+)(?:\.|\,)\d{2}"
    pattern_retencion = r"RETENCION ING.BRUTOS SANTA FE\s+\$\s*(?:\d{1,3}(?:,\d{3})*|\d+)(?:\.|\,)\d{2}"
    pattern_iva_promo_cuota = r"IVA PROMO CUOTA AHORA/SIMPLE 10,50%\s+\$\s*(?:\d{1,3}(?:,\d{3})*|\d+)(?:\.|\,)\d{2}"
    pattern_iva_cred_fisc = r"IVA CRED.FISC.COM.L.25063 S/DTO F.OTOR 10,50%\s+\$\s*(?:\d{1,3}(?:,\d{3})*|\d+)(?:\.|\,)\d{2}"
    pattern_cargo_sistema_cuotas = r"CARGO SISTEMA CUOTAS MENS\s+\$\s*(?:\d{1,3}(?:,\d{3})*|\d+)(?:\.|\,)\d{2}"
    pattern_iva_ri_sist_cuotas = r"IVA RI SIST CUOTAS\s+\$\s*(?:\d{1,3}(?:,\d{3})*|\d+)(?:\.|\,)\d{2}"
    pattern_iva_ri_cred_fisc = r"IVA RI CRED.FISC.COMERCIO S/DTO F.OTORG\s+\$\s*(?:\d{1,3}(?:,\d{3})*|\d+)(?:\.|\,)\d{2}"
    pattern_iva_ri_cred_sobre_arancel = r"IVA CRED.FISC.COMERCIO S/ARANC 21,00%\s+\$\s*(?:\d{1,3}(?:,\d{3})*|\d+)(?:\.|\,)\d{2}"
    pattern_ventas_c_dto_contado = r"VENTAS C/DESCUENTO CONTADO\s+\$\s*(?:\d{1,3}(?:,\d{3})*|\d+)(?:\.|\,)\d{2}"
    pattern_desc_financ_otorg = r"DESCUENTO FINANC.OTORG. CUOTAS\s+\$\s*(?:\d{1,3}(?:,\d{3})*|\d+)(?:\.|\,)\d{2}"
    # Patrón para extraer solo el monto de la línea
    amount_pattern = r"\$\s*\d{1,3}(?:\.\d{3})*(?:,\d{2})"
    for pdf_file in pdf_files:
        with pdfplumber.open(pdf_file) as pdf:
            for page in pdf.pages:
                text = page.extract_text()
                if text:
                    lines = text.split("\n")
                    for line in lines:
                        # Buscar líneas que contengan "IMPORTE NETO DE PAGOS"
                        if re.search(pattern_desc_financ_otorg, line):
                            print("Línea encontrada:", line)  # Para depuración
                            # Extraer el monto de la línea
                            match = re.search(amount_pattern, line)
                            if match:
                                amount = match.group(0)
                                print(amount)
                                # Limpiar el monto
                                cleaned_amount = amount.replace("$", "").replace(" ", "").replace(".", "")
                                cleaned_amount = cleaned_amount.replace(",", ".")
                                print(f"Monto extraído: {amount} -> {cleaned_amount}")  # Para depuración
                                try:
                                    total_desc_financ_otorg += float(cleaned_amount)
                                except ValueError:
                                    print(f"Error al convertir: {cleaned_amount}")
                                    
                        if re.search(pattern_importe_neto_de_pagos, line):
                            print("Línea encontrada:", line)  # Para depuración
                            # Extraer el monto de la línea
                            match = re.search(amount_pattern, line)
                            if match:
                                amount = match.group(0)
                                print(amount)
                                # Limpiar el monto
                                cleaned_amount = amount.replace("$", "").replace(" ", "").replace(".", "")
                                cleaned_amount = cleaned_amount.replace(",", ".")
                                print(f"Monto extraído: {amount} -> {cleaned_amount}")  # Para depuración
                                try:
                                    total_importe_neto_de_pagos += float(cleaned_amount)
                                except ValueError:
                                    print(f"Error al convertir: {cleaned_amount}")
                         
                        if re.search(pattern_ventas_c_dto_contado, line):
                            print("Línea encontrada:", line)  # Para depuración
                            # Extraer el monto de la línea
                            match = re.search(amount_pattern, line)
                            if match:
                                amount = match.group(0)
                                print(amount)
                                # Limpiar el monto
                                cleaned_amount = amount.replace("$", "").replace(" ", "").replace(".", "")
                                cleaned_amount = cleaned_amount.replace(",", ".")
                                print(f"Monto extraído: {amount} -> {cleaned_amount}")  # Para depuración
                                try:
                                    total_ventas_c_dto_contado += float(cleaned_amount)
                                except ValueError:
                                    print(f"Error al convertir: {cleaned_amount}")
                                    
                        if re.search(pattern_arancel, line):
                            print("Línea encontrada:", line)  # Para depuración
                            # Extraer el monto de la línea
                            match = re.search(amount_pattern, line)
                            if match:
                                amount = match.group(0)
                                print(amount)
                                # Limpiar el monto
                                cleaned_amount = amount.replace("$", "").replace(" ", "").replace(".", "")
                                cleaned_amount = cleaned_amount.replace(",", ".")
                                print(f"Monto extraído: {amount} -> {cleaned_amount}")  # Para depuración
                                try:
                                    total_arancel += float(cleaned_amount)
                                except ValueError:
                                    print(f"Error al convertir: {cleaned_amount}")
                            
                        if re.search(pattern_ventas_c_dto_financiamiento, line):
                            print("Línea encontrada:", line)  # Para depuración
                            # Extraer el monto de la línea
                            match = re.search(amount_pattern, line)
                            if match:   
                                amount = match.group(0)
                                print(amount)
                                # Limpiar el monto
                                cleaned_amount = amount.replace("$", "").replace(" ", "").replace(".", "")
                                cleaned_amount = cleaned_amount.replace(",", ".")
                                print(f"Monto extraído: {amount} -> {cleaned_amount}")  # Para depuración
                                try:
                                    total_ventas_c_dto_financiamiento += float(cleaned_amount)
                                except ValueError:
                                    print(f"Error al convertir: {cleaned_amount}")                    
                                    
                        if re.search(pattern_promo_cuota, line):
                            print("Línea encontrada:", line)  # Para depuración
                            # Extraer el monto de la línea
                            match = re.search(amount_pattern, line)
                            if match:   
                                amount = match.group(0)
                                print(amount)
                                # Limpiar el monto
                                cleaned_amount = amount.replace("$", "").replace(" ", "").replace(".", "")
                                cleaned_amount = cleaned_amount.replace(",", ".")
                                print(f"Monto extraído: {amount} -> {cleaned_amount}")  # Para depuración
                                try:
                                    total_promo_cuota += float(cleaned_amount)
                                except ValueError:
                                    print(f"Error al convertir: {cleaned_amount}")   
                                    
                        if re.search(pattern_retencion, line):
                            print("Línea encontrada:", line)  # Para depuración
                            # Extraer el monto de la línea
                            match = re.search(amount_pattern, line)
                            if match:   
                                amount = match.group(0)
                                print(amount)
                                # Limpiar el monto
                                cleaned_amount = amount.replace("$", "").replace(" ", "").replace(".", "")
                                cleaned_amount = cleaned_amount.replace(",", ".")
                                print(f"Monto extraído: {amount} -> {cleaned_amount}")  # Para depuración
                                try:
                                    total_retencion += float(cleaned_amount)
                                except ValueError:
                                    print(f"Error al convertir: {cleaned_amount}")    
                                    
                        if re.search(pattern_iva_promo_cuota, line):
                            print("Línea encontrada:", line)  # Para depuración
                            # Extraer el monto de la línea
                            match = re.search(amount_pattern, line)
                            if match:   
                                amount = match.group(0)
                                print(amount)
                                # Limpiar el monto
                                cleaned_amount = amount.replace("$", "").replace(" ", "").replace(".", "")
                                cleaned_amount = cleaned_amount.replace(",", ".")
                                print(f"Monto extraído: {amount} -> {cleaned_amount}")  # Para depuración
                                try:
                                    total_iva_promo_cuota += float(cleaned_amount)
                                except ValueError:
                                    print(f"Error al convertir: {cleaned_amount}")   
                                    
                        if re.search(pattern_iva_cred_fisc, line):
                            print("Línea encontrada:", line)  # Para depuración
                            # Extraer el monto de la línea
                            match = re.search(amount_pattern, line)
                            if match:   
                                amount = match.group(0)
                                print(amount)
                                # Limpiar el monto
                                cleaned_amount = amount.replace("$", "").replace(" ", "").replace(".", "")
                                cleaned_amount = cleaned_amount.replace(",", ".")
                                print(f"Monto extraído: {amount} -> {cleaned_amount}")  # Para depuración   
                                try:
                                    total_iva_cred_fisc += float(cleaned_amount)
                                except ValueError:
                                    print(f"Error al convertir: {cleaned_amount}")   
                        if re.search(pattern_cargo_sistema_cuotas, line):
                            print("Línea encontrada:", line)  # Para depuración
                            # Extraer el monto de la línea
                            match = re.search(amount_pattern, line)
                            if match:      
                                amount = match.group(0)
                                print(amount)
                                # Limpiar el monto
                                cleaned_amount = amount.replace("$", "").replace(" ", "").replace(".", "")
                                cleaned_amount = cleaned_amount.replace(",", ".")
                                print(f"Monto extraído: {amount} -> {cleaned_amount}")  # Para depuración      
                                try:
                                    total_cargo_sistema_cuotas += float(cleaned_amount)
                                except ValueError:
                                    print(f"Error al convertir: {cleaned_amount}")   
                        if re.search(pattern_iva_ri_sist_cuotas, line):
                            print("Línea encontrada:", line)  # Para depuración
                            # Extraer el monto de la línea
                            match = re.search(amount_pattern, line)
                            if match:      
                                amount = match.group(0)
                                print(amount)
                                # Limpiar el monto
                                cleaned_amount = amount.replace("$", "").replace(" ", "").replace(".", "")
                                cleaned_amount = cleaned_amount.replace(",", ".")
                                print(f"Monto extraído: {amount} -> {cleaned_amount}")  # Para depuración                     
                                try:
                                    total_iva_ri_sist_cuotas += float(cleaned_amount)
                                except ValueError:
                                    print(f"Error al convertir: {cleaned_amount}")   
                        if re.search(pattern_iva_ri_cred_fisc, line):
                            print("Línea encontrada:", line)  # Para depuración
                            # Extraer el monto de la línea
                            match = re.search(amount_pattern, line)
                            if match:      
                                amount = match.group(0)
                                print(amount)
                                # Limpiar el monto
                                cleaned_amount = amount.replace("$", "").replace(" ", "").replace(".", "")
                                cleaned_amount = cleaned_amount.replace(",", ".")
                                print(f"Monto extraído: {amount} -> {cleaned_amount}")  # Para depuración                     
                                try:
                                    total_iva_ri_cred_fisc += float(cleaned_amount)
                                except ValueError:
                                    print(f"Error al convertir: {cleaned_amount}")   
                        if re.search(pattern_iva_ri_cred_sobre_arancel, line):
                            print("Línea encontrada:", line)  # Para depuración
                            # Extraer el monto de la línea
                            match = re.search(amount_pattern, line)
                            if match:      
                                amount = match.group(0)
                                print(amount)
                                # Limpiar el monto
                                cleaned_amount = amount.replace("$", "").replace(" ", "").replace(".", "")
                                cleaned_amount = cleaned_amount.replace(",", ".")
                                print(f"Monto extraído: {amount} -> {cleaned_amount}")  # Para depuración                     
                                try:
                                    total_iva_ri_cred_sobre_arancel += float(cleaned_amount)
                                except ValueError:
                                    print(f"Error al convertir: {cleaned_amount}")   
                                    
                                

    total_ventas = total_ventas_c_dto_financiamiento + total_ventas_c_dto_contado
    total_comisiones = total_arancel +  total_promo_cuota  + total_cargo_sistema_cuotas  + total_desc_financ_otorg
    total_iva = total_iva_ri_cred_fisc + total_iva_ri_cred_sobre_arancel + total_iva_ri_sist_cuotas + total_iva_promo_cuota + total_iva_cred_fisc + total_cargo_sistema_cuotas
    total_retenciones = total_retencion
    total_neto = total_ventas - total_comisiones - total_iva - total_retenciones
    
    
    total_importe_neto_de_pagos = formato_monto(total_importe_neto_de_pagos)
    total_arancel = formato_monto(total_arancel)
    total_ventas_c_dto_financiamiento = formato_monto(total_ventas_c_dto_financiamiento)
    total_promo_cuota = formato_monto(total_promo_cuota)
    total_retencion = formato_monto(total_retencion)
    total_iva_promo_cuota = formato_monto(total_iva_promo_cuota)
    total_iva_cred_fisc = formato_monto(total_iva_cred_fisc)
    total_cargo_sistema_cuotas = formato_monto(total_cargo_sistema_cuotas)
    total_iva_ri_sist_cuotas = formato_monto(total_iva_ri_sist_cuotas)
    total_iva_ri_cred_fisc = formato_monto(total_iva_ri_cred_fisc)
    total_iva_ri_cred_sobre_arancel = formato_monto(total_iva_ri_cred_sobre_arancel)
    total_ventas_c_dto_contado = formato_monto(total_ventas_c_dto_contado)
    total_ventas = formato_monto(total_ventas)
    total_comisiones = formato_monto(total_comisiones)
    total_iva = formato_monto(total_iva)
    total_retenciones = formato_monto(total_retenciones)
    total_neto = formato_monto(total_neto)
    total_desc_financ_otorg = formato_monto(total_desc_financ_otorg)
    
    
    
    
    #Haceme un mensaje con un titulo para cada total
    mensaje = "📊 RESUMEN DE TOTALES\n\n"
    mensaje += "💳 VENTAS C/DTO CUOTAS FINANC. OTORG.\n"
    mensaje += f"${total_ventas_c_dto_financiamiento}\n\n"
    mensaje += "💵 VENTAS C/DTO CONTADO\n"
    mensaje += f"${total_ventas_c_dto_contado}\n\n\n"
    
    mensaje += "💵 ARANCEL\n"
    mensaje += f"${total_arancel}\n\n"
    mensaje += "📎 IVA RI CRED.FISC.COMERCIO S/ARANC 21,00%\n"
    mensaje += f"${total_iva_ri_cred_sobre_arancel}\n\n"
    mensaje += "💵 DESCUENTO FINANC.OTORG. CUOTAS\n"
    mensaje += f"${total_desc_financ_otorg}\n\n"
    mensaje += "🎯 PROMO CUOTA/SIMPLE\n"
    mensaje += f"${total_promo_cuota}\n\n"
    mensaje += "📋 IVA PROMO CUOTA AHORA/SIMPLE 10,50%\n"
    mensaje += f"${total_iva_promo_cuota}\n\n"
    mensaje += "📄 IVA CRED.FISC.COM.L.25063 S/DTO F.OTOR 10,50%\n"
    mensaje += f"${total_iva_cred_fisc}\n\n"
    mensaje += "📎 IVA RI CRED.FISC.COMERCIO S/DTO F.OTORG\n"
    mensaje += f"${total_iva_ri_cred_fisc}\n\n"
    
    mensaje += "💸 CARGO SISTEMA CUOTAS MENS\n"
    mensaje += f"${total_cargo_sistema_cuotas}\n\n"
    mensaje += "📑 IVA RI SIST CUOTAS\n"
    mensaje += f"${total_iva_ri_sist_cuotas}\n\n"
    mensaje += "📝 RETENCION ING.BRUTOS SANTA FE\n"
    mensaje += f"${total_retencion}\n\n\n"
    
  
    
    mensaje += "💰 VENTAS\n"
    mensaje += f"${total_ventas}\n\n"
    mensaje += "💰 COMISIONES\n"
    mensaje += f"${total_comisiones}\n\n"
    mensaje += "💰 IVA\n"
    mensaje += f"${total_iva}\n\n"
    mensaje += "💰 RETENCIONES\n"
    mensaje += f"${total_retenciones}\n\n"
    mensaje += "💰 NETO CALCULADO\n"    
    mensaje += f"${total_neto}\n\n"
    mensaje += "💰 IMPORTE NETO DE PAGOS SEGÚN REPORTE\n"
    mensaje += f"${total_importe_neto_de_pagos}\n\n"
    
    mensaje += "🎉 ¡Proceso completado!"
    return mensaje



def process_pdfs(pdf_files):
    if not pdf_files:
        return "❌ Por favor, sube al menos un archivo PDF para procesar."
    total = extract_and_sum_amounts(pdf_files)
    return f"{total}"