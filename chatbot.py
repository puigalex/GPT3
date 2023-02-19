import openai
#import asyncio 
import os

openai.api_key = "" # nunca dejen sus credenciales dentro del código! pueden hacerlo una variable de ambiente

def enviar_prompt(prompt, engine="text-davinci-002", temp=0.5, max_tokens=100, top_p=1, frequency_penalty=0, presence_penalty=0):
    respuesta = openai.Completion.create(
                                            engine=engine,
                                            prompt=prompt,
                                            temperature=temp,
                                            max_tokens=max_tokens,
                                            top_p=top_p,
                                            frequency_penalty=frequency_penalty,
                                            presence_penalty=presence_penalty
                                            )
    return respuesta['choices'][0]['text']


def main():
    historico = "- Hola GPT soy Alex Puig \n"
    while True:
        print("HISTORICO \n" , historico, "\n-----------------------\n")
        respuesta = enviar_prompt(historico)
        os.system("clear")
        #print(historico)
        print("Respuesta: \n" + respuesta)
        prompt = input("\n Escribe tu prompt: \n >>>")
        historico = historico + respuesta + "\n- " + prompt

if __name__ == "__main__":
    main()
