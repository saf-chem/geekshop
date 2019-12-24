from django.contrib.auth.mixins import UserPassesTestMixin
from django.shortcuts import HttpResponseRedirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView
from django.views.generic.list import ListView
from mainapp.models import Product, ProductCategory
from .forms import ProductAdminForm


class IsSuperUserView(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_superuser


class ProductListView(IsSuperUserView, ListView):
    model = Product
    template_name = 'adminapp/products.html'
    queryset = Product.objects.all()

    def get_queryset(self):
        queryset = super(ProductListView, self).get_queryset()
        category_pk = self.kwargs.get('category_pk')
        if category_pk:
            category = get_object_or_404(ProductCategory, pk=category_pk)
            queryset = queryset.filter(category=category)
        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProductListView, self).get_context_data(**kwargs)
        context['title'] = 'Продукты'
        context['categories'] = ProductCategory.objects.all()
        return context


class ProductDetailView(IsSuperUserView, DetailView):
    model = Product
    template_name = 'adminapp/product.html'




class ProductCreateView(IsSuperUserView, CreateView):
    model = Product
    template_name = 'admin/product_update.html'
    success_url = reverse_lazy('admin_custom:products')
    fields = '__all__'


class ProductDeleteView(IsSuperUserView, DeleteView):
    model = Product
    template_name = 'adminapp/product_delete.html'
    success_url = reverse_lazy('admin_custom:products')


class ProductUpdateView(IsSuperUserView, UpdateView):
    model = Product
    template_name = 'adminapp/product_update.html'
    fields = '__all__'
    success_url = reverse_lazy('admin_custom:products')
    form_class = ProductAdminForm

    def get_success_url(self):
        return reverse_lazy('admin_custom:product_read', kwargs={'pk': self.kwargs.get('pk')})
