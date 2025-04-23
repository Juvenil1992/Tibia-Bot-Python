#importando as bibliotecas.
from pynput.mouse import Button, Controller as mouse_controller
from pynput.keyboard import Key, Controller as keyboard_controller
import time

#A Vida será Checada Sem parar ao dar o Play No Main.py.
#Para Iniciar o Cavebot dar Play no Cavebot.py
#Essa Função é importada para o Cavebot para coletar o loot
#As Positions devem ser mudadas de acordo com o tamanho da sua tela configuração para tela 1080p e modo janela.

mouse = mouse_controller()
keyboard = keyboard_controller()

positions = [
    (800, 370),
    (800, 440),
    (800, 515),
    (870, 515),
    (940, 515),
    (945, 445),
    (940, 370),
    (865, 365),
    (800, 370)
]

def pick_loot_around():
    original_position = mouse.position

    for i in positions:
        mouse.position = i
        time.sleep(0.1)

        with keyboard.pressed(Key.shift):
            mouse.press(Button.right)
            mouse.release(Button.right)
            time.sleep(0.1)
        
    mouse.position = original_position

if (__name__ == "__main__"):
    pick_loot_around()