#importa 
from model.Pessoa import Pessoa
from database.Database import Database
from dao.PessoaDAO import PessoaDAO

#Exemplo de uso
artur = Pessoa(1, "Artur Moreira")
print (artur)
#Quero mostrar so o nome 
print(artur.nome)
#Chama o objeto no banco de dados
db = Database()
#Instancia o objeto
pessoaDAO = PessoaDAO(db.conexao, db.cursor)

#Quero carregar uma lista com o que veio do banco de dados
pessoas = pessoaDAO.getAll(orderBy=True)
for pessoa in pessoas:
  print(pessoa)