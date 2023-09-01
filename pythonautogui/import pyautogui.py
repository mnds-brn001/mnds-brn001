# Passo a passo do projeto
# Passo 1: Entrar no sistema da empresa


import pyautogui as pgui
import time
import pandas as pd

# pyautogui.write - > escrever um texto
# pyautogui.press -> aperta 1 tecla
# pyautogui.hotkey -> combinação de teclas
pgui.PAUSE = 0.3 # Tempo de espera entre cada comando.


#pyautogui.hotkey("ctrl","c")
#Abrir o navegador
pgui.press("win")
pgui.write("chrome")
pgui.press("enter")
time.sleep(3)
pgui.hotkey("win","up")

#entrar no link
pgui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pgui.press("enter")
time.sleep(3)

# Passo 2: Fazer Login

# Seleciona o Campo de email
pgui.click(x=668, y=451)
# escrever o seu email
pgui.write("pythonaula@gmail.com")
pgui.press("tab")
pgui.write("sua senha")
pgui.click(x=923, y=649) # Clique botão login
time.sleep(3)


# Passo 3: Importar a base de produtos pra cadastrar

tabela = pd.read_csv("C:/Users/Antonio/Desktop/pythonautogui/produtos.csv")
print(tabela)

for linha in tabela.index:
    # Clicar no campo de Código de Produto(No Formulário)
    pgui.click(x=604, y=308)
    # Pegar da tabela o valor da coluna/linha, nesse caso -> codigo, marca, custo, obs
    pgui.write(str(tabela.loc[linha, "codigo"]))
    pgui.press("tab")
    pgui.write(str(tabela.loc[linha, "marca"]))
    pgui.press("tab")
    pgui.write(str(tabela.loc[linha, "tipo"]))
    pgui.press("tab")
    pgui.write(str(tabela.loc[linha, "categoria"]))
    pgui.press("tab")
    pgui.write(str(tabela.loc[linha, "preco_unitario"]))
    pgui.press("tab")
    pgui.write(str(tabela.loc[linha, "custo"]))
    pgui.press("tab")

    obs = tabela.loc[linha, "obs"]
    if not pd.isna(obs):
        pgui.write(str(obs))
    pgui.press("tab")
    pgui.press("enter")
    # Dar scroll de tudo pra cima (recomenda-se uso de valor alto no scoll)
    # Uma alternativa seria utilizar o comando HOME ou PAGE UP
    pgui.press("home")

# Passo 5: Repetir o processo de cadastro até o fim
# Utilizando um simples loop >>for com a função .index do pandas
# e uma condicional if not com a função pd.isna também do pandas.