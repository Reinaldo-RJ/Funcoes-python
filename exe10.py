def login(usuario, senha):
    
    if usuario == "admin":
        print("Acesso permitido")
    else:
        print("Acesso negado")
    
    if senha == 4321:
        print("Acesso permitido")
    else:
        print("Acesso negado")

login("admin", 4321)