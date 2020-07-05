from models import Pessoas

def insere_pessoas():
    pessoa = Pessoas(nome='Vinicius', idade=26)
    print(pessoa)
    pessoa.save()

def consulta_pessoas():
    pessoa = Pessoas.query.all()
    #pessoa = Pessoas.query.filter_by(nome='Marcus').first()
    print(pessoa)

def altera_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Marcus').first()
    pessoa.idade = 25
    pessoa.save()

def exclui_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Vinicius').first()
    pessoa.delete()

if __name__=='__main__':
    #insere_pessoas()
    #altera_pessoa()
    exclui_pessoa()
    consulta_pessoas()

