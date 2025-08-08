#importando as bibliotecas.
import pyautogui
from PIL import Image
import pytesseract
import time
import cv2
import numpy as np
from Mana_Potion import obter_numero_da_mana
import pyautogui as pg
pg.FAILSAFE = False


#A Vida e Mana será Checada sem parar ao dar o Play No Main.py.
#Para Iniciar o Cavebot dar Play no Cavebot.py
#Certifique-se que os valores de Vida, Mana e as coordenadas de tela estão corretamente ajustados.
#Lembrando que as Configurações estão para Tela 1080P em modo Janela.


# *** Certifique-se de que o caminho para o executável do Tesseract esteja correto ***
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # 

#Nome do char para o script achar a tela

Nome_Char = 'Thadalafilaahh'

#Valores para Curar a vida e mana.

limite_vida = 650
limite_vida_potion = 300
limite_mana_ = 100

#teclas usadas no cliente

tecla_cura = 'F1'
tecla_cura_potion = 'F2'
tecla_potion_mana = 'F5'


# Coordenadas da região da tela onde o número da vida e mana aparece 1080p em modo janela.
#pode mudar de acordo com seu monitor.
#Box(left=np.int64(1848), top=np.int64(176), width=58, height=18)

x_numero_vida = 1848
y_numero_vida = 176
largura_numero_vida = 58
altura_numero_vida = 18

x_numero_mana = 1846
y_numero_mana = 194
largura_numero_mana = 72
altura_numero_mana = 18

def preprocessar_imagem_vida(img_pil):
    """Pré-processa imagem para melhorar OCR (usa OpenCV)."""
    img = np.array(img_pil)
    img_gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    
    # Binariza para aumentar contraste
    _, img_bin = cv2.threshold(img_gray, 127, 255, cv2.THRESH_BINARY)

    # Aumenta o tamanho (OCR funciona melhor com imagens maiores)
    img_bin = cv2.resize(img_bin, None, fx=2, fy=2, interpolation=cv2.INTER_LINEAR)

    return Image.fromarray(img_bin)

def obter_numero_da_life():
    try:
        # Captura a região da tela com as coordenadas fornecidas
        screenshot = pyautogui.screenshot(region=(x_numero_vida, y_numero_vida, largura_numero_vida, altura_numero_vida))
        #processa a imagem para melhor leitura do Pytesseract
        img_proc = preprocessar_imagem_vida(screenshot)
         # Usa PyTesseract para ler o texto da imagem
        texto_life = pytesseract.image_to_string(img_proc, config='--psm 7 -c tessedit_char_whitelist=0123456789')
        
        numero_str = texto_life.strip()
        if numero_str.isdigit():
            return int(numero_str)
        else:
            return None
    except Exception as e:
        print(f"Erro ao obter a vida: {e}")
        return None


#Funções Para Pressionar tecla de Cura.  

def curar_se():
     time.sleep(0.01)  # Pequena pausa antes de pressionar a tecla
     pyautogui.press(tecla_cura)
     print(f"Vida baixa! Curando com '{tecla_cura}'.")


def curar_se_potion():
    time.sleep(0.01)  # Pequena pausa antes de pressionar a tecla
    pyautogui.press(tecla_cura)
    pyautogui.press(tecla_cura_potion)
    print(f"Vida muito baixa! Curando com '{tecla_cura}{tecla_cura_potion}'.")
  

def curar_mana_potion():
    time.sleep(0.01)  # Pequena pausa antes de pressionar a tecla
    pyautogui.press(tecla_potion_mana)
    print(f"Mana baixa! Curando com '{tecla_potion_mana}'.")

#Estrutura de Repetção de checagem da Vida e Mana.
   
def monitorar_vida_mana():
        print("Iniciando monitoramento da vida via OCR...")
        while True:
            time.sleep(0.01)
            vida_atual = obter_numero_da_life()
            mana_atual = obter_numero_da_mana()
            if vida_atual is not None:
                print(f"Vida atual lida da tela: {vida_atual}")
                print(f"Mana atual lida da tela: {mana_atual}")
                if vida_atual <= limite_vida and vida_atual >= limite_vida_potion:
                    curar_se()
                    time.sleep(0.05)
                    if mana_atual is not None:    
                          if mana_atual <= limite_mana_ and vida_atual >= limite_vida_potion:
                             curar_mana_potion()

                elif vida_atual <= limite_vida_potion:
                    curar_se_potion()
                    time.sleep(0.05)
                    
                elif mana_atual is not None:    
                          if mana_atual <= limite_mana_:
                             curar_mana_potion()
                             time.sleep(0.05)
                            
            
            else:
                print("Não foi possível ler o número de vida da tela.")

            time.sleep(0.01)

"""image = pyautogui.screenshot(region=(x_numero_vida, y_numero_vida, largura_numero_vida, altura_numero_vida))
image.save("teste_vida.png")"""










