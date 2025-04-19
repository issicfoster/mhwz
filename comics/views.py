
from django.shortcuts import render, redirect, get_object_or_404
from .models import Comic
from .forms import ComicForm

def comic_list(request):
    comics = Comic.objects.all()
    return render(request, 'comics/comic_list.html', {'comics': comics})

def comic_detail(request, pk):
    comic = get_object_or_404(Comic, pk=pk)
    return render(request, 'comics/comic_detail.html', {'comic': comic})

def comic_create(request):
    if request.method == 'POST':
        form = ComicForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('comic_list')
    else:
        form = ComicForm()
    return render(request, 'comics/comic_form.html', {'form': form})

def comic_update(request, pk):
    comic = get_object_or_404(Comic, pk=pk)
    if request.method == 'POST':
        form = ComicForm(request.POST, request.FILES, instance=comic)
        if form.is_valid():
            form.save()
            return redirect('comic_detail', pk=comic.pk)
    else:
        form = ComicForm(instance=comic)
    return render(request, 'comics/comic_form.html', {'form': form})

def comic_delete(request, pk):
    comic = get_object_or_404(Comic, pk=pk)
    if request.method == 'POST':
        comic.delete()
        return redirect('comic_list')
    return render(request, 'comics/comic_confirm_delete.html', {'comic': comic})
    

# Create your views here.
