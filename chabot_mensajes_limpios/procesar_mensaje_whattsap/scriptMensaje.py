# Impotamos lo nesesario
import json
import os
import re

# Abrimos el contenido txt extraido y lo guardamos en otra variable
with open("TUruta", 'r', encoding='utf-8') as archivo_txt:
    contenido_txt = archivo_txt.read()
# Usamos patrones de expreciones regulares para eliminar fechas, horas, comas y guiones
patron = r"(?m)^(.*?)- "
# Reemplazamos con espacios vacios y guardamos en una variable
texto_modificado = re.sub(patron, "", contenido_txt, flags=re.MULTILINE)

# Reemplazamos el al emisor y receptor por usuario y modelo
texto_modificado = texto_modificado.replace("emisor del mensaje", "model:")
texto_modificado = texto_modificado.replace("receptor del mensaje ", "user:")
# Asignamos una variable
texto_json = texto_modificado

# Usamos expreciones regulares nuevamente
patron_archivo = "(?m)^.*?: "
# Espacios vacios reeemplazados
texto_json = re.sub(patron_archivo, "", contenido_txt, flags=re.MULTILINE)

# Asignamos el JSON a una variable
file_path = "mensajes.json"
# Verificamos si el archivo esta vacio
if not os.path.exists(file_path) or os.path.getsize(file_path) == 0:
    data = []
else:
# Cargar los datos del archivo JSON
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
# Ordeamos
for line in texto_modificado.splitlines():
    if line.startswith("user:"):
        role = "user"
        message = line[len("user:"):].strip() + "\n"
    elif line.startswith("model:"):
        role = "model"
        message = line[len("model:"):].strip() + "\n"
    else:
        continue
    data.append({"role": role, "parts": [message]})
# Guardamos los datos actualizados de nuevo en el archivo JSON
with open(file_path, 'w', encoding='utf-8') as file:
    json.dump(data, file, ensure_ascii=False, indent=4)
# Simplemente para ver en consola
json_str = json.dumps(data, indent= 4)
print(json_str)




