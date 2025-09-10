import tkinter as tk
import webbrowser


def abrir_link_windows():
    webbrowser.open("https://www.microsoft.com/pt-br/software-download/windows11")


def abrir_link_flyoobe():
    webbrowser.open("https://github.com/builtbybel/Flyoobe")


# Criar janela principal
janela = tk.Tk()
janela.title("Orientador de Instalação - Windows 11 com Flyoobe")
janela.geometry(
    "500x300+0+100"
)  # Largura x Altura + posição X + posição Y (esquerda da tela)
janela.resizable(False, False)

# Título
titulo = tk.Label(
    janela, text="Instalação do Windows 11 com Flyoobe", font=("Arial", 14, "bold")
)
titulo.pack(pady=10)

# Instruções
instrucoes = tk.Label(
    janela,
    text="Siga os passos abaixo para preparar sua instalação:",
    font=("Arial", 10),
)
instrucoes.pack(pady=5)

# Passo 1
passo1 = tk.Label(
    janela, text="1️⃣ Baixe a imagem ISO do Windows 11:", font=("Arial", 10)
)
passo1.pack(anchor="w", padx=20)

link1 = tk.Label(
    janela,
    text="👉 Abrir site da Microsoft",
    fg="blue",
    cursor="hand2",
    font=("Arial", 10, "underline"),
)
link1.pack(anchor="w", padx=40)
link1.bind("<Button-1>", lambda e: abrir_link_windows())

# Passo 2
passo2 = tk.Label(janela, text="2️⃣ Baixe o Flyoobe:", font=("Arial", 10))
passo2.pack(anchor="w", padx=20, pady=(10, 0))

link2 = tk.Label(
    janela,
    text="👉 Abrir repositório Flyoobe no GitHub",
    fg="blue",
    cursor="hand2",
    font=("Arial", 10, "underline"),
)
link2.pack(anchor="w", padx=40)
link2.bind("<Button-1>", lambda e: abrir_link_flyoobe())

# Passo 3
passo3 = tk.Label(
    janela,
    text="3️⃣ Siga o roteiro no README para continuar a instalação.",
    font=("Arial", 10),
)
passo3.pack(anchor="w", padx=20, pady=(10, 0))

# Rodapé
rodape = tk.Label(
    janela, text="Desenvolvido por Marcos • Indaiatuba/SP", font=("Arial", 8), fg="gray"
)
rodape.pack(side="bottom", pady=10)

# Executar janela
janela.mainloop()
