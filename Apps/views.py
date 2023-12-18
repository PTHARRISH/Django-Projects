from django.shortcuts import render
from django.http import HttpResponse,JsonResponse # import and return data in httpresponse,jsonresponse

# Create your views here.

# print Hello world in HttpResponse
def myfunctioncall(request):
    return HttpResponse('Hai Harrish')

# pass parameter and add a+b(mention a and b in argument) else Type error occur unexpected keyword arguments
def add(request,a,b): 
    return HttpResponse(a+b)

# pass parameter and display name print in http response
def printname(request,name):
    return HttpResponse(f'Hai {name}') #dynamically print the name formating  

# pass parameter and display name and age stored in mydictionary print in json response
def intro(request,name,age):
    mydictionary={
        'name':name,
        'age':age
    }
    return JsonResponse(mydictionary)

# first html page create navigation bar and extends to second page
def firstpage(request):
    return render(request,'apps/first.html')

# extend navigation bar in second page
def secondpage(request):
    return render(request,'apps/second.html')

# create dictionary and display in templates
# dictionary data
def thirdpage(request):
    name="Harrish"
    age=22
    DOB="22/03/2001"
    mydict={
        'name':name,
        'age':age,
        'DOB':DOB,
    }
    return render(request,'apps/third.html',context=mydict) # only context send the dictionary data 

# create fruit list convert dictionary and display in templates
# Dictionary and For loop
def fruits(request):
    fruits=['apple','banana','orange','mango']
    mydict={
        'name':fruits,
        'fruits':fruits,
    }
    # pass the dictionary key and value you need to mention {'dict1':mydict}
    return render(request,'apps/fruits.html',{'dict1':mydict})


# If else part print num1 or num2 Greater
def num(request,num1,num2):
    ans=num1>num2
    mydict={
        'ans':ans,
        'num1':num1,
        'num2':num2
    }
    return render(request,'apps/num.html',context=mydict)


