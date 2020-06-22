## 1. Todas as importacoes
from selenium import webdriver
from time import sleep
## 2. Todos os parametros
URL_LINKEDIN_DS = 'https://br.linkedin.com/jobs/ci%C3%AAncia-de-dados-vagas?position=1&pageNum=0'

## 3. Execucao do codigo
if __name__ == '__main__':
    # Criar uma instancia do Google Chrome pelo Selenium
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    
    # Acessar URL do Linkedin
    driver.get(URL_LINKEDIN_DS)

    # Pegar lista de resultado de vagas de DS
    resultados = driver.find_elements_by_class_name('result-card')    
    lista_descricao = []
    
    # Iniar While loop em cima de todos os resultados
    while True:
        # For loop para coletar descrições de dados
        for r in resultados[len(lista_descricao):]:
            r.click() # Clicar na descricao
            sleep(1)
            try:
                # Pegar elemento com a descricao
                descricao = driver.find_element_by_class_name('description')
                # Anexar o texto na lista 
                lista_descricao.append(descricao.text)
            except:
                print('Erro')
                pass
            
        resultados = driver.find_elements_by_class_name('result-card')

        # Critério de saída do While
        if len(lista_descricao) == len(resultados):
            break
    
    # Salvar descricões de vagas
    descricao_salvar = '\n'.join(lista_descricao)
    with open('descricoes_vagas.txt', 'w') as f:
        f.write(descricao_salvar)

    # Fechar o Google Chrome
    driver.quit()
    
    
