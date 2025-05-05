import time

def ENTREGAS():
    print("--------------------Seja Bem-vindo a quitanda-------------")
    print("Registre-se:")
    no = str(input(""))
    bo = int(input(""))
    print("Login cadastrado com sucesso")
    time.sleep(3)
    return no, bo

usuario_cadastrado, senha_cadastrada = ENTREGAS()

def TeladeCadastro():
    print("-------------------------------------")
    print("-------------------------------------")
    print("          Bem-Vindo a Sala de login          ")
    print("-------------------------------------")
    print("-------------------------------------")

    pi = str(input("Coloque seu usuário: "))
    oi = int(input("Coloque sua Senha: "))

    print("Obrigado pelo registro...")
    time.sleep(3)
    return pi, oi

usuario_login, senha_login = TeladeCadastro()

def Verificação(no, bo, pi, oi):
    print("-------------------------------------")
    print("-------------------------------------")
    print("           Tela de verificação           ")
    print("-------------------------------------")
    print("-------------------------------------")

    if pi == no and oi == bo:
        print("Aprovado")
        return True
    else:
        print("Negado")
        return False

ResultadodaVerificação = Verificação(usuario_cadastrado, senha_cadastrada, usuario_login, senha_login)

def Lista():
    print("-------------------------------")
    print("--------------------------------")
    print("       LISTA DE FRUTAS         ")

    Item1 = "Manga"
    Item2 = "Maçã"
    Item3 = "Banana"
    Item4 = "Melancia"
    Item5 = "Pera"
    Item6 = "Acerola"
    Item7 = "Uva"
    Item8 = "Kiwi"
    Item9 = "Abacaxi"
    Item10 = "Laranja"
    Item11 = "Morango"
    Item12 = "Jaca"

    print(Item1)
    print(Item2)
    print(Item3)
    print(Item4)
    print(Item5)
    print(Item6)
    print(Item7)
    print(Item8)
    print(Item9)
    print(Item10)
    print(Item11)
    print(Item12)

    print("Quais itens você quer? ")
    Escreva = input("Escreva:")

    if Escreva == Item1:
        print(" R$19,99 ")
        time.sleep(3)
        return True
    elif Escreva == Item2:
        print(" R$10,99 ")
        time.sleep(3)
        return True
    elif Escreva == Item3:
        print(" R$5,00 ")
        time.sleep(3)
        return True
    elif Escreva == Item4:
        print(" R$4,00 ")
        time.sleep(3)
        return True
    elif Escreva == Item5:
        print(" R$7,00 ")
        time.sleep(3)
        return True
    elif Escreva == Item6:
        print(" R$13,00 ")
        time.sleep(3)
        return True
    elif Escreva == Item7:
        print(" R$12,00 ")
        time.sleep(3)
        return True
    elif Escreva == Item8:
        print(" R$6,00 ")
        time.sleep(3)
        return True
    elif Escreva == Item9:
        print(" R$9,00 ")
        time.sleep(3)
        return True
    elif Escreva == Item10:
        print(" R$12,00 ")
        time.sleep(3)
        return True
    elif Escreva == Item11:
        print(" R$13,00 ")
        time.sleep(3)
        return True
    elif Escreva == Item12:
        print(" R$5,00 ")
        time.sleep(3)
        return True
    else:
        print("Procurando seu item.......")
        time.sleep(6)
        print("Perdão, item não encontrado")
        print("Fechando.....")
        return False

Lista()

def Lista():
    print("-------------------------------")
    print("--------------------------------")
    print("       LISTA DE FRUTAS         ")

    Item1 = "Manga"
    Item2 = "Maçã"
    Item3 = "Banana"
    Item4 = "Melancia"
    Item5 = "Pera"
    Item6 = "Acerola"
    Item7 = "Uva"
    Item8 = "Kiwi"
    Item9 = "Abacaxi"
    Item10 = "Laranja"
    Item11 = "Morango"
    Item12 = "Jaca"

    print(Item1)
    print(Item2)
    print(Item3)
    print(Item4)
    print(Item5)
    print(Item6)
    print(Item7)
    print(Item8)
    print(Item9)
    print(Item10)
    print(Item11)
    print(Item12)

    print("Quais itens você quer? ")
    Escreva = input("Escreva:")

    if Escreva == Item1:
        print(" R$19,99 ")
        time.sleep(3)
        return True
    elif Escreva == Item2:
        print(" R$10,99 ")
        time.sleep(3)
        return True
    elif Escreva == Item3:
        print(" R$5,00 ")
        time.sleep(3)
        return True
    elif Escreva == Item4:
        print(" R$4,00 ")
        time.sleep(3)
        return True
    elif Escreva == Item5:
        print(" R$7,00 ")
        time.sleep(3)
        return True
    elif Escreva == Item6:
        print(" R$13,00 ")
        time.sleep(3)
        return True
    elif Escreva == Item7:
        print(" R$12,00 ")
        time.sleep(3)
        return True
    elif Escreva == Item8:
        print(" R$6,00 ")
        time.sleep(3)
        return True
    elif Escreva == Item9:
        print(" R$9,00 ")
        time.sleep(3)
        return True
    elif Escreva == Item10:
        print(" R$12,00 ")
        time.sleep(3)
        return True
    elif Escreva == Item11:
        print(" R$13,00 ")
        time.sleep(3)
        return True
    elif Escreva == Item12:
        print(" R$5,00 ")
        time.sleep(3)
        return True
    else:
        print("Procurando seu item.......")
        time.sleep(6)
        print("Perdão, item não encontrado")
        print("Fechando.....")
        return False

