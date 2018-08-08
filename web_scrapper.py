from bs4 import BeautifulSoup
#from basic_func import *
import requests

def web_sc(link,key):
    try:
        source = requests.get(link).text
        s = BeautifulSoup(source,'lxml')
        #c=1
        #found=[]
        abc=[]
        for j in ['h1','h2','h3','h4','h5','h6','div','p','span','a']:
            for para in s.find_all(j):
                list1 = (para.text).split(' ')
                #print(list1)
                for i in list1:
                    abc+=(i.split('\n'))
                #print(abc)    
                if key in abc or key.capitalize() in abc or key.upper() in abc:
                    #c=0
                    print(link)
                    #found+=[link]
                    return 1
        #print(link)
        return 0 
    except Exception as _:
        return 0    

#print(web_sc(input(),input()))    
