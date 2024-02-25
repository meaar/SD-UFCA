import socket
import datetime
from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler

# Registrar caminho para o servidor
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

# Create server
with SimpleXMLRPCServer(('localhost', 21212),requestHandler=RequestHandler) as server:
    server.register_introspection_functions()

    #Definição de funções
    messages = []
    
    def addMessage(message):
        messages.append(message)
        return (True)
    
    def getMessages():
        return(messages)
    
    def getHostAddress():
        return (socket.gethostbyname(socket.gethostname()))
    
    def getDateTime():
        return (getDate()+' '+getTime())
    
    def getTime():
        now = datetime.datetime.now()
        hour = str(now.hour)
        minute = str(now.minute)
        if len(hour) < 2:   
            hour = '0'+hour
        elif len(minute) < 2:
            minute = '0'+minute
        return hour+':'+minute

    def getDate():
        now = datetime.datetime.now()
        day = str(now.day)
        month = str(now.month)
        year = str(now.year)
        if len(day) < 2:   
            day = '0'+day
        elif len(month) < 2:
            month = '0'+month
        elif len(year) < 2:
            year = '0'+year
        return year+'-'+month+'-'+day

    
    #Registrar funções
    server.register_function(addMessage, 'addMessage')
    server.register_function(getMessages, 'getMessages')
    server.register_function(getHostAddress, 'getHostAddress')
    server.register_function(getDateTime, 'getDateTime')

    # Iniciar servidor
    server.serve_forever()
