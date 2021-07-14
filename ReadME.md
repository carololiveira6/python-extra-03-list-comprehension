
## **Table of Contents**
- [Extra - List Comprehension](https://npepa32v9l.execute-api.us-east-1.amazonaws.com/v2/?project_id=19989138&filename=python/outubro-20/1a_ee_03_list-comprehension.html&ref=master#mcetoc_1esj4slvm0) 
  - [Objetivo](https://npepa32v9l.execute-api.us-east-1.amazonaws.com/v2/?project_id=19989138&filename=python/outubro-20/1a_ee_03_list-comprehension.html&ref=master#mcetoc_1f33pqfa47)
  - [Preparativos](https://npepa32v9l.execute-api.us-east-1.amazonaws.com/v2/?project_id=19989138&filename=python/outubro-20/1a_ee_03_list-comprehension.html&ref=master#mcetoc_1f33pqfa48)
- [Entregáveis](https://npepa32v9l.execute-api.us-east-1.amazonaws.com/v2/?project_id=19989138&filename=python/outubro-20/1a_ee_03_list-comprehension.html&ref=master#mcetoc_1egvoav555j) 
  - [Repositório](https://npepa32v9l.execute-api.us-east-1.amazonaws.com/v2/?project_id=19989138&filename=python/outubro-20/1a_ee_03_list-comprehension.html&ref=master#mcetoc_1egvrpv6k1l4)
- [Critérios de aceitação](https://npepa32v9l.execute-api.us-east-1.amazonaws.com/v2/?project_id=19989138&filename=python/outubro-20/1a_ee_03_list-comprehension.html&ref=master#mcetoc_1esj6ecle3)
# **Extra - List Comprehension**
Nessa entrega você exercitará seus conhecimentos sobre **list comprehension** desenvolvendo operações lógicas básicas no estilo *kata*.
## **Objetivo**
O objetivo dessa atividade é trabalhar seus conhecimentos de listas e dicionários no python.

- ***Atenção:*** Os intervalos contemplam os dois extremos.
- ***Atenção:*** Você deverá ***obrigatoriamente*** usar **list comprehension**.
## **Preparativos**
Você deverá criar um arquivo chamado main.py. 

- ***Atenção:*** Os intervalos contemplam os dois extremos.
- ***Atenção:*** Você deverá ***obrigatoriamente*** usar **list comprehension**.

Defina as seguintes funções, observando os exemplos de chamada de cada uma: 

- **list\_comprehension\_exercise\_1()**
  - **Parâmetros:** A função não recebe parâmetros.
  - **Procedimento:** Produza uma lista de valores num intervalo de 0 a 10.
  - **Retorno**: Um List Comprehension que produza uma lista de acordo com o procedimento especificado.

\# Exemplo de chamada:

list\_comprehension\_exercise\_1()

\> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]



- **list\_comprehension\_exercise\_2()**
  - **Parâmetros:** A função não recebe parâmetros
  - **Procedimento:** Produza uma lista num intervalo de 0 a 21 em somente com os valores divisíveis por 2 ou por 3.
  - **Retorno:** Um List Comprehension que produza uma lista de acordo com o procedimento especificado.

\# Exemplo de chamada:

list\_comprehension\_exercise\_2()

\> [0, 2, 3, 4, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20, 21]



- **list\_comprehension\_exercise\_3()**
  - **Parâmetros:** A função não recebe parâmetros
  - **Procedimento:** Produza uma lista num intervalo de -5 a 31 em que seus valores não sejam divisíveis nem por 2 e nem por 5.
  - **Retorno:** Um List Comprehension que produza uma lista de acordo com o procedimento especificado.

\# Exemplo de chamada:

list\_comprehension\_exercise\_3()

\> [-3, -1, 1, 3, 7, 9, 11, 13, 17, 19, 21, 23, 27, 29, 31]



- **list\_comprehension\_exercise\_4()**
  - **Parâmetros:** A função não recebe parâmetros
  - **Procedimento:** Produza uma lista num intervalo de 0 a 10 com o quadrado de cada numero do intervalo.
  - **Retorno:** Um List Comprehension que produza uma lista de acordo com o procedimento especificado.

\# Exemplo de chamada:

list\_comprehension\_exercise\_4()

\> [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]



- **list\_comprehension\_exercise\_5(sentence: str)**
  - **Parâmetros:** A função recebe uma **sentence** em formato de string.
  - **Procedimento:** Produza uma lista somente com as letras maiusculas da frase.
  - **Retorno:** Um List Comprehension que produza uma lista de acordo com o procedimento especificado.

\# Exemplo de chamada:

sentence = 'O Rato Rui Gosta De QueiJo FresQuiNho'

list\_comprehension\_exercise\_5(sentence)

\> ['O', 'R', 'R', 'G', 'D', 'Q', 'J', 'F', 'Q', 'N']



- **list\_comprehension\_exercise\_6(sentence: str)**
  - **Parâmetros:** A função recebe uma **sentence** em formato de string.
  - **Procedimento:** Produza uma lista somente com as palavras que começam com a letra ***r*** e que tenham pelo menos 4 letras.
  - **Retorno:** Um List Comprehension que produza uma lista de acordo com o procedimento especificado.

` `# Exemplo de chamada:

sentence = 'o rato rui roeu a roupa do rei de roma'

list\_comprehension\_exercise\_6(sentence)

\> ['rato', 'roeu', 'roupa', 'roma']
# -----
# **Entregáveis**
## **Repositório**
- Link do **repositório** do **GitLab**
- **Código fonte:** 
  - arquivo **main.py**.
- **Privacidade** 
  - Incluir **ka-br-out-2020-correcoes** como reporter.
# **Critérios de aceitação**

|**pts**|**Dado**|**Quando**|**É esperado**|
| :-: | :-: | :-: | :-: |
|0.5|**list\_comprehension\_exercice\_1**|Executada a função|Lista de números entre 1 e 10 (1 e 10 inclusos).|
|0.5|**list\_comprehension\_exercice\_2**|Executada a função|Lista de números entre 0 e 21 que são divisíveis por 2 ou por 3 (0 e 21 inclusos se necessário).|
|0.5|**list\_comprehension\_exercice\_3**|Executada a função|Lista números entre -5 e 31 não divisíveis por 2 nem por 5 (-5 e 31 inclusos se necessário).|
|0.5|**list\_comprehension\_exercise\_4**|Executada a função|Lista com o quadrado de cada número no intervalo de 0 a 10 (0 e 10 inclusos).|
|0.5|**list\_comprehension\_exercise\_5**|Executada a função|Lista com o procedimento especificado no exercicio|
|0.5|**list\_comprehension\_exercise\_6**|Executada a função|Lista com o procedimento especificado no exercicio|


**Boa diversão dev! 😁**


