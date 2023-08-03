from django.shortcuts import render
from . forms import CheckForm
from django.forms import formset_factory
# Create your views here.
def home_view(request):
    context = {}
    checkFormset = formset_factory(CheckForm, extra= 4)
    form = checkFormset(request.POST or None)
    if form.is_valid():
        for f in form:
            print(f.cleaned_data)
        form.save()
    context['form'] = form
    return render(request, 'accounts/home.html', context)