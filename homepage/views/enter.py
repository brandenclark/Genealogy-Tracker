from django.contrib.auth import authenticate, login
from homepage.models import Person
from django_mako_plus import view_function
from django.http import HttpResponseRedirect
from formlib import Formless
from django import forms
import re


@view_function
def process_request(request):

    form = SignupForm(request)

    if form.is_valid():
        form.commit()
        return HttpResponseRedirect('/homepage/enter')

    context = {
        'form': form,
    }

    return request.dmp.render('enter.html', context)


class SignupForm(Formless):

    def init(self):
        self.fields['first_name'] = forms.CharField(label='First Name :')
        self.fields['last_name'] = forms.CharField(label='Last Name :')
        self.fields['names'] = forms.IntegerField(label='Names Searched :',required=False)
        self.fields['ordinances'] = forms.IntegerField(label='Ordinances Found :', required=False)

    def clean_first_name(self):
        if '<' in self.cleaned_data['first_name']:
            raise forms.ValidationError("Don't be hacking me!")
        return self.cleaned_data['first_name']

    def clean_last_name(self):
        if '<' in self.cleaned_data['last_name']:
            raise forms.ValidationError("Don't be hacking me!")
        return self.cleaned_data['last_name']

    def clean(self):
        return self.cleaned_data


    def commit(self):
        p1 = Person()
        p1.first_name = self.cleaned_data.get('first_name')
        p1.last_name = self.cleaned_data.get('last_name')
        p1.names = self.cleaned_data.get('names')
        p1.ordinances = self.cleaned_data.get('ordinances')

        p1.save()
