#BIBLIOTECAS QUE SERAM USADAS
import time
import pywhatkit
from datetime import datetime
import keyboard

#DEFINIR OS CONTATOS

contatos = ['+55 16 98110-6717','+55 16 99314-3740','+55 16 98250-8141','+55 16 99279-7113']

#ESTRUTURA DE REPETIÇÃO PARA ENVIAR AS MENSAGENS ENQUANTO TIVER MAIS DE 1 CONTATO

while len(contatos) >= 0:

    #ENVIAR AS MENSAGENS

    pywhatkit.sendwhatmsg(contatos[0], 'MENSAGEM AUTOMATIZADA!', datetime.now(
    ).hour,datetime.now(). minute + 1)
    del contatos[0]
    time.sleep(10)
    keyboard.press_and_release('ctrl + w')
