from pydoc import render_doc
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.core.files.storage import FileSystemStorage
import string
import random
from .models import Inspector, JobMaster, Manager,Coordinator,ClientMaster
from django.contrib.auth import authenticate, login
from django.contrib import messages
# Create your views here.

# Manager
def addManager(request):
    if request.method == 'POST':
        FullName = request.POST['fname']
        ContactNumber = request.POST['contact']
        EmailAddress = request.POST['email']
        Username = request.POST['uname']
        Image = request.FILES['photo']
        fs = FileSystemStorage()
        fs.save(Image.name, Image)
        letters = string.ascii_letters
        password = ''.join(random.choice(letters) for i in range(8))
        data = Manager.objects.create(FullName=FullName,ContactNumber=ContactNumber,EmailAddress=EmailAddress,Username=Username,Photo=Image.name,Password=password)
        data.save()
        messages.info(request, 'Added successfully!')
        return redirect(addManager)
    return render(request,'add-manager.html')

def viewManager(request):
    views = Manager.objects.all()
    return render(request,'view-manager.html',{'viewdata':views})

def editManager(request,id): 
    edit_data = Manager.objects.get(id=id)
    return render(request,'edit-manager.html',{'editdata':edit_data})

def updateManager(request,id):
    if request.method == 'POST':
        FullName = request.POST['fname']
        ContactNumber = request.POST['contact']
        EmailAddress = request.POST['email']
        Username = request.POST['uname']
        Password = request.POST['pass']
        if request.FILES:
            Image = request.FILES['profile_photo']
            fs = FileSystemStorage()
            fs.save(Image.name, Image)
            img_name = Image.name
        else:
            img_name = request.POST['photo']
        
    data = Manager.objects.get(id=id)
    data.FullName = FullName
    data.ContactNumber = ContactNumber
    data.EmailAddress = EmailAddress
    data.Username = Username
    data.Password = Password
    data.Photo = img_name
    data.save()
    return redirect(viewManager)


# Coordinator
def addCoordinator(request):
    if request.method == 'POST':
        FullName = request.POST['fname']
        ContactNumber = request.POST['contact']
        EmailAddress = request.POST['email']
        Username = request.POST['uname']
        Image = request.FILES['photo']
        fs = FileSystemStorage()
        fs.save(Image.name, Image)
        letters = string.ascii_letters
        password = ''.join(random.choice(letters) for i in range(8))
        data = Coordinator.objects.create(FullName=FullName,ContactNumber=ContactNumber,EmailAddress=EmailAddress,Username=Username,Photo=Image.name,Password=password)
        data.save()
        messages.info(request, 'Added successfully!')
        return redirect(addCoordinator)
    return render(request,'add-coordinator.html')

def viewCoordinator(request):
    views = Coordinator.objects.all()
    return render(request,'view-coordinator.html',{'viewdata':views})

def editCoordinator(request,id): 
    edit_data = Coordinator.objects.get(id=id)
    return render(request,'edit-coordinator.html',{'editdata':edit_data})

def updateCoordinator(request,id):
    if request.method == 'POST':
        FullName = request.POST['fname']
        ContactNumber = request.POST['contact']
        EmailAddress = request.POST['email']
        Username = request.POST['uname']
        Password = request.POST['pass']
        if request.FILES:
            Image = request.FILES['profile_photo']
            fs = FileSystemStorage()
            fs.save(Image.name, Image)
            img_name = Image.name
        else:
            img_name = request.POST['photo']
        
    data = Coordinator.objects.get(id=id)
    data.FullName = FullName
    data.ContactNumber = ContactNumber
    data.EmailAddress = EmailAddress
    data.Username = Username
    data.Password = Password
    data.Photo = img_name
    data.save()
    return redirect(viewCoordinator)


