import re
import sys

class resources : 
  def auto_typecast(self,value):
    
    try:
      return int(value)
    except:
      pass
    
    try:
      return float(value)
    except:
      pass
    
    try:
      if value in ['true','false']:
        return bool(value.lower == 'true')
    except:
      pass
    
    return value
  def rey(self,tokenized_code,variables,i):
           self.tokenized_code = tokenized_code
           
           if "'" in self.tokenized_code[i+1] or '"' in self.tokenized_code[i+1]:
              result = self.tokenized_code[i+1] + " "
              i += 1
              for element in self.tokenized_code[i+1:]:
                      i +=1
                      if "'" in element or '"' in element :
                        result += element
                        break
                      result += element + ' '
              
              if "'" in result:
                 print(result.replace("'",""))
              else:
                 print(result.replace('"',''))
  
              
           elif self.tokenized_code[i+1] == '(' :
              result = ''
              i+=1
              for element in self.tokenized_code[i+1:]:
                  i +=1 
                  if element == ')':
                     i += 1
                     break
                  result += element
                  
              print(eval(result,variables))
              
           elif '(' in self.tokenized_code[i+1]:          
              print(eval(self.tokenized_code[i+1],variables))    
              i += 2
                                         
           elif self.tokenized_code[i+1] in variables:
             print(variables[self.tokenized_code[i+1]])
             i += 2
             
           return i
  def mari(self,tokenized_code,variables,i):
             if self.tokenized_code[i+1][0].lower() in "_abcdefghijklmnopqrstuvwxyz":
               if self.tokenized_code[i+2] == "=" and self.tokenized_code[i+3] != "(":
                  variables[self.tokenized_code[i+1]] = res_ob.auto_typecast(self.tokenized_code[i+3])
                  i += 4
               else:
                  item = self.tokenized_code[i+1]
                  result = ''
                  i+=3
                  for element in self.tokenized_code[i+1:]:
                      i +=1 
                      if element == ')':
                         i += 1
                         break
                      result += element
                  variables[item]=eval(result,variables)
             else:
              print('invalid variable',self.tokenized_code[i+1])
              return False
             return i
           
  def while_run(self,condition,tokenizer,variables):
            self.tokenized_code = tokenizer
            self.variables = variables
            self.codition = condition
    


class Lexical (resources) :
  def __init__(self,code,res_ob):
     self.code = code
     self.tokenized_code=[]
     self.res_ob = res_ob
  
  def tokenize(self):
    self.tokenized_code = [item for item in re.split(r"[ \n]",self.code) if item]
  
  def parse(self):
    variables = {}
    i=0
    
    while(i<len(self.tokenized_code)-1):
      if self.tokenized_code[i] == "rey":       
        try:
           if self.tokenized_code[i+1] not in variables:
             print(f'{self.tokenized_code[i+1]} is not defined')
             break
           else:
             i = res_ob.rey(self.tokenized_code,variables,i)
          
        except:
          print('error')
          break
      
          
      elif self.tokenized_code[i] == "mari":
        try:
           result = res_ob.mari(self.tokenized_code,variables,i)
           if result:
             i = result
           else:
             break
        except:
          print('error')
          break
        

           
    
code = """

mari x = 20
mari y = 20
rey x
rey (x+y)
rey (x-30)

"""


if __name__ == "__main__":
    if len(sys.argv[1]) > 1:        
        filename = sys.argv[1]
        try:
            with open(filename, 'r') as file:
                code = file.read()
                res_ob=resources()
                object = Lexical(code,res_ob)
                object.tokenize()
                object.parse()
                
        except FileNotFoundError:
            print(f"File {filename} not found.")
    else:
      print('file not provided')

