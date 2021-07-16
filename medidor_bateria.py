# Verificar o status do carregamento bateria em função do tempo
# Devolver os dados
# Resulta no gráfico e tabela de valores recolhidos

import psutil
import time
import matplotlib.pyplot as plt

# pega as informações da bateria
# lista de valores da bateria
lista_bat_val = []
lista_temp = []
segundos = minutos = 0
iniciar = True


def verificador_bat(prim_percentual, tempo_ver=3):
    global segundos
    # global minutos
    time.sleep(tempo_ver)
    # Retira os dados dos sensores e os deixa padronizados
    bateria = psutil.sensors_battery()
    if bateria.power_plugged:
        percentual = prim_percentual - float(bateria.percent)
    else:
        percentual = 100 + float(bateria.percent) - prim_percentual
    # Contador
    segundos += tempo_ver
    hora = segundos
    # Adiciona na lista de dados
    lista_bat_val.append(percentual)
    lista_temp.append(hora)
    print(f'{percentual:^10}|{hora:^10}')


def principal(dados_col):
    print('--' * 20)
    print('Iniciando o programa...')
    print('--' * 20)
    print(f'     Y          |        X        ')
    print('--' * 20)
    bateria = psutil.sensors_battery()
    prim_percentual = float(bateria.percent)
    while True:
        # Retira os dados da bateria
        if iniciar:
            verificador_bat(prim_percentual)
        if len(lista_bat_val) == dados_col:
            print('--' * 20)
            print('lista_bat_val = ', lista_bat_val)
            print('lista_temp =', lista_temp)
            print('--' * 20)
            criador_grafico(lista_temp, lista_bat_val)
            break


def criador_grafico(eixox, eixoy):
    plt.plot(eixox, eixoy)
    plt.ylabel('Porcentagem da Bateria')
    plt.xlabel('Tempo em Segundos')
    plt.show()


principal(4)
