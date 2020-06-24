from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author': 'Lanice',
        'title': "Automation",
        'content': "This suggests the system in place is already sufficient and the process should be damn near effortless. This is concerning for numerous reasons. We see how AI and automation seek to replace human decision-making process - including accepting or rejecting employment, housing and public benefits applications, setting or rejecting bail, and analyzing insurance claims",
        'date_posted': 'June 18, 2020'
    },
    {
        'author': 'Lanice',
        'title': '''Transitions''',
        'content': '''I am noticing a problem while I work to restructure my day. Transitions. It seemingly takes a lot of time getting from one task to another. One of the issues I encounter is not stopping my current task when I say I am going to. I tell myself "oh this will only take a second" or " I just need 5 minutes." Meanwhile, 30 min have passed.''',
        'date_posted': 'June 15, 2020'
    }
]

def home(request):
    context = {
    'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
