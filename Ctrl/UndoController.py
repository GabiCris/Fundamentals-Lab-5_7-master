
class UndoController:
    
    def __init__(self):
        self._operations = []
        self._index = -1
        self._recorded = True
        
    def add_operationList(self, operationList):
        if self.isRecorded() == False:
            return
        #clear operations list of previous undo's before adding a new op
        self._operations = self._operations[0:self._index+1]
        
        self._operations.append(operationList)
        self._index += 1
        
    def isRecorded(self):
        return self._recorded
    
    def undo(self):
        if self._index < 0:
            raise Exception("No action to UNDO!!!")
        
        self._recorded = False
        
        for operation in self._operations[self._index]:
            operation.undoOperation()
            
        self._recorded = True
        self._index -= 1
        
    def redo(self):
        if self._index == len(self._operations)-1:
            raise Exception("No undo to REDO!!!")
        
        self._recorded = False
        
        for operation in self._operations[self._index+1]:
            operation.redoOperation()
            
        self._recorded = True
        self._index += 1
        
class FunctionCall:
    def __init__(self, functionRef, *parameters):
        self._functionRef = functionRef
        self._parameters = parameters

    def call(self):
        self._functionRef(*self._parameters)

class Operation:
    def __init__(self, functionUndo, functionRedo):
        self._functionRedo = functionRedo
        self._functionUndo = functionUndo

    def undoOperation(self):
        self._functionUndo.call()

    def redoOperation(self):
        self._functionRedo.call()
    
    def __str__(self):
        return str(self._functionRedo)
