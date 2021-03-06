from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('user', views.user, name='user'),
    path('detail/<int:alim_id>/', views.detail, name='detail'),
    path('result', views.result, name='result'),
    path('my-aliments', views.my_aliments, name='my_aliments'),
    path('legal', views.legal, name='legal'),
    path('contact', views.contact, name='contact'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('add_alim/', views.add_alim, name='add_alim'),
    path('remove_alim/', views.remove_alim, name='remove_alim'),
    path('notation/', views.notation, name='notation'),
    path('accounts/register', views.register, name="register"),
]
