#importando as bibliotecas.
import ctypes
import pygetwindow as gw

#Essa Função é para Mudar A opacidade do Client para que o Script Consigar Ler.
#Use OPACITY = 1 para o cliente ficar transparente e Use o OBS Studio por baixo em modo janela para oque o bot consiga rechocer oque esta na tela.


#Coloque o Nome Do Personagem Para Altera a Janela.

Nome_Char = 'Thadalafilaahh'

GWL_EXSTYLE = -20
WS_EX_LAYERED = 0x00080000
LWA_ALPHA = 0x00000002

OPACITY = 1   # 0 -- 255
WINDOW_TITLE = f"Tibia - {Nome_Char}"
target_window = gw.getWindowsWithTitle(WINDOW_TITLE)[0]

if target_window is not None:
    target_hwnd = target_window._hWnd

    ex_style = ctypes.windll.user32.GetWindowLongA(target_hwnd, GWL_EXSTYLE)
    ctypes.windll.user32.SetWindowLongA(target_hwnd, GWL_EXSTYLE, ex_style | WS_EX_LAYERED)

    ctypes.windll.user32.SetLayeredWindowAttributes(target_hwnd, 0, OPACITY, LWA_ALPHA)

    print("Opacidade da janela modificada.")
else:
    print("Janela não encontrada.")