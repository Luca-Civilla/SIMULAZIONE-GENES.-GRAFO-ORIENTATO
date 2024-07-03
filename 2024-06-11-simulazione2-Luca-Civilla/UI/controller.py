import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handle_graph(self, e):
        self._model.buildGraph()
        nodi,archi= self._model.graphDetails()
        self._view.txt_result.controls.clear()
        self._view.txt_result.controls.append(ft.Text(f"Numero di nodi: {nodi}, Numero di archi: {archi}"))
        archiOrdinati = self._model.sortGraph()
        self._view.txt_result.controls.append(ft.Text(f"Valore minimo:{archiOrdinati[0][2]["weight"]} --- Valore massimo: {archiOrdinati[-1][2]["weight"]}"))

        self._view.update_page()


    def handle_countedges(self, e):
        if len(self._model._grafo.edges)==0:
            self._view.txt_result2.controls.clear()
            self._view.txt_result2.controls.append(ft.Text("Attenzione creare prima il grafo"))
            return
        try:
            int(self._view.txt_name.value)
        except ValueError:
            self._view.txt_result2.controls.clear()
            self._view.txt_result2.controls.append(ft.Text(f"Inserire un numero!"))
            return

        soglia = int(self._view.txt_name.value)
        numeroSup, numeroInf = self._model.contaArchi(soglia)
        self._view.txt_result2.controls.clear()
        self._view.txt_result2.controls.append(
            ft.Text(f"Numero di archi con peso maggiore della soglia {soglia}: {numeroSup}"))
        self._view.txt_result2.controls.append(ft.Text(f"Numero di archi con peso minore della soglia {soglia}: {numeroInf}"))

        self._view.update_page()

    def handle_search(self, e):
        pass