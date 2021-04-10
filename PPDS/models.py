from django.db import models

class OwnerRegistrationData(models.Model):
    name = models.CharField(max_length=100)
    ownername = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.EmailField(max_length=50)
    mobile = models.BigIntegerField()
    address = models.CharField(max_length=100)
    gender = models.CharField(max_length=20)
    dob = models.DateField(max_length=20)
    profile_pic = models.ImageField(upload_to='owner/owner_photo')
    status = models.CharField(max_length=100)

class UserRegistrationData(models.Model):
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.EmailField(max_length=50)
    mobile = models.BigIntegerField()
    address = models.CharField(max_length=100)
    gender = models.CharField(max_length=20)
    dob = models.DateField(max_length=20)
    profile_pic = models.ImageField(upload_to='user/user_photo')
    status = models.CharField(max_length=100)

class OwnerUPDData(models.Model):
    owner_name=models.CharField(max_length=100)
    patient_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=50)
    mobile = models.BigIntegerField()
    address = models.CharField(max_length=100)
    hospital_name = models.CharField(max_length=100)
    patient_blood_group = models.CharField(max_length=100)
    disease_name = models.CharField(max_length=20)
    disease_symptom = models.CharField(max_length=20)
    patient_age = models.IntegerField()
    file_name = models.CharField(max_length=20)
    dob = models.DateField(max_length=20)
    joining_date = models.CharField(max_length=30)
    select_file = models.FileField(upload_to='patient/files')
    patient_pic = models.ImageField(upload_to='patient/patient_photo')
    permission = models.CharField(max_length=100)

class OwnerSACData(models.Model):
    owner=models.CharField(max_length=100)
    patient_id=models.BigIntegerField()
    patient = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    profession = models.CharField(max_length=100)

class KeyRequestData(models.Model):
    owner = models.CharField(max_length=100)
    patient_id = models.BigIntegerField()
    patient = models.CharField(max_length=100)
    file = models.CharField(max_length=100)
    secret_key = models.CharField(max_length=100)

class TransactionData(models.Model):
    owner = models.CharField(max_length=100)
    patient = models.CharField(max_length=100)
    filename = models.CharField(max_length=100)
    task = models.CharField(max_length=100)
    date = models.CharField(max_length=100)

class AttackerData(models.Model):
    owner = models.CharField(max_length=100)
    patient = models.CharField(max_length=100)
    date = models.CharField(max_length=100)