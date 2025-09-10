# 🖥️ Instalador Windows 11 com Flyoobe

Script em Python com interface gráfica para facilitar a instalação do Windows 11 em dispositivos não compatíveis, utilizando a ferramenta Flyoobe.

---

## 📦 Sobre o Projeto

Este projeto foi criado por **Marcos de Indaiatuba/SP** para ajudar usuários a instalar o Windows 11 de forma simples e visual, mesmo em máquinas que não atendem aos requisitos oficiais da Microsoft, como **TPM 2.0** ou **Secure Boot**.

---

## 🧭 Tutorial de Instalação do Windows 11 com Flyoobe

Este guia mostra passo a passo como usar o script Python e a ferramenta Flyoobe para instalar o Windows 11 em qualquer PC.

### 🔹 Etapa 1: Baixar a ISO do Windows 11

Acesse o site oficial da Microsoft:

🔗 [Download oficial da ISO do Windows 11](https://www.microsoft.com/pt-br/software-download/windows11)

- Clique em **"Baixar imagem ISO"**.
- Selecione o idioma, por exemplo, Português - Brasil.
- Escolha a versão **64 bits (x64)**.

![Página oficial de download do Windows 11](assets/WIN11.png)

### 🔹 Etapa 2: Baixar o Flyoobe

Acesse o repositório oficial:

🔗 [Repositório Flyoobe no GitHub](https://github.com/builtbybel/Flyoobe)

- Baixe o executável mais recente.
- O Flyoobe permite instalar o Windows 11 ignorando requisitos como TPM e Secure Boot.

### 🔹 Etapa 3: Executar o Script Python - Atalho para os links

No repositório, localize o arquivo `instalador_gui.py`. Para executá-lo:

1.  Certifique-se de ter o Python instalado.
2.  Execute o script com um clique duplo ou via terminal:
    ```bash
    python instalador_gui.py
    ```

A interface gráfica será exibida com os links organizados à esquerda da tela.

### 🔹 Etapa 4: Usar o Flyoobe

Execute o Flyoobe como administrador e siga os passos:

- Escolha entre instalação limpa ou atualização.
- Personalize a instalação conforme desejado.
- Para manter seus arquivos, configurações e aplicativos, selecione a opção que mantém seu perfil do Windows 10.

---

## 📌 Observações Importantes

- Faça um **backup** dos seus arquivos antes de iniciar a instalação.
- Tenha uma chave válida do Windows.
- O Flyoobe ignora os requisitos de TPM e Secure Boot.

---

## 📁 Estrutura do Repositório
instalador-win11-flyoobe/
├── assets/                  # Imagens usadas no tutorial
│   ├── WIN11.png
│   └── ISO_WIN11.png
├── instalador_gui.py        # Script principal com interface gráfica
└── README.md                # Este arquivo

---

## 👨‍💻 Autor

**Marcos – Indaiatuba/SP**

Este projeto foi criado para facilitar a instalação do Windows 11 em qualquer PC.
