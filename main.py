'''
  Teste da empresa Idwall. Link https://github.com/idwall/python-test
  Além de retornar as condições que o teste pedia, resolvi retornar um objeto json com o cpf
'''
from flask import Flask,jsonify
from leitura_blacklist import cpf_bloqueado, formata_cpf

# iniciando flask
app = Flask(__name__)

# rota
@app.route('/<cpf>', methods=['GET'])
def cpf(cpf):
    resposta = None
    # se digitou alguma string em vez de apenas números inteiros, retornar RUNNING.
    if cpf.isdigit() == False or len(cpf) > 11 or len(cpf) < 11 :
        
        resposta = jsonify(cpf = cpf, estado = 'RUNNING'), 406
        
    
    else:
        # retorna um valor booleano 
        estado_cpf = cpf_bloqueado(cpf = cpf)
        # cpf bloqueado 
        if estado_cpf == True:
            # deixei o cpf formatado no objeto json 
            resposta = jsonify(cpf = formata_cpf(cpf), estado = 'BLOCK ')
            
        # cpf liberado 
        else:
           # deixei o cpf formatado no objeto json 
            resposta = jsonify(cpf = formata_cpf(cpf), estado = 'FREE ')
        
    return resposta

# Retornar RUNNING caso seja acessada sem um CPF

@app.route('/')
def index():
    return jsonify( estado = 'RUNNING'), 406 
    
        
app.run(debug=True)