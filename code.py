import numpy as np

def exibir_usuarios(base):
  listausuarios = base[:,0]
  print(*listausuarios,sep="\n") 

def autenticar_usuario(usuario, senha, base):
  #auth
  if ([usuario,senha] in base[:,0:2].tolist()): #convert to list #all rows (0:) and two first elements (0:2)
   return True
  else:
   return False

def papel_usuario(usuario,base,recursos):
  gerente = recursos[0:] #primeira linha (0) e todas colunas (0:) - (:) seria todas linhas e todas colunas
  regular = recursos[0:1]
  papel = base[np.where(base == usuario)[0],2][0]
  if papel == "gerente":
    papel = gerente
  else:
    papel = regular
  return papel

def controle_acesso_recurso(papel,recurso):
  if recurso in papel:
    return True
  else:
    return False


base = np.array([["ricardo", 123,"gerente"], ["fulano", 456,"regular"]],dtype='object') #all type exist on Python int, str,bool,float,bytes...
recursos = ["visualizar","remover","editar","inserir","atualizar"]

exibir_usuarios(base)
usuario = input("Informe um usuário: ")
senha = int(input("Informe a senha: "))

if autenticar_usuario(usuario, senha, base):
  print("\nRecursos acessíveis")
  print(*recursos)
  print("\n")
  recurso = input("Informe qual recurso deseja acessar: ")

  papel = papel_usuario(usuario,base,recursos)

  if controle_acesso_recurso(papel,recurso):
    print("recurso liberado!!")  
  else:
    print("sem permissões para acessar recurso!!")
else:
  print("usuário não autorizado!")
  exit()

