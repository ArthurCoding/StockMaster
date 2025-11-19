Automação de Estoque – Projeto inspirado no site do Lira (Hashtag Programação)

Este projeto automatiza o controle de estoque de produtos usando Python.
Ele lê a base de dados, identifica itens críticos, atualiza saldos e envia relatórios prontos para uso.
É uma ferramenta prática para reduzir erros e acelerar a gestão de estoque.

📌 Objetivo

Automatizar processos manuais de estoque.

Identificar produtos com quantidade baixa.

Atualizar informações de entrada e saída.

Gerar relatórios rápidos e confiáveis.


🛠 Tecnologias usadas

Python 3.x

Pandas

OpenPyXL / CSV

Jupyter ou VS Code

Selenium (opcional, caso busque dados do site)



🚀 Funcionalidades

Leitura automática da planilha de estoque.

Aplicação de entradas, saídas e correções.

Detecção de itens abaixo do limite mínimo.

Exportação de um relatório atualizado.

(Opcional) Coleta de dados direto do site usando Selenium.





▶️ Como executar

Clone o repositório

"git clone https://github.com/seu-user/seu-projeto.git "


Instale as dependências

"pip install -r requirements.txt"


Execute o script principal

python src/automacao.py

📊 Exemplo de saída do relatório

Lista de produtos com estoque crítico.

Quantidade atualizada após movimentações.

Produtos cadastrados com inconsistências.

Arquivo final exportado como relatorio_estoque.xlsx



📈 Fluxo da automação

Carrega as planilhas.

Limpa e organiza os dados.

Aplica as movimentações do dia.

Atualiza estoque final.

Gera aviso de itens críticos.

Exporta relatório.

🧩 Personalização

Você pode adaptar:

Limite mínimo de estoque.

Origem dos dados (Excel, CSV ou Web).

Formato do relatório.

Métodos de envio (e-mail, WhatsApp, dashboard).

📘 Sobre o projeto
Este projeto foi inspirado nas aulas do Lira da Hashtag Programação.
Serve como estudo prático de automação, Python e manipulação de dados.



