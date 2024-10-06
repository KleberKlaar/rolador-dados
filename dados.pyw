import tkinter as tk
import random

# Função para rolar os dados e mostrar o resultado
def roll_dice(faces):
    result = random.randint(1, faces)
    result_label.config(text=f"Resultado: {result}")

# Função para rolar um dado personalizado
def roll_custom_dice():
    try:
        faces = int(custom_entry.get())
        if faces > 0:
            roll_dice(faces)
        else:
            result_label.config(text="Insira um número válido")
    except ValueError:
        result_label.config(text="Insira um número válido")

# Criação da janela principal
root = tk.Tk()
root.title("Rolador de Dados - Kleber Klaar")

# Título do programa
title_label = tk.Label(root, text="Rolador de Dados", font=("Helvetica", 20, "bold"))
title_label.pack(pady=10)

# Frame para organizar os botões de dados comuns
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

# Criação dos botões para os dados comuns (2 por linha)
dice_buttons = {
    "D4": 4,
    "D6": 6,
    "D8": 8,
    "D10": 10,
    "D12": 12,
    "D20": 20,
    "D100": 100
}

row = 0
col = 0
for dice, faces in dice_buttons.items():
    button = tk.Button(button_frame, text=dice, command=lambda faces=faces: roll_dice(faces), width=10)
    button.grid(row=row, column=col, padx=5, pady=5)
    col += 1
    if col == 2:  # 2 botões por linha
        row += 1
        col = 0

# Label para dado personalizado
custom_label = tk.Label(root, text="Dado personalizado (nº de faces):")
custom_label.pack(pady=5)

# Campo de entrada para dado personalizado
custom_entry = tk.Entry(root)
custom_entry.pack(pady=5)

# Botão para rolar o dado personalizado
custom_button = tk.Button(root, text="Rolar", command=roll_custom_dice)
custom_button.pack(pady=10)

# Label para mostrar o resultado da rolagem, abaixo dos botões
result_label = tk.Label(root, text="Resultado: ", font=("Helvetica", 16))
result_label.pack(pady=10)

# Rodapé com o nome do criador
footer_label = tk.Label(root, text="Criado por Kleber Klaar", font=("Helvetica", 10))
footer_label.pack(side=tk.BOTTOM, pady=10)

# Iniciar o loop principal
root.mainloop()
