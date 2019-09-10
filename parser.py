from ast import AST

class Parser():
    def __init__(self, tokens):
        self.tokens = tokens
        #print self.tokens

    
    def parse(self):
        isVar = 0
        for i in range(0,len(self.tokens)):
            for token in self.tokens[i]:
                if(token == "print"):
                    AST().printToScreen(self.tokens[i][2])
                    break
                elif (token.startswith("$")):
                    #print(self.tokens[i])
                    if(isVar == 0):
                        isVar = 1
                    else:
                        isVar = 0
                    
                    if(isVar == 1):
                        AST().setVariable(self.tokens[i])
                        isVar = 0
                        
                    
                


        

