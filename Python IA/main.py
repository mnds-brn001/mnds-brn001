import pandas as pd

from IPython.display import display

from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

tabela = pd.read_csv("C:/Users/Antonio/Desktop/Exercícios Refeitos/Python IA/clientes.csv") # Essa linha importa a base de dados.
display(tabela)

# Verificar se há valores vazios ou valores reconhecidos em formato errado

print(tabela.info())
print(tabela.columns)


codificador = LabelEncoder() # Essa linha vai transformar as colunas
# de Texto em Números.

for coluna in tabela.columns:
   if tabela[coluna].dtype == "object" and coluna != "score_credito":
       tabela[coluna] = codificador.fit_transform(tabela[coluna])

# Agora para verificar se as colunas foram realmente Transformadas.
print(tabela.info())



x = tabela.drop(["score_credito", "id_cliente"], axis=1)
y = tabela["score_credito"]

x_treino, x_teste, y_treino, y_teste = train_test_split(x, y, test_size=0.3, random_state=1 )

modelo_arvore = RandomForestClassifier() # Módulo de arvore de decisão
modelo_knn = KNeighborsClassifier() # Módulo Klosest Neighbors (vizinhos próximos).

# .fit para realizar o treino da IA

modelo_arvore.fit(x_treino, y_treino)
modelo_knn.fit(x_treino, y_treino)


# Teste para verificar a acurácia do Modelo caso 'Chutasse' Standard em todas as linhas.
contagem_scores = tabela["score_credito"].value_counts()
print(contagem_scores['Standard'] / sum(contagem_scores))

# Calculo de Previsão
previsao_arvore = modelo_arvore.predict(x_teste)
previsao_knn = modelo_knn.predict(x_teste.to_numpy())

# Ao adquirir essa previsão, então a comparamos seus valores,
# Nesse teste buscamos o maior valor de acurácia, mirando 
# ser mais alto do que o feito com a IA chutando tudo como "Standard"

print(accuracy_score(y_teste, previsao_arvore)) # Acuracia = 0.086033333 83%
print(accuracy_score(y_teste, previsao_knn)) #0.7324 73%


novos_clientes = pd.read_csv("novos_clientes.csv")
display(novos_clientes)
for coluna in novos_clientes.columns:
    if novos_clientes[coluna].dtype == "object" and coluna != "score_credito":
        novos_clientes[coluna] = codificador.fit_transform(novos_clientes[coluna])

previsoes = modelo_arvore.predict(novos_clientes)
print(previsoes)
