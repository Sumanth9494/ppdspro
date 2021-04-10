import mimetypes
import os
import random
import datetime as dt
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from wsgiref.util import FileWrapper
from django.shortcuts import render
from django.http.response import HttpResponse
from PPDS_Project import settings
from .models import *
from .forms import *

def jdate():
    global y
    x = dt.datetime.now()
    y = (x.strftime("%d-%m-%Y"))
    return y
def tdate():
    global z
    x = dt.datetime.now()
    z = format(x)
    return z

def url_path_link(request):
    global owner_reg,owner_login,user_reg,user_login,authority_login,ehcs_login
    owner_reg='/ownerRegister/'
    owner_login='/ownerLogin/'
    user_reg = '/userRegister/'
    user_login = '/userLogin/'
    authority_login = '/authorityLogin/'
    ehcs_login = '/ehcsLogin/'
    url_path = request.path
    if url_path == owner_reg:
        return ownerRegister_view(request)
    elif url_path == owner_login:
        return ownerLogin_view(request)
    elif url_path == user_reg:
        return userRegister_view(request)
    elif url_path == user_login:
        return userLogin_view(request)
    elif url_path == authority_login:
        return authorityLogin_view(request)
    elif url_path == ehcs_login:
        return ehcsLogin_view(request)
    else:
        pass

def home(request):
    return render(request,'home.html')

def OwnerRegForm(request):
    o_formname = 'Owner Registration Form'
    orform = RegistrationForm()
    context = {
        'orform': orform,
        'o_formname': o_formname
    }
    return render(request, 'RegistrationForm.html', context)
def OwnerLogForm(request):
    o_formname = 'Owner Login Form'
    olform = LoginForm()
    context = {
        'olform': olform,
        'o_formname': o_formname,
    }
    return render(request, 'LoginForm.html', context)
def UserRegForm(request):
    u_formname = 'User Registration Form'
    reg_form = user_reg
    urform = RegistrationForm()
    context = {
        'urform': urform,
        'u_formname': u_formname,
        'reg_form': reg_form
    }
    return render(request, 'RegistrationForm.html', context)
def UserLogForm(request):
    u_formname = 'User Login Form'
    log_form = user_login
    ulform = LoginForm()
    context = {
        'ulform': ulform,
        'u_formname': u_formname,
        'log_form': log_form
    }
    return render(request, 'LoginForm.html', context)
def AuthorityLogForm(request):
    a_formname = 'Authority Login Form'
    auth_log_form = authority_login
    alform = LoginForm()
    context = {
        'alform': alform,
        'a_formname': a_formname,
        'auth_log_form': auth_log_form
    }
    return render(request, 'LoginForm.html', context)
def EhcsLogForm(request):
    e_formname = 'EHCS Login Form'
    ehcs_log_form = ehcs_login
    elform = LoginForm()
    context = {
        'elform': elform,
        'e_formname': e_formname,
        'ehcs_log_form': ehcs_log_form
    }
    return render(request, 'LoginForm.html', context)
def ownerRegister_view(request):
    if request.method == 'POST':
        orform = RegistrationForm(request.POST,request.FILES)
        if orform.is_valid():
            name = request.POST.get("name")
            username = request.POST.get("username")
            password = request.POST.get("password")
            email = request.POST.get("email")
            mobile = request.POST.get("mobile")
            address = request.POST.get("address")
            gender = orform.cleaned_data.get("gender")
            dob = orform.cleaned_data.get("dob")
            profile_pic = orform.cleaned_data.get("profile_pic")

            data = OwnerRegistrationData(
                name=name,
                ownername=username,
                password=password,
                email=email,
                mobile=mobile,
                address=address,
                gender=gender,
                dob=dob,
                profile_pic=profile_pic,
                status='Inactive'
            )
            data.save()
            response = HttpResponse()  # Created a HttpResponse
            response['Cache-Control'] = 'no-cache'  # Set Cache-Control Header
            return OwnerRegForm(request)
        else:
            return HttpResponse('Invalid Details')
    else:
        return OwnerRegForm(request)

