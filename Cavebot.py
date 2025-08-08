#importando as bibliotecas.
import pyautogui as pg
import time
import math
pg.useImageNotFoundException(False)
pg.FAILSAFE = False
import keyboard


#Aqui você Configura o Cavebot, Para que o bot ande pela cave é preciso marcar o mapa com os Icones de Way Points da Cave.
#Lembrando que as Configurações estão para Tela 1080P em modo Janela.
#Para Começar a basta dar Play Nesse Arquivo.

Tecla_Ataque = '1' #Tecla Configurada no Cliente Para Atacar.
tecla_life_ring = 'f3'
tecla_loot = '5'


# Posição dos objetos de tela
Battle = (1699, 552, 198, 200)
center_x = 1699 + 198 // 2
center_y = 582
mini_map = (1708,28,137,141)

#funções do cavebot

Confianca = 0.75
Confianca_bicho = 0.91
Confianca_battle = 0.8

Delay_Waypoint = 0.3 #Delay da Função clicar em ordem
Delay_Click_Waypoint = 2 #Delay apos clicar no mapa até o proximo click

def eat_food():
  if pg.locateOnScreen('imgs/sinal_battle_so.png' , confidence=0.8) != None:
    pg.press('2')
    time.sleep(0.1)
    pg.press('2')
    time.sleep(0.1)
    pg.press('2')
    time.sleep(0.1)
    print('comendo food')

def exori_ico():
  if pg.locateOnScreen('imgs/exori_ico.png' , confidence=0.8) != None:
    time.sleep(0.2)
    pg.press('f7')
    time.sleep(0.1)
    print('exori ico')

def Utura():
  if pg.locateOnScreen('imgs/Utura.png' , confidence=0.8) != None:
    time.sleep(0.1)
    pg.press('3')
    time.sleep(0.1)
    pg.press('3')
    print('utura')

def exori_infir_min():
  if pg.locateOnScreen('imgs/exori_infir_min.png' , confidence=0.8) != None:
    time.sleep(0.2)
    pg.press('f7')
    time.sleep(0.1)
    print('exori min')

#Funções Checagem do Battle.  

def check_battle():
   return pg.locateOnScreen('imgs/Region_Battle.png' , confidence = Confianca_battle , region = Battle)



def criatura_prioridade_1():
   return pg.locateOnScreen('imgs/Mark_Red_Battle1.png' , confidence=Confianca_bicho  , region = Battle)


def use_obsidian_knife():
  while True:
    img = pg.locateOnScreen('imgs/Dragon_Death.png', confidence = 0.75)
    if img != None:
        time.sleep(0.05)
        x, y = pg.center(img)
        pg.moveTo(x, y)
        time.sleep(0.2)
        pg.press('f9')
        time.sleep(0.3)
        pg.leftClick()
        time.sleep(2)
        print('usando obsisdian knife!')
    else:
       print('Sem corpo')
       break



#Estrutura de Repetção do Battle

def kill_monsters():
    while True:
        is_battle = check_battle()

        if is_battle is None:
            pg.press(F'{Tecla_Ataque}')
            print('clicando no bixo')
            time.sleep(0.5)
            

            while criatura_prioridade_1() is not None:
                check_mark = criatura_prioridade_1()
                print('esperando o monstro morrer!')
                time.sleep(0.1)
                if check_mark is not None:
                 exori_ico()
                else:
                    break
        
            eat_food()
            time.sleep(0.05)
            pg.press(tecla_loot)
            time.sleep(0.05)
            print('Pegando Loot')
            time.sleep(0.05)
            Utura()
            
        else:    
            print('sem bicho na tela')
            use_obsidian_knife()
            break  # saiu da batalha
    

#Icones de Way Points da Cave

pixel_centro_minimap = 7

tempo_antitrap = 60 #quanto tempo ele ficara tentando chegar a marção do mapa

def distancia(p1, p2):
    return math.hypot(p1[0] - p2[0], p1[1] - p2[1])

