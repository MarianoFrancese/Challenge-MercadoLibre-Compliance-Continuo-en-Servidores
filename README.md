# Challenge-MercadoLibre
Challenge Técnico de Mercado Libre

## Información general
Agente y API rest desarrolladas en Python. Para la API, utilizando el framework Flask.

## Ambiente de desarrollo virtual
Se usó un entorno virtual para instalar las librerias necesarias, venv que viene incluido con python.
Para instalarlo, hay que ejecutar el siguiente comando:
``` python -m  venv venv ```

Después de instalado, es necesaria la activación del ambiente, por lo que hay que ejecutar:
``` venv\Scripts\activate ```

Luego, se debe seguir los siguientes pasos:

1. Instalar las librerias del archivo requirements.txt ``` pip install -r requirements.txt ```
2. Indicar el main de la aplicación ``` $env:FLASK_APP = "api.py" ```
3. Levantar la aplicación desde el entorno virtual: ``` python -m flask run ```

## Comentarios
Se hizo uso de Postman para pruebas de la API rest. https://www.postman.com/
