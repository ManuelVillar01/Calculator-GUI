import tkinter as tk
#Widget Root
mainW = tk.Tk()
mainW.title("Calculadora Estándar")
mainW.geometry("400x360")
mainW.resizable(False,False)
mainW.config(bg="#16232f")

#Resultado
resultado = tk.Label(mainW,text="")
resultado.grid(column=0,row=1,columnspan=5)
resultado.config(bg="#16232f",fg="#FFFFFF", font=("Arial", 14,"bold"))

#Campo
campo = tk.Entry(mainW,text="")
campo.grid(column=0,row=2,columnspan=5)
campo.config(bg="#16232f",fg="#FFFFFF", font=("Arial", 14,"bold"),width=35)

#Funciones
def borrar():
    valor = len(campo.get())
    campo.delete(0,valor)
    resultado["text"] = " "
    
def ingresar(s):
    valor = campo.get()
    campo.insert(len(valor),s)

def ingresarSim(s):
    valor = campo.get()
    campo.insert(len(valor)," ")
    campo.insert(len(valor)+1,s)
    campo.insert(len(valor)+2," ")
    
def borrarEle():
    valor = len(campo.get())
    campo.delete(valor-1,valor)

def calcRes():
    num = campo.get()
    try:
         resultado["text"] = int(eval(num))
    except Exception:
        resultado["text"] = "Operación invalida"
   

#Números
num1 = tk.Button(mainW, text=1,command=lambda j=1:ingresar(j))
num1.grid(column=0,row=3)
num1.config(width=11, height=3, fg="#FFFFFF",font=("Arial",10,"bold"),bg="#000000")
num2 = tk.Button(mainW, text=2,command=lambda j=2:ingresar(j))
num2.grid(column=1,row=3)
num2.config(width=11, height=3, fg="#FFFFFF",font=("Arial",10,"bold"),bg="#000000")
num3 = tk.Button(mainW, text=3,command=lambda j=3:ingresar(j))
num3.grid(column=2,row=3)
num3.config(width=11, height=3, fg="#FFFFFF",font=("Arial",10,"bold"),bg="#000000")
num4 = tk.Button(mainW, text=4,command=lambda j=4:ingresar(j))
num4.grid(column=0,row=4)
num4.config(width=11, height=3, fg="#FFFFFF",font=("Arial",10,"bold"),bg="#000000")
num5 = tk.Button(mainW, text=5,command=lambda j=5:ingresar(j))
num5.grid(column=1,row=4)
num5.config(width=11, height=3, fg="#FFFFFF",font=("Arial",10,"bold"),bg="#000000")
num6 = tk.Button(mainW, text=6,command=lambda j=6:ingresar(j))
num6.grid(column=2,row=4)
num6.config(width=11, height=3, fg="#FFFFFF",font=("Arial",10,"bold"),bg="#000000")
num7 = tk.Button(mainW, text=7,command=lambda j=7:ingresar(j))
num7.grid(column=0,row=5)
num7.config(width=11, height=3, fg="#FFFFFF",font=("Arial",10,"bold"),bg="#000000")
num8 = tk.Button(mainW, text=8,command=lambda j=8:ingresar(j))
num8.grid(column=1,row=5)
num8.config(width=11, height=3, fg="#FFFFFF",font=("Arial",10,"bold"),bg="#000000")
num9 = tk.Button(mainW, text=9,command=lambda j=9:ingresar(j))
num9.grid(column=2,row=5)
num9.config(width=11, height=3, fg="#FFFFFF",font=("Arial",10,"bold"),bg="#000000")
num0 = tk.Button(mainW, text=0,command=lambda j=0:ingresar(j))
num0.grid(column=1,row=6)
num0.config(width=11, height=3, fg="#FFFFFF",font=("Arial",10,"bold"),bg="#000000")

#Simbolos
botonSum = tk.Button(mainW, text="+", command=lambda j="+": ingresarSim(j))
botonSum.grid(column=4,row=3)
botonSum.config(width=11, height=3, fg="#FFFFFF",font=("Arial",10,"bold"),bg="#000000")
botonRes = tk.Button(mainW, text="-", command=lambda j="-": ingresarSim(j))
botonRes.grid(column=4,row=4)
botonRes.config(width=11, height=3, fg="#FFFFFF",font=("Arial",10,"bold"),bg="#000000")
botonMul = tk.Button(mainW, text="*", command=lambda j="*": ingresarSim(j))
botonMul.grid(column=4,row=5)
botonMul.config(width=11, height=3, fg="#FFFFFF",font=("Arial",10,"bold"),bg="#000000")
botonDiv = tk.Button(mainW, text="/", command=lambda j="/": ingresarSim(j))
botonDiv.grid(column=4,row=6)
botonDiv.config(width=11, height=3, fg="#FFFFFF",font=("Arial",10,"bold"),bg="#000000")
botonIgual = tk.Button(mainW, text="=", command=calcRes)
botonIgual.grid(column=0,row=6)
botonIgual.config(width=11, height=3, fg="#FFFFFF",font=("Arial",10,"bold"),bg="#000000")
botonDel = tk.Button(mainW, text="C", command=borrar)
botonDel.grid(column=0,row=7)
botonDel.config(width=11, height=3, fg="#FFFFFF",font=("Arial",10,"bold"),bg="#000000")
botonDelEle = tk.Button(mainW, text="<-", command=borrarEle)
botonDelEle.grid(column=1,row=7)
botonDelEle.config(width=11, height=3, fg="#FFFFFF",font=("Arial",10,"bold"),bg="#000000")



    


mainW.mainloop()


