# -*- coding: utf-8 -*-
"""
Created on Tue Aug 28 20:06:10 2018

Anderson Carvalho                         RA: 82496
Angela de Mendonça Pereira                RA: 645450
Camila Coutinho Magalhães Marques         RA: 83101
Marina Iolanda Oliveira                   RA: 1100212


"""

import numpy as np
import pandas as pd


df = pd.read_excel("C://Temp//_Angela//ML//Atividades//Atividade 1 - Automoveis.xlsx", sheet_name=0) 

# Listar as primeiras linhas (Nao aparece todas as colunas)
print(df.head(5))

df.head()

# Listar todas as colunas
df[['Fabricante','Combustível','Portas','Estilo Chassis','Tração','Comprimento','Largura','Altura','Tipo de motor','Número de cilindros','Tamanho do motor','Tipo de injeção','Potência (HP)','Pico RPM','Preço']]

# Tipo do Dados
print(df.dtypes)



# Convertendo os dados
# Problemas de formatação de dados. (ponto e virgula)
# Valores inconsistentes. (Cilindros com valores inteiros e string)

df["Comprimento"] = [x.replace(',','.') for x in df["Comprimento"]]
df["Comprimento"] = df["Comprimento"].astype(float)

df["Altura"] = [x.replace(',','.') for x in df["Altura"]]
df["Altura"] = df["Altura"].astype(float)

df["Largura"] = [x.replace(',','.') for x in df["Largura"]]
df["Largura"] = df["Largura"].astype(float)



df["Número de cilindros"] = [x.replace('doze','12') for x in df["Número de cilindros"].astype(str)]
df["Número de cilindros"] = [x.replace('oito','8') for x in df["Número de cilindros"].astype(str)]
df["Número de cilindros"] = df["Número de cilindros"].astype(int)

df["Tamanho do motor"] = [x.replace(',','.') for x in df["Tamanho do motor"]]
df["Tamanho do motor"] = df["Tamanho do motor"].astype(float)

df["Potência (HP)"] = [x.replace(',','.') for x in df["Potência (HP)"]]
df["Potência (HP)"] = df["Potência (HP)"].astype(float)

df["Pico RPM"] = [x.replace(',','.') for x in df["Pico RPM"].astype(str)]
df["Pico RPM"] = df["Pico RPM"].astype(float)

df["Preço"] = [x.replace(',','.') for x in df["Preço"]]
df["Preço"] = df["Preço"].astype(float)

# Tipo do Dados
print(df.dtypes)







# http://felipegalvao.com.br/blog/2016/02/29/manipulacao-de-dados-com-python-pandas/

# Verificando valores NULL, nesse caso mostra se o Valor e True (Nulo) e False (Nao Nulo).
# Mas nao e muito pratico se tiver muitos dados
df['Combustível'].isnull()

# Para saber quais colunas tem valores Nulos
df.isnull().any()

# Para saber quais colunas NAO tem valores Nulos
df.notnull().all()

###############################################################################################

#tipo de dados
datatypes = df.dtypes
print(datatypes)

# Estatística descritiva dos dados
descricao_automoveis = df.describe()
print(descricao_automoveis)

#valores omissos numericos. O describe vê isso no count.

#valroes omissos categoricos
omissosFabricante = np.where(df["Fabricante"].isnull() == True)
print("\nValores omissos no atributo Fabricante:", omissosFabricante, sep='\n')
print("\nQuantidade de valores omissos no atributo Fabricante:", len(omissosFabricante[0]), sep='\n')


omissosCombustivel = np.where(df["Combustível"].isnull() == True)
print("\nValores omissos no atributo Combustível:", omissosCombustivel, sep='\n')
print("\nQuantidade de valores omissos no atributo Combustível:", len(omissosCombustivel[0]), sep='\n')

print(df["Combustível"].describe())

##########################################
df.groupby(["Fabricante","Combustível"])["Combustível"].count()




##########################################
# Valores Distinct 

df["Fabricante"].unique()
df["Combustível"].unique()
df["Portas"].unique()
df["Estilo Chassis"].unique()
df["Tração"].unique()
df["Comprimento"].unique()
df["Largura"].unique()
df["Altura"].unique()
df["Tipo de motor"].unique()
df["Número de cilindros"].unique()
df["Tamanho do motor"].unique()
df["Tipo de injeção"].unique()
df["Potência (HP)"].unique()
df["Pico RPM"].unique()
df["Preço"].unique()

##########################################
# Descricao Campo

#tipo de dados
datatypes = df.dtypes
print(datatypes)

# Estatística descritiva dos dados (Todas as colunas)
descricao_automoveis = df.describe()
print(descricao_automoveis)


# Estatística descritiva dos dados (Por Coluna)
print(df["Fabricante"].describe())
print(df["Combustível"].describe())
print(df["Portas"].describe())
print(df["Estilo Chassis"].describe())
print(df["Tração"].describe())
print(df["Comprimento"].describe())
print(df["Largura"].describe())
print(df["Altura"].describe())
print(df["Tipo de motor"].describe())
print(df["Número de cilindros"].describe())
print(df["Tamanho do motor"].describe())
print(df["Tipo de injeção"].describe())
print(df["Potência (HP)"].describe())
print(df["Pico RPM"].describe())
print(df["Preço"].describe())

##########################################

