from global_shared import vars
from ops_parens import *

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
            string = self._evalVariable(string)

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
                    var_value = self._evalVariable(token)
            elif(token == "="):
                pass
            else:
                if(token == "io"):
                    if(len(tokens) > 4):
                        var_value = raw_input(tokens[4].strip("\""))
                        break
                    else:
                        var_value = raw_input()
                else:
                    var_value = token
                
        if var_value.startswith("\""):
            var_value = var_value.strip("\"")
        vars[var_name] = var_value
        #print(vars)
        
    # Get Variables
    def _getVariable(self,varName):
        return vars[varName]
    
    # Evaluate multiple Variables from token
    def _evalVariable(self,token):
        
        tks =[]
        tk = ""
        expression = ""
        multipleVar = False
        #print(token)
        
        if(token.startswith("$")):
            
            for mo in mat_ops:
                if mo in token:
                    multipleVar = True
                    break
            
            
            if(multipleVar):
                for char in list(token):
                    if char in mat_ops:
                        tks.append(tk)
                        tks.append(char)
                        tk = ""
                    else:
                        tk += char
                        #print("tk :" + tk)
                if(tk != ""):
                    tks.append(tk)
                #print(tks)
                
                for tk in tks:
                    if tk.startswith("$"):
                        val = self._getVariable(tk.strip("$"))
                        expression += val
                    else:
                        expression += tk
                
                
                return str(eval(expression))
            else:
                return  self._getVariable(token.strip("$"))
                
                
                
        
            
