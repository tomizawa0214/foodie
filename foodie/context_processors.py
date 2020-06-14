from .models import Area, Category

def common(request):
    context = {
        'area_list': Area.objects.all().order_by('areacode_m'),
        'category_list': Category.objects.all().order_by('category_l'),
    }
    return context