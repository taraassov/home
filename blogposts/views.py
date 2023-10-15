from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from pytils.templatetags.pytils_translit import slugify

from blogposts.models import Blogpost


class BlogpostCreateView(LoginRequiredMixin, CreateView):
    model = Blogpost
    fields = ('title', 'content')
    success_url = reverse_lazy('blogposts:list')

    def form_valid(self, form):
        if form.is_valid():
            new_mat = form.save()
            new_mat.slug = slugify(new_mat.title)
            new_mat.save()

        return super().form_valid(form)


class BlogpostUpdateView(LoginRequiredMixin, UpdateView):
    model = Blogpost
    fields = ('title', 'content')
    success_url = reverse_lazy('blogposts:list')

    def form_valid(self, form):
        if form.is_valid():
            new_mat = form.save()
            new_mat.slug = slugify(new_mat.title)
            new_mat.save()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse('blogposts:view', args=[self.kwargs.get('pk')])


class BlogpostListView(ListView):
    model = Blogpost

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(is_published=True)
        return queryset


class BlogpostDetailView(DetailView):
    model = Blogpost

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_count += 1
        self.object.save()
        return self.object


class BlogpostDeleteView(LoginRequiredMixin, DeleteView):
    model = Blogpost
    success_url = reverse_lazy('blogposts:list')