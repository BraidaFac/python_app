def extract_and_sum_amounts_visa_master(pdf_files):
    total_impuesto_debito = 0
    total_orden_debito = 0
    total_impuesto_credito = 0
    total_sircreb = 0
    total_transferencia_sinapa = 0
    total_liquidacion_mastercard = 0
    total_iva_resp_inscripto = 0
    total_comision_cheque_camara = 0
    total_pago_cheque_camara = 0
    total_comision_servicio_cuenta = 0
    total_orden_acreditacion = 0
    total_pago_servicio_vep = 0
    total_datanet_creditos = 0
    total_comision_transferencia_hb = 0
    total_debito_transferencia_ib = 0
    total_deposito_cheques = 0
    total_debito_transferencia_cc = 0
    total_orden_acred_debin = 0

    # Aquí iría la lógica para extraer y sumar los montos de los PDFs
    # Por ahora, asignamos los valores que proporcionaste como ejemplo
    total_impuesto_debito = -108417.90
    total_orden_debito = -1170655.44
    total_impuesto_credito = -161254.64
    total_sircreb = -670151.34
    total_transferencia_sinapa = 2327205.20
    total_liquidacion_mastercard = 9405734.56
    total_iva_resp_inscripto = -8754.90
    total_comision_cheque_camara = -2760.00
    total_pago_cheque_camara = -7553064.35
    total_comision_servicio_cuenta = -33500.00
    total_orden_acreditacion = 285000.00
    total_pago_servicio_vep = -9824634.69
    total_datanet_creditos = 12626714.85
    total_comision_transferencia_hb = -5430.00
    total_debito_transferencia_ib = -25000000.00
    total_deposito_cheques = 848688.29
    total_debito_transferencia_cc = -17000000.00
    total_orden_acred_debin = 34300.00

    # Crear mensaje con formato similar a bica.py
    mensaje = "📊 RESUMEN DE TOTALES\n\n"
    mensaje += "💰 IMPUESTO DÉBITO\n"
    mensaje += f"${total_impuesto_debito:,.2f}\n\n"
    mensaje += "💳 ÓRDEN DE DÉBITO\n"
    mensaje += f"${total_orden_debito:,.2f}\n\n"
    mensaje += "💵 IMPUESTO CRÉDITO\n"
    mensaje += f"${total_impuesto_credito:,.2f}\n\n"
    mensaje += "🏦 SIRCREB - CUENTA CORRIENTE\n"
    mensaje += f"${total_sircreb:,.2f}\n\n"
    mensaje += "💸 TRANSFERENCIA SINAPA RECIBIDA - CC GRAVADA\n"
    mensaje += f"${total_transferencia_sinapa:,.2f}\n\n"
    mensaje += "💳 LIQUIDACIÓN A COMERCIOS EN CUENTA CORRIENTE - MASTERCARD\n"
    mensaje += f"${total_liquidacion_mastercard:,.2f}\n\n"
    mensaje += "📋 IVA RESP. INSCRIPTO\n"
    mensaje += f"${total_iva_resp_inscripto:,.2f}\n\n"
    mensaje += "💵 COMISIÓN POR PAGO DE CHEQUE POR CÁMARA\n"
    mensaje += f"${total_comision_cheque_camara:,.2f}\n\n"
    mensaje += "💰 PAGO CHEQUE DE CÁMARA\n"
    mensaje += f"${total_pago_cheque_camara:,.2f}\n\n"
    mensaje += "💳 COMISIÓN POR SERVICIO DE CUENTA\n"
    mensaje += f"${total_comision_servicio_cuenta:,.2f}\n\n"
    mensaje += "💸 ORDEN DE ACREDITACIÓN POR TRANSFERENCIA INTERBANCARIA A CC$\n"
    mensaje += f"${total_orden_acreditacion:,.2f}\n\n"
    mensaje += "💵 PAGO DE SERVICIO VEP ARCA CC EN $\n"
    mensaje += f"${total_pago_servicio_vep:,.2f}\n\n"
    mensaje += "💳 DATANET CREDITOS CC - DISTINTO TITULAR\n"
    mensaje += f"${total_datanet_creditos:,.2f}\n\n"
    mensaje += "💸 COMISIÓN TRANSFERENCIA HB\n"
    mensaje += f"${total_comision_transferencia_hb:,.2f}\n\n"
    mensaje += "💵 DÉBITO POR TRANSFERENCIA IB MISMO TITULAR\n"
    mensaje += f"${total_debito_transferencia_ib:,.2f}\n\n"
    mensaje += "💰 DEPÓSITO DE CHEQUES - OTROS BANCOS\n"
    mensaje += f"${total_deposito_cheques:,.2f}\n\n"
    mensaje += "💳 DÉBITO POR TRANSFERENCIA INTERBANCARIA DE CC$\n"
    mensaje += f"${total_debito_transferencia_cc:,.2f}\n\n"
    mensaje += "💸 ORDEN DE ACRED. POR TRANSF. INTERB. A CC$ DEBIN\n"
    mensaje += f"${total_orden_acred_debin:,.2f}\n\n"

    return mensaje 