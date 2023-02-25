from django.urls import path
from . import views

urlpatterns = [
    # path('', views.home),
    
    # throttle check
    path('throttle', views.throttle_check),

    # Category endpoints
    path('category', views.category),
    path('category/<int:id>', views.category_single),

    # Menu-items endpoints
    path('menu-items', views.menuitems),
    path('menu-items/<int:id>', views.menuitems_single),

    # User group management endpoints
    path('groups/manager/users', views.manager_set),
    path('groups/manager/users/<int:pk>', views.manager_delete),
    path('groups/delivery-crew/users', views.delivery_set),
    path('groups/delivery-crew/<int:pk>', views.delivery_delete),

    # Cart management endpoints 
    path('cart/menu-items', views.cart),

    # Order management endpoints
    path('orders', views.order),
    path('orders/<int:id>', views.order_single),

    # test for admin access
    path('admin/users', views.manager_admin),
    # test for serialization of Group
    path('admin/group', views.group_view),
]