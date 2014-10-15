from site_options import models as optmodels


def global_vars(request):
    shop_name = optmodels.Setting.objects.get(key='shop_name')
    footer_text = optmodels.Setting.objects.get(key='footer_text')
    return {
        'shop_name': shop_name,
        'footer_text': footer_text,
    }

