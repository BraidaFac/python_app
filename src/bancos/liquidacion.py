import pdfplumber
import re

def formato_monto(valor):
    return "{:,.2f}".format(valor).replace(",", "X").replace(".", ",").replace("X", ".")

def extract_tables_from_pdf_liquidacion(pdf_files):
    movimientos = {}
    capturando = False
    for pdf_file in pdf_files:
        with pdfplumber.open(pdf_file) as pdf:
            for page in pdf.pages:
                text = page.extract_text_simple()
                lineas = text.split('\n')
                for linea in lineas:
                    # Si encontramos una línea que comienza con TOT. FEC. PAGO, empezamos a capturar
                    if linea.strip().startswith('TOT. FEC. PAGO:'):
                        capturando = True
                        continue
                    
                    # Si encontramos una línea de guiones bajos, dejamos de capturar
                    if re.match(r'^_+$', linea.strip()):
                        capturando = False
                        continue
                    
                    # Si estamos capturando y encontramos una línea vacía o una nueva fecha, dejamos de capturar
                    if capturando and (not linea.strip() or linea.startswith('FECHA DE PAGO')):
                        capturando = False
                        continue
                    
                    # Si estamos capturando, procesamos la línea
                    if capturando and linea.strip():
                        # Dividimos la línea por espacios y tomamos el concepto y el último valor
                        partes = linea.strip().split()
                        if len(partes) >= 2:
                            # Excluimos líneas que comienzan con TOTAL DE VENTAS
                            if partes[0] == "TOTAL":
                                continue
                                
                            concepto = ' '.join(partes[:-1])  # Todo excepto el último elemento
                            # Intentamos convertir el último elemento a un valor numérico
                            try:
                                valor_str = partes[-1].replace('.', '').replace(',', '.').replace('-', '')
                                valor = float(valor_str)
                                # Si el valor original tenía un guión, lo hacemos negativo
                                if partes[-1].endswith('-'):
                                    valor = -valor
                                
                                if concepto not in movimientos:
                                    movimientos[concepto] = valor
                                else:
                                    movimientos[concepto] += valor
                            except ValueError:
                                continue  # Si no podemos convertir el valor, saltamos esta línea
    
    # Generar mensaje con los movimientos
    mensaje = "📊 RESUMEN DE TOTALES\n\n"
    for key, value in movimientos.items():
        mensaje += f"💰 {key}\n"
        mensaje += f"${formato_monto(value)}\n\n"
    
    return mensaje 