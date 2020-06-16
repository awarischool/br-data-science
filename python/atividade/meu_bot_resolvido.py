"""
NOTE: This example has been presented at the following course: https://www.udemy.com/course/aprenda-a-programar-um-bot-do-whatsapp
"""

# Importar pacotes necessarios
from time import sleep
from whatsapp_api import WhatsApp

# Inicializar o whatsapp
wp = WhatsApp()

# Esperar que enter seja pressionado
input("Pressione enter apos escanear o QR Code")

# Lista de nomes ou nomeros de telefone a serem pesquisados
# IMPORTANTE: O nome deve ser nao ambiguo pois ele retornara o primeiro resultado
#nomes_palavras_chaves = ['Luciano Bot', 'Aline Bot', 'Beatriz Bot', 
#                         'Joao Bot', 'Maria Bot', 'Pedro Bot']


nomes_palavras_chaves = list(msg['Contato'])

mensagens = list(msg['Mensagem'])

# Lista dos nomes que vou me referir na mensagem
# primeiros_nomes = [n.split(' ')[0] for n in nomes_palavras_chaves]
#primeiros_nomes = ['Luciano', 'Aline', 'Beatriz', 'Joao', 
#                   'Maria', 'Pedro']

#lista_produtos = ['acucar', 'feijao', 'bicicleta', 'cenoura', 'abacate', 'beringela']

# Loop para mandar mensagens para os clientes
for nome_pesquisar, mensagem in zip(nomes_palavras_chaves, mensagens):
    
    # Pesquisar pelo contato e esperar um pouco
    wp.search_contact(nome_pesquisar)
    sleep(2)
    
    # Enviar mensagem
    wp.send_message(mensagem)

# Esperar 10 segundos e fechar
sleep(10)
wp.driver.close()
