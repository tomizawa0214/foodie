from django.views.generic import TemplateView

GNAVI_URL = "https://api.gnavi.co.jp/RestSearchAPI/v3/"
GNAVI_KEY = "c217fca9b867dc74d2e68d3ec67af7f8"

class IndexView(TempplateView):
    template_name = 'foodie.index.html'