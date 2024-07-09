#passo 1 - entrar no sistema da empresa 
    #link - https://dlp.hashtagtreinamentos.com/python/intensivao/login
#passo 2 -fazer login 
    #login - usuario
    #senha - senha
#passo 3 - importar a base de dados
#passo 4 - cadastrar um produto
#passo 5 - repetir o passo 4 ate cadastrar todos os produtos

import pyautogui as auto #ferramenta de automatização de mouse, teclado e tela do computador 
import time
import pandas as pd


# pyautogui.click- auto.click - clicar com o mouse
# pyautogui.write - auto.write - escrever um texto
# pyautogui.press - auto.press - apertar uma tecla
# pyautogui.hotkey - auto.hotkey - combinação de teclas(ctrl c)
# pyautogui.scroll - auto.scroll - rolar a tela para cima ou para baixo
auto.PAUSE = 0.5#define o tempo de pausa a cada iteração

#passo 1 ===================================================================================================================================================================
#abrir o navegador

auto.press("win")
auto.write("chrome")
auto.press("enter")
time.sleep(1.5)#esperar a quantidade de tempo para continuar o codigo
#entrar no link 

#link - https://dlp.hashtagtreinamentos.com/python/intensivao/login
auto.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
auto.press("enter")
time.sleep(2)#esperar a quantidade de tempo para continuar o codigo
#entrar no link 

#passo 2 fazer login =======================================================================================================================================================


auto.click(x=724, y=372)
auto.write("usuario")
auto.press("tab")
auto.write("senha")
auto.click(x=964, y=527)
time.sleep(1.5)
auto.click(x=1137, y=365)



#passo 3 importar base de dados============================================================================================================================================

tabela = pd.read_csv('JORNADA-PYTHON\PYTHON POWER UP\produtos.csv')

for linha in tabela.index:
    # Clicar no campo de código
    
    
    # Pegar valores da linha atualMouse
    codigo = tabela.loc[linha, "codigo"]
    marca = tabela.loc[linha, "marca"]
    tipo = tabela.loc[linha, "tipo"]
    categoria = tabela.loc[linha, "categoria"]
    preco_unitario = tabela.loc[linha, "preco_unitario"]
    custo = tabela.loc[linha, "custo"]
    obs = tabela.loc[linha, "obs"]
    
    # Preencher campos com os valores correspondentes\
    time.sleep(0.3)
    auto.click(x=780, y=262)
    #tab nao deu certo, coloquei click e time.sleep

    auto.write(str(codigo))
    auto.press("tab")
    auto.write(str(marca))
    auto.press("tab")
    auto.write(str(tipo))
    auto.press("tab")
    auto.write(str(categoria))
    auto.press("tab")
    auto.write(str(preco_unitario))
    auto.press("tab")
    auto.write(str(custo))
    
    # Preencher o campo 'obs' se não for NaN
    if not pd.isna(obs):
        auto.press("tab")
        auto.write(str(obs))
    
    auto.press("tab")
    auto.press("enter") # Cadastrar o produto (botão enviar)
    
    # Dar scroll para cima
    auto.scroll(5000)
    time.sleep(0.2)
    








