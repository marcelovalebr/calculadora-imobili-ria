import tkinter as tk

def calcular_valor_imovel():
    try:
        financiamento = float(entrada_financiamento.get())
        taxa = 0.20  # 20% como decimal
        valor_imovel = financiamento / (1 - taxa)
        resultado.config(text=f"Valor do imóvel sem entrada: R$ {valor_imovel:.2f}")
    except ValueError:
        resultado.config(text="Por favor, insira um valor válido.")

# Criação da janela
janela = tk.Tk()
janela.title("Calculadora Imóvel Sem Entrada")
janela.geometry("350x200")  # Define o tamanho da janela

# Rótulo e entrada para o financiamento
rotulo_financiamento = tk.Label(janela, text="Informe o valor que o imóvel está sendo vendido (R$):", font=("Arial", 12))
rotulo_financiamento.pack(pady=10)  # Espaçamento vertical

entrada_financiamento = tk.Entry(janela, font=("Arial", 12))
entrada_financiamento.pack(pady=5)  # Espaçamento vertical

# Botão para calcular o valor do imóvel
botao_calcular = tk.Button(janela, text="Calcular Valor Sem Entrada", command=calcular_valor_imovel, font=("Arial", 12))
botao_calcular.pack(pady=10)  # Espaçamento vertical

# Rótulo para exibir o resultado
resultado = tk.Label(janela, text="", font=("Arial", 14), fg="yellow")
resultado.pack(pady=10)  # Espaçamento vertical

# Iniciar a interface gráfica
janela.mainloop()
