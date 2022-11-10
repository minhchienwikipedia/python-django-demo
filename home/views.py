from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Item
from .forms import ItemForms

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


@login_required
def item_create_views(request):
    form = ItemForms(request.POST or None)
    context = {
        "form": form
    }
    if form.is_valid():
        new_item = form.save()
        context['form'] = ItemForms()
    return render(request, 'create.html', context)


def index(request):
    items = Item.objects.all()
    return render(request, 'index.html', {"items": items})
