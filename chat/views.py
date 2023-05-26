from django.shortcuts import render, redirect
from .models import Room, Message
from django.http import HttpResponse, JsonResponse


def home(request):
    title = "Home"
    return render(request, "home.html", {"title": title})


def room(request, room):
    title = "Room-" + room
    username = request.GET.get("username")
    room_details = Room.objects.get(name=room)

    return render(
        request,
        "room.html",
        {
            "title": title,
            "room_details": room_details,
            "username": username,
            "room": room,
        },
    )


def checkview(request):
    room = request.POST["room_name"]
    username = request.POST["username"]

    if Room.objects.filter(name=room).exists():
        return redirect("/" + room + "/?username=" + username)
    else:
        new_room = Room.objects.create(name=room)
        return redirect("/" + room + "/?username=" + username)

def send(request):
    message = request.POST["message"]
    username = request.POST["username"]
    room_id = request.POST["room_id"]
    message_room = Room.objects.get(id=room_id)

    new_message = Message.objects.create(value=message,user=username, room=message_room)
    new_message.save()

    return HttpResponse("Message sent successfull")

def getMessages(request, room):
    room_details = Room.objects.get(name=room)
    messages = Message.objects.filter(room=room_details)

    return JsonResponse({"messages":list(messages.values())})