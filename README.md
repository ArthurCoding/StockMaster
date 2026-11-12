# StockMaster – Cadastro automatizado de produtos (RPA em Python)

Automação que simula um usuário: abre o navegador, faz login em um sistema web de cadastro e registra, um a um, os produtos de uma planilha CSV (cerca de 290 itens), sem digitação manual.

Projeto desenvolvido a partir do Intensivão de Python da Hashtag Programação.

## Como funciona
1. Abre o navegador e acessa a página de login do sistema.
2. Preenche e-mail e senha lidos de variáveis de ambiente (nada fica no código).
3. Lê `produtos.csv` com Pandas.
4. Para cada produto, preenche código, marca, tipo, categoria, preço, custo e observação e envia o formulário.

## Tecnologias
- Python 3
- PyAutoGUI (automação de teclado e mouse)
- Pandas (leitura e tratamento da planilha)

## Como executar
```powershell
pip install pyautogui pandas
$env:HASHTAG_EMAIL="seu_email"
$env:HASHTAG_SENHA="sua_senha"
python codigo.py
```
As coordenadas de clique (`pyautogui.click`) dependem da resolução da tela. O script `auxiliar.py` mostra a posição do mouse para ajustá-las.

## Arquivos
| Arquivo | Função |
|---|---|
| `codigo.py` | Automação principal |
| `auxiliar.py` | Captura a posição do mouse para calibrar os cliques |
| `produtos.csv` | Base com os produtos a cadastrar |
