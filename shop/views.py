from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required


from django.db.models import Q #used for 'or' logic to search in title and description
from django.db.models.functions import Lower
from .models import Product, Category


# Create your views here.

def shop_all(request):
    """ view for all products and sorting and searhing queries """

    products = Product.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:

        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))

            if sortkey == 'category':
                sortkey == 'category__name' # a double underscore __ allows us to drill into a related model

            if 'direction' in request.GET:
                if 'direction' == 'desc':
                    sortkey = f'-{sortkey}'         
            products = products.order_by(sortkey)


        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories) #queries in django often use __
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "you didn't search for anything DUMB DUMB")
                return redirect (reverse('products'))

            queries = Q(name__icontains = query) | Q(description__icontains = query) #the i makes things case insensitive
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
    }

    return render(request, 'shop/shop.html', context)
    