Lista()

def Lista():
    print("-------------------------------")
    print("--------------------------------")
    print("       LISTA DE FRUTAS         ")

    Item1 = "Manga"
    Item2 = "Maçã"
    Item3 = "Banana"
    Item4 = "Melancia"
    Item5 = "Pera"
    Item6 = "Acerola"
    Item7 = "Uva"
    Item8 = "Kiwi"
    Item9 = "Abacaxi"
    Item10 = "Laranja"
    Item11 = "Morango"
    Item12 = "Jaca"

    print(Item1)
    print(Item2)
    print(Item3)
    print(Item4)
    print(Item5)
    print(Item6)
    print(Item7)
    print(Item8)
    print(Item9)
    print(Item10)
    print(Item11)
    print(Item12)

    print("Quais itens você quer? ")
    Escreva = input("Escreva:")

    if Escreva == Item1:
        print(" R$19,99 ")
        time.sleep(3)
        return True
    elif Escreva == Item2:
        print(" R$10,99 ")
        time.sleep(3)
        return True
    elif Escreva == Item3:
        print(" R$5,00 ")
        time.sleep(3)
        return True
    elif Escreva == Item4:
        print(" R$4,00 ")
        time.sleep(3)
        return True
    elif Escreva == Item5:
        print(" R$7,00 ")
        time.sleep(3)
        return True
    elif Escreva == Item6:
        print(" R$13,00 ")
        time.sleep(3)
        return True
    elif Escreva == Item7:
        print(" R$12,00 ")
        time.sleep(3)
        return True
    elif Escreva == Item8:
        print(" R$6,00 ")
        time.sleep(3)
        return True
    elif Escreva == Item9:
        print(" R$9,00 ")
        time.sleep(3)
        return True
    elif Escreva == Item10:
        print(" R$12,00 ")
        time.sleep(3)
        return True
    elif Escreva == Item11:
        print(" R$13,00 ")
        time.sleep(3)
        return True
    elif Escreva == Item12:
        print(" R$5,00 ")
        time.sleep(3)
        return True
    else:
        print("Procurando seu item.......")
        time.sleep(6)
        print("Perdão, item não encontrado")
        print("Fechando.....")
        return False

Lista()

def Lista():
    print("-------------------------------")
    print("--------------------------------")
    print("       LISTA DE FRUTAS         ")

    Item1 = "Manga"
    Item2 = "Maçã"
    Item3 = "Banana"
    Item4 = "Melancia"
    Item5 = "Pera"
    Item6 = "Acerola"
    Item7 = "Uva"
    Item8 = "Kiwi"
    Item9 = "Abacaxi"
    Item10 = "Laranja"
    Item11 = "Morango"
    Item12 = "Jaca"

    print(Item1)
    print(Item2)
    print(Item3)
    print(Item4)
    print(Item5)
    print(Item6)
    print(Item7)
    print(Item8)
    print(Item9)
    print(Item10)
    print(Item11)
    print(Item12)

    print("Quais itens você quer? ")
    Escreva = input("Escreva:")

    if Escreva == Item1:
        print(" R$19,99 ")
        time.sleep(3)
        return True
    elif Escreva == Item2:
        print(" R$10,99 ")
        time.sleep(3)
        return True
    elif Escreva == Item3:
        print(" R$5,00 ")
        time.sleep(3)
        return True
    elif Escreva == Item4:
        print(" R$4,00 ")
        time.sleep(3)
        return True
    elif Escreva == Item5:
        print(" R$7,00 ")
        time.sleep(3)
        return True
    elif Escreva == Item6:
        print(" R$13,00 ")
        time.sleep(3)
        return True
    elif Escreva == Item7:
        print(" R$12,00 ")
        time.sleep(3)
        return True
    elif Escreva == Item8:
        print(" R$6,00 ")
        time.sleep(3)
        return True
    elif Escreva == Item9:
        print(" R$9,00 ")
        time.sleep(3)
        return True
    elif Escreva == Item10:
        print(" R$12,00 ")
        time.sleep(3)
        return True
    elif Escreva == Item11:
        print(" R$13,00 ")
        time.sleep(3)
        return True
    elif Escreva == Item12:
        print(" R$5,00 ")
        time.sleep(3)
        return True
    else:
        print("Procurando seu item.......")
        time.sleep(6)
        print("Perdão, item não encontrado")
        print("Fechando.....")
        return False

Lista()