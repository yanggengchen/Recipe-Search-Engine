# load the query_auto_completion model and run it
class QueryAutoCompletion():
    def __init__(self, someVariable):
        self.someVariable = someVariable

    def someFunction(self):
        print(self.someVariable)


def queryAutoComplete():
    newObj = QueryAutoCompletion("queryAutoComplete")
    newObj.someFunction()
    print("yayyyyyy!")
