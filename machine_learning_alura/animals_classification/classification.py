"""
Features: 1 Sim, 0 Não

cabelo longo
perna curta
faz au au

"""
from sklearn.svm import LinearSVC

porco1 = [0, 1, 0]
porco2 = [0, 1, 1]
porco3 = [1, 1, 0]


cachorro1 = [0, 1, 1]
cachorro2 = [1, 0, 1]
cachorro3 = [1, 1, 1]


dados = [porco1, porco2, porco3, cachorro1, cachorro2, cachorro3]
classes = [1, 1, 1, 0, 0, 0]


model = LinearSVC()
model.fit(dados, classes)


animal_misterioro = [1, 1, 1]


# Prevê as informações com base no modelo passado
predicted_animal = model.predict([animal_misterioro])
print(predicted_animal)
