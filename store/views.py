from django.shortcuts import render, redirect, get_object_or_404
from .models import Category, Product
from .forms import CategoryForms, ProductForms



def category_list(request):
    categories = Category.object.all()
    return render(request, 'store/category_list.html', {'categories': categories})


def create_category(request):
    if request.method == 'POST':
        form = CategoryForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('category_list')
    else:
        form = CategoryForms()
        return render(request, 'cars_store/create_category.html', {'form': form})
    

def category_detail(request, pk):
    category = get_object_or_404(Category, pk=pk)
    product = Product.objects.all()
    return render(request, 'store/category_detail.html', {'category': category, 'product': product})


def create_good(request, pk):
    if request.method == 'POST':
        form = ProductForms(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('category_detail', pk=pk)
        else:
            form = ProductForms()
            return render(request, 'store/create_good.html', {'form': form})
        

def good_detail(request, c_pk, g_pk):
    good = get_object_or_404(Product, pk=g_pk)
    return render(request, 'store/good_detail.html', {'good': good, 'c_pk': c_pk})