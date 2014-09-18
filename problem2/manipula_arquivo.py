def manipulaArquivo(nomeArquivo):
    arquivo = open(nomeArquivo)
    #print('nome do arquivo: '+ arquivo.name)
    str = arquivo.read()
    return str