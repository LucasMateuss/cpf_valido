import tkinter as tk
from function import *

janela = tk.Tk()

janela.title("Verificador de CPF")

rotulo_cpf = tk.Label(janela, text="Informe o CPF:")
rotulo_cpf.pack()

entrada_cpf = tk.Entry(janela)
entrada_cpf.pack()

def verifica():
  cpf = entrada_cpf.get()
  if verifica_cpf(cpf):
    resultado = "CPF válido"
  else:
    resultado = "CPF inválido"
  
  janela_resultado = tk.Toplevel(janela)
  janela_resultado.title("Resultado")
  rotulo_resultado = tk.Label(janela_resultado, text=resultado)
  rotulo_resultado.pack()

botao = tk.Button(janela, text="Verificar", command=verifica)
botao.pack()

janela.mainloop()

