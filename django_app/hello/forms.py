from django import forms
from.models import Friend

class FriendForm(forms.ModelForm):
  class Meta:
    model = Friend
    fields = ['name', 'mail', 'gender', 'age', 'birthday']


class FriendForm(forms.Form):
  name = forms.CharField(label='Name', widget=forms.TextInput(attrs={'class':'forms-control'}))
  mail = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class':'form-control'}))
  gender = forms.BooleanField(label='Gender', widget=forms.CheckboxInput(attrs={'class':'form-check'}))
  age = forms.IntegerField(label='Age', widget=forms.NumberInput(attrs={'class':'form-control'}))
  birthday = forms.DateField(label='Birth', widget=forms.DateInput(attrs={'class':'form-control'}))


class FindForm(forms.Form):
  find = forms.CharField(label='Find', required=False, widget=forms.TextInput(attrs={'class':'form-control'}))


class CheckForm(forms.Form):
  required = forms.IntegerField(label='Required', widget=forms.NumberInput(attrs={'class':'form-control'}))
  min = forms.IntegerField(label='Min', min_value=100, widget=forms.NumberInput(attrs={'class':'form-control'}))
  max = forms.IntegerField(label='Max', max_value=1000, widget=forms.NumberInput(attrs={'class':'form-control'}))
