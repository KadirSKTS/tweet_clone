from django.shortcuts import render, redirect
from . import models
from django.urls import reverse, reverse_lazy
from tweetapp.forms import AddTweetForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView


# Create your views here.

def listtweet(request):
    all_tweets = models.Tweet.objects.all()
    tweet_dict = {"tweets": all_tweets}
    return render(request, "tweetapp/listtweet.html", context=tweet_dict)

@login_required(login_url='/login')
def addtweet(request):
    if request.POST:
        
        massage=request.POST['massage']
        models.Tweet.objects.create(username=request.user,massage=massage)
        return redirect(reverse('tweetapp:listtweet'))
    else:
        return render(request, "tweetapp/addtweet.html")

def addtweetbyform(request):
    if request.method =='POST':
        form = AddTweetForm(request.POST)
        if form.is_valid():
            nickname = form.cleaned_data['nickname_input']
            massage = form.cleaned_data['massage_input']
            models.Tweet.objects.create(nickname=nickname, massage=massage)
            return redirect(reverse('tweetapp:listtweet'))
        else:
            print('error in form')
            return render(request, 'tweetapp/addtweetbyform.html', context={'form':form})

    else:   
        form = AddTweetForm()
        return render(request, 'tweetapp/addtweetbyform.html', context={'form':form})
@login_required
def deletetweet(request, id):
    tweet = models.Tweet.objects.get(pk=id)
    if request.user == tweet.username:
        tweet.delete()
        return redirect('tweetapp:listtweet')
class SingUpView(CreateView):
    form_class = UserCreationForm        
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"
