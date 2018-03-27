from django.urls import path,include
from . import views
#from voltageview.views import index

#template tagging
app_name = 'voltage_view'

urlpatterns = [
    path('index/', views.index,name='index'),
    path('form/', views.VoltapiForm,name="form"),
    path('register/', views.register,name="register"),
    path('logout/',views.user_logout,name="logout"),
    path('special/',views.special,name="special"),
    path('user_login/',views.user_login,name="user_login"),
]
