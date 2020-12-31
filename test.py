import ibpm

client = ibpm.client('http://localhost:56338')
client.authorizationToken = "JBBVFNWXOSSSEVVPPXOPUVECFBPJRUWBIRPFGKVGDTYRJSBQMUP"
client.userName = "ADMIN"

v = client.getVersion()

r = client.getProcess(model='RICHIESTE OFFERTA', documentName='2020 55.1', includeGraph=True)

s = client.getSchema(modelName='RICHIESTE OFFERTA', activityName='Activity1')


print(s)