def ownerLogin_view(request):
    if request.method == 'POST':
        olform = LoginForm(request.POST)
        if olform.is_valid():
            global username
            username = request.POST.get("username")
            password = request.POST.get("password")
            uname = OwnerRegistrationData.objects.filter(ownername=username)
            pwd = OwnerRegistrationData.objects.filter(password=password)
            if uname and pwd:
                response = HttpResponse()  # Created a HttpResponse
                response['Cache-Control'] = 'no-cache'  # Set Cache-Control Header
                check_status = OwnerRegistrationData.objects.filter(ownername=username)
                for i in check_status:
                    x = i.status
                    if x == 'Inactive':
                        return HttpResponse('Your Account is not Authorized')
                    else:
                        return ownerHome_view(request)
            elif not uname:
                return HttpResponse("You Have Not Registered")
            else:
                return HttpResponse("Please enter correct ownername / password")
        else:
            return HttpResponse("Invalid Details")
    else:
        return OwnerLogForm(request)

def ownerHome_view(request):
    odata=OwnerRegistrationData.objects.filter(ownername=username)
    return render(request, 'Owner.html',{'odata':odata})

def owner_data():
    global a
    ownerName=OwnerRegistrationData.objects.filter(ownername=username)
    for i in ownerName:
        a=i.ownername
        return a

def ownerUPD_view(request):
    if request.method == 'POST':
        oupdform = OwnerUPDForm(request.POST,request.FILES)
        if oupdform.is_valid():
            global patient_name
            patient_name = request.POST.get("patient_name")
            email = request.POST.get("email")
            mobile = request.POST.get("mobile")
            address = request.POST.get("address")
            hospital_name = request.POST.get("hospital_name")
            patient_blood_group = request.POST.get("patient_blood_group")
            disease_name = request.POST.get("disease_name")
            disease_symptom = request.POST.get("disease_symptom")
            patient_age = request.POST.get("patient_age")
            file_name = request.POST.get("file_name")
            dob = oupdform.cleaned_data.get("dob")
            select_file = oupdform.cleaned_data.get("select_file")
            patient_pic = oupdform.cleaned_data.get("patient_pic")


            data = OwnerUPDData(
                owner_name=owner_data(),
                patient_name=patient_name,
                email=email,
                mobile=mobile,
                address=address,
                hospital_name=hospital_name,
                patient_blood_group=patient_blood_group,
                disease_name=disease_name,
                disease_symptom=disease_symptom,
                patient_age=patient_age,
                file_name=file_name,
                dob=dob,
                select_file=select_file,
                patient_pic=patient_pic,
                joining_date=jdate(),
                permission='Send Request'
            )
            data.save()
            tdata = TransactionData(owner=owner_data(), patient=patient_name, filename=select_file, task='Upload', date=tdate())
            tdata.save()
            response = HttpResponse()  # Created a HttpResponse
            response['Cache-Control'] = 'no-cache'  # Set Cache-Control Header
            oupdform = OwnerUPDForm()
            return render(request,'Owner.html',{'oupdform':oupdform})
        else:
            return HttpResponse('Invalid Details')
    else:
        oupdform = OwnerUPDForm()
        return render(request,'Owner.html',{'oupdform':oupdform})

def ownerVPD_view(request):
    pddata = OwnerUPDData.objects.filter(owner_name=owner_data())
    return render(request, 'Owner.html', {'pddata' : pddata,'pderror':'No Data'})

def patientId():
    global name,patientname
    patientname=OwnerUPDData.objects.filter(patient_name=patient,owner_name=username)
    for i in patientname:
        name=i.id
        return name

def ownerSAC_view(request):
    sacdata = OwnerUPDData.objects.filter(owner_name=owner_data())
    return render(request, 'Owner.html', {'sacform': sacdata})

def ownerSacForm(request):
    if ('patient' and 'department' and 'profession') in request.POST:
        global patient

        patient = request.POST.get('patient')
        department = request.POST.get('department')
        profession = request.POST.get('profession')

        data = OwnerSACData(
            owner=owner_data(),
            patient_id=patientId(),
            patient=patient,
            department=department,
            profession=profession
        )
        data.save()
        return ownerSAC_view(request)
    else:
        message = 'You submitted an empty form.'
        return HttpResponse(message)

def ownerVAC_view(request):
    vacdata = OwnerSACData.objects.filter(owner=owner_data())
    return render(request, 'Owner.html', {'vacdata': vacdata,'acerror':'No Data'})

