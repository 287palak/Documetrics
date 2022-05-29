from django import forms
from results.models import FaceRecognition
from results.models import OTP

class FaceRecognitionform(forms.ModelForm):

    class Meta:
        model = FaceRecognition
        fields =['image']

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['image'].widget.attrs.update({'class':'form-control'})


class OTPform(forms.Form):
    otp = forms.IntegerField()

class uploadform(forms.Form):
    stu_id = forms.IntegerField()
    exam = forms.CharField(max_length=20)
    result = forms.CharField(max_length=20)
    certificate = forms.IntegerField()