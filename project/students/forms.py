from django import forms
from students.models import Registration
from students.models import Authentication


class Registrationform(forms.ModelForm):
    class Meta:
        model = Registration
        fields =['name','image', 'exam']

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['image'].widget.attrs.update({'class':'form-control'})
        self.fields['name'].widget.attrs.update({'class': 'textarea','rows':1,'placeholder': 'Enter your name'})
        self.fields['exam'].widget.attrs.update({'class': 'textarea','rows':1,'placeholder': 'Enter the name of the exam'})

class Authenticationform(forms.ModelForm):
    class Meta:
        model = Authentication
        fields =['name','image', 'exam']

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['image'].widget.attrs.update({'class':'form-control'})
        self.fields['name'].widget.attrs.update({'class': 'textarea','rows':1,'placeholder': 'Enter your name'})
        self.fields['exam'].widget.attrs.update({'class': 'textarea','rows':1,'placeholder': 'Enter the name of the exam'})