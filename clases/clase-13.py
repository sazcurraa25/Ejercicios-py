import asyncio
async def tarea(nombre, duracion):
    print(f"Tarea {nombre} iniciada")
    await asyncio.sleep(duracion)
    print(f"Tarea {nombre} finalizada en {duracion} segundos")
async def main():
# Ejecutar varias tareas de forma concurrente
    await asyncio.gather(
    tarea("A", 2),
    tarea("B", 3),
    tarea("C", 1),
)
asyncio.run(main())

# Chatbots 
#   Herramientas para automatizar la comunicación

# ¿Que es un chatbot comunicacional?
#     un programa que facilita la comunicacion entre una marca o servicio y el usuario a traves de mensajes automatizados
#     Mejorar la experiencia del usuario mediante respuestas rapidas y personalizadas 
# ¿Porque elegimos telegram?
#     Plataforma abierta y accesible
#     Variedad de opciones de interacción de texto, multimedia y botones
#     Experiencia fluida y familiar para el usuario
# Tipos de chatbots
#     Chatbots informativos:
#         Enfocados en ofrecer información y resolver dudas 
#         Usos: noticias, información de productos, recordatorios 
#     Chatbots de servicio al cliente:
#         Automatizan consultas comunes y resuelven problemas básicos 
#         Usos: soporte técnico, asistencia en linea, resolucion de preguntas frecuentes
#     Chatos de venta y marketing:
#         Facilitan el proceso de compra o promocionan productos y servicios 
#         Usos: recomendaciones de productos, reservas, promociones, pagos, reservas, suscripciones, pedidos.
# Lógica en los chatbots
#     Chatbots basados en reglas
#         ● Responden a preguntas frecuentes y sencillas
#         ● Utilizan lógica de decisión (si-entonces)
#     Chatbots basados en IA
#         ● Utilizan IA, procesamiento de lenguaje natural (NLP) y aprendizaje automático (ML)
#         ● Responden de manera más personalizada y natural
#     Chatbots híbridos
#         ● Combinan lógica de reglas e IA avanzada
#         ● Pueden manejar preguntas simples y complejas
# Diferentes chatbots
#     Chatbots Basados en Menús o Botones
#         ● Descripción: Son los chatbots más básicos, donde el usuario selecciona opciones en un menú predeterminado para navegar por opciones específicas.
#         ● Funcionalidad: Operan como un árbol de decisiones; son útiles para consultas simples y repetitivas.
#         ● Limitaciones:
#             ○ Pueden ser lentos para resolver necesidades si el usuario debe pasar por varias opciones.
#             ○ Si la consulta del usuario no está en el menú, el chatbot no puede ayudar.