from django.urls import path, include
from django.conf import settings
from .views import (
    HomeView,
    ItemDetailView,
    add_to_cart,
    remove_from_cart,

)

app_name = "core"

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('accounts/', include('allauth.urls')),
    path('product/<slug>/', ItemDetailView.as_view(), name="product"),
    path('add-to-cart/<slug>', add_to_cart, name="add-to-cart"),
    path('remove-from-cart/<slug>', remove_from_cart, name="remove-from-cart"),

]
if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [path('__debug__/', include(debug_toolbar.urls))]
