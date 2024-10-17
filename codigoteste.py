# .txt
# banco de dados
#SQLite

#SQL = Linguagem de consulta estruturada
#ORM (para SQL) CREATE DATABASE meu banco
# i/o # i = input(entrada) #o = output(saída)

# Select * from clientes
#nome, sobrenome, idade

#ORM = biblioteca p esconder comandos como o select, na sua linguagem
# pip install sqlalchemy

import os
from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import sessionmaker, declarative_base

# Criando banco de dados
MEU_BANCO = create_engine("sqlite:///meubanco.db")

# Meio dos dois, um cria e o outro comunica

#criando conexão com banco de dados
session = sessionmaker(bind=MEU_BANCO)
session = session()

# Criando tabela.

base = declarative_base()

class Usuario(base):
    __tablename__ = "usuarios"


    # Definindo campos da tabela
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    nome = Column("nome", String)
    email = Column("email", String)
    senha = Column("senha", String)

    # Definindo atributos da classe
    def _init_(self, nome: str, email: str, senha: str):
        self.name = nome
        self.email = email
        self.senha = senha

# Criando tabela no banco de dados
base.metadata.create_all(bind=MEU_BANCO)

# Salvar no banco de dados
os.system("cls || clear")

# Create
print("Solicitando dados para o usuário")
inserir_nome=input("Digite seu nome")
inserir_email=input("Digite seu  email")
inserir_senha=input("Digite sua senha")

usuario = Usuario (nome=inserir_nome, email=inserir_email, senha=inserir_senha)
session.add(usuario)
session.commit()

usuario = Usuario(nome="Maria", email="maria@gmail.com", senha="456")
session.add(usuario)
session.commit()

# Listando todos os usuários do banco de dados
print("\nExibindo todos os usuários do banco de dados.")
lista_usuarios = session.query(Usuario).all()

#Read
for usuario in lista_usuarios:
    print(f"{usuario.id} - {usuario.nome} - {usuario.senha}")

#Fechando conexão.
session.close()
