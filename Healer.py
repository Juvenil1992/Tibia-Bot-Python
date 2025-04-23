#importando as bibliotecas.
import pyautogui
from PIL import Image
import pytesseract
import time
from Mana_Potion import obter_numero_da_mana


#A Vida e Mana será Checada sem parar ao dar o Play No Main.py.
#Para Iniciar o Cavebot dar Play no Cavebot.py
#Certifique-se que os valores de Vida, Mana e as coordenadas de tela estão corretamente ajustados.
#Lembrando que as Configurações estão para Tela 1080P em modo Janela.


# *** Certifique-se de que o caminho para o executável do Tesseract esteja correto ***
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'  # 

#Nome do char para o script achar a tela

Nome_Char = 'Thadalafilaahh'

#Valores para Curar a vida e mana.

limite_vida = 350
limite_vida_potion = 250
limite_mana_ = 70

#teclas usadas no cliente

tecla_cura = 'F1'
tecla_cura_potion = 'F2'
tecla_potion_mana = 'F5'


# Coordenadas da região da tela onde o número da vida e mana aparece 1080p em modo janela.
#pode mudar de acordo com seu monitor.

x_numero_vida = 1847
y_numero_vida = 174
largura_numero_vida = 60
altura_numero_vida = 21

x_numero_mana = 1846
y_numero_mana = 194
largura_numero_mana = 72
altura_numero_mana = 18


def obter_numero_da_life():
    """Captura a região da tela com o número e usa OCR para extraí-lo."""
    try:
        # Captura a região da tela com as coordenadas fornecidas
        screenshot_da_life = pyautogui.screenshot(region=(x_numero_vida, y_numero_vida, largura_numero_vida, altura_numero_vida))

        # Usa PyTesseract para ler o texto da imagem
        texto_life = pytesseract.image_to_string(screenshot_da_life, config='--psm 6')

        # Tenta converter o texto para um numero inteiro
        numero_str = texto_life.strip()
        if numero_str:
            numero = int(numero_str)
            return numero
        else:
            return None
    except Exception as e:
        print(f"Erro ao obter o número da Life: {e}")
        return None


#Funções Para Pressionar tecla de Cura.  

def curar_se():
     time.sleep(0.1)  # Pequena pausa antes de pressionar a tecla
     pyautogui.press(tecla_cura)
     print(f"Vida baixa! Curando com '{tecla_cura}'.")


def curar_se_potion():
    time.sleep(0.1)  # Pequena pausa antes de pressionar a tecla
    pyautogui.press(tecla_cura)
    pyautogui.press(tecla_cura_potion)
    print(f"Vida muito baixa! Curando com '{tecla_cura}{tecla_cura_potion}'.")
  


def curar_mana_potion():
        time.sleep(0.1)  # Pequena pausa antes de pressionar a tecla
        pyautogui.press(tecla_potion_mana)
        print(f"Mana baixa! Curando com '{tecla_potion_mana}'.")

#Estrutura de Repetção de checagem da Vida e Mana.
   
def monitorar_vida_mana():
        print("Iniciando monitoramento da vida via OCR...")
        while True:
            vida_atual = obter_numero_da_life()
            mana_atual = obter_numero_da_mana()
            if vida_atual is not None:
                print(f"Vida atual lida da tela: {vida_atual}")
                print(f"Mana atual lida da tela: {mana_atual}")
                if vida_atual <= limite_vida and vida_atual >= limite_vida_potion:
                    curar_se()
                    if mana_atual is not None:    
                          if mana_atual <= limite_mana_ and vida_atual >= limite_vida_potion:
                             curar_mana_potion()

                elif vida_atual <= limite_vida_potion:
                    curar_se_potion()
                    
                elif mana_atual is not None:    
                          if mana_atual <= limite_mana_:
                             curar_mana_potion()
                            
            
            else:
                print("Não foi possível ler o número de vida da tela.")

            time.sleep(0.1)











