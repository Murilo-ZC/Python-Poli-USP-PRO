# Manipulação de strings
texto = """Os amigos do maestro querem que dificilmente se possa acha obra tão bem acabada. Um ou outro admite certas rudezas e tais ou quais lacunas, mas com o andar da ópera é provável que estas sejam preenchidas ou explicadas, e aquelas desapareçam inteiramente, não se negando o maestro a emendar a obra onde achar que não responde de todo ao pensamento sublime do poeta. Já não dizem como mesmo os amigos deste. Juram que o libreto foi sacrificado, que a partitura corrompeu o
sentido da letra, e, posto seja bonita em alguns lugares, e trabalhada com arte em outros, é absolutamente diversa e até contrária ao drama"""

# Separando as frases do texto
frases = texto.split(".")

# Passando pelas frases
for frase in frases:
    # Colocando todas as letras minusculas e procurando pela palavra "amigo"
    if "amigo" in frase.lower():
        print("amigo encontrado!")
    print("Frase analisada:", frase)
    
    