# Inspector
def addInspector(request):
    if request.method == 'POST':
        FullName = request.POST['fname']
        ContactNumber = request.POST['contact']
        EmailAddress = request.POST['email']
        Username = request.POST['uname']
        Image = request.FILES['photo']
        fs = FileSystemStorage()
        fs.save(Image.name, Image)
        letters = string.ascii_letters
        password = ''.join(random.choice(letters) for i in range(8))
        data = Inspector.objects.create(FullName=FullName,ContactNumber=ContactNumber,EmailAddress=EmailAddress,Username=Username,Photo=Image.name,Password=password)
        data.save()
        messages.info(request, 'Added successfully!')
        return redirect(addInspector)
    return render(request,'add-inspector.html')

def viewInspector(request):
    views = Inspector.objects.all()
    return render(request,'view-inspector.html',{'viewdata':views})

def editInspector(request,id): 
    edit_data = Inspector.objects.get(id=id)
    return render(request,'edit-inspector.html',{'editdata':edit_data})

def updateInspector(request,id):
    if request.method == 'POST':
        FullName = request.POST['fname']
        ContactNumber = request.POST['contact']
        EmailAddress = request.POST['email']
        Username = request.POST['uname']
        Password = request.POST['pass']
        if request.FILES:
            Image = request.FILES['profile_photo']
            fs = FileSystemStorage()
            fs.save(Image.name, Image)
            img_name = Image.name
        else:
            img_name = request.POST['photo']
        
    data = Inspector.objects.get(id=id)
    data.FullName = FullName
    data.ContactNumber = ContactNumber
    data.EmailAddress = EmailAddress
    data.Username = Username
    data.Password = Password
    data.Photo = img_name
    data.save()
    return redirect(viewInspector)

def login(request):
    if request.method == 'POST':
        UserName = request.POST['uname']
        Password = request.POST['pass']

        user = authenticate(request, username = UserName, password = Password)
        if user is not None:
            return redirect(adminHome)
        elif Coordinator.objects.filter(Username=UserName,Password=Password).exists():
            coordinator = Coordinator.objects.filter(Username=UserName,Password=Password)
            return redirect(coordinatorHome)
    return render(request,'login.html')

def logout(request):
    return redirect(login)


def adminHome(request):
    return render(request,'admin-home.html')

def coordinatorHome(request):
    return render(request,'coordinator-home.html')

def coordinatorAddInspector(request):
    return render(request,'coordinator-add-inspector.html')

def coordinatorViewInspector(request):
    views = Inspector.objects.all()
    return render(request,'coordinator-view-inspector.html',{'viewdata':views})

def coordinatorEditInspector(request,id): 
    print(id)
    edit_data = Inspector.objects.get(id=id)
    return render(request,'coordinator-edit-inspector.html',{'editdata':edit_data})

def coordinatorUpdateInspector(request,id):
    if request.method == 'POST':
        FullName = request.POST['fname']
        ContactNumber = request.POST['contact']
        EmailAddress = request.POST['email']
        Username = request.POST['uname']
        Password = request.POST['pass']
        if request.FILES:
            Image = request.FILES['profile_photo']
            fs = FileSystemStorage()
            fs.save(Image.name, Image)
            img_name = Image.name
        else:
            img_name = request.POST['photo']
        
    data = Inspector.objects.get(id=id)
    data.FullName = FullName
    data.ContactNumber = ContactNumber
    data.EmailAddress = EmailAddress
    data.Username = Username
    data.Password = Password
    data.Photo = img_name
    data.save()
    return redirect(coordinatorViewInspector)

def viewClient(request):
    data = ClientMaster.objects.all()
    return render(request,'view-clientmaster.html',{'data':data})


def jobSchedule(request):
    if request.method == 'POST':
        InspectorName = request.POST['iname']
        ClientName = request.POST['cname']
        ClientLocation = request.POST['clocation']
        scheduledDate = request.POST['date']

        data = JobMaster.objects.create(inspector_id=InspectorName,clientname_id=ClientName,clientlocation=ClientLocation,scheduledDate=scheduledDate)
        data.save()
        return redirect(jobSchedule)
    else:
        inspctor = Inspector.objects.all()
        client = ClientMaster.objects.all()
        return render(request,'job-master.html',{'clientdata':client,'inspectordata':inspctor})