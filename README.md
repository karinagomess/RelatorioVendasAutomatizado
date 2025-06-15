Relatório de Vendas Automatizado

Este é um projeto para automatizar a geração de relatórios de vendas utilizando Python, SQL Server, Power BI e Excel. O objetivo é processar os dados de vendas, armazená-los em um banco de dados e criar relatórios dinâmicos que ajudam na tomada de decisões.

Tecnologias Utilizadas:

Python: Usado para processar os dados, conectar ao banco de dados e automatizar a execução do processo.

SQL Server: Banco de dados relacional usado para armazenar os dados de vendas.

Power BI: Utilizado para criar dashboards interativos e relatórios dinâmicos.

Excel: Usado para criar e exportar os dados iniciais em formato CSV.

Como Usar
1. Pré-requisitos

Certifique-se de ter as seguintes ferramentas instaladas em seu computador:

Python 3.x: Para rodar o código Python. Você pode baixá-lo em: https://www.python.org/downloads/.

SQL Server: O banco de dados usado no projeto. Você pode obter mais informações e o download em: https://www.microsoft.com/en-us/sql-server/sql-server-downloads.

Power BI Desktop: Para criar os relatórios e dashboards. Pode ser baixado em: https://powerbi.microsoft.com/desktop/.

Editor de Código (opcional): Como o Visual Studio Code (VSCode) para facilitar a edição do código.


2. Instalar as Dependências
Clone o repositório ou faça o download dos arquivos para o seu computador.

Em terminal, execute:

git clone https://github.com/seu-usuario/RelatorioVendasAutomatizado.git

Instale as dependências do Python. No terminal, na pasta do projeto, execute:

instalar as bibliotecas necessárias, como pandas e pyodbc.

3. Executar o Código Python
No arquivo relatorio_vendas.py, você pode rodar o código para processar os dados de vendas.

Passos:

Certifique de ter o arquivo vendas.csv com os dados de vendas.

Execute o script Python com o seguinte comando:


python codigo.py  

O script Python irá:

Ler os dados do CSV.

Calcular o total das vendas.

Criar o banco de dados no SQL Server, se necessário.

Inserir os dados no banco de dados.

4. Conectar o Power BI
Abra o Power BI Desktop.

Selecione a opção "Obter Dados" e escolha SQL Server.

Insira as credenciais do seu SQL Server (servidor e banco de dados).

Importe a tabela Vendas para começar a criar relatórios e dashboards interativos.
