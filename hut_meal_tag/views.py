from django.shortcuts import render

from hut_meal_tag.models import Tag


# Create your views here.




def list_tags(request):
    print("1")
    list_tags = Tag.objects.all()
    print(list_tags)
    context = {"list_tags": list_tags}
    return render(request, 'list_tag.html', context)
