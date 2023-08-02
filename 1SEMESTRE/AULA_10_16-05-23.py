####################### def pt.1 ####################
def mostra_mensagem():                      # Assinatura da função
    print("Bem-vindo ao def do Python.")
# Chama a função dentro do main

if __name__ == '__main__':                  # Atalho: mai + tecla<tab>
    mostra_mensagem()                       # Chama a função sem passar nada'''
''' ----- ALTERAÇÕES:
a. Na função principal, mostre uma mensagem antes de chamar a função (def) 
b. Na função principal, mostre uma mensagem depois de chamar a função (def)
c. Crie mais uma função mostra_mensagem_2, ela recebe uma frase e mostra a frase
   recebida. Na função principal, chame a função passando uma mensagem.
d. No main, chame a função mostra_mensagem2 mais uma vez passando a mensagem.
e. No main, use o input para ler uma mensagem e chame a função mostra_mensagem2 
   mais uma vez passando a mensagem lida.'''
--
# a.
def mensagem():
    print('Bem-vindo ao def do Python.')
if __name__== '__main__':
    print('Mensagem antes da chamada da função')
    mensagem()
--
# b.
def mensagem():
    print('Bem-vindo ao def do Python.')
if __name__== '__main__':
    print('Mensagem antes da chamada da função.')
    mensagem()
    print('Mensagem depois da chamada da função.')
--

# a, b, c, d, e.
def mensagem():
    print('Bem vindo ao def de Python.')         
def mensagem2(msg):  # c.
    print(msg)       # c.
if __name__== '__main__':
    print('Mensagem antes da chamada da função.')   # a.
    mensagem()                                      # a.
    print('Mensagem depois da chamada da função.')  # b.
    mensagem2('Mensagem passada para função LETRA C')  # c.
    var = 'Mensagem passada para função LETRA D' # d.
    mensagem2(var)                               # d. 
    var = input('Mensagem LETRA E: ')            # e.
    mensagem2(var)                               # e.
