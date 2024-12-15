from django.shortcuts import render

from django.shortcuts import render


def index(request):
    context = {
        'title' : 'Главная страница',
        'user' : 'Ivan',
    }
    return render(request, 'products/index.html', context=context)


def products(request):
    context = {
        'title' : 'Товары',
        'products' : [
            {
                'image': '/static/vendor/img/products/Blue-jacket-The-North-Face.png',
                'name': 'Синяя куртка The North Face',
                'price': '23 725,00',
                'description': 'Гладкая ткань. Водонепроницаемое покрытие. Легкий и теплый пуховый наполнитель.',
            },
            {
                'image': '/static/vendor/img/products/Brown-sports-oversized-top-ASOS-DESIGN.png',
                'name': 'Коричневый спортивный oversized-топ ASOS DESIGN',
                'price': '3 390,00',
                'description': 'Материал с плюшевой текстурой. Удобный и мягкий.',

            },
            {
                'image': '/static/vendor/img/products/Adidas-hoodie.png',
                'name': 'Худи черного цвета с монограммами adidas Originals',
                'price': '6 090,00',
                'description': 'Мягкая ткань для свитшотов. Стиль и комфорт – это образ жизни.',

            },
        ]
    }
    return render(request, 'products/products.html', context=context)