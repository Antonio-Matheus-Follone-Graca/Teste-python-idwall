# Teste para desenvolvedores Python

Instruções do teste
------

Desenvolva uma aplicação em linguagem Python que seja acessível localmente e verifique se um determinado número de CPF está em uma        *Blacklist*.

A aplicação deve:
 
1. Ser acessível como um serviço através de uma URL do tipo `http://IP:PORT/<cpf>`, por exemplo:
`http://127.0.0.1:5000/00000000000`


2. Ser `FREE` se o CPF não estiver na *Blacklist* e `BLOCK` se o CPF estiver na black list.
 
3. Retornar `RUNNING` caso seja acessada sem um CPF.

Para este teste você pode usar qualquer framework de sua escolha.

Os CPFs a serem testados estão no arquivo `blacklist.txt`.


Como entregar este teste
-----

Você deve forkar este projeto em sua própria conta do GitHub e fazer o commit em seu próprio repositório.


Como rodar o projeto
----
1. Baixe o projeto e abra no cmd a pasta do projeto;
2. Crie uma venv com o comando python -m venv nome_da_venv;
3. Ative a venv digitando : nome_da_venv\Scripts\activate;
4. Importe as bibliotecas do projeto com pip install -r requirements.txt;
5. Com a venv ativada, digite no cmd: python main.py;
6. Digite o endereço da url com seu respectivo paramêtro  em um navegador ou se desejar no postman.