import sqlite3

# Abre o banco. Se o arquivo não existir, ele é criado.

conexao = sqlite3.connect("banco_teste.db")
cursor = conexao.cursor () # Cursor é quem executa os comandos SQL

#Uma tabela é como uma planilha: colunas fixas, uma linha por registro.
cursor.execute("""
CREATE TABLE IF NOT EXISTS produtos(
codigo INTEGER PRIMARY KEY AUTOINCREMENT,
nome TEXT NOT NULL,
setor TEXT NOT NULL
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS lote (
codigo INTEGER PRIMARY KEY AUTOINCREMENT,
carga_atual INTEGER NOT NULL,
produto INTEGER,
FOREIGN KEY (produto) REFERENCES produtos(codigo)
)
""")

conexao.commit() # grava de verdade as mudanças no arquivo
conexao.close( ) # fecha a conexão ao terminar

