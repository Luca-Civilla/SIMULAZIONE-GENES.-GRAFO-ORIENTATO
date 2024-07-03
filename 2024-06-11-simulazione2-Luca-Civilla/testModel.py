from model.model import Model
mymodel = Model()
mymodel.buildGraph()
nodi,archi = mymodel.graphDetails()
print(nodi)
print(archi)
archiOrdinati = mymodel.sortGraph()
print(f"peso piu basso:{archiOrdinati[0][2]["weight"]} mentre quello piu alto: {archiOrdinati[-1]}")
score, path = mymodel.getPercorso(3)
print(score)
for i in range(0,len(path)-1):
    print(f"{path[i]}--->{path[i+1]}")
