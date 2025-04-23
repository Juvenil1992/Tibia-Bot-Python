#importando as bibliotecas.
import pyautogui
import pytesseract


#A Vida e Mana será Checada sem parar ao dar o Play No Main.py.
#Para Iniciar o Cavebot dar Play no Cavebot.py
#Certifique-se que os valores de Vida, Mana e as coordenadas de tela estão corretamente ajustados.

#ESSA FUNÇÃO É DE RECONHECIMENTO DA MANA e é importado para o Healer.py deixar não esquecer de nem um arquivo.

#Lembrando que as Configurações estão para Tela 1080P em modo Janela.

# *** Certifique-se de que o caminho para o executável do Tesseract esteja correto ***
# Isso pode variar dependendo da sua instalação.
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'  # 


x_numero_mana = 1846
y_numero_mana = 194
largura_numero_mana = 72
altura_numero_mana = 18


    
def obter_numero_da_mana():
    """Captura a região da tela com o número e usa OCR para extraí-lo."""
    try:
        # Captura a região da tela com as coordenadas fornecidas
        screenshot_da_life = pyautogui.screenshot(region=(x_numero_mana, y_numero_mana, largura_numero_mana, altura_numero_mana))

        # Usa PyTesseract para ler o texto da imagem
        texto_mana = pytesseract.image_to_string(screenshot_da_life, config='--psm 6')

        # Tenta converter o texto para um inteiro
        # Remova espaços em branco e tente a conversão
        numero_str = texto_mana.strip()
        if numero_str:
            numero = int(numero_str)
            return numero
        else:
            return None
    except Exception as e:
        print(f"Erro ao obter o número da Mana: {e}")
        return None
  


#pritando_mana = obter_numero_da_mana()

#print(pritando_mana)







