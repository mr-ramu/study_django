from django import forms
from.models import Friend

class FriendForm(forms.ModelForm):
  class Meta:
    model = Friend
    fields = ['name', 'mail', 'gender', 'age', 'birthday']
    widgets = {
      'name':forms.TextInput(attrs={'class':'form-control'}),
      'mail':forms.EmailInput(attrs={'class':'form-control'}),
      'age':forms.NumberInput(attrs={'class':'form-control'}),
      'birthday':forms.DateInput(attrs={'class':'form-control'}),
    }


class FriendForm(forms.Form):
  name = forms.CharField(label='Name', widget=forms.TextInput(attrs={'class':'forms-control'}))
  mail = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class':'form-control'}))
  gender = forms.BooleanField(label='Gender', widget=forms.CheckboxInput(attrs={'class':'form-check'}))
  age = forms.IntegerField(label='Age', widget=forms.NumberInput(attrs={'class':'form-control'}))
  birthday = forms.DateField(label='Birth', widget=forms.DateInput(attrs={'class':'form-control'}))



class CheckForm(forms.Form):
  str = forms.CharField(label='String', widget=forms.TextInput(attrs={'class':'form-control'}))
  
  def clean(self):
    cleaned_data = super().clean()
    str = cleaned_data['str']
    if (str.lower().startswith('no')):
      raise forms.ValidationError('you input "NO"')
