import ibpm

client = ibpm.client('https://az.ibimec.it')
client.authorizationToken = "XALKDJASKLDJIWLAKSDJ"
client.userName = "rgallini"

vars = {
    "a": 1,
    "b": 2,
    "list": [
        {
            "x":1,
            "y":2
        },
        {
            "x":12,
            "y":11
        }
    ]
}

r = client.createNewProcess("APPROVAZIONE", vars)
n = r.documentName

print(r)   
