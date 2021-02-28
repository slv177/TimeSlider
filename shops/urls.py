from django.urls import path
from shops import views

urlpatterns = [
    path('', views.contactPage), # FBV
    path('ajax/contact', views.postContact, name ='contact_submit'),
    path('map/', views.MapView.as_view()),
    path('user', views.userPanel),
    path('ajax/get_user_info', views.getUserInfo, name = 'get_user_info'),
]