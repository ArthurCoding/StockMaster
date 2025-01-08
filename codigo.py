import pyautogui
import time


pyautogui.PAUSE = 0.6


pyautogui.press("win")
pyautogui.write("opera")
pyautogui.press("enter")

pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
time.sleep(6)

pyautogui.click(x=707, y=403,)

pyautogui.write("arthursaraiva27@gmail.com")
pyautogui.press("tab") 
pyautogui.write("@Ams566477")
pyautogui.press("tab")
pyautogui.press("enter")
time.sleep(3)

import pandas 

tabela = pandas.read_csv("produtos.csv")

print(tabela)
time.sleep(1.5)
pyautogui.click(x=680, y=272)

linha = 0 

for linha in tabela.index:
    time.sleep(1.5)
    pyautogui.click(x=689, y=295)

    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(str(codigo))
    pyautogui.press("tab")
    
    marca = tabela.loc[linha, "marca"]
    pyautogui.write(str(marca))
    pyautogui.press("tab")
    
    tipo = tabela.loc[linha, "tipo"]
    pyautogui.write(str(tipo))
    pyautogui.press("tab")
    
    categoria = tabela.loc[linha, "categoria"]
    pyautogui.write(str(categoria))
    pyautogui.press("tab")
    
    preco = tabela.loc[linha, "preco_unitario"]
    pyautogui.write(str(preco))
    pyautogui.press("tab")
    
    custo = tabela.loc[linha, "custo"]
    pyautogui.write(str(custo))
    pyautogui.press("tab")
    
    obs = tabela.loc[linha, "obs"]
    if not pandas.isna(obs):
        pyautogui.write(str(obs))
    pyautogui.press("tab")
    
    pyautogui.press("enter")
    pyautogui.scroll(5000)

        
        
   



