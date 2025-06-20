from django.shortcuts import redirect, render, get_object_or_404
from .models import Tweet, Search
from .forms import TweetForm, UserRegistrationForm, SearchForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login

# Create your views here.

def index(request):
    return render(request, 'index.html')

def tweet_list(request):
    tweets = Tweet.objects.all().order_by("-created_at")
    return render (request, "tweet_list.html", {"tweets" : tweets})

@login_required
def tweet_create(request):
    if request.method == "POST":
        form = TweetForm(request.POST, request.FILES)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user = request.user
            form.save()
            return redirect("tweet_list")
    else:
        form = TweetForm()
    return render(request, "tweet_form.html", {"form": form})

@login_required
def tweet_edit(request, tweet_id):
    tweet = get_object_or_404(Tweet, pk=tweet_id, user=request.user)
    if request.method == "POST": 
        form = TweetForm(request.POST, request.FILES, instance=tweet)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user = request.user
            form.save()
            return redirect("tweet_list")
    else:
        form = TweetForm(instance=tweet)
    return render(request, "tweet_form.html", {"form": form})

@login_required
def tweet_delete(request, tweet_id):
    tweet = get_object_or_404(Tweet, pk=tweet_id, user=request.user)
    if request.method == "POST":
        tweet.delete()
        return redirect("tweet_list")
    return render(request, "tweet_delete_confirm.html", {"tweet": tweet})

def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            login(request, user)
            return redirect("tweet_list")
    else: 
        form = UserRegistrationForm()
    return render(request, "registration/register.html", {"form": form})

def tweet_search(request):
    search_term = request.GET.get("search_term", "")

    tweets = Tweet.objects.filter(text__icontains=search_term) if search_term else Tweet.objects.all()

    return render(request, "tweet_search.html", {"tweets": tweets, "search_term": search_term})

