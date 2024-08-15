# myapp/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import TextEntry
from .forms import TextEntryForm



def text_list(request):
    texts = TextEntry.objects.all()
    return render(request, 'building_site/text_list.html', {'texts': texts})



def text_new(request):
    if request.method == "POST":
        form = TextEntryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('text_list')
    else:
        form = TextEntryForm()
    return render(request, 'building_site/text_form.html', {'form': form})
    # http://localhost:8000/building_site/new/



def text_edit(request, pk):
    text_entry = get_object_or_404(TextEntry, pk=pk)
    if request.method == "POST":
        form = TextEntryForm(request.POST, instance=text_entry)
        if form.is_valid():
            form.save()
            return redirect('text_list')
    else:
        form = TextEntryForm(instance=text_entry)
    return render(request, 'building_site/text_form.html', {'form': form})