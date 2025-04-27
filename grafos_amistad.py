import tkinter as tk
from tkinter import ttk
from ttkbootstrap import Style
import random

class Grafo:
    def __init__(self):
        self.adyacencia = {}

    def agregar_usuario(self, usuario):
        if usuario not in self.adyacencia:
            self.adyacencia[usuario] = []

    def agregar_amistad(self, usuario1, usuario2):
        if usuario1 in self.adyacencia and usuario2 in self.adyacencia:
            if usuario2 not in self.adyacencia[usuario1]:
                self.adyacencia[usuario1].append(usuario2)
                self.adyacencia[usuario2].append(usuario1)

    def obtener_amigos(self, usuario):
        return self.adyacencia.get(usuario, [])

    def sugerencias_amistad(self, usuario):
        visitado = set()
        cola = [(usuario, 0)]
        sugerencias = set()

        while cola:
            actual, nivel = cola.pop(0)
            if nivel > 2:
                break
            visitado.add(actual)
            for vecino in self.adyacencia.get(actual, []):
                if vecino not in visitado:
                    if nivel == 1 and vecino not in self.adyacencia[usuario]:
                        sugerencias.add(vecino)
                    cola.append((vecino, nivel + 1))
                    visitado.add(vecino)
        return sugerencias

class AplicacionRedSocial:
    def __init__(self, root):
        self.grafo = Grafo()
        self.posiciones_nodos = {}
        self.root = root
        self.root.title("Roblox - AÑADIR AMIGOS")
        self.style = Style("cyborg")

        self.frame = ttk.Frame(root)
        self.frame.pack(side=tk.LEFT, fill=tk.Y, padx=10, pady=10)

        self.canvas = tk.Canvas(root, bg="white", width=600, height=600)
        self.canvas.pack(side=tk.RIGHT, expand=True, fill=tk.BOTH)

        self.entrada_usuario = ttk.Entry(self.frame)
        self.entrada_usuario.pack(pady=5)
        ttk.Button(self.frame, text="Agregar usuario", command=self.agregar_usuario).pack(pady=5)

        self.entrada_amigo1 = ttk.Entry(self.frame)
        self.entrada_amigo1.pack(pady=5)
        self.entrada_amigo2 = ttk.Entry(self.frame)
        self.entrada_amigo2.pack(pady=5)
        ttk.Button(self.frame, text="Conectar usuarios", command=self.conectar_usuarios).pack(pady=5)

        self.entrada_seleccion = ttk.Entry(self.frame)
        self.entrada_seleccion.pack(pady=5)
        ttk.Button(self.frame, text="Ver amigos y sugerencias", command=self.mostrar_info_usuario).pack(pady=5)

        self.resultado = tk.Text(self.frame, height=15, width=30)
        self.resultado.pack(pady=5)

    def agregar_usuario(self):
        usuario = self.entrada_usuario.get().strip()
        if usuario:
            self.grafo.agregar_usuario(usuario)
            x = random.randint(50, 550)
            y = random.randint(50, 550)
            self.posiciones_nodos[usuario] = (x, y)
            self.dibujar_grafo()

    def conectar_usuarios(self):
        usuario1 = self.entrada_amigo1.get().strip()
        usuario2 = self.entrada_amigo2.get().strip()
        if usuario1 and usuario2:
            self.grafo.agregar_amistad(usuario1, usuario2)
            self.dibujar_grafo()

    def dibujar_grafo(self):
        self.canvas.delete("all")
        for usuario, amigos in self.grafo.adyacencia.items():
            x1, y1 = self.posiciones_nodos.get(usuario, (0, 0))
            for amigo in amigos:
                x2, y2 = self.posiciones_nodos.get(amigo, (0, 0))
                self.canvas.create_line(x1, y1, x2, y2, fill="green", width=2)

        for usuario, (x, y) in self.posiciones_nodos.items():
            self.canvas.create_oval(x-20, y-20, x+20, y+20, fill="#3498db", outline="black", width=2)
            self.canvas.create_text(x, y, text=usuario, fill="white")

    def mostrar_info_usuario(self):
        usuario = self.entrada_seleccion.get().strip()
        if usuario:
            amigos = self.grafo.obtener_amigos(usuario)
            sugerencias = self.grafo.sugerencias_amistad(usuario)
            self.resultado.delete(1.0, tk.END)
            self.resultado.insert(tk.END, f"Amigos de {usuario}:")
            self.resultado.insert(tk.END, "\n" + ", ".join(amigos))
            self.resultado.insert(tk.END, f"\n\nSugerencias de amistad:")
            self.resultado.insert(tk.END, "\n" + ", ".join(sugerencias))

if __name__ == '__main__':
    root = tk.Tk()
    app = AplicacionRedSocial(root)
    root.mainloop()