from django import forms

class RegistrationForm(forms.Form):
    name=forms.CharField(
        label=False,
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Name'
            }
        )
    )
    username = forms.CharField(
        label=False,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Username'
            }
        )
    )
    password = forms.CharField(
        label=False,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Password'
            }
        )
    )
    email = forms.EmailField(
        label=False,
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Email'
            }
        )
    )
    mobile = forms.IntegerField(
        label=False,
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Mobile'
            }
        )
    )
    address = forms.CharField(
        label=False,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Address'
            }
        )
    )

    gender_choices = (
        ('male','Male'),
        ('female','Female')
    )
    gender = forms.ChoiceField(label='Gender',widget=forms.RadioSelect,choices=gender_choices)

    y = range(1950, 3000)
    dob = forms.DateField(label='Date of Birth', widget=forms.SelectDateWidget(years=y))

    profile_pic = forms.ImageField(
        label='Photo',
        widget=forms.FileInput(
            attrs={
                'class': 'form-control',
            }
        )
    )

class LoginForm(forms.Form):
    username = forms.CharField(
        label=False,
        widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Username'})
    )
    password = forms.CharField(
        label=False,
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'})
    )

class OwnerUPDForm(forms.Form):
    patient_name=forms.CharField(
        label='Patient Name',
        label_suffix="",
        widget=forms.TextInput(
            attrs={
                'class':'form-control',

            }
        )
    )
    email = forms.EmailField(
        label='Email',
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
            }
        )
    )
    mobile = forms.IntegerField(
        label='Mobile',
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
            }
        )
    )
    address = forms.CharField(
        label='Address',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
            }
        )
    )
    hospital_name = forms.CharField(
        label='Hospital Name',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
            }
        )
    )
    BGROUP_CHOICES = [
        ('A+', 'A+'),
        ('O+', 'O+'),
        ('B+', 'B+'),
        ('AB+', 'AB+'),
        ('A-', 'A-'),
        ('O-', 'O-'),
        ('B-', 'B-'),
        ('AB-', 'AB-'),
    ]

    patient_blood_group = forms.CharField(
        label='Patient Blood Group',
        widget=forms.Select(choices=BGROUP_CHOICES)
    )
    disease_name = forms.CharField(
        label='Disease Name',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
            }
        )
    )
    disease_symptom = forms.CharField(
        label='Disease Symptom',
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
            }
        )
    )
    patient_age = forms.IntegerField(
        label='Patient Age',
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
            }
        )
    )
    file_name = forms.CharField(
        label='File Name',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
            }
        )
    )
    y=range(1950,3000)
    dob = forms.DateField(label='Date of Birth', widget=forms.SelectDateWidget(years=y))

    select_file = forms.FileField(
        label='Report File',
        widget=forms.FileInput(
            attrs={
                'class': 'form-control',
            }
        )
    )
    patient_pic = forms.ImageField(
        label='Photo',
        widget=forms.FileInput(
            attrs={
                'class': 'form-control',
            }
        )
    )