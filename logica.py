﻿from config import *
from funcoes import *
from webexteams import getwebexMsg, webexmsgRoomviaID
import json
from influxdb import InfluxDBClient

def logica(comando,usermail):

    # faz a logica de entender o comando pedido e a devida resposta para o usuario
    # o parametro usermail e' utilizado para identificar o usuario que solicitou o comando
    # O usuario pode ser uzado como filtro para se executar ou negar o comando
    #
    # Retorna mensagem para ser enviada para console ou Webex teams
    
    #Separa o comando por espacos
    #Primeiro item e'o comando em si, os demais sao parametros deste comando
    #
    
    comando = comando.lower()
    box=comando

    while box == "oi" or box == "ola" or box == "hey" or box == "ei" or box == "alo" or box == "teste" or box =="Oi" or box == "Olá" or box == "help":
        msg=""
        arquivo=""
        msg= "Olá Humano, antes de liberar o escoamento da água utilizada nos processos industriais, verifique comigo se o tanque especificado está pronto para voltar ao meio ambiente.\n" 
        msg=msg+ "Qual das seguintes opções deseja ?\n"   
        msg=msg+ "(1) - Temperatura atual da água\n"  
        msg=msg+ "(2) - Buscar histórico de temperatura semanal\n"
        msg=msg+ "(3) - Buscar histórico de temperatura mensal\n"
        return msg,arquivo
    else:
        msg=""
        arquivo=""
        box2 = box
        #condicional atual para temperatura da água - busca no InfluxDB
        if box2 == "1":
            #dbClient = InfluxDBClient(host="191.177.186.32", port=8086)
            #temperatura= dbClient.query('select last(*) from CoreTemperature', database='test')
            msg="A temperatura atual da água é de XX graus. "
            return msg,arquivo
        elif box2 == "agua":
            #dbClient = InfluxDBClient(host="191.177.186.32", port=8086)
            #temperatura= dbClient.query('select last(*) from CoreTemperature', database='test')
            msg="A temperatura atual da água é de XX graus. "
            return msg,arquivo
        elif box2 == "temperatura":
            #dbClient = InfluxDBClient(host="191.177.186.32", port=8086)
            #temperatura= dbClient.query('select last(*) from CoreTemperature', database='test')
            msg="A temperatura atual da água é de XX graus. "
            return msg,arquivo
        elif box2 == "atual":
            #dbClient = InfluxDBClient(host="191.177.186.32", port=8086)
            #temperatura= dbClient.query('select last(*) from CoreTemperature', database='test')
            msg="A temperatura atual da água é de XX graus. "
            return msg,arquivo
        elif box2 == "temperatura atual":
            #dbClient = InfluxDBClient(host="191.177.186.32", port=8086)
            #temperatura= dbClient.query('select last(*) from CoreTemperature', database='test')
            msg="A temperatura atual da água é de XX graus. "
            return msg,arquivo
        #ajudinha antecedendo possíveis erros de digitação de temperatura atual 
        elif box2 == "atula":
            msg="As palavras que você digitou chegaram perto de 'atual' e 'temperatura atual', tente elas"
            return msg,arquivo
        elif box2 == "temperaturar":
            msg="As palavras que você digitou chegaram perto de 'temperatura' e 'temperatura atual', tente elas"
            return msg,arquivo
        #histórico de temperatura semanal
        elif box2 == "2":
            msg="Segue o link para histórico de temperatura semanal"
            return msg,arquivo
        elif box2 == "histórico semanal":
            msg="Segue o link para histórico de temperatura semanal"
            return msg,arquivo
        elif box2 == "semanal":
            msg="Segue o link para histórico de temperatura semanal"
            return msg,arquivo
        elif box2 == "temperatura semanal":
            msg="Segue o link para histórico de temperatura semanal"
            return msg,arquivo
        #possíveis erros de digitação em histórico de temperatura semanal
        elif box2 == "historico":
            msg="A palavra que você digitou chegou perto de 'histórico' , 'histórico semanal' , 'histórico mensal', tente elas"
            return msg,arquivo        
        elif box2 == "semana":
            msg="A palavras que você digitou chegou perto de 'semanal' , 'histórico semana', tente elas"
            return msg,arquivo
        #Histórico de temperatura mensal
        elif box2 == "3" or box2 == "mensal":
            msg= "Segue o link para histórico de temperatura mensal"
            return msg,arquivo
        elif box2 == "histórico mensal":
            msg="Segue o link para histórico de temperatura mensal"
        #Possiveis erros em histórico de temperatura mensal
        elif box2 == "mes" or box2 == "mensa":
            msg: "A palavra que você digitou chegou perto de 'mensal', 'temperatura mensal', tente elas"
            return msg,arquivo

        
            



    # sp=comando.split(" ")

    # print(sp)
    
    # comando na variavel box, lower deixa em minusculo para normalizar
    
    # Para o caso de nenhum pedido coberto aqui
    mais="\nEscreva 'mais' para saber suas opções"
    
    # 21.11.19
    # variavel arquivo para o caso do bot devolver arquivos anexados
    
    # arquivo=""
    
    # msg=""
	
    # chamadas de acordo com os parametros

    # Funcoes para todos
    
    # Uso da funcao "mais"

    print(comando)
    print(box)

    if box == "oi":
        
        
        if box == "1":
            msg="dancing"

    elif box == "ei":
        msg= "Olá Humano, antes de liberar o escoamento da água utilizada nos processos industriais, verifique comigo se o tanque especificado está pronto para voltar ao meio ambiente.\n" 
        msg=msg+ "Qual das seguintes opções deseja ?\n"   
        msg=msg+ "(1) - Temperatura atual da água\n"  
        msg=msg+ "(2) - Buscar histórico de temperatura semanal\n"
        msg=msg+ "(3) - Buscar histórico de temperatura mensal\n"

    elif box == "ola":
        msg= "Olá Humano, antes de liberar o escoamento da água utilizada nos processos industriais, verifique comigo se o tanque especificado está pronto para voltar ao meio ambiente.\n" 
        msg=msg+ "Qual das seguintes opções deseja ?\n"   
        msg=msg+ "(1) - Temperatura atual da água\n"  
        msg=msg+ "(2) - Buscar histórico de temperatura semanal\n"
        msg=msg+ "(3) - Buscar histórico de temperatura mensal\n"

    elif box == "alo":
        msg= "Olá Humano, antes de liberar o escoamento da água utilizada nos processos industriais, verifique comigo se o tanque especificado está pronto para voltar ao meio ambiente.\n" 
        msg=msg+ "Qual das seguintes opções deseja ?\n"   
        msg=msg+ "(1) - Temperatura atual da água\n"  
        msg=msg+ "(2) - Buscar histórico de temperatura semanal\n"
        msg=msg+ "(3) - Buscar histórico de temperatura mensal\n"

    else:
        msg="Não entendi o que você quis dizer, por favor tente dizer 'oi' pra mim"


    #  if len(sp)>2:
    #             tema=sp[1]
    #             msg=maissobre(tema)
    #             print(sp)
    
        
    # # Funcoes que usam outras APIs
    # if len(sp)>1 and box=="api":
    #     # URL
    #     site="apitesteexample.com"
    #     # Parametro de autorizacao
    #     token="123456"
    #     msg=APICall(site,token)
        

    # return msg,arquivo


