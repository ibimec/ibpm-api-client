import ibpm

client = ibpm.client('http://localhost:56338')
client.authorizationToken = "JBBVFNWXOSSSEVVPPXOPUVECFBPJRUWBIRPFGKVGDTYRJSBQMUP"
client.userName = "ADMIN"


r = client.getProcess(model='RICHIESTE OFFERTA', documentName='2020 55.1', includeGraph=True)

r.graph.show()

print(r)   
