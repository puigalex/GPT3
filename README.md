# GPT3
Este código es una guia rapida para empezar a utilizar GPT-3 desde el api de openai para python. La explicación del código está en este [video en Youtube](https://youtu.be/oBjubWuvBPE)

Tambíen esta la guia de como hacer fine tuning del modelo para poderlo adecuar a algun caso de uso especifico que tengas. Esto esta explicado en este otro [video en Youtube](https://youtu.be/oBjubWuvBPE)

## La única configuración requerida es hacer la instalación del API de openAI

```code 
pip install openai
```

## Archivos y carpetas
El archivo **main.ipynb** es un Jupyter Notebook que define dos funciones, una para generar texto con GPT3 y otra para generar imágenes con DallE2

El archivo **chatbot.py** usa las mismas funciones de main.ipynb solo que estan integradas en un ciclo el cual permite usar a GPT3 como un chatbot por medio de la terminal.

En la carpeta **fine_tuning** se tiene un exemplo del csv que se debe tener para poder hacer fine tuning del modelo.

## Fine tuning 
Para enseñar un nuevo patrón o tarea a GPT3 se puede hacer un fine tuning, explicado en el [video]()

Para hacerlo debes de instalar pandas primero y hacer tu API KEY de open AI en una variable de ambiente para que el CLI de openai pueda procesar tus peticiones

```code 
pip install pandas
export OPENAI_API_KEY="<OPENAI_API_KEY>"
```

Una vez hecho esto, tienes que generar un archivo con tus prompts y el texto que debería aprender a responder GPT. Como en el ejemplo **./finetuning/haikus.csv**

### **Convertir .csv a jsonl**
Para hacer el fine tuning se requiere tener nuestros prompts y texto a completar en un formato jsonl.

Para esto podemos correr el siguiente comando

```code 
openai tools fine_tunes.prepare_data -f <ARCHIVO>
```

### **Realizar el fine tuning**
Ahora que ya tenemos el archivo en formato jsonl lo unico que debemos hacer es correr este comando y esperar unos minutos.


```code 
openai api fine_tunes.create -t <ARCHIVO_JSONL> -m <MODELO_SOBRE_EL_CUAL_HACER_FINE_TUNING>
```

Un vez que termina de entrenar nos va a desplegar en la terminal el nombre del nuevo modelo o lo podemos ver dentro de el playground de openAI.

Para poderlo usar en vez de usar el nombre de modelo ada (por ejemplo), se pone el nombre del modelo que ya fue ajustado. 


