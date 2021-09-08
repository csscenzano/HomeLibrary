import pyisbn
from pyisbn import Isbn

# Importa dado de pyisbn programa generado por python
class Is_bn:   
    def __init__ (self, ISBN_number=False):
        self.bole = False
        self.ISBN_number=ISBN_number
        self.checkISBN()
        
# Cria a funcao Is_bn para checar o numero    
    def checkISBN(self):
        if self.ISBN_number:
            livro=Isbn(self.ISBN_number)
            if livro.validate():
                self.bole = True
                print()
                livro.to_urn()
# Cria a funcao checkISBN para checar o nuemro si valido               
            else:
                print()
                return
#caso contrario retorna            
        #else:
         #   ISBN_num=input("Enter with ISBN:")
          # livro=Isbn(ISBN_num)
          #  if livro.validate():
                #print ("aqui1")
           #     livro.to_urn()
           #     print (livro.to_url())
            #    #print ("aqui2")
             #   print ("True")
#                
          #  else:
           #     print("ISBN no valido")
                