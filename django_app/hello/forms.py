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
  empty = forms.CharField(label='Empty', empty_value=True, widget=forms.TextInput(attrs={'class':'form-control'}))
  min = forms.CharField(label='Min', min_length=10, widget=forms.TextInput(attrs={'class':'form-control'}))
  max = forms.CharField(label='Max', max_length=10, widget=forms.TextInput(attrs={'class':'form-control'}))