def Norte_cave():
    center_minimap = (1780, 102)  # centro do minimapa
    tolerancia = pixel_centro_minimap  # margem de erro em pixels
    max_tempo = tempo_antitrap  # tempo máximo tentando (evita loop infinito)
    inicio = time.time()
    while True:
        waypotin_img = pg.locateOnScreen('imgs/norte_cave.png', confidence=Confianca, region=mini_map)
        if waypotin_img is not None:
            x, y = pg.center(waypotin_img)
            dist = distancia((x, y), center_minimap)

            if dist <= tolerancia:
                print('Imagem centralizada no minimapa.')
                break

            pg.moveTo(x, y)
            pg.click()
            print(f'Indo Distância do centro: {dist:.2f}')
            time.sleep(1.5)  # aguarda movimento
            kill_monsters()

        else:
            print('Imagem não encontrada.')
            break
        if time.time() - inicio > max_tempo:
            print('Tempo máximo atingido tentando centralizar.')
            break



def meio_cave():
    center_minimap = (1780, 102)  # centro do minimapa
    tolerancia = pixel_centro_minimap  # margem de erro em pixels
    max_tempo = tempo_antitrap  # tempo máximo tentando (evita loop infinito)
    inicio = time.time()
    while True:
        waypotin_img = pg.locateOnScreen('imgs/meio_cave.png', confidence=Confianca , region = mini_map )
        if waypotin_img is not None:
            x, y = pg.center(waypotin_img)
            dist = distancia((x, y), center_minimap)

            if dist <= tolerancia:
                print('Imagem centralizada no minimapa.')
                break

            pg.moveTo(x, y)
            pg.click()
            print(f'Indo Distância do centro: {dist:.2f}')
            time.sleep(1.5)  # aguarda movimento
            kill_monsters()

        else:
            print('Imagem não encontrada.')
            break
        if time.time() - inicio > max_tempo:
            print('Tempo máximo atingido tentando centralizar.')
            break
        

def meio_cave2():
    center_minimap = (1780, 102)  # centro do minimapa
    tolerancia = pixel_centro_minimap  # margem de erro em pixels
    max_tempo = tempo_antitrap  # tempo máximo tentando (evita loop infinito)
    inicio = time.time()
    while True:
        waypotin_img = pg.locateOnScreen('imgs/meio_cave2.png', confidence=Confianca , region = mini_map )
        if waypotin_img is not None:
            x, y = pg.center(waypotin_img)
            dist = distancia((x, y), center_minimap)

            if dist <= tolerancia:
                print('Imagem centralizada no minimapa.')
                break

            pg.moveTo(x, y)
            pg.click()
            print(f'Indo Distância do centro: {dist:.2f}')
            time.sleep(1.5)  # aguarda movimento
            kill_monsters()

        else:
            print('Imagem não encontrada.')
            break
        if time.time() - inicio > max_tempo:
            print('Tempo máximo atingido tentando centralizar.')
            break
        


def meio_cave3():
    center_minimap = (1780, 102)  # centro do minimapa
    tolerancia = pixel_centro_minimap  # margem de erro em pixels
    max_tempo = tempo_antitrap  # tempo máximo tentando (evita loop infinito)
    inicio = time.time()
    while True:
        waypotin_img = pg.locateOnScreen('imgs/meio_cave3.png', confidence=Confianca , region = mini_map )
        if waypotin_img is not None:
            x, y = pg.center(waypotin_img)
            dist = distancia((x, y), center_minimap)

            if dist <= tolerancia:
                print('Imagem centralizada no minimapa.')
                break

            pg.moveTo(x, y)
            pg.click()
            print(f'Indo Distância do centro: {dist:.2f}')
            time.sleep(1.5)  # aguarda movimento
            kill_monsters()

        else:
            print('Imagem não encontrada.')
            break
        if time.time() - inicio > max_tempo:
            print('Tempo máximo atingido tentando centralizar.')
            break


def meio_cave4():
    center_minimap = (1780, 102)  # centro do minimapa
    tolerancia = pixel_centro_minimap  # margem de erro em pixels
    max_tempo = tempo_antitrap  # tempo máximo tentando (evita loop infinito)
    inicio = time.time()
    while True:
        waypotin_img = pg.locateOnScreen('imgs/meio_cave4.png', confidence=Confianca , region = mini_map )
        if waypotin_img is not None:
            x, y = pg.center(waypotin_img)
            dist = distancia((x, y), center_minimap)

            if dist <= tolerancia:
                print('Imagem centralizada no minimapa.')
                break

            pg.moveTo(x, y)
            pg.click()
            print(f'Indo Distância do centro: {dist:.2f}')
            time.sleep(1.5)  # aguarda movimento
            kill_monsters()

        else:
            print('Imagem não encontrada.')
            break
        if time.time() - inicio > max_tempo:
            print('Tempo máximo atingido tentando centralizar.')
            break


