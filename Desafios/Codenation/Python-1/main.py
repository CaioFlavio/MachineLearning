# coding: utf-8

# Todas as perguntas são referentes ao arquivo `data.csv`
# Você ** não ** pode utilizar o pandas e nem o numpy para este desafio.
import csv
from collections import defaultdict

def readColumn(column_name):
    filename = 'data.csv'
    columns = defaultdict(list)

    with open(filename, encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            for (k, v) in row.items():
                columns[k].append(v)

    return columns[column_name]

def countUnique(data_list):
    return len(set(data_list))

def getPlayerList(list_size=False, order_column='ID', is_reverse=True):
    filename = 'data.csv'
    players = []

    with open(filename, encoding='utf-8') as f:
        reader = csv.DictReader(f)
        player_list = sorted(reader, key=lambda x: float(x[order_column]), reverse=is_reverse)
        if list_size:
            player_list = player_list[:list_size]
        for row in player_list:
            new_player = {}
            for (k, v) in row.items():
                new_player[k] = v
            players.append(new_player)
    return players
# **Q1.** Quantas nacionalidades (coluna `nationality`) diferentes existem no arquivo?
#
def q_1():
    return countUnique(readColumn('nationality'))

# **Q2.** Quantos clubes (coluna `club`) diferentes existem no arquivo?
def q_2():
    return countUnique(readColumn('club'))

# **Q3.** Liste o primeiro nome dos 20 primeiros jogadores de acordo com a coluna `full_name`.
def q_3():
    full_name = readColumn('full_name')
    return full_name[:20]

# **Q4.** Quem são os top 10 jogadores que ganham mais dinheiro (utilize as colunas `full_name` e `eur_wage`)?
def q_4():
    players = getPlayerList(10, 'eur_wage', True)
    most_paid_players = []
    for player in players:
        most_paid_players.append(player['full_name'])
    return most_paid_players

# **Q5.** Quem são os 10 jogadores mais velhos?
def q_5():
    players = getPlayerList(10, 'age', True)
    most_old_players = []
    for player in players:
        most_old_players.append(player['full_name'])
    return most_old_players


# **Q6.** Conte quantos jogadores existem por idade. Para isso, construa um dicionário onde as chaves são as idades e os valores a contagem.
def q_6():
    age_list = defaultdict(list)
    players = getPlayerList(False, 'age', True)
    for player in players:
        if int(player['age']) in age_list:
            age_list[int(player['age'])] += 1
        else:
            age_list[int(player['age'])] = 1
    return age_list