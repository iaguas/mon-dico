from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from . import models, forms


@login_required
def index(request):
    return render(request, 'index.html')


@login_required
def dictionary(request):
#    words = models.Word.objects.get(user=request.user)
    words = models.Word.objects.all().filter(user=request.user)
    return render(request, 'all_words.html', {'words': words})


@login_required
def new_word(request):
    if request.method == 'POST':
        form = forms.NewWordForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            word = form.save(commit=False)
            word.user = request.user
            word.save()
    form = forms.NewWordForm()
    return render(request, 'new_word.html', {'form': form})


@login_required
def report(request):
    return render(request, 'report.html')
