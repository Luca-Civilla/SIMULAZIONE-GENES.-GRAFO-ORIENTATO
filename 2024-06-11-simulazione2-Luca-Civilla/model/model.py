import copy

import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self._grafo = nx.DiGraph()
        self._cromosomi = DAO.getCromosomi()
        self._grafo.add_nodes_from(self._cromosomi)
        self._bestPath = []
        self._bestScore = 0


    def getPercorso(self,soglia):
        self._bestPath = []
        self._bestScore = 0
        for node in self._grafo.nodes():
            parziale = [node]
            visited_edges = []
            self._ricorsione(parziale,soglia,visited_edges)
        return self._bestScore,self._bestPath


    def _ricorsione(self,parziale,soglia,visited_edges):
        #CONDIZIONE FINALE
        vicini = len(list(self._grafo.successors(parziale[-1])))
        #if len(list(self._grafo.neighbors(parziale[-1]))) == 0:#SBAGLIATA, MANCA CONDIZIONE PER USCIRE DAL CICLO
        if self.calcolaPeso(parziale)>self._bestScore:
            self._bestScore = self.calcolaPeso(parziale)
            self._bestPath = copy.deepcopy(parziale)

        for neighbor in self._grafo.successors((parziale[-1])):
            #GUARDO TUTTI I VICINI DELL'ULTIMO ELEMENTO IN LISTA
            pesoArcoTemp = self._grafo[parziale[-1]][neighbor]["weight"]
            arcoTemp = (parziale[-1],neighbor)
            arcoTempInv = (neighbor, parziale[-1])
            if self._grafo[parziale[-1]][neighbor]["weight"]>soglia:
                if arcoTemp not in visited_edges and arcoTempInv not in visited_edges:
                    parziale.append(neighbor)
                    visited_edges.append(arcoTemp)
                    visited_edges.append(arcoTempInv)
                    self._ricorsione(parziale,soglia,visited_edges)
                    parziale.pop()

    def calcolaPeso(self,listOfNodes):
        pesoTotale = 0
        if len(listOfNodes)==1:
            return pesoTotale
        for i in range(0,len(listOfNodes)-1):
            pesoArco = self._grafo[listOfNodes[i]][listOfNodes[i+1]]["weight"]
            pesoTotale += pesoArco
        return pesoTotale



    def buildGraph(self):
        self._grafo.clear_edges()
        for u in self._grafo.nodes():
            for v in self._grafo.nodes():
                if u!=v:
                    listaInterazioni = DAO.getArchi(u,v)#POTREBBE NON VEDERE IL CROMOSOMA COME INTERO
                    if listaInterazioni:
                        #se entro qua esiste gia l'iterazione tra i cromosomi quindi posso evitare di fare i controlli sulla
                        #dimensione dell'array
                        pesoLista = DAO.getPeso(u,v)
                        peso = pesoLista[0]
                        self._grafo.add_edge(u,v,weight=peso)

    def sortGraph(self):
        sorted_edges = sorted(self._grafo.edges(data=True),key=lambda x:x[2]["weight"])
        return sorted_edges

    def contaArchi(self,soglia):
        #verifico soglia compresa nell'intervallo
        archi = self.sortGraph()
        if soglia >= archi[0][2]["weight"] and soglia <= archi[-1][2]["weight"]:
            listaSuperiori = []
            listaInferiori = []
            for u in archi:
                if u[2]["weight"] > soglia:
                    listaSuperiori.append(u)
                if u[2]["weight"] < soglia:
                    listaInferiori.append(u)
            return len(listaSuperiori),len(listaInferiori)
        else:
            return "Soglia non compresa nell'intervallo"





    def graphDetails(self):
        return len(self._grafo.nodes),len(self._grafo.edges)