def userRegister_view(request):
    if request.method == 'POST':
        urform = RegistrationForm(request.POST, request.FILES)
        if urform.is_valid():
            name = request.POST.get("name")
            username = request.POST.get("username")
            password = request.POST.get("password")
            email = request.POST.get("email")
            mobile = request.POST.get("mobile")
            address = request.POST.get("address")
            gender = urform.cleaned_data.get("gender")
            dob = urform.cleaned_data.get("dob")
            profile_pic = urform.cleaned_data.get("profile_pic")

            data = UserRegistrationData(
                name=name,
                username=username,
                password=password,
                email=email,
                mobile=mobile,
                address=address,
                gender=gender,
                dob=dob,
                profile_pic=profile_pic,
                status='Inactive'
            )
            data.save()
            response = HttpResponse()  # Created a HttpResponse
            response['Cache-Control'] = 'no-cache'  # Set Cache-Control Header
            return UserRegForm(request)
        else:
            return HttpResponse('Invalid Details')
    else:
        return UserRegForm(request)

def userLogin_view(request):
    if request.method == 'POST':
        ulform = LoginForm(request.POST)
        if ulform.is_valid():
            global lusername
            lusername = request.POST.get("username")
            password = request.POST.get("password")
            uname = UserRegistrationData.objects.filter(username=lusername)
            pwd = UserRegistrationData.objects.filter(password=password)
            if uname and pwd:
                response = HttpResponse()  # Created a HttpResponse
                response['Cache-Control'] = 'no-cache'  # Set Cache-Control Header
                check_status = UserRegistrationData.objects.filter(username=lusername)
                for i in check_status:
                    x = i.status
                    if x == 'Inactive':
                        return HttpResponse('Your Account is not Authorized')
                    else:
                        return userHome_view(request)
            elif not uname:
                return HttpResponse("You Have Not Registered")
            else:
                return HttpResponse("Please enter correct ownername / password")
        else:
            return HttpResponse("Invalid Details")
    else:
        return UserLogForm(request)

def userHome_view(request):
    udata = UserRegistrationData.objects.filter(username=lusername)
    return render(request,'User.html',{'udata':udata})

def searchKey(request):
    if ('keyword') in request.POST:
        global searchData
        keyword = request.POST.get('keyword')
        search = OwnerUPDData.objects.all().filter(patient_name__icontains=keyword)
        for i in search:
            pname = i.patient_name
            fname = i.select_file
            data = TransactionData(owner=lusername, patient=pname, filename=fname, task='Search', date=tdate())
            data.save()
            return render(request,'User.html',{'search':search,'spview':'spview'})
        else:
            return render(request,'User.html',{'Kmessage':'No Data'})
    else:
        message = 'No Data'
        return render(request,'User.html',{'Kmessage':message})

def viewFD(request,id):
    req_id = id
    data = OwnerUPDData.objects.filter(id=req_id)
    if data:
        return render(request,'User.html',{'data':data,'spview':'spview'})
    else:
        message = 'No Data'
        return render(request, 'User.html', {'Dmessage': message})

def sendKeyRequest(request,id,patient_name):
    odata = OwnerUPDData.objects.filter(id=id,patient_name=patient_name)
    for i in odata:
        fileData = i.select_file
        odata.update(permission = 'success')
        data=KeyRequestData(owner=lusername,patient_id=id,patient=patient_name,file=fileData,secret_key='waiting')
        if data:
            data.save()
            return render(request,'User.html',{'Rmessage':'Request Success'})
        else:
            return render(request,'User.html',{'Rmessage':'Request Failed'})

def userSearchPatient_view(request):
    sp = 'spview'
    return render(request, 'User.html',{'spview':sp})

def userSKR_view(request):
    kdata = KeyRequestData.objects.all()
    return render(request, 'User.html',{'kdata': kdata,'kmsg':'No Data'})

def downloadFile(request,patient_id):
    if ('key') in request.POST:
        global key
        key = request.POST.get('key')
        kdata = KeyRequestData.objects.filter(patient_id=patient_id)
        for i in kdata:
            x = i.secret_key
            fileData = i.file
            pname = i.patient
            if x == key:
                data = TransactionData(owner=lusername, patient=pname, filename=fileData, task='Download', date=tdate())
                data.save()
                file_path = settings.MEDIA_ROOT + '/' + fileData
                file_wrapper = FileWrapper(open(file_path, 'rb'))
                file_mimetype = mimetypes.guess_type(file_path)
                response = HttpResponse(file_wrapper, content_type=file_mimetype)
                response['X-Sendfile'] = file_path
                response['Content-Length'] = os.stat(file_path).st_size
                response['Content-Disposition'] = 'attachment; filename=%s/' % str(fileData)
                return response
            elif not key:
                return HttpResponse('Enter Secret Key')
            else:
                data = AttackerData(owner=lusername, patient=pname,date=tdate())
                data.save()
                return HttpResponse('Attacker')
    else:
        message = 'No Key'
        return HttpResponse(message)

