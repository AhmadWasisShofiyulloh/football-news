from django.shortcuts import render

def show_main(request):
    context = {
        'npm' : '2406362646',
        'name': 'Ahmad Wasis Shofiyulloh',
        'class': 'PBP C'
    }

    return render(request, "main.html", context)