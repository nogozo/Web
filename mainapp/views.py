from django.shortcuts import render, get_object_or_404
from .forms import FeedbackForm, MerchantFeedbackForm
from .models import Feedback, MerchantFeedback
from blog.models import Article, Category

def index(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
 
        if form.is_valid():
            form.save()
    else:
        form = FeedbackForm()
    return render(request, 'mainapp/index.html', {'form': form})


def privacy(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
 
        if form.is_valid():
            form.save()
            return render(request, 'mainapp/thanks.html', context)
    else:
        form = FeedbackForm()    
    context = {
    }
    return render(request, 'mainapp/privacy.html', {'form': form} )


def tnc(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
 
        if form.is_valid():
            form.save()
            return render(request, 'mainapp/thanks.html', context)
    else:
        form = FeedbackForm()    
    context = {
    }
    return render(request, 'mainapp/tnc.html', {'form': form} )


def comming(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
 
        if form.is_valid():
            form.save()
            return render(request, 'mainapp/thanks.html', context)
    else:
        form = FeedbackForm()    
    context = {
    }
    return render(request, 'mainapp/comming.html', {'form': form} )


def download(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
 
        if form.is_valid():
            form.save()
    else:
        form = FeedbackForm()
    return render(request, 'mainapp/download.html', {'form': form})

 
def contact(request): 
    all_articles = Article.objects.all().order_by("article_id").reverse()
    context = {
        'all_articles' : all_articles,
     }
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
 
        if form.is_valid():
            form.save()
            return render(request, 'mainapp/thanks.html', context)
    else:
        form = FeedbackForm()
    return render(request, 'mainapp/contact.html', {'form': form})

 
def merchantcontact(request):
    all_articles = Article.objects.all().order_by("article_id").reverse()
    context = {
        'all_articles' : all_articles,
     }    
    if request.method == 'POST':
        form = MerchantFeedbackForm(request.POST)
 
        if form.is_valid():
            form.save()
            return render(request, 'mainapp/thanks.html', context)
    else:
        form = MerchantFeedbackForm()
    return render(request, 'mainapp/merchantcontact.html', {'form': form})
