import gradio as gr
from logic import process_pdfs
import os
# Definir la interfaz
def chat_interface(pdf_files, red_bancaria):
    response = process_pdfs(pdf_files, red_bancaria)
    return response

css = """
    .container { max-width: 800px; margin: auto; }
    .title { color: #1a73e8; }
    .description { color: #5f6368; }
    .button-custom { background-color: #1a73e8; color: white; }
    .button-custom:hover { background-color: #1557b0; }
"""
# Crear la aplicación de Gradio
# Crear la interfaz con Blocks
with gr.Blocks(css=css, theme=gr.themes.Soft()) as interface:
    gr.Markdown("# Calculadora de Montos Maxx")
    gr.Markdown("Sube tus archivos PDF para calcular los totales de los diferentes conceptos.")

    with gr.Row():
        with gr.Column():
            pdf_input_red_bancaria = gr.Dropdown( label="Selecciona tu red bancaria", choices=["VISA-MASTER", "CABAL", "BICA", "ICBC"], value="VISA-MASTER" )
            pdf_input = gr.Files(label="Selecciona tus archivos PDF", file_types=[".pdf"], file_count="multiple")
            submit_btn = gr.Button("Procesar", elem_classes="button-custom")  # Cambia "Submit"
            clear_btn = gr.Button("Limpiar", elem_classes="button-custom") 
        with gr.Column():
            output = gr.Textbox(label="Resultados", lines=15, scale=10)
            
        submit_btn.click(fn=chat_interface, inputs=[pdf_input, pdf_input_red_bancaria], outputs=output)
        clear_btn.click(lambda: "", inputs=[], outputs=output)  # Limpia el resultado

# Lanzar la aplicación
if __name__ == "__main__":
    interface.launch(
        server_name="0.0.0.0",  # Escuchar en todas las interfaces
        server_port=int(    os.environ.get("PORT", 7860)),
    )