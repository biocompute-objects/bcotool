# Alhanouf Altuwayjiri
#the needed package to use JSON
import requests
# ask the user for tool name 
def ToolType(inp):
#use the templet http and add the tool name to it 
    x="https://bio.tools/api/t/?format=json&q=&sort=score"
   
    LINK=x[:39]+inp+x[39:]

#reterive all the information about The input tool name and store them in the result
    result=requests.get((LINK))
# change it from JSON to Python Dictionary 
    dic=result.json()
#print the tool type for the used tool name

    typet=[]
    for i,key in enumerate(dic['list']):
        x=(dic['list'][i]['function'][0]['operation'])
        for r,key in enumerate(x):
            y=(dic['list'][i]['function'][0]['operation'][r]['term'])
            typet.append(y)
    
    h=(set(typet))
    final=typet
    for i in h:
        final.remove(i)
   
    return set(final)