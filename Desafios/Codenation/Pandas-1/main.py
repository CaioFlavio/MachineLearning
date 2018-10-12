#!/usr/bin/env python
# coding: utf-8

# # Code:Nation's Pandas-1 Challenge

# Você precisará de python 3.6 (ou superior) e o módulo pandas. Você pode instalar o que precisa com o arquivo `requirements.txt`.
# 
# Para cada questão será preciso criar uma função que retorna o resultado solicitado, conforme o exemplo **Q0** abaixo. No arquivo `sanity_checks.py` existem funções que vão verificar se a sua resposta está no formato esperado para submissão.
# 
# Todas as perguntas são referentes ao arquivo `data.csv`

# In[2]:


import sanity_checks as sc
import pandas as pd


# **Q0.** Cria um dataframe vazio.

# In[5]:


def part_0():
    return pd.DataFrame()

assert sc.part_0(part_0())


# **Q1.** Quantas nacionalidades (coluna `nationality`) diferentes existem no arquivo?
# 

# In[17]:


def part_1():
    df = pd.read_csv('data.csv')
    return len(set(df.nationality))
assert sc.part_1(part_1())


# **Q2.** Quantos clubes (coluna `club`) diferentes existem no arquivo?

# In[9]:


def part_2():
    df = pd.read_csv('data.csv', delimiter=',')
    return len(set(df.club.dropna()))
assert sc.part_2(part_2())


# **Q3.** Liste o nome completo dos 20 primeiros jogadores de acordo com a coluna `full_name`.

# In[4]:


def part_3():
    df = pd.read_csv('data.csv')
    return df.full_name[:20]

assert sc.part_3(part_3())


# **Q4.** Quem são os top 10 jogadores que ganham mais dinheiro (utilize as colunas `full_name` e `eur_wage`)?

# In[16]:


def part_4():
    df = pd.read_csv('data.csv', delimiter=',')
    most_paid_players = df.sort_values(by=['eur_wage'], ascending=[False])
    return most_paid_players.full_name[:10]

assert sc.part_4(part_4())


# **Q5.** Liste, em ordem, o `full_name` dos 10 jogadores mais velhos (use como critério de desempate o campo `eur_wage`).

# In[12]:


def part_5():
    df = pd.read_csv('data.csv', delimiter=',')
    most_older_players = df.sort_values(by=['age', 'eur_wage'], ascending=[False, False])
    return most_older_players.full_name[:10]

assert sc.part_5(part_5())


# **Q6.** Conte quantos jogadores existem por idade. Para isto, utilize a o método `.groupby`.

# In[12]:


def part_6():
    df = pd.read_csv('data.csv', delimiter=',')
    return df.groupby(by=['age']).size()

assert sc.part_6(part_6())


# **Q7.** Quais jogadores tem potencial para fazerem gols mais bonitos? (chip_shot_trait == True, avoids_using_weaker_foot_trait == True).

# In[ ]:


def part_7():
    df = pd.read_csv('data.csv', delimiter=',')
    pĺayers_can_make_beauty_goals = df.loc[(df['chip_shot_trait'] == True) & (df['avoids_using_weaker_foot_trait'] == True)]
    return pĺayers_can_make_beauty_goals.full_name

assert sc.part_7(part_7())

