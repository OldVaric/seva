
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect


from .models import Articles
from .forms import ArticlesForm


from django.views.generic import DetailView, UpdateView, ListView
from django.db.models import Q

# Create your views here.

class NewsView(ListView):
    model = Articles
    queryset = Articles.objects.order_by('-date')
    paginate_by = 2
    template_name = 'news/news_home.html'
    context_object_name = "news"
#def news_home(request):
#    news = Articles.objects.order_by('-date')
#    return render(request, 'news/news_home.html', {'news': news})


class Search(ListView):
    paginate_by = 2
    template_name = 'news/search.html'
    context_object_name = "result"

    def get_queryset(self):
        return Articles.objects.filter(Q(title__icontains=self.request.GET.get('q')))

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['q'] = self.request.GET.get('q')
        return context


class NewsDV(LoginRequiredMixin, DetailView):
    model = Articles
    template_name = 'news/details_view.html'
    context_object_name = 'article'

    raise_exception = True


class NewsUV(LoginRequiredMixin, UpdateView):
    model = Articles
    template_name = 'news/create.html'

    form_class = ArticlesForm

    raise_exception = True


def create(request):
    error = ''
    if request.method == 'POST':
        form = ArticlesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('news_home')
        else:
            error = 'Форма была неверной'

    form = ArticlesForm()

    data = {
        'form': form,
        'error': error
    }

    return render(request, 'news/create.html', data, )