def meio_cave5():
    center_minimap = (1780, 102)  # centro do minimapa
    tolerancia = pixel_centro_minimap  # margem de erro em pixels
    max_tempo = tempo_antitrap  # tempo máximo tentando (evita loop infinito)
    inicio = time.time()
    while True:
        waypotin_img = pg.locateOnScreen('imgs/meio_cave5.png', confidence=Confianca , region = mini_map )
        if waypotin_img is not None:
            x, y = pg.center(waypotin_img)
            dist = distancia((x, y), center_minimap)

            if dist <= tolerancia:
                print('Imagem centralizada no minimapa.')
                break

            pg.moveTo(x, y)
            pg.click()
            print(f'Indo Distância do centro: {dist:.2f}')
            time.sleep(1.5)  # aguarda movimento
            kill_monsters()

        else:
            print('Imagem não encontrada.')
            break
        if time.time() - inicio > max_tempo:
            print('Tempo máximo atingido tentando centralizar.')
            break


        
   

def sul_cave():
    center_minimap = (1780, 102)  # centro do minimapa
    tolerancia = pixel_centro_minimap  # margem de erro em pixels
    max_tempo = tempo_antitrap  # tempo máximo tentando (evita loop infinito)
    inicio = time.time()
    while True:
        waypotin_img = pg.locateOnScreen('imgs/sul_cave.png', confidence=Confianca , region = mini_map )
        if waypotin_img is not None:
            x, y = pg.center(waypotin_img)
            dist = distancia((x, y), center_minimap)

            if dist <= tolerancia:
                print('Imagem centralizada no minimapa.')
                break

            pg.moveTo(x, y)
            pg.click()
            print(f'Indo Distância do centro: {dist:.2f}')
            time.sleep(1.5)  # aguarda movimento
            kill_monsters()

        else:
            print('Imagem não encontrada.')
            break
        if time.time() - inicio > max_tempo:
            print('Tempo máximo atingido tentando centralizar.')
            break



def Drop_vials():
    empty_vials = pg.locateOnScreen('imgs/Empty_Vial.png', confidence=0.88)
    
    if empty_vials is not None:
        x, y = pg.center(empty_vials)

        # Coordenadas do centro da tela
        largura, altura = pg.size()
        centro_tela = (largura // 2, altura // 2)

        # Mover até a imagem, clicar e arrastar até o centro
        pg.moveTo(x, y, duration=0.2)
        pg.mouseDown()
        time.sleep(0.1)
        pg.moveTo(centro_tela[0], centro_tela[1], duration=0.5)
        pg.mouseUp()

        print('Arrastando imagem para o centro da tela')
        time.sleep(Delay_Click_Waypoint)
    else:
        print('Sem Vials não')

    
# Função de clicar no mapa na sequência

def clicar_na_cave():
        pg.press(tecla_life_ring)
        Norte_cave()

        meio_cave()

        meio_cave2()

        Drop_vials()

        pg.press(tecla_life_ring)

        meio_cave3()

        meio_cave4()

        meio_cave5()

        sul_cave()
    
    


def saindo_cave():
   while True:
    saida = pg.locateOnScreen('imgs/Saida_Cave.png', confidence = Confianca , region = mini_map)
    
    if saida != None:
        time.sleep(3)
        x, y = pg.center(saida)
        pg.moveTo(x, y)
        pg.click()
        print('Sem Pot, saindo da cave!')
    else:
        kill_monsters()
        time.sleep(3)
        pg.hotkey('ctrl','q')
        time.sleep(Delay_Click_Waypoint)





def hunt_check_potions():
    while True:
        time.sleep(0.2)
        mana = pg.locateOnScreen('imgs/Strong_Mana_Check.png', confidence=0.8)
        if mana is not None:  # Verifica 1se mana não é None 
                clicar_na_cave()
        else:
            print(mana)
            saindo_cave()
            time.sleep(0.5)

hunt_check_potions()











