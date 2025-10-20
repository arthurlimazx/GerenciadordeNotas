def calcular_media(listaNotas):
    somaNotas=0
    nNotas=0
    for nota in listaNotas:
        somaNotas+=nota
        nNotas+=1
    media= somaNotas/nNotas
    return media

def verificar_situacao(media):
    if media>=7:
        return "Aprovado"
    elif media>5 and media<6.9:
        return "Recuperação"
    elif media<5:
        return "Reprovado"