from django import forms
from django.contrib.auth.models import User
from church.models import Event, Comment, Responses, signUp, chosenGroup, attendanceList, Pledge
from django.core import validators


class Userform(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput,validators=[validators.MinLengthValidator(5)])
    email = forms.EmailField(validators=[validators.EmailValidator()])
    username = forms.CharField(validators=[validators.MinLengthValidator(5)])

    class Meta:
        model = User
        fields = ['username', 'password', 'email']


class SignForm(forms.ModelForm):
    profile_picture = forms.ImageField(required=False)
    agree_with_terms_and_conditions = forms.BooleanField(required=True)

    class Meta:
        model = signUp
        fields = ['full_name', 'gender', 'nationality', 'address', 'relationship_status', 'profile', 'tel_number',
                  'occupation', 'profile_picture', 'agree_with_terms_and_conditions']


class JoinGroup(forms.ModelForm):
    class Meta:
        model = chosenGroup
        fields = ['user','group']



class Queries(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['person', 'topic', 'query']


class Contribution(forms.ModelForm):
    class Meta:
        model = Pledge
        fields = ['group', 'person', 'pledge']


class Response(forms.ModelForm):
    class Meta:
        model = Responses
        fields = ['full_name', 'query', 'answer']


class Attend(forms.ModelForm):
    class Meta:
        model = attendanceList
        fields = ['event', 'person']


class Group(forms.ModelForm):
    class Meta:
        model = chosenGroup
        fields = ['user', 'group']
