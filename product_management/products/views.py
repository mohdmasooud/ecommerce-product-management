from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator
from .models import Category, Product
from .forms import ProductForm


# 1. Login View
def user_login(request):
    if request.user.is_authenticated:
        return redirect('dashboard')

    error = None
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            error = "Invalid username or password. Please try again."

    return render(request, 'products/login.html', {'error': error})


# 2. Logout View
def user_logout(request):
    logout(request)
    return redirect('login')


# 3. Dashboard View
@login_required(login_url='login')
def dashboard(request):
    total_products = Product.objects.count()
    active_products = Product.objects.filter(status='Active').count()
    inactive_products = Product.objects.filter(status='Inactive').count()
    
    # Requirement: Stock <= 5 is Low Stock
    low_stock_products = Product.objects.filter(stock__lte=5).count()

    context = {
        'total_products': total_products,
        'active_products': active_products,
        'inactive_products': inactive_products,
        'low_stock_products': low_stock_products,
    }
    return render(request, 'products/dashboard.html', context)


# 4. Product List View (Search, Filters & Pagination)
@login_required(login_url='login')
def product_list(request):
    search_query = request.GET.get('search', '').strip()
    selected_category = request.GET.get('category', '').strip()
    selected_status = request.GET.get('status', '').strip()

    # Query all products, newest first
    products = Product.objects.all().select_related('category').order_by('-created_at')

    # Filter by Name
    if search_query:
        products = products.filter(name__icontains=search_query)

    # Filter by Category
    if selected_category:
        products = products.filter(category_id=selected_category)

    # Filter by Status
    if selected_status:
        products = products.filter(status=selected_status)

    # Pagination: 10 products per page
    paginator = Paginator(products, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    categories = Category.objects.all()

    context = {
        'page_obj': page_obj,
        'categories': categories,
        'search_query': search_query,
        'selected_category': selected_category,
        'selected_status': selected_status,
    }
    return render(request, 'products/product_list.html', context)


# 5. Add Product View
@login_required(login_url='login')
def product_add(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product added successfully!')
            return redirect('product_list')
    else:
        form = ProductForm()

    return render(request, 'products/product_form.html', {'form': form})


# 6. Edit Product View (Uses the exact same form/template as Add)
@login_required(login_url='login')
def product_edit(request, pk):
    product = get_object_or_404(Product, pk=pk)

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product updated successfully!')
            return redirect('product_list')
    else:
        form = ProductForm(instance=product)

    return render(request, 'products/product_form.html', {'form': form, 'product': product})


# 7. Delete Product View (Requires Confirmation)
@login_required(login_url='login')
def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)

    if request.method == 'POST':
        product_name = product.name
        product.delete()
        messages.success(request, f'Product "{product_name}" deleted successfully!')
        return redirect('product_list')

    return render(request, 'products/product_confirm_delete.html', {'product': product})
