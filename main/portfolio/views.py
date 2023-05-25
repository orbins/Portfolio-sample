from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from django.db.models import F
from django.shortcuts import render, redirect, reverse
from django.views.generic import DetailView, ListView, FormView

from .forms import ContactForm
from .models import Project, Gallery
from .services import get_projects


class HomeView(FormView):
    form_class = ContactForm
    template_name = 'base.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['items'] = get_projects()
        return context

    def form_valid(self, form):
        mail = send_mail(
            subject=form.cleaned_data['subject'],
            message=(
                f"{form.cleaned_data['content']} "
                f"\nfrom {form.cleaned_data['name']}, "
                f"{form.cleaned_data['email']}"),
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=(settings.EMAIL_HOST_USER, ),
            fail_silently=False
        )
        if mail:
            messages.success(self.request, "Сообщение успешно отправлено")
        else:
            messages.error(self.request, "Данные введены некорректно!")
        return redirect('home')


def get_category(request, slug):
    items = get_projects(slug=slug)
    form = ContactForm()
    return render(request, 'base.html', {'items': items, 'form': form})


class ProjectView(DetailView):
    template_name = 'portfolio/single.html'
    allow_empty = False
    context_object_name = 'item'

    # Обычно фильтрация происходит благодаря методу get_absolute_url в модели, он определяет адрес конкретного объекта
    # Но здесь я не определял, model
    def get_queryset(self):
        return Project.objects.select_related('category').only('title', 'content', 'image', 'views','category__slug',
                                                               'category__title').filter(slug=self.kwargs['slug'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        project = self.get_queryset()[0]
        project.views = F('views') + 1
        project.save()
        context['photos'] = Gallery.objects.filter(project=project.id) #/pk
        return context


class ProjectByTag(ListView):
    template_name = 'base.html'
    allow_empty = False
    context_object_name = 'items'

    def get_queryset(self):
        return Project.objects.only('slug', 'image').filter(tags__slug=self.kwargs['slug']).prefetch_related('tags')
