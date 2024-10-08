from django.http import HttpResponse
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from .forms import userforms
from newservice.models import newserviceclass
from news.models import news
from django.core.paginator import Paginator
from contactq.models import contactq
from django.core.mail import send_mail, EmailMultiAlternatives
from login.models import loginclass
from django.shortcuts import render, redirect 
from django.contrib import messages


def home(request):
       
  
    #VID 51 SIMPLE EMAIL SENDING METHOD
    #--------------------------------------------
    # send_mail(
    #     'Subject esting mail',
    #     'Here is Dhara\'s message.',
    #     'djangodhara@gmail.com',
    #     ['dharamaru406@gmail.com'],
    #     fail_silently=False,
    # )
    
    
    #VID 52 EMAIL MULTI ALTERNATIVES METHOD : 
    #---------------------------------------------
    # subject='Subject esting mail'
    # from_email = 'djangodhara@gmail.com'
    # msg = '<p>Eda Mone!!!</p>'
    # to_email= 'dharamaru406@gmail.com'
    # msg = EmailMultiAlternatives(subject, msg, from_email, [to_email]) 
    # msg.content_subtype='html'
    # msg.send()
    

   

    newsdata = news.objects.all().order_by('-id');
    newservicedata = newserviceclass.objects.all().order_by('-id')[:3]
    testimonialdata = contactq.objects.all().order_by('id')
    data={
        'mytitle':"Finexo",
        'newsdata': newsdata,
        'servicesdata': newservicedata,
        'testimonialdata': testimonialdata
    }
 
    
    return render(request,"index.html",data)

def newsdetail(request, id):
    newsdetail = news.objects.get(id=id)
    data={
        'newsdetail':newsdetail,
    }
    return render(request,"newsdetail.html",data)
    

def about1(request):
    if request.method == "GET":
        output=request.GET.get('finalans')
        
    return render(request,"about.html",{'finalans':output})



def service1(request):
    
    
    # Fetch all records from the newserviceclass model
    newservicedata = newserviceclass.objects.all().order_by('-id')
    paginator=Paginator(newservicedata,3)
    page_number=request.GET.get('page')
    servicedatafinal=paginator.get_page(page_number)
    totalpage=servicedatafinal.paginator.num_pages;
    
    
    # Check if there is a GET request with 'servicename' parameter
    st = request.GET.get('servicename')
    if st:
        # Filter the newservicedata based on the 'service_title' field
        newservicedata = newserviceclass.objects.filter(service_title__icontains=st).order_by('-id')

    # Pass the filtered or unfiltered data to the template
    data = {
        'servicesdata': servicedatafinal,
        'lastpage':totalpage,
        'totalpagelist':[n+1 for n in range(totalpage)]
    }

    return render(request, "service.html", data)






def contact1(request):
    return render(request, "contact.html")

def saveenquiry1(request):
    if request.method=="POST":
        msg=''
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        website=request.POST.get('website')
        msg=request.POST.get('msg')
        
        data=contactq(contactq_name=name, contactq_email=email, contactq_phone=phone, contactq_website=website, contactq_message = msg )
        
        data.save()
        msg="Thanks for your Query!"
    return render(request, "contact.html",{'msg':msg})



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
   


def signup1(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Save the data to the model
        user = loginclass(login_username=username, login_email=email, login_password=password)
        user.save()

        # Redirect to login page after successful signup
        return redirect('loginform1')  # Assuming you have a URL named 'login'
    return render(request, 'signup.html')



def loginform1(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = loginclass.objects.get(login_username=username, login_password=password)
            # Redirect to the home page if credentials are correct
            return redirect('home')
        except loginclass.DoesNotExist:
            # Display an error message if login fails
            messages.error(request, 'Invalid username or password.')

    return render(request, 'loginform.html')
