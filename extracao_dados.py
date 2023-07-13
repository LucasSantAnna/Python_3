# from datetime import date
import matplotlib.pyplot as plt
Variavel = -1
dados = []

def importarArquivo():
    arq = open("ArquivoDadosProjeto.csv" , "r") 
    linhas = arq.readlines()[1:]
    for linha in linhas:
        valores = linha.split(';')
        tupla = (str(valores[0]), float(valores[1]), float(valores[2]),float(valores[3]),
                float(valores[4]),float(valores[5]),float(valores[6]),float(valores[7])) 
        dados.append(tupla)

def listardados():
    print(len(dados))
    for tupla in dados:
        print(tupla)

def precipitacao():
    mesinicio = int(input('informe um mes : '))  
    anoinicio = int(input('informe um ano : '))   
    for tupla in dados: 
        dataSeparada = tupla[0].split('/')
        if mesinicio == int(dataSeparada[1]) and anoinicio == int(dataSeparada[2]): 
            print("data:",tupla[0],'precipitação' ,tupla[1])

def temperatura():
    maiortemp = ()
    ultimomes = 0  
    anotemperatura = int(input('informe um ano : '))
    for tupla in dados:
        dataSeparada = tupla[0].split('/')
        if int(dataSeparada[0]) <=7 and anotemperatura == int(dataSeparada[2]):
            if int(dataSeparada[1]) == int(ultimomes) : 
                if tupla[5] > maiortemp:      
                    maiortemp = tupla[5]
            else:                
                if ultimomes != 0:
                    print("no mes: ",ultimomes,"a maior temperatura foi de: ", maiortemp)
                ultimomes = dataSeparada[1]
                maiortemp = tupla[5]

def meschuvoso():
    dic = {} 
    qtdchuva = 0
    ultimomes = 0
    ulitmoano = 0
    for tupla in dados:
        dataSeparada = tupla[0].split('/')
        if int(dataSeparada[1]) == int(ultimomes) and int(dataSeparada[2]) == int(ulitmoano):
            qtdchuva = qtdchuva + tupla[1]
            dic[str(int(dataSeparada[1]))+'/'+str(int(dataSeparada[2]))] = qtdchuva
        else:             
            ultimomes = dataSeparada[1]
            ulitmoano = dataSeparada[2]
            qtdchuva = tupla[1]
    max_value = max(dic.values())
    max_data = max(dic, key=dic.get)
    print("o mes/ ano com maior quantaide de chuva é: ",max_data,'. valor acomulado:',max_value)


def moda():
    dictemperatura = {}
    dicumidade = {}
    dicvento = {}
    tempmed = 0
    umidade = 0
    velvento = 0
    for tupla in dados:
        dataSeparada = tupla[0].split('/')
        if int(dataSeparada[2]) >= 2006 and int(dataSeparada[2]) <= 2016:
            if int(dataSeparada[1]) == 8:
                tempmed = tempmed + tupla[3]
                umidade = umidade + tupla[6]
                velvento = velvento + tupla[7]
                keytemp = tupla[3]
                keyumid = tupla[6]
                keyvento = tupla[7]
                if keytemp not in dictemperatura:
                    dictemperatura[tupla[3]] = 1
                else:
                    dictemperatura[keytemp] = dictemperatura.get(keytemp)+1
                if keyumid not in dicumidade:
                    dicumidade[tupla[6]] = 1
                else:
                    dicumidade[keyumid] = dicumidade.get(keyumid)+1
                if keyvento not in dicvento:
                    dicvento[tupla[3]] = 1
                else:
                    dicvento[keyvento] = dicvento.get(keyvento)+1
                if int(dataSeparada[0]) == 31:
                    tempmed = tempmed / 31
                    umidade = umidade / 31
                    velvento = velvento / 31
                    print('em agosto de ',dataSeparada[2])
                    print('temperatura media:',tempmed)  
                    print('moda da temperatura:', max(dictemperatura, key=dictemperatura.get))
                    print('umidade media:',umidade) 
                    print('moda da umidade:', max(dicumidade, key=dicumidade.get))
                    print('vento media:',velvento) 
                    print('moda da vento:', max(dicvento, key=dicvento.get))
                    print('------------')

def decada():
    dic = {} 
    chuva = 0
    for tupla in dados:
        dataSeparada = tupla[0].split('/')
        decada = int(f"{str(dataSeparada[2][2])}0")
        anocomeco = str(dataSeparada[2])[:2]       
        decadafinal = anocomeco + str(decada).zfill(2)
        if decadafinal not in dic:
            chuva = int(tupla[1])
            dic[decadafinal] = chuva
        else:
            chuva = chuva + float(tupla[1])
            dic[decadafinal] = chuva
    for key, value in dic.items():
        print('na decada de ',key, ' houve ', value,'de')
        plt.bar(key, value, color ='brown',width = 0.4)
        plt.xlabel("decadas")
        plt.ylabel("precipitação ")
        plt.title("precipitação por decada")
    plt.show()



while Variavel != 0:
    print("----------------------------------------------------------------")
    print("selecione a opção")
    print("0 - sair")
    print("1 - importar arquivo")
    print("2 - intervalo")
    print("3 - temp maxima")
    print('4 - Listar aquivo importado')
    print("5 - Mês mais chuvoso")
    print("6 - Média, moda de agosto")
    print("7 - Decada(conforme ISO 8601) mais chuvosa e e gráfico")

    Variavel = int(input('informe a opção: '))

    if Variavel == 1:
        print('iniciando importação de arquivo')
        importarArquivo()
        print('finalizada importação de arquivo')
    elif Variavel == 2:
        precipitacao()
    elif Variavel == 3:
        temperatura()
    elif Variavel == 4:
        print('iniciando listagem de dados')
        listardados()
        print('finlizado listagem de dados')
    elif Variavel == 5:
        meschuvoso()
    elif Variavel == 6:
        moda()
    elif Variavel == 7:
        decada()
    else:
        print('Opção invalida')
print ('programa finalizado')