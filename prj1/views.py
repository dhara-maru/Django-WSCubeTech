from django.http import HttpResponse
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from .forms import userforms

def home(request):
    data={
       "title":"Dhara's Site",
        "dharas":"Dhara's",
        "secondtext":"Website",
        "clist":["php", "java", "Django"],
        "numbers" : [10,20,30,40,50],
        "student_details" : [
            {'name':'Dhara', 'phone':'8724958284'},
             {'name':'Hetvi', 'phone':'8724958284'},
        ]
    }
   
    return render(request,"index.html",data)
def about1(request):
    if request.method == "GET":
        output=request.GET.get('finalans')
        
    return render(request,"about.html",{'finalans':output})
def service1(request):
    return render(request,"service.html")
def team1(request):
    return render(request,"team.html")
def why1(request):
    return render(request,"why.html")

def calc1(request):
    try:
        c=''
        if request.method=="POST":
            n1=eval(request.POST.get('num1'))
            opr=request.POST.get('opr')
            n2=eval(request.POST.get('num2'))
            
            if opr=="+":
                c=n1+n2
            elif opr=="-":
                c=n1-n2
            elif opr=="*":
                c=n1*n2
            elif opr=="/":
                c=n1/n2
          
    except:
        print("Invalid Operator")
    print(c)
    return render(request,"calc.html",{'c':c})


def evenorodd1(request):
    try:
        ans=''
        if request.method=="POST":
            n1=eval(request.POST.get('num1'))
            if n1%2==0:
                ans="Even"
            else:
                ans="Odd"
    except:
        print("Invalid Number")
    print(ans)
    return render(request,"evenorodd.html",{'ans':ans})




def userform1(request):
   fn=userforms()
   finalans=0
   data={'form':fn}
   try:
        if request.method=="POST":
             n1=int(request.POST.get('num1'))
             n2=int(request.POST.get('num2'))
             n3=int(request.POST.get('num3'))
             finalans=n1+n2+n3
             data={
                 'num1': n1,
                 'num2':n2,
                 'num3':n3,
                 'finalans':finalans,
                 'form':fn
             }
             url="/about1/?finalans={}".format(finalans)
             return HttpResponseRedirect(url)
   except:
        pass
   return render(request,"userform.html",data)

def submitform1(request):
   finalans=0
   data={}
   try:
        if request.method=="POST":
             n1=int(request.POST.get('num1'))
             n2=int(request.POST.get('num2'))
             n3=int(request.POST.get('num3'))
             finalans=n1+n2+n3
             data={
                 'num1': n1,
                 'num2':n2,
                 'num3':n3,
                 'finalans':finalans
             }
           
             return HttpResponse(finalans)
   except:
        pass
   
