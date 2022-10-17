#Programa: EditorDeTexto.py
#Proposito: Creación de un Editor de Texto con opciones básicas.
#Autor: Ezequiel Lopez
#Fecha: 17/10/2022

import tkinter as tk
from tkinter.filedialog import askopenfile, asksaveasfile, asksaveasfilename

class EditorDeTexto(tk.Tk):
    
    def __init__(self):
        super().__init__()

        # Creamos y parametrizamos la ventana
        #self.geometry("1000x900")
        self.title("Editor de Texto")
        self.resizable(0,0)
        self.rowconfigure(0, minsize=600, weight=1)
        self.columnconfigure(1, minsize=600, weight=1)

        # Atributo de Campo de Texto
        self._campo_texto = tk.Text(self, wrap=tk.WORD, bg="#FFFFFF", fg="black", font=("arial", 14))

        # Atributo de archivo
        self._archivo = None

        # Atributo para saber si ya se abrió un archivo anteriormente
        self._archivo_abierto = False

        # Llamado a la función Menu de Opciones
        self._crear_menu()

        # Llamado a la funcion Frame_Opciones
        self._creacion_componentes()

    def _crear_menu(self):

        # Creación del Menu Principal
        main_menu = tk.Menu(self)

        # Creación de Archivo
        archivo = tk.Menu(main_menu, tearoff=False)

        # Agregado de opciones al Menu de Archivo
        archivo.add_command(label="Abrir", command= self._abrir)
        archivo.add_command(label="Guardar", command= self._guardar)
        archivo.add_command(label="Guardar como...", command= self._guardar_como)

        # Agregado de un separador
        archivo.add_separator()

        # Agregamos la opción de salida dentro del Menu de Archivo
        archivo.add_command(label="Salir", command= self._salir)

        # Agregado el menu Archivo al Main_Menu
        main_menu.add_cascade(menu=archivo, label="Archivo")

        # Mostramos el Menu
        self.config(menu=main_menu)

    def _abrir(self):
        try:
            
            # Abrimos el archivo para edición (Lectura-Escritura)
            self._archivo_abierto = askopenfile(mode="r+")
            
            # Eliminamos el texto anterior
            self._campo_texto.delete(1.0, tk.END)
            
            # Revisamos si hay un archivo
            if not self._archivo_abierto:return

            # Abrimos el archivo en modo Lectura/Escritura como un recurso
            with open(self._archivo_abierto.name, mode="r+", encoding="UTF-8") as self._archivo:
                # Leemos el contenido
                self._campo_texto.insert(1.0, self._archivo.read())

                # Modificamos el titulo de la aplicación
                self.title(f"*Editor de Texto - {self._archivo.name}")
                                                                       
        except Exception as e:tk.messagebox.showerror(f"Ocurrio un error {e}")

    def _guardar(self):
        try:
            # Si ya se abrió un archivo previamente, lo sobreescribe
            if self._archivo_abierto:
                with open(self._archivo_abierto.name, mode="w") as self._archivo:
                    # Leemos el contenido de la caja de texto
                    texto = self._campo_texto.get(1.0, tk.END)
                    # Escribimos el mismo contenido al archivo
                    self._archivo.write(texto)
                    # Cambiamos el nombre del titulo de la App
                    self.title(f"Editor de Texto - {self._archivo.name}") 

            else: self._guardar_como()

        except Exception as e:tk.messagebox.showerror(f"Ocurrio un error {e}") 

    def _guardar_como(self):
        try:

            self._archivo = asksaveasfilename(
            defaultextension='txt',
            filetypes=[('Archivos de Texto', '*.txt'), ('Todos los archivos', '*.*')]
            )

            if not self._archivo: return

            # Abrimos el archivo en modo Lectura/Escritura como un recurso
            with open(self._archivo, mode="w") as self._archivo:
                # Leemos el contenido
                self._archivo.write(self._campo_texto.get(1.0, tk.END))

                # Modificamos el titulo de la aplicación
                self.title(f"Editor de Texto - {self._archivo.name}")
         
                # Indicamos que ya hemos abierto un archivo
                self._archivo_abierto = self._archivo

        except Exception as e: tk.messagebox.showerror(f"Ocurrio un error {e}")

    def _salir(self):
        pass

    def _creacion_componentes(self):
        
        # Creación del Frame de Bótones
        frame_bot = tk.Frame(self, relief=tk.RAISED, bd=2, bg="#FFFFFF")

        # Publicación del Frame
        frame_bot.grid(row=0, column=0, sticky="ns")

        # Creación de los Bótones
        boton_abrir = tk.Button(frame_bot, text="Abrir", bd=0, bg="#FFFFFF", font=("arial", 10, "bold"), fg="black",
                                command=self._abrir)

        boton_guardar = tk.Button(frame_bot, text="Guardar", bd=0, bg="#FFFFFF", font=("arial", 10, "bold"), fg="black",
                                command= self._guardar)

        boton_guardar_como = tk.Button(frame_bot, text="Guardar como...", bd=0, bg="#FFFFFF", font=("arial", 10, "bold"), fg="black",
                                command= self._guardar_como)

        # Publicación de los bótones
        boton_abrir.grid(row=0, column=0, padx=5, pady=5, sticky="we")
        boton_guardar.grid(row=1, column=0, padx=5, pady=5, sticky="we")
        boton_guardar_como.grid(row=2, column=0, padx=5, pady=5, sticky="we")

        # Agregamos el campo de texto
        self._campo_texto.grid(row=0, column=1, sticky="nswe")


if __name__ == "__main__":
    intento = EditorDeTexto()
    intento.mainloop()