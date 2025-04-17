from bancos.visamaster import extract_and_sum_amounts_visa_master
from bancos.bica import extract_tables_from_pdf
from bancos.icbc import extract_tables_from_pdf_icbc
from bancos.cabal import extract_tables_from_pdf_cabal
def process_pdfs(pdf_files, red_bancaria):
    match red_bancaria:
        case "VISA-MASTER":
            total = extract_and_sum_amounts_visa_master(pdf_files)
        case "BICA":
            total = extract_tables_from_pdf(pdf_files)
        case "ICBC":
            total = extract_tables_from_pdf_icbc(pdf_files)
        case "CABAL":
            total = extract_tables_from_pdf_cabal(pdf_files)
        case _:
            total = "❌ Por favor, selecciona una red bancaria válida."
    return f"{total}"           