# QA Challenge - Automation Project (UI & API)

Este projeto contém a automação de testes de UI e API para o site **DemoQA**, desenvolvido como parte de um desafio técnico de QA pela Accenture. A estrutura utiliza a abordagem BDD (Behavior Driven Development) para garantir clareza e facilitar a a leitura dos testes e seu propósito.

## Tecnologias Utilizadas

* **Linguagem:** Python 3.12+
* **Framework de BDD:** Behave (abaixo explico do porque nâo utilizei o cucumber)
* **Automação de UI:** Selenium WebDriver
* **Automação de API:** Requests
* **Gerenciamento de Drivers:** WebDriver Manager (Chrome)
* **Padrão de Escrita:** Gherkin (Given, When, Then)

## Cenários Automatizados

### Interface de Usuário (UI)
1.  **Practice Form:** Preenchimento completo de formulário com upload de arquivos e validação de modal.
2.  **Browser Windows:** Gerenciamento de múltiplas abas e validação de conteúdo em novas janelas.
3.  **Web Tables:** Operações de CRUD (Create, Update, Delete) com inserção de múltiplos registros e edição.
4.  **Progress Bar:** Controle de elementos dinâmicos, parando a barra em um ponto específico e realizando o reset.
5.  **Sortable:** Interação complexa de Drag and Drop para reordenar listas.

### API (BookStore)
* Criação de novo usuário com ID dinâmico (UUID).
* Geração e validação de Token de Acesso.
* Listagem e aluguel de livros através de requisições POST.

##  Behave vs. Cucumber: Por que Behave?

Optei pelo **Behave** pelos seguintes motivos técnicos:

1.  **Compatibilidade Nativa:** O Cucumber é focado em ecossistemas como Java, Ruby e JavaScript. Para Python, o **Behave** é a implementação oficial e mais estável do BDD.
2.  **Integração com Selenium:** O Behave gerencia o objeto de contexto (`context`) de forma muito eficiente no Python, permitindo compartilhar o WebDriver entre diferentes arquivos de passos sem complexidade extra.
3.  **Ecossistema Python:** O uso do Behave permite que todas as bibliotecas de suporte (como `Requests` para API e `PyTest` para asserções) trabalhem de forma síncrona e simplificada.

## Configuração do Ambiente

### Pré-requisitos
* Python instalado (versão 3.12 ou superior).
* Navegador Google Chrome.

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/opedroamarall/QA_Challenge_of.git

   cd \QA_Challenge_of

### O projeto utiliza o comando padrão do framework para disparo dos cenários. ###

**Executar todos os testes**
- Execute este comando no Terminal onde está localizado o projeto
`behave`