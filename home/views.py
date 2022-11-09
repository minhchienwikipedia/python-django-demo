from django.shortcuts import render
from django.http import HttpResponse
from .models import Item

# Create your views here.

def item_search_views(request):
    query_dict = request.GET
    try:
        query = int(query_dict.get('q'))
    except:
        query = None
    obj = None
    if query is not None:
        try:
            obj = Item.objects.get(id=query)
        except Item.DoesNotExist:
            obj = None
    context = { 'item': obj }
    return render(request, 'search.html', context)


def item_create_views(request):
    context = {}
    if request.method == 'POST':
        query_dict = request.POST
        title = query_dict.get('title')
        image_url = query_dict.get('image_url')
        new_item = Item.objects.create(title=title, image_url=image_url)
        context['item'] = new_item
        context['created'] = True
    return render(request, 'create.html', context)


def index(request):
    items = Item.objects.all()
    return render(request, 'index.html', {"items": items})
