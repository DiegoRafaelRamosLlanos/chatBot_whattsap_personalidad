"""
Install the Google AI Python SDK

$ pip install google-generativeai

See the getting started guide for more information:
https://ai.google.dev/gemini-api/docs/get-started/python
"""

import os
import json
import google.generativeai as genai

genai.configure(api_key="Tu api previamente creada")

# Create the model
# See https://ai.google.dev/api/python/google/generativeai/GenerativeModel
generation_config = {
  "temperature": 99,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}
'''
safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    #"threshold": "BLOCK_MEDIUM_AND_ABOVE",
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE",
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE",
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE",
  },
]
'''
model = genai.GenerativeModel(
  model_name="gemini-1.5-flash",
  generation_config=generation_config,
  system_instruction="dale personalidad a tu ia.\nMantenga sus respuestas en menos de 3 párrafos,"
)
with open('tu ruta\procesar_mensaje_whattsap\\mensajes.json', 'r', encoding='utf-8') as archivo:
    datos = json.load(archivo)

lista_datos = []

for dato in datos:
    lista_datos.append(dato)

chat_session = model.start_chat(
    history=lista_datos
)

chat_history=[]
while True:
    pregunta = input("(Escribe 'Salir' para terminar):")

    if pregunta.lower() == "salir":
        break
    chat_history.append({"role ": "user","content" : pregunta})
    #genero la respuesta del modelo
    response = chat_session.send_message(pregunta)
    chat_history.append({"role ": "assistant","content" : response})
    print(response.text)
 #   print(chat_history)

#print(chat_session.history)
