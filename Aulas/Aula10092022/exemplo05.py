def importaao01():
    print("importação 01")
    import utilitários.matematica
    resultado = utilitários.matematica.somar(1,2)
    print(resultado)

def importaao02():
    print("importação 02")
    import utilitários.matematica as utilmat
    resultado = utilmat.somar(1,2)
    print(resultado)

def importaao03():
    print("importação 03")
    from utilitários.matematica import somar
    resultado = somar(1,2)
    print(resultado)

if __name__ == "__main__":
    importaao01()
    importaao02()
    importaao03()