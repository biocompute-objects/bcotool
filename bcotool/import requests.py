import requests

def tooltype2(x,y): #  function that will return the tool type from ELIXIR databases
 
     l="https://bio.tools/api/t/?biotoolsID=%22%22&format=json"   # The http used to reterive info
   
     LINK = l[:39]+x+l[39:]  # add the input to the http link 
     LINK2 = l[:39]+y+l[39:]
     

     result = requests.get((LINK))  #reterive all the information about The input tool name and store them in the result
     result2 = requests.get((LINK2))

     dic=result.json()  # change it from JSON to Python Dictionary 
     dic2=result2.json()
     
     if dic['count']>1: # if there is more than one tool with the same name
         typet = []
         for i,key in enumerate(dic['list']):
             x = (dic['list'][i]['function'][0]['operation'])
             for r,key in enumerate(x):
                 y = (dic['list'][i]['function'][0]['operation'][r]['term'])
                 typet.append(y)
    
         h = (set(typet))
         final = typet
         for i in h: # go over the two tools and find the similarity 
            final.remove(i)
     else:  # if only one tool has the same name 
         typet = []
         for r,key in enumerate(dic['list'][0]['function'][0]['operation']):
                 y = (dic['list'][0]['function'][0]['operation'][r]['term'])
                 typet.append(y)
         final = typet
     if dic2['count']>1:
         typet = []
         for i,key in enumerate(dic2['list']):
             x = (dic2['list'][i]['function'][0]['operation'])
             for r,key in enumerate(x):
                 y = (dic2['list'][i]['function'][0]['operation'][r]['term'])
                 typet.append(y)
    
         h = (set(typet))
         final2 = typet
         for i in h:
            final2.remove(i)
     else:
         typet = []
         for r,key in enumerate(dic2['list'][0]['function'][0]['operation']):
                 y = (dic2['list'][0]['function'][0]['operation'][r]['term'])
                 typet.append(y)   
         final2 = typet
     res = [x for x in final + final2 if x in final 
            and x  in final2]  # go over the two tools and find the similarity 
           
     return set(res) 
