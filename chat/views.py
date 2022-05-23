from django.shortcuts import render


def random(request):
    return render(
        request, 
        'chat/basic_count.html', 
        context={'text': "Hello World!"})
