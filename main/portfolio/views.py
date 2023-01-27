from django.shortcuts import render, redirect
from .models import Project, Gallery
from .service.portfolio import get_projects
from django.views.generic import DetailView, ListView
from django.db.models import F
from django.core.mail import send_mail
from django.contrib import messages
from .forms import ContactForm


def home(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            mail = send_mail(subject=form.cleaned_data['subject'],
                             message= f"{form.cleaned_data['content']} \nfrom {form.cleaned_data['email']}",
                             from_email="orwellj@mail.ru", recipient_list=("orwellj@mail.ru",),
                             fail_silently=False)
            if mail:
                messages.success(request, 'Письмо отправлено!')
                return redirect('home')
            else:
                messages.error(request, 'Ошибка отправки')
        else:
            messages.error(request, "Данные введены некорректно!")
    else:
        form = ContactForm()
    items = get_projects()
    return render(request, 'base.html', {'items': items, 'form': form})


def get_category(request, slug):
    items = get_projects(slug=slug)
    form = ContactForm()
    return render(request, 'base.html', {'items': items, 'form': form})


class ProjectView(DetailView):
    template_name = 'portfolio/single.html'
    allow_empty = False
    context_object_name = 'item'

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
