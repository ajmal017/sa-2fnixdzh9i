""" App metatags """
from app_stylesheet import get_theme_color
from sa_func import get_random_str

def get_metatags(burl):
    """ xxx """
    scale = 1
    viewport = '<meta name="viewport" content="width=device-width, initial-scale='+str(scale)+'">'
    charset = '<meta charset="UTF-8" />'
    theme_color = '<meta name="theme-color" content="'+ get_theme_color() +'" />'
    favicon = '<link rel="icon" href="'+ burl +'static/favicon.ico?r='+ get_random_str(9) +'">'
    cache_control = '<meta http-equiv="Cache-control" content="public">'
    return_data = charset +\
        viewport +\
        cache_control +\
        theme_color +\
        favicon
    return return_data
