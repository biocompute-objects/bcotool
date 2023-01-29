#Tool type call
#the needed package to use JSON
import requests
# ask the user for tool name 
inp=input("Tool Name?")
#use the templet http and add the tool name to it 
x="https://bio.tools/api/t/?biotoolsID=%22%22&format=json"
y=x[:39]+inp+x[39:]
#reterive all the information about The input tool name and store them in the result
result=requests.get((y))
# change it from JSON to Python Dictionary 
dic=result.json()
#print the tool type for the used tool name
print(dic['list'][0]['toolType'])