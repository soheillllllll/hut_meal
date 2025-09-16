from django.shortcuts import render



def header(request):
    context= {}
    return render(request, 'base/header.html', context)

def footer(request):
    context={}
    return render(request, 'base/footer.html', context)


def home_page(request):
    context={}
    return render(request, 'index.html', context)