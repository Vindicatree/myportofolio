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
    json_response = get_achievements_json(request)

    achievements = serializers.deserialize(
        "json",
        json_response.content.decode("utf-8"),
    )
    achievements = [achievement.object for achievement in achievements]
    title_query = request.GET.get("title", "").strip()

    context = {
        "name": "Orrick",
        "achievements_list": achievements,
        "title_query": title_query,
    }
    return render(request, "achievements.html", context)

def create_achievements(request):
    form = AchievementsForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Achievement baru berhasil ditambahkan!")
        return redirect("main:show_achievements")

    context = {
        "name": "Orrick",
        "form": form,
    }
    return render(request, "achievements_form.html", context)

def get_achievements_json(request):
    title_query = request.GET.get("title", "").strip()
    achievements = Achievements.objects.all()

    if title_query:
        achievements = achievements.filter(title__icontains=title_query)

    achievements_json = serializers.serialize("json", achievements)
    return HttpResponse(achievements_json, content_type="application/json")

def delete_achievement(request, achievement_id):
    achievement = get_object_or_404(Achievements, pk=achievement_id)

    if request.method == "POST":
        achievement.delete()
        messages.success(request, "Achievement berhasil dihapus!")
        return redirect("main:show_achievements")

    return redirect("main:show_achievements")