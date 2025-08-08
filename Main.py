#importando as bibliotecas.
import threading
import time
import Healer  
import pyautogui as pg
pg.useImageNotFoundException(False)
pg.FAILSAFE = False

#Ao dar Play no Main.py será feito a checagem da Vida Full Time.
#Certifique-se que os valores de Vida, Mana e as coordenadas de tela estão corretamente ajustados.
#Lembrando que as Configurações estão para Tela 1080P em modo Janela.

running = True
pause_event = threading.Event()

def executar_bot_vida_mana():
        Healer.monitorar_vida_mana()
        time.sleep(0.1)




if __name__ == "__main__":
    thread_vida_mana = threading.Thread(target=executar_bot_vida_mana)

    
    thread_vida_mana.start()
  

