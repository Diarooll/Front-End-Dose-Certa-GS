limite_No_Prazo_Min = 30
limite_DA_Janela_Min = 60


registros = [
    {'dia': 'SEG', 'periodo': 'Manhã', 'atraso_min': 10},
    {'dia': 'SEG', 'periodo': 'Tarde', 'atraso_min': 45},
    {'dia': 'SEG', 'periodo': 'Noite', 'atraso_min': 30},
    {'dia': 'SEG', 'periodo': 'Dormir', 'atraso_min': None},

    {'dia': 'TER', 'periodo': 'Manhã', 'atraso_min': 5},
    {'dia': 'TER', 'periodo': 'Tarde', 'atraso_min': 31},
    {'dia': 'TER', 'periodo': 'Noite', 'atraso_min': 60},
    {'dia': 'TER', 'periodo': 'Dormir', 'atraso_min': 12},

    {'dia': 'QUA', 'periodo': 'Manhã', 'atraso_min': 15},
    {'dia': 'QUA', 'periodo': 'Tarde', 'atraso_min': None},
    {'dia': 'QUA', 'periodo': 'Noite', 'atraso_min': 55},
    {'dia': 'QUA', 'periodo': 'Dormir', 'atraso_min': 20},

    {'dia': 'QUI', 'periodo': 'Manhã', 'atraso_min': 8},
    {'dia': 'QUI', 'periodo': 'Tarde', 'atraso_min': 27},
    {'dia': 'QUI', 'periodo': 'Noite', 'atraso_min': 61},
    {'dia': 'QUI', 'periodo': 'Dormir', 'atraso_min': 33},

    {'dia': 'SEX', 'periodo': 'Manhã', 'atraso_min': 18},
    {'dia': 'SEX', 'periodo': 'Tarde', 'atraso_min': 40},
    {'dia': 'SEX', 'periodo': 'Noite', 'atraso_min': 0},
    {'dia': 'SEX', 'periodo': 'Dormir', 'atraso_min': 25},

    {'dia': 'SAB', 'periodo': 'Manhã', 'atraso_min': 22},
    {'dia': 'SAB', 'periodo': 'Tarde', 'atraso_min': 35},
    {'dia': 'SAB', 'periodo': 'Noite', 'atraso_min': None},
    {'dia': 'SAB', 'periodo': 'Dormir', 'atraso_min': 29},

    {'dia': 'DOM', 'periodo': 'Manhã', 'atraso_min': 6},
    {'dia': 'DOM', 'periodo': 'Tarde', 'atraso_min': 58},
    {'dia': 'DOM', 'periodo': 'Noite', 'atraso_min': 32},
    {'dia': 'DOM', 'periodo': 'Dormir', 'atraso_min': 30},
]

atraso= []
total_em_alerta = 0

for registro in registros:
    atraso_min = registro['atraso_min']
    if atraso_min is None:
        status = 'Perdida'
    elif atraso_min <= limite_No_Prazo_Min:
        status = 'Confirmada no prazo'
    elif atraso_min <= limite_DA_Janela_Min:
        status = 'Atrasada'
    else:
        status = 'Perdida'
    registro ['status'] = status
    if atraso_min is not None:
        atraso.append(atraso_min)
    if status in ('Atrasada', 'Perdida'):
        total_em_alerta += 1

while True:
    print('\n------ Dose Certa ------')
    print('1 - Listar registros')
    print('2 - Ver classificações')
    print('3 - Mostrar resumo')
    print('0 - Sair')
    opcao = input('Escolha uma opção: ').strip()

    if opcao in ('1', '2'):
        if opcao == '1':
            print('\nDia | Período | Tempo até confirmar')
        else:
            print('\nDia | Período | Status')

        dia_anterior = None
        for registro in registros:
            dia = registro['dia']
            if dia_anterior is not None and dia != dia_anterior:
                print()

            if opcao == '2':
                detalhe = registro['status']
            elif registro['atraso_min'] is None:
                detalhe = 'Sem confirmação'
            else:
                detalhe = f"{registro['atraso_min']} min"

            print(f"{dia} | {registro['periodo']:<7} | {detalhe}")
            dia_anterior = dia
    elif opcao == '3':
        print('\nResumo da semana simulada')
        total_doses = len(registros)

        if atraso:
            media_atraso = sum(atraso) / len(atraso)
            print(f'Média até a confirmação: {media_atraso:.2f} min')
            print(f'Maior tempo até a confirmação: {max(atraso)} min')
        else:
            print('Sem confirmações para calcular os tempos.')

        percentual_alerta = total_em_alerta / total_doses * 100
        print(f'Doses em alerta: {percentual_alerta:.2f}% '
              f'({total_em_alerta} de {total_doses})')
    elif opcao == '0':
        print('Programa encerrado.')
        break
    else:
        print('Opção inválida. Tente de novo.')
