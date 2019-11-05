# preparacao-de-dados
PREPARAÇÃO DE DADOS: 

**TRANSFORMAÇÃO DE DADOS**
Tratamento de dados omissos. Dados omissos não são valores zero. Eles são dados faltantes. Dados omissos podem representar um valor nulo ou um problema. 
  a. Por exemplo, em Statistics observa-se que o Outras_redes_sociais possui 7 Missing (omissos). Isso significa que o usuário não utiliza outra rede social, e o valor é válido. 
  b. Por outro lado, no campo Joga_online, cuja resposta deve ser sim/não, o valor omisso não tem significado.
  
**REDUÇÃO DE ATRIBUTOS**
1- A redução de atributos é útil quando desejamos remover um atributo irrelevante para responder uma pergunta específica sem removê-lo da base de dados. As boas práticas de mineração de dados sugerem que todos os dados sejam importados, e os atributos sejam removidos na medida em que eles vão se mostrando desinteressantes ou redundantes.
2- Suponha que que iremos estudar a demografia dos usuários de internet. Por isso, desejamos selecionar os atributos: Ano_nascimento, Gênero, Estado_civil, Raça e Anos_na_internet.

**AMOSTRAR DADOS**
1- Ao eliminarmos registros com atributos omissos em atributos chave, nós reduzimos a nossa base de dados, tornando o processamento mais rápido e eficiente, sobre dados mais confiáveis. Outra forma de reduzir o tempo de processamento é utilizando a amostragem. Amostre 50% da base de dados (DataFrame.sample). 

**DADOS INCONSISTENTES**
1- Dados inconsistentes são diferentes de dados omissos. Eles acontecem quando um valor existe na base de dados, mas não tem significado ou não é válido. Veja o parâmetro Twitter, por exemplo. Ele é nitidamente um tributo Binominal, mas se tornou Nominal (Categórico) devido a um registro com valor igual a 99. 

**REDUÇÃO DE ATRIBUTOS**
1- A redução de atributos é útil quando desejamos remover um atributo irrelevante para responder uma pergunta específica sem removê-lo da base de dados. As boas práticas de mineração de dados sugerem que todos os dados sejam importados, e os atributos sejam removidos na medida em que eles vão se mostrando desinteressantes ou redundantes. 
2- Suponha que que iremos estudar a demografia dos usuários de internet. Por isso, desejamos selecionar os atributos: Ano_nascimento, Gênero, Estado_civil, Raça e Anos_na_internet. 


_Atividade de Laboratório de Aprendizado de Máquina com o Prof. Hugo de Paula_



