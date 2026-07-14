from django.urls import path
from .import views

urlpatterns = [
    path('', views.guest , name='guest'),
    path('home/', views.home , name='home'),
    path('registration/', views.registration , name='registration'),
    path('login/', views.login , name='login'),
    path('logout', views.logout , name='logout'),
    path('about/', views.about , name='about'),
    path('productdetail/<int:pk>', views.productdetail , name='productdetail'),
    path('search', views.search , name='search'),
    path('add_to_cart/', views.add_to_cart , name='add_to_cart'),
    path('feedback/', views.feedback , name='feedback'),
    path('show_cart/', views.show_cart , name='show_cart'),
    path('show_cart/update/', views.update_cart, name='update_cart'),
    path('show_cart/remove/', views.remove_cart_item, name='remove_cart_item'),
    path('show_cart/checkout/', views.checkout, name='checkout'),
    path('show_cart/checkout/orderdetails/', views.orderdetails, name='orderdetails'),
    path('receipe/', views.receipe, name='receipe'),
    # path('createcheckoutsession/', views.createcheckoutsession, name='createcheckoutsession'),
    path('success/', views.success, name='success'),
    path('cancel/', views.cancel, name='cancel'),
    path('inquirys/', views.inquirys, name='inquirys'),
    path('deletes/', views.deletes, name='deletes'),
    # path('delete/<str:order_id>/', views.delete_order, name='delete_order'),
]
