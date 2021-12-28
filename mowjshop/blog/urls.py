from django.urls import path, register_converter
from . import views
from django.urls.converters import SlugConverter


app_name = 'blog'


class PersianSlugConvertor(SlugConverter):
    regex = '[-0-9 ا-ی]+'


register_converter(PersianSlugConvertor, 'persian_slug')


urlpatterns = [
    #Post views
    path('', views.post_mowj, name='post_mowj' ),
    path('<int:year>/<int:month>/<int:day>/<persian_slug:slug>/', views.post_detail, name='post_detail')
]