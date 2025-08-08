#importando as bibliotecas.
import pyautogui
import pytesseract
from PIL import Image
import cv2
import numpy as np


#A Vida e Mana será Checada sem parar ao dar o Play No Main.py.
#Para Iniciar o Cavebot dar Play no Cavebot.py
#Certifique-se que os valores de Vida, Mana e as coordenadas de tela estão corretamente ajustados.

#ESSA FUNÇÃO É DE RECONHECIMENTO DA MANA e é importado para o Healer.py deixar não esquecer de nem um arquivo.

#Lembrando que as Configurações estão para Tela 1080P em modo Janela.

# *** Certifique-se de que o caminho para o executável do Tesseract esteja correto ***
# Isso pode variar dependendo da sua instalação.
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # 

#Coordenadas da Mana do Char

x_numero_mana = 1848
y_numero_mana = 194
largura_numero_mana = 72
altura_numero_mana = 18

#Coordenadas da Mana Potion
#Box(left=np.int64(679), top=np.int64(355), width=24, height=12)



x_numero_mana_potions = 17
y_numero_mana_potions = 329
largura_numero_mana_potions = 24
altura_numero_mana_potions = 12

def preprocessar_imagem_mana(img_pil):
    """Pré-processa imagem para melhorar OCR (usa OpenCV)."""
    img = np.array(img_pil)
    img_gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    
    # Binariza para aumentar contraste
    _, img_bin = cv2.threshold(img_gray, 127, 255, cv2.THRESH_BINARY)

    # Aumenta o tamanho (OCR funciona melhor com imagens maiores)
    img_bin = cv2.resize(img_bin, None, fx=2, fy=2, interpolation=cv2.INTER_LINEAR)

    return Image.fromarray(img_bin)

def preprocessar_imagem_qtd_mana(img_pil):
    """Pré-processa imagem para melhorar OCR (usa OpenCV)."""
    img = np.array(img_pil)
    img_gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    
    # Binariza para aumentar contraste
    _, img_bin = cv2.threshold(img_gray, 127, 255, cv2.THRESH_BINARY)

    # Aumenta o tamanho (OCR funciona melhor com imagens maiores)
    img_bin = cv2.resize(img_bin, None, fx=2, fy=2, interpolation=cv2.INTER_LINEAR)

    return Image.fromarray(img_bin)



def obter_numero_da_mana():
    try:
        # Captura a região da tela com as coordenadas fornecidas
        screenshot_mana = pyautogui.screenshot(region=(x_numero_mana, y_numero_mana, largura_numero_mana, altura_numero_mana))
        #processa a imagem para melhor leitura do Pytesseract
        img_proc = preprocessar_imagem_mana(screenshot_mana)
        # Usa PyTesseract para ler o texto da imagem
        texto_mana = pytesseract.image_to_string(img_proc, config='--psm 7 -c tessedit_char_whitelist=0123456789')
        
        numero_str = texto_mana.strip()
        if numero_str.isdigit():
            return int(numero_str)
        else:
            return None
    except Exception as e:
        print(f"Erro ao obter a vida: {e}")
        return None
    
def obter_quantidade_de_mana_potions():
    """Captura a região da tela com o número e usa OCR para extraí-lo."""
    try:
        # Captura a região da tela com as coordenadas fornecidas
        screenshot_de_mana_potions = pyautogui.screenshot(region=(x_numero_mana_potions, y_numero_mana_potions, largura_numero_mana_potions, altura_numero_mana_potions))
        #processa a imagem para melhor leitura do Pytesseract
        img_proc = preprocessar_imagem_qtd_mana(screenshot_de_mana_potions)
        # Usa PyTesseract para ler o texto da imagem
        texto_Qmana_potions = pytesseract.image_to_string(img_proc, config='--psm 7 -c tessedit_char_whitelist=0123456789')
        #texto_Qmana_potions = pytesseract.image_to_string(screenshot_de_mana_potions, config='--psm 7 --oem 1 -c tessedit_char_whitelist=0123456789')

        # Tenta converter o texto para um inteiro
        # Remova espaços em branco e tente a conversão
        numero_str = texto_Qmana_potions.strip()
        if numero_str.isdigit():
            return int(numero_str)
        else:
            return None
    except Exception as e:
        print(f"Erro ao obter a vida: {e}")
        return None
  


#pritando_mana = obter_numero_da_mana()

#print(pritando_mana)







