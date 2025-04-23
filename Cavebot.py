#importando as bibliotecas.
import pyautogui as pg
import time
import keyboard
from Pick_loot import pick_loot_around
pg.useImageNotFoundException(False)

#Aqui você Configura o Cavebot, Para que o bot ande pela cave é preciso marcar o mapa com os Icones de Way Points da Cave.
#Lembrando que as Configurações estão para Tela 1080P em modo Janela.
#Para Começar a basta dar Play Nesse Arquivo.

Tecla_Ataque = '1' #Tecla Configurada no Cliente Para Atacar.


# Posição dos objetos de tela
Battle = (1699, 552, 198, 200)
center_x = 1699 + 198 // 2
center_y = 582
mini_map = (1710,33,134,138)

#funções do cavebot

Confianca = 0.71
Confianca_bicho = 0.95
Confianca_battle = 0.8

def eat_food():
  if pg.locateOnScreen('imgs/sinal_battle_so.png' , confidence=0.9) != None:
    pg.press('2')
    print('comendo food')

#Funções Checagem do Battle.  

def check_battle():
   return pg.locateOnScreen('imgs/Region_Battle.png' , confidence = Confianca_battle)



def criatura_prioridade_1():
   return pg.locateOnScreen('imgs/Mark_Red_Battle2.png' , confidence=Confianca_bicho)



#Estrutura de Repetção do Battle

def kill_monsters():
    while True:
        is_battle = check_battle()

        if is_battle is None:
            pg.press(F'{Tecla_Ataque}')
            print('clicando no bixo')
            time.sleep(0.5)
            print('Pegando Loot')

            while criatura_prioridade_1() is not None:
                print('esperando o monstro morrer!')
                time.sleep(0.1)
        
            eat_food()
            pick_loot_around()
            time.sleep(0.7)
        else:    
            break  # saiu da batalha

    print('sem bicho na tela')
    

#Icones de Way Points da Cave

def Norte_cave():
    kill_monsters()
    Norte = pg.locateOnScreen('imgs/norte_cave.png', confidence=8)
    
    if Norte != None:
        x, y = pg.center('Norte')
        pg.moveTo(x, y)
        pg.click()
        print('indo Norte')
        time.sleep(3)



def meio_cave():
    kill_monsters()
    Meio = pg.locateOnScreen('imgs/meio_cave.png', confidence=Confianca  )
            
    if Meio != None:
        x, y = pg.center(Meio)
        pg.moveTo(x, y)
        pg.click()
        print('indo meio')
        time.sleep(3)
        

def meio_cave2():
    kill_monsters()
    meio2 = pg.locateOnScreen('imgs/meio_cave2.png', confidence=Confianca )
            
    if meio2 != None:
        x, y = pg.center(meio2)
        pg.moveTo(x, y)
        pg.click()
        print('indo meio2')
        time.sleep(3)


def meio_cave3():
    kill_monsters()
    meio3 = pg.locateOnScreen('imgs/meio_cave3.png', confidence=Confianca)
            
    if meio3 != None:
        x, y = pg.center(meio3)
        pg.moveTo(x, y)
        pg.click()
        print('indo meio3')
        time.sleep(3)


def meio_cave4():
    kill_monsters()
    meio4 = pg.locateOnScreen('imgs/meio_cave4.png', confidence=Confianca)
    
    if meio4 != None:
        x, y = pg.center(meio4)
        pg.moveTo(x, y)
        pg.click()
        print('indo meio4')
        time.sleep(3)
   

def sul_cave():
    kill_monsters()
    sul = pg.locateOnScreen('imgs/Sul_cave.png', confidence=Confianca)
    
    if sul != None:
        x, y = pg.center(sul)
        pg.moveTo(x, y)
        pg.click()
        print('indo sul')
        time.sleep(3)
    
# Função de clicar no mapa na sequência
#Você pode alterar os nomes de acordo com a volta na cave

def clicar_em_ordem():
  while True:
    
    Norte_cave()
    time.sleep(0.3)
    
    Norte_cave()
    time.sleep(0.3)

    sul_cave()
    time.sleep(0.3)

    sul_cave()
    time.sleep(0.3)

    sul_cave()
    time.sleep(0.3)

    sul_cave()
    time.sleep(0.3)

    meio_cave()
    time.sleep(0.3)

    meio_cave()
    time.sleep(0.3)

    meio_cave()
    time.sleep(0.3)
    
    meio_cave()
    time.sleep(0.3)

    meio_cave()
    time.sleep(0.3)

    meio_cave()
    time.sleep(0.3)

    meio_cave()
    time.sleep(0.3)

    meio_cave()
    time.sleep(0.3)

    meio_cave2()
    time.sleep(0.3)

    meio_cave2()
    time.sleep(0.3)
    
    meio_cave2()
    time.sleep(0.3)

    meio_cave2()
    time.sleep(0.3)
    
    meio_cave2()
    time.sleep(0.3)

    meio_cave2()
    time.sleep(0.3)

    meio_cave3()
    time.sleep(0.3)

    meio_cave3()
    time.sleep(0.3)

    meio_cave4()
    time.sleep(0.3)

    meio_cave4()
    time.sleep(0.3)
    
    meio_cave4()
    time.sleep(0.3)

    meio_cave4()
    time.sleep(0.3)




clicar_em_ordem()



