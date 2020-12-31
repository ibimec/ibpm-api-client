from typing import List
from typing import Optional


class IbpmResponse:
    def __init__(self, result, message):
        self.result = result
        self.message = message


class CreateNewProcessResponse(IbpmResponse):
    def __init__(self, result, message, documentName, instanceId):
        super().__init__(result, message)
        self.documentName = documentName
        self.instanceId = instanceId


class User:
    def __init__(self, userName):
        self.userName = userName

    def __str__(self):
        return self.userName


class Task:
    def __init__(self, activity, activityDescription, userName, assignedUsers: List[User]):
        self.activity = activity
        self.activityDescription = activityDescription
        self.userName = userName
        self.assignedUsers = assignedUsers

    def __str__(self):
        return self.activityDescription


class LinkedProcess:
    def __init__(self, model, documentName, documentDescription, instanceId):
        self.model = model
        self.documentName = documentName
        self.documentDescription = documentDescription
        self.instanceId = instanceId

    def __str__(self):
        return f"{self.model}:{self.documentName}"


class Process(IbpmResponse):
    def __init__(self, result, message, model, documentName, documentDescription, instanceId, activeTasks: Optional[List[Task]], links: Optional[List[LinkedProcess]], variables, state, graph):
        super().__init__(result, message)
        self.model = model
        self.documentName = documentName
        self.documentDescription = documentDescription
        self.instanceId = instanceId
        self.activeTasks = activeTasks
        self.links = links
        self.variables = variables
        self.state = state
        self.graph = graph

    def __str__(self):
        return f"{self.model}:{self.documentName} @ {self.activeTasks[0].activityDescription}"

def boolNull(x) -> bool:
    if x is None:
        return False
    else:
        return x

class VariableBase:
    def __init__(self, availableValues: Optional[List], propertyName, propertyType, variableType, description, required, readOnly, hasDefault):
        self.availableValues = availableValues
        self.propertyName = propertyName
        self.propertyType = propertyType
        self.variableType = variableType
        self.description = description
        self.required = boolNull(required)
        self.readOnly = boolNull(readOnly)
        self.hasDefault = boolNull(hasDefault)

    def __str__(self):
        return f'{self.propertyName}: {self.propertyType}'
        

class Variable(VariableBase):
    def __init__(self, availableValues: Optional[List], propertyName, propertyType, variableType, description, required, readOnly, hasDefault, subProperties: Optional[List[VariableBase]]):
        super().__init__(availableValues, propertyName, propertyType, variableType, description, required, readOnly, hasDefault)
        self.subProperties = subProperties


class Schema(IbpmResponse):
    def __init__(self, result, message, activity, properties: List[Variable]):
        super().__init__(result, message)
        self.activity = activity
        self.properties = properties

