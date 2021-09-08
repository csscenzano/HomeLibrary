import Ib
from Gbook import gbooks


from Ib import Is_bn


#livro=Is_bn(ISBN_number="0-446-35601-6")
#livro=Books("0-446-35601-7")
# livro=Is_bn()



ISBN_num=input("Enter with ISBN:")
livro=Is_bn(ISBN_num)
meugbook = gbooks()
if livro.bole==True:
    print(meugbook.search(ISBN_num))
else:
    print("livro falso")
   
# Define if the ISBN number is valid and open next step