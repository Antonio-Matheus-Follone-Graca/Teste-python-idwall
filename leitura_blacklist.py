'''
  Teste da empresa Idwall. Link https://github.com/idwall/python-test
  Além de retornar as condições que o teste pedia, resolvi retornar um objeto json com o cpf
'''
def cpf_bloqueado(cpf):
    # formatando cpf 
    cpf = formata_cpf(cpf= cpf)  
    cpf_estado = None; 
    cpf_a_ser_procurado = cpf
    # abrindo arquivo, operação read
    arquivo = open("blacklist.txt", "r") 
    dados_arquivo = arquivo.read() 
    # se o cpf estiver no arquivo, cpf bloqueado 
    if cpf_a_ser_procurado in dados_arquivo:  
        cpf_estado = True
    
    # senão, livre
    else:  
        cpf_estado = False    
    # fechando arquivo
    arquivo.close()  

    # de acordo com o  valor do cpf_estado, retorna se o cpf está livre ou bloqueado
    if cpf_estado == True:
        
        return True
    
    else:
        return False
    

def formata_cpf(cpf):
    # nem formata o cpf
    if len(cpf) < 11 or len(cpf) > 11:
        cpf = cpf 
    
    else:
        cpf = cpf = cpf[:3] + "." + cpf[3:6] + "." + cpf[6:9] + "-" + cpf[9:]  
    
    
    return cpf 
         
        
    
 
    
       
    



    


