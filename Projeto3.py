from selenium import webdriver
import pandas as pd

nav = webdriver.Chrome()

tabela = pd.read_excel('commodities.xlsx')
tabela = tabela.drop(labels=0, axis=0)

for linha in tabela.index:
    moeda = tabela.loc[linha, 'Moeda']
    link = f'https://www.google.com/search?q=cotação+{moeda}&oq=cota&aqs=chrome.0.69i59l2j69i57j0i67l2j69i60j69i61l2.2452j0j7&sourceid=chrome&ie=UTF-8%27'
    nav.get(link)
    preco = nav.find_element('xpath', '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute('data-value')
    preco = float(preco)
    preco = round(preco, 2)  # Mostrar duas casas decimais
    tabela.loc[linha, 'Preço Atual'] = preco
    

nav.quit()

tabela["Comprar"] = tabela['Preço Ideal'] > tabela['Preço Atual']
tabela.to_excel('commodities_atualizado.xlsx', index=False)

print(tabela)


    




