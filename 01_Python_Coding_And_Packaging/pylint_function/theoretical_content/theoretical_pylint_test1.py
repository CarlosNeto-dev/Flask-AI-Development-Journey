# O comando "writefile" cria um arquivo ".py" no mesmo local que está localizado o código "ipynb" e
# permite o uso do comando "!pylint" no ambiente do Jupyter Notebook.

def NoSumOfNumbers(num1,num2):
    """
    Exemplo de código com alguns avisos (warnings) do Pylint.
    1. Nome da função (C0103)
    2. Variável não usada (W0612)
    """

    no_sum_of_numbers = num1+num2

    return num1

# Chamar a função evita o erro de "função nunca usada"
NoSumOfNumbers(5,10)
