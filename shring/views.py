from django.http import HttpResponse
from django.shortcuts import render
from firebase import firebase
import operator



def homepage(request):
    return render(request,'home.html')
def homepage2(request):
    return render(request,'home2.html')
 
    
def insert(request):
    name=request.POST['txt1']
    code=request.POST['txtarea']
    con=firebase.FirebaseApplication("https://shring-7b415.firebaseio.com/",None)
    keylist={}
    result2=con.get('/shrink',"name/")
    list_length=len(result2)
    
    for word in result2:
        if name in word:
            print("key is generated")
            break
        else:
            print("key is not generated")
            result=con.patch('/shrink/name',{name:code})
            break
    return render(request,'home.html',{'name':name,'code':code,'result':keylist})



def retrive(request):
    vall=request.POST['txt2']
    vall2='name/'
    vall3=vall2+vall
    fcon2=firebase.FirebaseApplication("https://shring-7b415.firebaseio.com/",None)
    result2=fcon2.get('/shrink',vall3)
    print (result2)
    
    
    return render(request,'home2.html',{'result2':result2,'vall':vall})
