#Importar biblioteca
import xmlrpc.client

#Definir servidor
s = xmlrpc.client.ServerProxy('http://localhost:21212')

#Chamar funções disponíveis no servidor
s.addMessage("Mensagem 1")
s.addMessage("Mensagem 2")
print(s.getMessages())
print(s.getHostAddress())
print(s.getDateTime())

# Print list of available methods
print(s.system.listMethods())
