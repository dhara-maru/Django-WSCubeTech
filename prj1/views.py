from django.http import HttpResponse
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from .forms import userforms
from service.models import Services

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
    
    servicedata = Services.objects().all()
    return render(request,"service.html")
def team1(request):
    return render(request,"team.html")
def why1(request):
    return render(request,"why.html")

def marksheet1(request):
    try:
        totalm = ''
        percent = ''
        division = ''
        if request.method == "POST":
            pythonm = eval(request.POST.get('pythonm'))
            javam = eval(request.POST.get('javam'))
            dbmsm = eval(request.POST.get('dbmsm'))
            englishm = eval(request.POST.get('englishm'))
            accountsm = eval(request.POST.get('accountsm'))
            
            total = pythonm + javam + dbmsm + englishm + accountsm
            percent = total * 100 / 500
            
            if percent > 90 and percent <= 100:
                division = 'Distinction'
            elif percent > 80 and percent <= 90:
                division = 'First Class'
            elif percent > 60 and percent <= 80:
                division = 'Second Class'
            elif percent > 40 and percent <= 60:
                division = 'Third Class'
            elif percent < 33:
                division = "Failed"
            
            datamarks = {
                't1': total,
                'p1': percent,
                'd1': division
            }
            return render(request, "marksheet.html", datamarks)
    except Exception as e:
        # Log the exception for debugging
        print(f"Error: {e}")
        # Return an error response or redirect to an error page
        return HttpResponse("ENTER VALID VALUES PLEASE!")

    # If the request method is not POST, render the form page
    return render(request, "marksheet.html")
    

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
            if request.POST.get('num1')=='':
                return render(request,"evenorodd.html",{'error':True})
            
            
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
   
