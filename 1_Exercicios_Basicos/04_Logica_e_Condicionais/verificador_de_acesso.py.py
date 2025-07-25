print("*** Verificador de Acesso ***")
"""
    instruções: 
    Crie uma variável booleana (que só pode ser TRUE ou FALSE) chamada eh_admin.
    Escreva uma estrutura if/else.
    A condição do if deve verificar se o usuário NÃO é um administrador.
    Se a condição for verdadeira (ou segja, se eh_admin for False),O programa deve imprimir: Acesso negado.Área restrita para administradores.
    Caso contrario (se eh_admin for true),deve imprimir: Bem-vindo,admin!
"""
eh_admin = True

if not eh_admin:
    print("Acesso negado. Área restrita para administradores.")
else:
    print("Bem-vindo, admin!")