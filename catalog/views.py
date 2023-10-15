from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.cache import cache
from django.forms import inlineformset_factory
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

from catalog.forms import ProductForm, VersionForm
from catalog.models import Product, Version, Category
from catalog.services import get_categories_cache


class HomeView(ListView):
    model = Product
    template_name = 'catalog/home.html'
    extra_context = {
        'title': 'Наш ассортимент'
    }


def contacts(request):
    return render(request, 'catalog/contacts.html')


class GoodsView(ListView):
    model = Product
    template_name = 'catalog/goods.html'
    extra_context = {
        'title': 'Наши товары'
    }


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:home')

    def form_valid(self, form):
        self.object = form.save()
        self.object.user = self.request.user
        self.object.save()

        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:home')

    def get_success_url(self):
        return reverse ('catalog:product_update', args=[self.kwargs.get('pk')])

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        VersionFormset = inlineformset_factory(Product, Version, form=VersionForm, extra=1)
        if self.request.method == 'POST':
            formset = VersionFormset(self.request.POST, instance=self.object)
        else:
            formset = VersionFormset(instance=self.object)
        context_data['formset'] = formset
        return context_data

    def form_valid(self, form):
        context_data = self.get_context_data()
        formset = context_data['formset']
        self.object = form.save()

        if formset.is_valid():
            formset.instance = self.object
            formset.save()
        return super().form_valid(form)


class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/product_detail.html'


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:home')


def categories(request):

    context = {
        'object_list': get_categories_cache(),
        'title': 'Категории товаров'
    }
    return render(request, 'catalog/categories.html', context=context)
