mails = [
    {"asunto": "¡Felicidades! Has ganado un iPhone 15 Pro Max", "etiqueta": "spam"},
    {"asunto": "Su cuenta de Netflix ha sido suspendida", "etiqueta": "spam"},
    {"asunto": "50% de descuento en todos los zapatos deportivos", "etiqueta": "oferta"},
    {"asunto": "Última oportunidad: nuestra oferta de temporada termina hoy", "etiqueta": "oferta"},
    {"asunto": "Confirmación de reserva para su vuelo a Madrid", "etiqueta": "recibidos"},
    {"asunto": "Informe mensual de ventas de la región norte", "etiqueta": "recibidos"},
    {"asunto": "Revisión del presupuesto para el tercer trimestre", "etiqueta": "recibidos"},
    {"asunto": "Información sobre el evento de integración de la empresa", "etiqueta": "recibidos"}
]

filterMails= list(filter(lambda spamAndOffer: spamAndOffer != "spam" and spamAndOffer != "oferta" and spamAndOffer== "recibidos", mails))
print(filterMails)
