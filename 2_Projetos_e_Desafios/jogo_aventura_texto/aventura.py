print("*** Mini Aventura de Texto ***")

print("Bem-vido á Aventura!")
escolha1 = input("Você está em uma floresta escura. Há dois caminhos:\nO caminhos das pedras\nO caminho de terra\nQual você escolhe?:")
escolha1 = escolha1.strip().lower()

if escolha1 == "pedras":
    print("Você escolheou o caminho de pedras ....")
    escolha2 = input("Você encontra uma ponte de corda bamba. 'atravessar' ou 'voltar'?")
    escolha2 = escolha2.strip().lower()
    if escolha2 == "atravessar":
        print("A ponte caiu e você morreu")
    else:
        print("você tentou voltar mais se perdeu no caminho")
elif escolha1 == "terra":
    escolha2 = input("Você encontra uma caverna misteriosa. Você 'entra' ou 'continuar'?")
    escolha2 = escolha2.strip().lower()
    if escolha2 == "entrar":
        print("Você morreu pelo um ataque de urso")
    else:
        print("Você encontro seus amigos na cidade")
else:
    print("Opção inválida. fim de jogo")