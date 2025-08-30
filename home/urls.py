from django.urls import path
from .views import index, product_search, contact, about, terms_and_conditions, privacy_policy, refund_policy, shipping_policy


urlpatterns = [
    path('', index, name='index'),
    path('search/', product_search, name='product_search'),
    path('contact/', contact, name='contact'),
    path('about/', about, name='about'),
    path('terms/', terms_and_conditions, name='terms-and-conditions'), 
    path('privacy/', privacy_policy, name='privacy-policy'),
    path('refund/', refund_policy, name='refund-policy'),
    path('shipping/', shipping_policy, name='shipping-policy'),

  

]
