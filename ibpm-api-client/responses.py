
class ibpmResponse:
    def __init__(self, result, message):
        self.result = result
        self.message = message


class createNewProcessResponse(ibpmResponse):
    def __init__(self, result, message, documentName, instanceId):
        super().__init__(result, message)
        self.documentName = documentName
        self.instanceId = instanceId

