from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request,'index.html') #using template file to return 

def inputis(request):
   # s='the input is : '
    input=request.POST.get('text','default') #gettin the text from html file and printing it 
    responsee=request.POST.get('response','off')#getting the checkbox input and printing it 
    uppercase=request.POST.get('uppercase','off') #getting the checkbox input and printing it 
    charcounter=request.POST.get('charcounter','off') #getting the checkbox input and printing it 
    print(input)
    print(charcounter)
   # print(responsee)
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    #analyzedd=""
    counter=0
    input1=input
    if responsee=='on':
        analyzedd=""
        for char in input:
            if char not in punctuations:
                analyzedd=analyzedd+char 
            #checking if the punctuations is in the input or not , if not then adding to a new variable called analyzed 
            #basically removing the punctuations 
        Params = {'rawinput' : input1,'newinput' :analyzedd } #taking the argument from analise.html file  with {{}} in html file 
        input=analyzedd
        #return render(request,'analise.html',Params)


    if(uppercase=='on'):
        analyzedd=""    
        for char in input:
            analyzedd=analyzedd + char.upper()  #converting lowercase to upper
        Params = {'rawinput' : input1,'newinput' :analyzedd } #taking the argument from analise.html file  with {{}} in html file 
        input=analyzedd
       # return render(request,'analise.html',Params) 

    if(charcounter=='on'):
        analyzedd=""
        for char in input:
            if char not in ' ':
                counter=counter+1
        analyzedd=counter               
        Params = {'rawinput' : input1,'newinput' :analyzedd } #taking the argument from analise.html file  with {{}} in html file 
        
    if(uppercase!='on' and charcounter!='on' and  responsee!='on'):
        return HttpResponse('please add check box ')
 
    return render(request,'analise.html',Params)     

   
        
            
  
    

    