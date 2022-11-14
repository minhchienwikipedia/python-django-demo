from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Item
from .forms import ItemForms
from python_settings import settings
from django.core.cache import cache


# Create your views here.

def item_search_views(request):
    query_dict = request.GET
    keyword = query_dict.get('q')
    cache_key = settings.CACHE_KEY % keyword
    item_found = cache.get(cache_key)
    print(item_found)
    if not item_found:
        try:
            query = int(keyword)
        except:
            query = None
        if query is not None:
            try:
                item_found = Item.objects.get(id=query)
                cache.set(cache_key, item_found, 86400)
            except Item.DoesNotExist:
                item_found = None
    context = {'item': item_found}
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
