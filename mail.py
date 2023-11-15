import yagmail
import os
from dotenv import load_dotenv

load_dotenv()

yag= yagmail.SMTP(user= os.getenv("USER"), password = os.getenv("PASSWORD"))

listaDedestinatarios= []
destinatario= input("Ingrese su correo electronico: ")
listaDedestinatarios.append(destinatario)
asunto = "Prueba"
mensaje= "Aca va el cuerpo de mensaje"

yag.send(listaDedestinatarios, asunto, mensaje)