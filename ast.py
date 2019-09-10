from global_shared import vars

class AST():
    def __init__(self):
        pass
    
    # Print Function
    def printToScreen(self,tokens):
        string = ""
        isString = 0
        isVar = 0
        #print(tokens)
        for char in list(tokens):
            if char != "\"":
                string += char
                if char == "$":
                    isVar = 1
            else:
                isString = 1

        # Check if its a variable and set it's value
        if(isVar == 1):
            string = self._getVariable(string.strip("$"))

        # Check if its an expression and get it's value
        try:
            if(isString == 0):
                string = eval(string)
        except:
            pass 
        print(string)

    # Set Variables
    def setVariable(self,tokens):
        var_name = ""
        var_value = ""
        isVar = 0
        #print(tokens)
        for token in tokens:
            if(token.startswith("$")):
                if(isVar == 1):
                    isVar = 0
                else:
                    isVar = 1
                if(isVar == 1):
                    var_name = token.strip("$")  
                else:
                    var_value = vars[token.strip("$")]            
            elif(token == "="):
                pass
            else:
                if(token == "io"):
                    var_value = raw_input(tokens[4].strip("\""))
                    break
                else:
                    var_value = token
                
        if var_value.startswith("\""):
            var_value = var_value.strip("\"")
        vars[var_name] = var_value
        #print(vars)
        
    # Get Variables
    def _getVariable(self,varName):
        return vars[varName]
