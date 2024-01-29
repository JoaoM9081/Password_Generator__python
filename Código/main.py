from random import choice
import string

# Definindo a função que gera a senha
def generator(tam):
    # Definindo os caracteres que podem ser usados na senha
    opc = string.ascii_letters + string.digits + string.punctuation
    
    # Inicializando a senha como uma string vazia
    password_user = ''
    
    # Adicionando caracteres aleatórios à senha até atingir o tamanho desejado
    for _ in range(tam):
        password_user += choice(opc)

    return password_user

while True:
    try:
        # Solicitando ao usuário o número de senhas que deseja gerar
        num_passwords = int(input('Digite o número de senhas que você deseja gerar: ').strip())
        
        # Solicitando ao usuário o número de caracteres para a senha
        choice_user = int(input('Digite o número de caracteres que você deseja para a sua senha: ').strip())
        
        # Verificando se o número de caracteres é pelo menos 8
        if choice_user < 8:
            print('\033[1;31mO número de caracteres deve ser no mínimo 8.\033[m')
            continue
    except ValueError:
        # Tratando o erro se o usuário não inserir um número
        print('\033[1;31mEntrada inválida, tente digitar um número válido\033[m')
        continue
    else:
        # Gerando e imprimindo as senhas
        for i in range(num_passwords):
            result = generator(choice_user)
            print(f'\n\033[1mSenha {i+1}:\033[m \033[1;32m{result}\033[m')
        
        print('\nObrigado, até logo...')
        break