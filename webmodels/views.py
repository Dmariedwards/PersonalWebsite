from webmodels.models import Section,User
from django.shortcuts import render, redirect
from forms import AddSectionForm
from django.forms.models import model_to_dict
from django.contrib import messages
from django.contrib.auth.hashers import check_password, make_password
import os
from django.contrib.auth.decorators import login_required

def index(request):
    """ Index Page"""
    
    sections = Section.objects.all()
    return render(request, 'webmodels/index.html', {
        'sections': sections
    })
@login_required(login_url="/login/")
def addsection(request):
    form = AddSectionForm()
    if request.method == 'POST':
        form = AddSectionForm(request.POST,request.FILES)
        if form.is_valid():
            if Section.objects.filter(name=form.cleaned_data['name'].lower()).exists():
                messages.add_message(request, messages.ERROR, 'Section already exists')
                return redirect(('/'))

            else:
                newsection = Section(
                    name=form.cleaned_data['name'].lower(),
                    text=form.cleaned_data['text'])
                errors= [form.clean_file(request)[1],form.clean_photo(request)[1]]
                if errors[0] == 0:
                    if form.clean_file(request)[0]:
                        newsection.pdffile = form.clean_file(request)[0]
                if errors[1] == 0:
                    if form.clean_photo(request)[0]:
                        newsection.image = form.clean_photo(request)[0]

                if errors[0] ==1 or errors[1] == 1:
                    messages.add_message(request, messages.ERROR, 'Error: Did not save. Check your files')
                    return render(request, 'webmodels/addsection.html', {
                        'form': form,
                    })
                newsection.save()
                messages.add_message(request, messages.SUCCESS, "User successfully added")
                return redirect(('/'))

        else:
            messages.add_message(request, messages.ERROR, 'Error: Did not save.')
            return render(request, 'webmodels/addsection.html', {
                'form': form,
            })
    return render(request, 'webmodels/addsection.html', {
                'form': form,
            })
 
