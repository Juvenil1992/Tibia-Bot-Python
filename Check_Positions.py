#importando as bibliotecas.
import pyautogui
pyautogui.useImageNotFoundException(False)

#Essa Função é para voce Verificar a Localização dos Arquivos.
#Para Mudança de Coordenadas, Checar a Confiança das Informações.
#Só alterar a Imagem e dar Play que ele irá encontrar na Tela e dar a coordenada.
#Caso de Resolução diferente de 1080p devem ser checada as imagens. 
#Se não reconhecer as Imagens voce deve refazer as que não forem rechonhecidas.
#Essa Verificação é para Caso de Mudança de Resolução da Tela.


def criatura_prioridade_2():
   return pyautogui.locateOnScreen('imgs/Region_Battle.png', confidence=0.9)

def criatura_prioridade_1():
 while True:
   battle=criatura_prioridade_2()
   print(battle)
criatura_prioridade_1()


