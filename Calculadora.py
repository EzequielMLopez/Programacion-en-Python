#Programa: Calculadora.py
#Proposito: Creación de una Calculadora con las funciones básicas.
#Autor: Ezequiel Lopez
#Fecha: 11/10/2022

import tkinter as tk
from tkinter import messagebox

class Calculadora(tk.Tk):

    def __init__(self):
        super().__init__()

        # Creamos la ventana de la caluladora
        self.geometry("400x450")
        self.title("Calculadora")
        self.resizable(0,0)

        # Atributos de clase, almacena lo que se escribe en la caja de texto
        self.expresion = ""

        # Caja de texto (input)
        self.entrada = None

        # Variable asociada a la caja de texto (string var) para obtener el valor del input
        self.entrada_var = tk.StringVar()   

        # Llamado al método para poder crear los componentes
        self._creacion_componentes()

    # Método para crear los componentes
    def _creacion_componentes(self):
        # Creación del frame para la caja de texto
        entrada_frame = tk.Frame(self, width=400, height=50)
        entrada_frame.pack(side=tk.TOP)

        # Caja de texto
        entrada = tk.Entry(entrada_frame, font=("arial", 18, "bold"), textvariable=self.entrada_var, width=30,
                                                 justify=tk.RIGHT, background="black")
        entrada.grid(row=0, column=0, ipady=10)

        # Creamos otro frame para la parte inferior
        botones_frame = tk.Frame(self, width=400, height=450, bg="grey")
        botones_frame.pack()

        # Primer renglón, definimos el bóton de limpieza (c)
        boton_clear = tk.Button(botones_frame, text="C", width='37', height=3, bd=0, #background="#eee",
                                 cursor="hand2", command=self._evento_limpiar)
        boton_clear.grid(row=0, column=0, columnspan=3, padx=1, pady=1)

        # Bóton de Division
        boton_division = tk.Button(botones_frame, text="/", width=10, height=3, bd=0, #background="#eee",
                                    cursor="hand2", command=lambda: self._evento_click("/"))
        boton_division.grid(row=0, column=3, padx=1, pady=1)

        # Segundo renglón
        boton_siete = tk.Button(botones_frame, text="7", width=10, height=3, bd=0, #background="white",
                                cursor="hand2", command=lambda: self._evento_click(7))
        boton_siete.grid(row=1, column=0, padx=1, pady=1)

        boton_ocho = tk.Button(botones_frame, text="8", width=10, height=3, bd=0, #background="white",
                                cursor="hand2", command=lambda: self._evento_click(8))
        boton_ocho.grid(row=1, column=1, padx=1, pady=1)


        boton_nueve = tk.Button(botones_frame, text="9", width=10, height=3, bd=0, #background="white",
                                cursor="hand2", command=lambda: self._evento_click(9))
        boton_nueve.grid(row=1, column=2, padx=1, pady=1)


        boton_multiplicacion = tk.Button(botones_frame, text="*", width=10, height=3, bd=0, #background="#eee",
                                    cursor="hand2", command=lambda: self._evento_click("*"))
        boton_multiplicacion.grid(row=1, column=3, padx=1, pady=1)

        # Tercer renglón
        boton_cuatro = tk.Button(botones_frame, text="4", width=10, height=3, bd=0, #background="white",
                                cursor="hand2", command=lambda: self._evento_click(4))
        boton_cuatro.grid(row=2, column=0, padx=1, pady=1)

        boton_cinco = tk.Button(botones_frame, text="5", width=10, height=3, bd=0, #background="white",
                                cursor="hand2", command=lambda: self._evento_click(5))
        boton_cinco.grid(row=2, column=1, padx=1, pady=1)


        boton_seis = tk.Button(botones_frame, text="6", width=10, height=3, bd=0, #background="white",
                                cursor="hand2", command=lambda: self._evento_click(6))
        boton_seis.grid(row=2, column=2, padx=1, pady=1)


        boton_menos = tk.Button(botones_frame, text="-", width=10, height=3, bd=0, #background="#eee",
                                    cursor="hand2", command=lambda: self._evento_click("-"))
        boton_menos.grid(row=2, column=3, padx=1, pady=1)

        # Cuarto renglón
        boton_uno = tk.Button(botones_frame, text="1", width=10, height=3, bd=0, #background="white",
                                cursor="hand2", command=lambda: self._evento_click(1))
        boton_uno.grid(row=3, column=0, padx=1, pady=1)

        boton_dos = tk.Button(botones_frame, text="2", width=10, height=3, bd=0, #background="white",
                                cursor="hand2", command=lambda: self._evento_click(2))
        boton_dos.grid(row=3, column=1, padx=1, pady=1)


        boton_tres = tk.Button(botones_frame, text="3", width=10, height=3, bd=0, #background="white",
                                cursor="hand2", command=lambda: self._evento_click(3))
        boton_tres.grid(row=3, column=2, padx=1, pady=1)


        boton_mas = tk.Button(botones_frame, text="+", width=10, height=3, bd=0, #background="#eee",
                                    cursor="hand2", command=lambda: self._evento_click("+"))
        boton_mas.grid(row=3, column=3, padx=1, pady=1)

        # Quinto renglón
        boton_cero = tk.Button(botones_frame, text="0", width=24, height=3, bd=0, #background="white",
                                cursor="hand2", command=lambda: self._evento_click(0))
        boton_cero.grid(row=4, column=0, columnspan=2, padx=1, pady=1)

        boton_coma = tk.Button(botones_frame, text=",", width=10, height=3, bd=0, #background="white",
                                cursor="hand2", command=lambda: self._evento_click(","))
        boton_coma.grid(row=4, column=2, padx=1, pady=1)


        boton_igual = tk.Button(botones_frame, text="=", width=10, height=3, bd=0, #background="white",
                                cursor="hand2", command= self._evento_evaluar)
        boton_igual.grid(row=4, column=3, padx=1, pady=1)


    # Método de Limpieza 
    def _evento_limpiar(self):
        self.expresion = ""
        self.entrada_var.set(self.expresion)

    def _evento_click(self, elemento):
        # Concatenamos el nuevo elemento que se haya presionado a la expresión ya existente
        self.expresion = f"{self.expresion}{elemento}"
        self.entrada_var.set(self.expresion)

    def _evento_evaluar(self):
        # Eval evalua la expresión aritmetica str como una expresión aritmética
        try:
            if self.expresion:
                resultado = str(eval(self.expresion))
                self.entrada_var.set(resultado)
        except Exception as e:
            messagebox.showerror("Erro", f"Ocurrio un error {e}")
            self.entrada_var.set("")
        finally:    
            self.expresion = ""

if __name__ == "__main__":
    calcu = Calculadora()
    calcu.mainloop()