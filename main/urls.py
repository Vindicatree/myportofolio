from django.urls import path

from main.views import (
    show_main,
    show_experience,
    show_achievements,
    create_achievements,
    get_achievements_json,
    delete_achievement,
    create_experience,
    get_experience_json,
    delete_experience,
    register,
    login_user,
    logout_user,
    toggle_star,
    toggle_achievement_star,
    create_experience_ajax,
    edit_experience,
    edit_experience_ajax,
    edit_achievement,
)

app_name = "main"

urlpatterns = [
    path("", show_main, name="show_main"),
    path("experience/", show_experience, name="show_experience"),
    path("achievements/", show_achievements, name="show_achievements"),
    path("achievements/add/", create_achievements, name="create_achievements"),
    path("api/achievements/", get_achievements_json, name="get_achievements_json"),
    path("achievements/<uuid:achievement_id>/delete/", delete_achievement, name="delete_achievement"),
    path("experience/add/", create_experience, name="create_experience"),
    path("api/experience/", get_experience_json, name="get_experience_json"),
    path("experience/<uuid:experience_id>/delete/", delete_experience, name="delete_experience"),
    path("register/", register, name="register"),
    path("login/", login_user, name="login"),
    path("logout/", logout_user, name="logout"),
    path("experience/<uuid:experience_id>/star/", toggle_star, name="toggle_star"),
    path("achievements/<uuid:achievement_id>/star/", toggle_achievement_star, name="toggle_achievement_star"),
    path("experience/add-ajax/", create_experience_ajax, name="create_experience_ajax"),
    path("experience/<uuid:experience_id>/edit/", edit_experience, name="edit_experience"),
    path("experience/<uuid:experience_id>/edit-ajax/", edit_experience_ajax, name="edit_experience_ajax"),
    path("achievements/<uuid:achievement_id>/edit/", edit_achievement, name="edit_achievement"),
]