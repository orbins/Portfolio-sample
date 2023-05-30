from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from django.db.models import F
from django.shortcuts import redirect
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.generic import DetailView, ListView, FormView

from .forms import ContactForm
from .models import Project, Gallery
from .services import get_projects


@method_decorator(cache_page(60 * 5), name='dispatch')
class HomeView(FormView):
    """
    View для домашней страницы
    """
    form_class = ContactForm
    template_name = 'base.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['items'] = get_projects()
        return context

    def form_valid(self, form):
        send_mail(
            subject=form.cleaned_data['subject'],
            message=(
                f"{form.cleaned_data['content']} "
                f"\nfrom {form.cleaned_data['name']}, "
                f"{form.cleaned_data['email']}"),
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=(settings.TO_EMAIL,),
            fail_silently=False
        )
        messages.success(self.request, "Сообщение успешно отправлено")
        return redirect('home')

    def form_invalid(self, form):
        messages.error(self.request, "Данные введены некорректно!")
        return super().form_invalid(form)


@method_decorator(cache_page(60 * 5), name='dispatch')
class CategoryView(FormView):
    """
    View для отображения проектов по категории
    """
    form_class = ContactForm
    template_name = 'base.html'

    def get_context_data(self, **kwargs):
        slug = self.kwargs['slug']
        context = super().get_context_data(**kwargs)
        context['items'] = get_projects(slug=slug)
        return context


@method_decorator(cache_page(60 * 15), name='dispatch')
class ProjectView(DetailView):
    """
    View для отображения отдельного проекта
    """
    template_name = 'portfolio/single.html'
    allow_empty = False
    context_object_name = 'item'
    model = Project

    def get_object(self):
        return Project.objects.select_related(
            'category').only(
                'title', 'content',
                'image', 'views',
                'category__slug',
                'category__title'
            ).get(
                slug=self.kwargs['slug']
            )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        project = self.get_queryset()[0]
        project.views = F('views') + 1
        project.save()
        context['photos'] = Gallery.objects.filter(
                                project=project.id)
        return context


@method_decorator(cache_page(60 * 5), name='dispatch')
class ProjectByTag(ListView):
    """
    View для отображения проектов по тегу
    """
    template_name = 'base.html'
    allow_empty = False
    context_object_name = 'items'

    def get_queryset(self):
        return Project.objects.only(
            'slug', 'image').filter(
                tags__slug=self.kwargs['slug']).prefetch_related(
                    'tags')
