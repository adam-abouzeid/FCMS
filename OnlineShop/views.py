from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Product, Order, OrderItem, User, Payment, Refund
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

@login_required  # Requires authentication to access this view
def product_list(request):
    if not Product.objects.exists():
        # If products don't exist, create them using the provided data
           create_products()

    # Retrieve all products from the database
    products = Product.objects.all()

    # Sorting
    sort_by = request.GET.get('sort_by')
    if sort_by == 'name':
        products = products.order_by('name')
    elif sort_by == 'price':
        products = products.order_by('price')
    elif sort_by == 'name_desc':
        products = products.order_by('-name')
    elif sort_by == 'price_desc':
        products = products.order_by('-price')

    # Pagination
    paginator = Paginator(products, 10)  # Show 10 products per page
    page = request.GET.get('page')
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page
        products = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g., 9999), deliver last page of results
        products = paginator.page(paginator.num_pages)

    # Render the template with the context
    return render(request, 'shop.html', {'products': products})


def create_products():
    from .models import Category, Product
    import os
    from django.core.files import File
   
    categories_data = ['Official Jerseys', 'Fan Collection', 'Scarves','Training Collection']

    products_data = [
            {'name': 'RBLZ JERSEY 23/24', 'description': 'Official away team jersey', 'price': 94.95,'category': 'Official Jerseys', 'image_path': 'static\images\RBLZ-Jersey-23-24 - Shortcut.lnk'},
            {'name': 'RBL NIKE HOME JERSEY 23/24', 'description': 'Official home team jersey', 'price': 94.95,'category': 'Official Jerseys', 'image_path': 'static\images\RBL-Nike-Home-Jersey-23-24 - Shortcut.lnk'},
            {'name': 'RBL YOUTH JUMP BULLI T-SHIRT', 'description': 'RB Leipzig Bulli T-Shirt for youth', 'price': 19.95,'category': 'Fan Collection', 'image_path': 'static\images\RB Leipzig Shop_ RBL Youth Jump Bulli T-Shirt _ only here at redbullshop.com - Shortcut.lnk'},
            {'name': 'DFB POKAL', 'description': 'Cup won in 2022 and 2023', 'price': 79.95,'category': 'Fan Collection',  'image_path': 'static\images\pokal - Shortcut.lnk'},
            {'name': 'RBL Fan Beanie Navy', 'description': 'Hat with team colors and logo', 'price': 19.95,'category': 'Fan Collection', 'image_path': 'static\images\cap - Shortcut.lnk'},
            {'name': 'RB Leipzig 2024 - Fanplanner', 'description': 'Fan plans for the year', 'price': 12.95,'category': 'Fan Collection', 'image_path': 'static\images\RB-Leipzig-2024-Fanplanner - Shortcut.lnk'}, 
            {'name': 'RBL Simons Player Scarf', 'description': 'RB Leipzig Simons Player Scarf', 'price': 17.95,'category': 'Scarves', 'image_path': 'static\images\simonsscarf - Shortcut.lnk'},
            {'name': 'RBL Winter Scarf 2023', 'description': 'RB Leipzig Winter Scarf', 'price': 17.95, 'category': 'Scarves','image_path': 'static\images\winterscarf - Shortcut.lnk'},
            {'name': 'RBL Dark Scarf', 'description': 'RB Leipzig dark Scarf', 'price': 18.95,'category': 'Scarves', 'image_path': 'static\images\die roten - Shortcut.lnk'},
            {'name': 'RBL Nike Pro Training Longsleeve 23/24', 'description': 'Pro Training Longsleeve for men by Nike', 'price': 64.95,'category': 'Training Collection', 'image_path': 'static\images\jacket - Shortcut.lnk'},
            {'name': 'RBL Nike Leipzig T-Shirt 23/24', 'description': 'Leipzig T-Shirt for men by Nike', 'price': 34.95, 'category': 'Training Collection','image_path': 'static\images\leipzig nike - Shortcut.lnk'},
            {'name': 'RBL Nike Training T-Shirt 23/24', 'description': 'Leipzig T-Shirt for men by Nike', 'price': 44.95, 'category': 'Training Collection','image_path': 'static\images\RBL-Nike-Training-T-Shirt-23-24 - Shortcut.lnk'},
            {'name': 'RBL Nike Training T-Shirt 23/24', 'description': 'Training T-Shirt for women by Nike', 'price': 44.95, 'category': 'Training Collection','image_path': 'static\images\training woman - Shortcut.lnk'},     
            {'name': 'RBL Nike Training Shorts 23/24', 'description': 'Training Shorts for men by Nike', 'price': 39.95,'category': 'Training Collection', 'image_path': 'static\images\shorts men - Shortcut.lnk'},
            {'name': 'RBL Nike Training Shorts 23/24', 'description': 'Training Shorts for women by Nike', 'price': 39.95,'category': 'Training Collection', 'image_path': 'static\images\shortswoman - Shortcut.lnk'}

    ]
    
        # Create categories    
    for category_name in categories_data:
        Category.objects.create(name=category_name)

    # Retrieve all categories
    categories = Category.objects.all()

    # Loop through products_data and create Product instances
    for product_data in products_data:
        # Assuming you have a Category object named 'Football' for football-related products
        category = Category.objects.get(name='Football')

        product = Product.objects.create(
            name=product_data['name'],
            description=product_data['description'],
            price=product_data['price'],
            category=category
        )

        # Assign image to product
        image_path = product_data['image_path']
        if os.path.exists(image_path):
            with open(image_path, 'rb') as f:
                product.image.save(os.path.basename(image_path), File(f))
        print("More products and categories for a football team generated successfully!")         


@login_required
def add_to_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    order, created = Order.objects.get_or_create(user=request.user, complete=False)
    order_item, created = OrderItem.objects.get_or_create(order=order, product=product)

    if not created:
        order_item.quantity += 1
        order_item.save()

    return redirect('cart')

@login_required
def remove_from_cart(request, order_item_id):
    order_item = OrderItem.objects.get(id=order_item_id)
    if order_item.quantity > 1:
        order_item.quantity -= 1
        order_item.save()
    else:
        order_item.delete()
    return redirect('cart')

@login_required
def cart(request):
    order = Order.objects.get(user=request.user, complete=False)
    order_items = order.orderitem_set.all()
    return render(request, 'football_shop/cart.html', {'order': order, 'order_items': order_items})

@login_required
def checkout(request):
    order = Order.objects.get(user=request.user, complete=False)
    if request.method == 'POST':
        # Process payment (you need to implement this part using a payment gateway like Stripe or PayPal)
        payment = Payment.objects.create(user=request.user, amount=order.get_cart_total())
        order.complete = True
        order.save()
        messages.success(request, f'Payment successful! Your order has been placed.')
        return redirect('home')
    return render(request, 'football_shop/checkout.html', {'order': order})

@login_required
def request_refund(request):
    if request.method == 'POST':
        order_id = request.POST.get('order_id')
        reason = request.POST.get('reason')
        order = Order.objects.get(id=order_id)
        refund = Refund.objects.create(order=order, reason=reason)
        refund.save()
        messages.info(request, f'A refund request has been submitted for order {order_id}.')
        return redirect('profile')
    return render(request, 'football_shop/request_refund.html')
# Create your views here.


def Shop_Main(request):
    products = Product.objects.all()
    for product in products:
        if product.image:
            product.image_url = product.image.url
        else:
            product.image_url = None  # Or a default placeholder image path
    return render(request, 'OnlineShop/shop.html', {'products': products})