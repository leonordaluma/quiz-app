from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from django.contrib.auth.decorators import login_required


from .models import Room, Test
from .forms import RoomForm
# Create your views here.

@login_required
def index(request):
        rooms = Room.objects.filter(creator=request.user)
        context = {'rooms': rooms}
        return render(request, 'index.html', context)

@login_required
def room(request, room_id):
     room = Room.objects.get(id=room_id)
     if room.creator != request.user:
          raise Http404

     context = {'room': room}
     return render(request, 'dashboard/room.html', context)

@login_required
def new_room(request):
    if request.method != 'POST':
        form = RoomForm()
    else:
        form = RoomForm(request.POST)
        if form.is_valid():
            new_room = form.save(commit=False)
            new_room.creator = request.user
            new_room.save()
            return HttpResponseRedirect(reverse('dashboard:index'))
    
    context = {'form': form}
    return render(request, 'dashboard/new_room.html', context)