## Grafos amigos y sugerencias

Esta es una aplicación gráfica creada en **Python** 🐍 que simula una **red social** donde puedes:
- 👤 Agregar usuarios
- 🔗 Conectarlos como amigos
- 🤝 Visualizar amistades y recibir sugerencias de nuevos amigos

La interfaz utiliza **Tkinter** junto con **ttkbootstrap** para el frontend

---

## 🛠️ Tecnologías Usadas

- Python 3
- Tkinter
- ttkbootstrap

---

## 🚀 ¿Cómo Funciona?

### ➕ Agregar usuario
Escribe el nombre de un nuevo usuario en el campo de entrada y presiona **Agregar usuario**.  
El usuario aparecerá representado como un nodo azul en el canvas.

```python
def agregar_usuario(self):
    usuario = self.entrada_usuario.get().strip()
    if usuario:
        self.grafo.agregar_usuario(usuario)
        x = random.randint(50, 550)
        y = random.randint(50, 550)
        self.posiciones_nodos[usuario] = (x, y)
        self.dibujar_grafo()
```

---

### 🔗 Conectar usuarios
Escribe el nombre de dos usuarios y presiona **Conectar usuarios** para crear una amistad.  
Se dibujará una línea verde entre ambos.

```python
def conectar_usuarios(self):
    usuario1 = self.entrada_amigo1.get().strip()
    usuario2 = self.entrada_amigo2.get().strip()
    if usuario1 and usuario2:
        self.grafo.agregar_amistad(usuario1, usuario2)
        self.dibujar_grafo()
```

---

### 🔍 Ver amigos y sugerencias
Escribe el nombre de un usuario, y al hacer clic en **Ver amigos y sugerencias**, verás:
- 👫 Lista de amigos actuales
- 🎯 Sugerencias de nuevos amigos

```python
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
```

---

## 🧠 Estructura del Código

- **Grafo** 📈  
  Maneja la estructura de usuarios y sus conexiones.

- **AplicacionRedSocial** 🎨  
  Controla la interfaz gráfica y las acciones del usuario.

- **main** 🚀  
  Inicializa y ejecuta la aplicación.

```python
if __name__ == '__main__':
    root = tk.Tk()
    app = AplicacionRedSocial(root)
    root.mainloop()
```

---


