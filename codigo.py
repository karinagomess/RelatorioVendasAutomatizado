import pandas as pd
import pyodbc

# ==========================
# 1. Leitura do arquivo CSV
# ==========================

try:
    df = pd.read_csv("vendas.csv", sep=";", encoding="utf-8-sig")
    print("Arquivo lido com sucesso!")
    print("Colunas encontradas:", df.columns.tolist())
except FileNotFoundError:
    print("Erro: Arquivo não encontrado.")
    exit()
except Exception as erro:
    print(f"Erro ao ler o arquivo: {erro}")
    exit()



# =======================================
# 2. Criar nova coluna com total da venda
# =======================================
df["Total_Vendas"] = df["Quantidade"] * df["Preco_Unitario"]




# =============================================
# 3. Conectar com o banco de dados (SQL Server)
# =============================================

server = "KARINAGOMES"  # ou seu servidor
database = 'RelatorioVendas' # nome do banco de dados
conexao = pyodbc.connect(
    f'DRIVER={{SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes;'
)
cursor = conexao.cursor()




# ================================
# 5. Criar tabela (se não existir)
# ================================

cursor.execute("""
IF OBJECT_ID('dbo.Vendas', 'U') IS NULL
    CREATE TABLE dbo.Vendas (
        ID_Venda INT,
        Data_Venda DATE,
        Produto VARCHAR(50),
        Categoria VARCHAR(50),
        Preco_Unitario FLOAT,
        Quantidade INT,
        Cliente VARCHAR(100),
        Região VARCHAR(50),
        Forma_Pagamento VARCHAR(50),
        Total_Vendas FLOAT
    )
""")
conexao.commit()



# =====================
# 6. Inserir os dados
# =====================

for _, linha in df.iterrows():
    cursor.execute("""
        INSERT INTO dbo.Vendas (ID_Venda, Data_Venda, Produto, Categoria, Preco_Unitario, 
                            Quantidade, Cliente, Região, Forma_Pagamento, Total_Vendas)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
        linha["ID_Venda"], linha["Data_Venda"], linha["Produto"],linha["Categoria"], 
        linha["Preco_Unitario"], linha["Quantidade"], linha["Cliente"],
        linha["Região"], linha["Forma_Pagamento"], linha["Total_Vendas"]
    )
conexao.commit()
print("Dados inseridos com sucesso!")
