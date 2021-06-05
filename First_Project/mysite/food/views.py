from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Item
from .forms import ItemForm
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.template import loader


# Create your views here.
# Function based view
# def index(request):
#     item_list = Item.objects.all()
#     context = {
#         'item_list': item_list,
#     }
#     return render(request, 'food/index.html', context)


# Class based view using List View, same output as above
class IndexClassView(ListView):
    model = Item
    template_name = 'food/index.html'
    context_object_name = 'item_list'


def item(request):
    return HttpResponse('<h1>This is an item view</h1>')


# Function based view
# def detail(request, item_id):
#     item = Item.objects.get(pk=item_id)
#     context = {
#         'item': item,
#     }
#     return render(request, 'food/detail.html', context)


# Class based view using Detail View, same output as above
class FoodDetail(DetailView):
    model = Item;
    template_name = 'food/detail.html'

# Function view for create_item
# def create_item(request):
#     form = ItemForm(request.POST or None)
#
#     if form.is_valid():
#         form.save()
#         return redirect('food:index')
#
#     return render(request, 'food/item-form.html', {'form': form})


# Class based view for create_item
class CreateItem(CreateView):
    model = Item
    # Only fields in form
    fields = ['item_name', 'item_desc', 'item_price', 'item_image']
    template_name = 'food/item-form.html'

    def form_valid(self, form):
        form.instance.user_name = self.request.user
        return super().form_valid(form)


def update_item(request, id):
    item = Item.objects.get(id=id)
    form = ItemForm(request.POST or None, instance=item)

    if form.is_valid():
        form.save()
        return redirect('food:index')

    return render(request, 'food/item-form.html', {'form':form, 'item':item})


def delete_item(request, id):
    item = Item.objects.get(id=id)

    if request.method == 'POST':
        item.delete()
        return redirect('food:index')

    return render(request, 'food/item-delete.html', {'item': item})
