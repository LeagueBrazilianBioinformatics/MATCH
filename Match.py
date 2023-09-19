import pandas as pd
import json
import format
import constants as CONTANTS
import sys
def conta_grupo(grupo):
	return len(grupo)

def main():
	try:
    	input_file = sys.argv[1]
	except IndexError:
    	print("Must contain a .csv input file")
    	return

	try:
    	output_file = sys.argv[2]
	except IndexError:
    	output_file = 'output_file.json'



	temp = pd.read_csv(input_file)
	len_dados = len(temp)
	quantidade_de_grupos = len_dados/3
	grupos = {}
	lista_membros = []

	v = CONTANTS.PhD # Completed PhD?
	nome = CONTANTS.name # Name
	email = CONTANTS.email # 'Email Address'
	cursando = CONTANTS.studying  # Education level
	completo = CONTANTS.complete # Completed Education Level

	#criação dos grupos

	for i in range(int(quantidade_de_grupos)):
    	for j in range(3):
        	lista_membros.append({'Name and Last name':"---------------"})
    	grupos['grupo{}'.format(i+1)] = lista_membros
    	lista_membros = []

	# applying the first constraint
# there can only be one person with a PhD
	j=0
	lista = []

	lista_index = []
	for i in temp:
    	lista_index.append(i)

	for i in range(len_dados):
    	if temp[v][i] == ‘Yes’:
        	lista.append(formatar.formata_dict(lista_index,temp,i))
        	grupos['grupo{}'.format(j+1)] = lista
        	j+=1
        	lista = []
        	temp = temp.drop([i])

	lista_index = []
	for i in temp:
    	lista_index.append(i)


	j=0
	for i in range(len_dados):
    	try:
        	if temp[cursando][i] == ‘Graduation’:
            	if not grupos['grupo{}'.format(j+1)][0][nome] ==  '---------------':
           	 
                	lista = grupos['grupo{}'.format(j+1)]
            	lista.append(formatar.formata_dict(lista_index,temp,i))  
            	grupos['grupo{}'.format(j+1)] = lista
            	j+=1
            	lista = []
            	temp = temp.drop([i])
    	except:
        	continue


	lista_index = []
	for i in temp:
    	lista_index.append(i)


	j=0
	for i in range(len_dados):
    	try:
        	if temp[cursando][i] == ‘Master’:
            	for h in range(int(quantidade_de_grupos)):
                	if not grupos['grupo{}'.format(h+1)][0][nome] ==  '---------------':
                    	lista = grupos['grupo{}'.format(h+1)]
                    	if len(lista) == 3:
                        	j+=1
                        	lista = []
                       	 
                        	continue

                	lista.append(formatar.formata_dict(lista_index,temp,i))  
                	grupos['grupo{}'.format(h+1)] = lista
                	j+=1
                	lista = []
                	temp = temp.drop([i])
    	except:
        	continue


	j=0

	lista_index = []
	for i in temp:
    	lista_index.append(i)

	for i in range(len_dados):
    	try:
        	if temp[cursando][i] == ‘PhD:
           	 
            	for h in range(int(quantidade_de_grupos)):

                	if not grupos['grupo{}'.format(h+1)][0][nome] ==  '---------------':
                   	 
                    	lista = grupos['grupo{}'.format(h+1)]
                    	if len(lista) == 3:
                        	j+=1
                        	lista = []
                        	continue
                	lista.append(formatar.formata_dict(lista_index,temp,i))  
                	grupos['grupo{}'.format(h+1)] = lista
                	j+=1
                	lista = []
                	temp = temp.drop([i])
    	except:
        	continue

	j=0

	lista_index = []
	for i in temp:
    	lista_index.append(i)

	for i in range(len_dados):
    	try:
        	if temp[completo][i] == 'Postdoc':
           	 
            	for h in range(int(quantidade_de_grupos)):

                	if not grupos['grupo{}'.format(h+1)][0][nome] ==  '---------------':
                   	 
                    	lista = grupos['grupo{}'.format(h+1)]
                    	if len(lista) == 3:
                        	j+=1
                        	lista = []
                        	continue
                	lista.append(formatar.formata_dict(lista_index,temp,i))  
                	grupos['grupo{}'.format(h+1)] = lista
                	j+=1
                	lista = []
                	temp = temp.drop([i])
    	except:
        	continue


	j=0

	lista_index = []
	for i in temp:
    	lista_index.append(i)

	for i in range(len_dados):
    	try:
        	if temp[cursando][i] == 'Working with Bioinformatics':
           	 
            	for h in range(int(quantidade_de_grupos)):

                	if not grupos['grupo{}'.format(h+1)][0][nome] ==  '---------------':
                   	 
                    	lista = grupos['grupo{}'.format(h+1)]
                    	if len(lista) == 3:
                        	j+=1
                        	lista = []

                        	continue
                	lista.append(formatar.formata_dict(lista_index,temp,i))  
                	grupos['grupo{}'.format(h+1)] = lista
                	j+=1
                	lista = []
                	temp = temp.drop([i])
    	except:
        	continue


	lista_index = []
	for i in temp:
    	lista_index.append(i)
   	 
	for i in range(len_dados):
    	try:
        	if temp[cursando][i] == '-':
           	 
            	for h in range(int(quantidade_de_grupos)):

                	if not grupos['grupo{}'.format(h+1)][0][nome] ==  '---------------':
                   	 
                    	lista = grupos['grupo{}'.format(h+1)]
                    	if len(lista) == 3:
                        	j+=1
                        	lista = []
                        	continue

                	lista.append(formatar.formata_dict(lista_index,temp,i))  
                	grupos['grupo{}'.format(h+1)] = lista
                	j+=1
                	lista = []
                	temp = temp.drop([i])
    	except:
        	continue

	arquivo_dict = {}

	lista_iii = []

	for i in grupos:
    	for j in grupos[i]:
        	d = str(j['Email Address'])
        	lista_iii.append({"Email":d if d!='nan' else "",
                        	"nome":j['Name and Last name']})

    	arquivo_dict[i] = lista_iii
    	lista_iii = []

	conta=0

	with open(output_file, 'w') as fp:

    	fp.write('{')
    	try:
        	for i in arquivo_dict:
            	conta+=1
            	fp.write('"{}":'.format(i))
            	fp.write(json.dumps(arquivo_dict[i]))
            	if conta != len(arquivo_dict):
                	fp.write("\n,")
            	else:
                	fp.write("\n")
                	print("Results in file:>",arquivo_saida)

    	except:
        	fp.write('{},\n'.format(json.dumps(j)))
        	pass
    	fp.write('}')

main()

================= constants.py ===================

PhD = 'Do you have a completed PhD?'
name = ‘First and Last name'
email = 'Email Address'
studying = 'Education level'
complete = 'Completed education level'

================= format.py  ========================

def formata_dict(lista,dados,i):
	dict_data={}

	for j in range(len(lista)):
    	dict_data[lista[j]] = dados[lista[j]][i]

	return dict_data