def userDownload_view(request):
    ddata = KeyRequestData.objects.all()
    return render(request,'User.html' ,{'ddata': ddata,'dmsg':'No Data'})

def authorityLogin_view(request):
    if request.method == 'POST':
        alform = LoginForm(request.POST)
        if alform.is_valid():
            uname = request.POST.get('username')
            pwd = request.POST.get('password')
            if uname == 'admin' and pwd == 'admin':
                return authorityHome_view(request)
            else:
                return HttpResponse('Please enter correct username / password')
        else:
            return HttpResponse('Invalid Login Details')
    else:
        return AuthorityLogForm(request)

def authorityHome_view(request):
    return render(request,'Authority.html',{'home':'Welcome to Authority'})

def ownerActivate(request,id):
    req_id = id
    req_status = 'Active'
    rid = OwnerRegistrationData.objects.filter(id=req_id)
    if rid:
        rid.update(status = req_status)
        return authorityVO_view(request)

def userActivate(request,id):
    req_id = id
    req_status = 'Active'
    rid = UserRegistrationData.objects.filter(id=req_id)
    if rid:
        rid.update(status = req_status)
        return authorityVU_view(request)

def ownerDeactivate(request,id):
    req_id = id
    req_status = 'Inactive'
    rid = OwnerRegistrationData.objects.filter(id=req_id)
    if rid:
        rid.update(status=req_status)
        return authorityVO_view(request)

def userDeactivate(request,id):
    req_id = id
    req_status = 'Inactive'
    rid = UserRegistrationData.objects.filter(id=req_id)
    if rid:
        rid.update(status=req_status)
        return authorityVU_view(request)

def authorityVO_view(request):
    odata = OwnerRegistrationData.objects.all()
    return render(request, 'Authority.html', {'odata': odata,'oerror':'No Data'})

def authorityVU_view(request):
    udata = UserRegistrationData.objects.all()
    return render(request, 'Authority.html', {'udata': udata,'uerror':'No Data'})

def generateKey(request,id):
    req_id = id
    key_value = random.randint(1111111, 9999999)
    kid = KeyRequestData.objects.filter(id=req_id)
    if kid:
        kid.update(secret_key=key_value)
        return authoritySK_view(request)

def authoritySK_view(request):
    kdata = KeyRequestData.objects.all()
    return render(request,'Authority.html',{'kdata':kdata,'kerror':'No Data'})

def authorityAttacker_view(request):
    adata = AttackerData.objects.all()
    return render(request,'Authority.html',{'adata':adata,'aerror':'No Data'})

def ehcsLogin_view(request):
    if request.method == 'POST':
        elform = LoginForm(request.POST)
        if elform.is_valid():
            uname = request.POST.get('username')
            pwd = request.POST.get('password')
            if uname == 'cloud' and pwd == 'cloud':
                return ehcsHome_view(request)
            else:
                return HttpResponse('Please enter username / password')
        else:
            return HttpResponse('Invalid Login Details')
    else:
        return EhcsLogForm(request)

def ehcsHome_view(request):
    return render(request,'EHCS.html',{'ehome':'ehome'})

def ehcsPatient_view(request):
    pdata = OwnerUPDData.objects.all()
    return render(request,'EHCS.html',{'pdata':pdata,'pderror':'No Data'})

def ehcsSAC_view(request):
    sacdata = OwnerSACData.objects.all()
    return render(request,'EHCS.html',{'sacdata':sacdata,'sacerror':'No Data'})

def ehcsTransaction_view(request):
    tdata = TransactionData.objects.all()
    return render(request,'EHCS.html',{'tdata':tdata,'terror':'No Data'})

def ehcsSKR_view(request):
    skrdata = KeyRequestData.objects.all()
    return render(request,'EHCS.html',{'skrdata':skrdata,'skrerror':'No Data'})

matplotlib.use('Agg')
x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])

plt.bar(x,y)
plt.show()

def ehcsAttackers_view(request):
    return render(request,'EHCS.html',{'amsg':'Attacker'})

def ehcsDC_view(request):
    return render(request,'EHCS.html',{'dcmsg':'Disease Chart'})

def ehcsSRC_view(request):
    return render(request,'EHCS.html',{'srcmsg':'Search rank in chart'})