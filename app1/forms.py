"""from django import forms


class register(forms.Form):
    firstname = forms.CharField(widget=forms.Textarea(attrs={'row':3}))
    lastname = forms.CharField(widget=forms.TextInput, label='Last_Name')
    age = forms.IntegerField(min_value=18, max_value=45)
    dob = forms.DateField(widget=forms.NumberInput(attrs={'type':'date'}))
    # yr = ['2017', '2018', '2019', '2020']
    # dob = forms.DateField(widget=forms.SelectDateWidget(years = yr))
    lst = [('male', 'MALE'), ('female', 'FEMALE'), ('other', 'OTHER')]
    gender = forms.ChoiceField(choices=lst)
    # gender = forms.MultipleChoiceField(choices=lst)
    # gender = forms.ChoiceField(widget=forms.RadioSelect, choices = lst)
    # gender = forms.MultipleChoiceField(widget=forms.CheckBoxSelectMultiple, choices = lst)
    email = forms.EmailField()
    phone = forms.IntegerField()
    username = forms.CharField(min_length=4, max_length=10, required=True,initial='Enter 4-10 letters')
    password = forms.CharField(widget=forms.PasswordInput)
    confirmPassword = forms.CharField(widget=forms.PasswordInput)
    # images = forms.ImageField()
    file = forms.FileField()
"""