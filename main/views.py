from django.shortcuts import render

from main.models import Experience, Achievements


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