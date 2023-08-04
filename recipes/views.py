from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, FormView

from .models import Recipe, Category, SavedPost


class CustomLoginView(LoginView):
    template_name = 'recipes/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('home')


class RegisterPage(FormView):
    template_name = 'recipes/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterPage, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('home')
        return super(RegisterPage, self).get(*args, **kwargs)


class RecipeList(ListView):
    model = Recipe
    context_object_name = 'recipes'

    def get_context_data(self, **kwargs):
        cats = Category.objects.all()
        context = super().get_context_data(**kwargs)
        context['cats'] = cats
        return context


class RecipeDetail(DetailView):
    model = Recipe
    context_object_name = 'recipe'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cats = Category.objects.all()
        context['cats'] = cats
        return context


@login_required
def save_post(request, post_id):
    post_id = request.POST.get('post_id')
    post = Recipe.objects.get(pk=post_id)
    saved_post, created = SavedPost.objects.get_or_create(user=request.user, post=post)

    if not created:
        saved_post.delete()

    return redirect('recipe_detail', post_id=post_id)


class CategoryDetail(DetailView):
    model = Category
    context_object_name = 'category'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        recipes = Recipe.objects.filter(cat_id=context['category'].pk)
        cats = Category.objects.all()
        context['recipes'] = recipes
        context['cats'] = cats

        return context








