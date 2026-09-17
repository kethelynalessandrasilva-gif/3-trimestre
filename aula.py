senha="12345678"
senha_cripitografada=""

for numero in senha:
    numero=int(numero) + 1
    senha_cripitografada= senha_cripitografada + str(numero) 

print(senha_cripitografada) 
