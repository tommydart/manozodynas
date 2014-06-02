from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from .forms import LoginForm
from django.contrib.auth import login

from django.views.generic import ListView, CreateView
from models import Word, Translation

def index_view(request):
    return render(request, 'manozodynas/index.html', {})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = form.cleaned_data['user']
            if user is not None and user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
    else:
        form = LoginForm()
    #import ipdb; ipdb.set_trace()
    return render(request, 'manozodynas/login.html', {'form':form})

def vote_view(request, id):
    translation = Translation.objects.get(id = id)
    translation.votes = translation.votes + 1
    translation.save()
    return HttpResponse("Sekmingai prabalsuota.")

def vote_delete_view(request, id):
    translation = Translation.objects.get(id = id)
    translation.delete()
    return HttpResponse("Vertimas sekmingai istrintas.")

def word_delete_view(request, id):
    word = Word.objects.get(id = id)
    word.delete()
    return HttpResponse("Zodis sekmingai istrintas.")

class CreateWord(CreateView):
    model = Word
    fields = ['word']
    success_url = '/'

class WordList(ListView):
    model = Word
    paginate_by = 10

class WordView(CreateView):
    model = Translation
    template_name = 'manozodynas/translation_list.html'    
    fields = ['translation']
    success_url = '/words'

    def form_valid(self, form):
        word_id = self.kwargs['id']
        word = Word.objects.get(id = word_id)
        form.instance.word = word
        return super(WordView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(WordView, self).get_context_data(**kwargs)
        word_id = self.kwargs['id']
        word = Word.objects.get(id = word_id)
        try:
            context['object_list'] = Translation.objects.filter(word = word.id)
        except:
            context['object_list'] = None
        context['word'] = word
        return context