def trataPOST_grafana(content):
    try:
        #msg="teste"
        msg=content["message"]
        arquivo=""
        sala="Y2lzY29zcGFyazovL3VzL1JPT00vZGQ1MmFjMDItYjU5YS0zYzczLTk2NzktODJlYTgxYmIzNDA5"

        # Envia resposta na sala apropriada
        webexmsgRoomviaID(sala,msg,arquivo)
        
        #if content['dashboardId']==3:
            #msg=(content['message'])
            #url=(content['ruleUrl'])
            #webexmsgRoomviaId=("Y2lzY29zcGFyazovL3VzL1JPT00vZGQ1MmFjMDItYjU5YS0zYzczLTk2NzktODJlYTgxYmIzNDA5",msg,url)
            #webextalk=getwebexMsg(msg_id)
            #usermail=webextalk[2]
            #mensagem=webextalk[0]
            #sala=webextalk[1]

            # executa a logica
            #msg,arquivo=logica(mensagem,usermail)
            
            # Envia resposta na sala apropriada
            #webexmsgRoomviaID(sala,msg,url)

    except Exception as e:
            print("POST nao reconhecido")
            print(str(e))
            pass

def trataPOST_user(content):

    # resposta as perguntas via webexteams
    # trata mensagem quando nao e' gerada pelo bot. Se nao e' bot, entao usuario
    try:     
        if content['name']==webhook_name and content['data']['personEmail']!=botmail:
            # identifica id da mensagem
            msg_id=(content['data']['id'])
            # identifica dados da mensagem
            webextalk=getwebexMsg(msg_id)
            usermail=webextalk[2]
            mensagem=webextalk[0]
            sala=webextalk[1]

            # executa a logica
            msg,arquivo=logica(mensagem,usermail)
        
            # Envia resposta na sala apropriada
            webexmsgRoomviaID(sala,msg,arquivo)
            
    except Exception as e:
            print("POST nao reconhecido")
            print(str(e))
            pass
