from django.db.models import Q
from django.shortcuts import render
from products.models import Product, Category
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

# Home Page View
def index(request):
    query = Product.objects.all()
    categories = Category.objects.all()
    selected_sort = request.GET.get('sort')
    selected_category = request.GET.get('category')

    if selected_category:
        query = query.filter(category__category_name=selected_category)

    if selected_sort:
        if selected_sort == 'newest':
            query = query.filter(newest_product=True).order_by('category_id')
        elif selected_sort == 'priceAsc':
            query = query.order_by('price')
        elif selected_sort == 'priceDesc':
            query = query.order_by('-price')

    page = request.GET.get('page', 1)
    paginator = Paginator(query, 20)

    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)
    except Exception as e:
        print(f"Pagination error: {e}")
        products = paginator.page(1)

    context = {
        'products': products,
        'categories': categories,
        'selected_category': selected_category,
        'selected_sort': selected_sort,
    }
    return render(request, 'home/index.html', context)


# ✅ Product Search View
def product_search(request):
    query = request.GET.get('q', '')  # "q" is the search input name from HTML form

    if query:
        products = Product.objects.filter(
            Q(product_name__icontains=query) | Q(product_name__istartswith=query)
        )
    else:
        products = Product.objects.none()

    context = {
        'query': query,
        'products': products
    }
    return render(request, 'home/search.html', context)
# Contact Page
def contact(request):
    context = {"form_id": "xgvvlrvn"}
    return render(request, 'home/contact.html', context)

# About Page
def about(request):
    return render(request, 'home/about.html')

# Terms and Conditions Page
def terms_and_conditions(request):
    return render(request, 'home/terms_and_conditions.html')

# Privacy Policy Page
def privacy_policy(request):
    return render(request, 'home/privacy_policy.html')
# Refund & Cancellation Policy Page
def refund_policy(request):
    return render(request, 'home/refund_policy.html')
def shipping_policy(request):
    return render(request, 'home/shipping_policy.html')



