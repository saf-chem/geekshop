from django.urls import path

import adminapp.views as adminapp

app_name = 'adminapp'

urlpatterns = [
    path(r'^users/create/$', adminapp.user_create, name='user_create'),
    path(r'^users/read/$', adminapp.users, name='users'),
    path(r'^users/update/(?P<pk>\d+)/$', adminapp.user_update, name='user_update'),
    path(r'^users/delete/(?P<pk>\d+)/$', adminapp.user_delete, name='user_delete'),
    path(r'^categories/create/$', adminapp.category_create,name='category_create'),
    path(r'^categories/read/$', adminapp.categories, name='categories'),
    path(r'^categories/update/(?P<pk>\d+)/$', adminapp.category_update, name='category_update'),
    path(r'^categories/delete/(?P<pk>\d+)/$', adminapp.category_delete, name='category_delete'),
    path('products/create/', adminapp.ProductCreateView.as_view(), name='product_create'),
    path('products/read/', adminapp.ProductListView.as_view(), name='products'),
    path('products/read/category/<int:category_pk>/', adminapp.ProductListView.as_view(), name='products_by_category'),
    path('products/read/<int:pk>/', adminapp.ProductDetailView.as_view(), name='product_read'),
    path('products/update/<int:pk>/', adminapp.ProductUpdateView.as_view(), name='product_update'),
    path('products/delete/<int:pk>/', adminapp.ProductDeleteView.as_view(), name='product_delete'),
]