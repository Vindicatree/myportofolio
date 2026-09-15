from django.shortcuts import render
from django.contrib import messages
from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from main.models import Experience, Achievements
from main.forms import AchievementsForm


def show_main(request):
    context = {
        "name": "Nathanael Orrick Hatmoko",
        "npm": "2506592125",
        "study_program": "S1 Ilmu Komputer",
        "bio": (
            "An active computer science student at Universitas Indonesia, thriving to learn and "
            "experiment more about AI and software. Dedicated to building practical solutions "
            "like student mobility apps and competing in high-intensity development hackathons, "
            "while balancing technical rigor. "
        ),
    }
    return render(request, "index.html", context)


def show_experience(request):
    context = {
        "name": "Nathanael Orrick Hatmoko",
        "experience_list": Experience.objects.all(),
    }
    return render(request, "experience.html", context)

def show_achievements(request):
    context = {
        "name": "Nathanael Orrick Hatmoko",
        "achievements_list": Achievements.objects.all(),
    }
    return render(request, "achievements.html", context)

def create_achievements(request):
    form = AchievementsForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Proyek baru berhasil ditambahkan!")
        return redirect("main:show_achievements")

    context = {
        "name": "Orrick",
        "form": form,
    }
    return render(request, "achievements_form.html", context)
