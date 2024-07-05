# Calculadora de Valor de Imóvel Sem Entrada

Este é um aplicativo de desktop em Python que calcula o valor de um imóvel sem a entrada. A interface gráfica foi criada com `tkinter`.

## Funcionalidades

- **Calcular Valor de Imóvel:** Insira o valor do financiamento e o aplicativo calculará o valor total do imóvel sem a entrada.

## Tecnologias Utilizadas

- Python
- Tkinter (para interface gráfica)

## Pré-requisitos

- Python 3.x
- Biblioteca Tkinter (inclusa por padrão em Python)

## Instalação

1. Clone o repositório:
    ```bash
    git clone https://github.com/seu-usuario/calculadora-imovel-sem-entrada.git
    cd calculadora-imovel-sem-entrada
    ```

2. Execute o script:
    ```bash
    python calculadora_imovel.py
    ```

## Uso

1. Abra o aplicativo e insira o valor do financiamento no campo de entrada.
2. Clique no botão "Calcular Valor Sem Entrada".
3. O valor total do imóvel sem a entrada será exibido na tela.

## Código Exemplo

```python
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

# Contribuição

Sinta-se à vontade para contribuir com melhorias. Faça um fork do projeto, crie uma branch para suas alterações e envie um pull request.

Faça um fork do projeto.
Crie uma branch com a nova feature (git checkout -b feature/nova-feature).
Comite as alterações (git commit -am 'Adiciona nova feature').
Envie a branch (git push origin feature/nova-feature).
Abra um Pull Request.

# Licença

Este projeto está licenciado sob a licença MIT. Consulte o arquivo LICENSE para mais detalhes.

Feito com ❤️ por Marcelo Vale
