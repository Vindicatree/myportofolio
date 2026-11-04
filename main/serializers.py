from django.utils.html import strip_tags
from rest_framework import serializers

from main.models import Experience


class ExperienceSerializer(serializers.ModelSerializer):
    star_count = serializers.SerializerMethodField()
    is_starred = serializers.SerializerMethodField()
    starred_by_names = serializers.SerializerMethodField()

    class Meta:
        model = Experience
        fields = [
            "id", "title", "description", "category",
            "thumbnail", "started_at", "ended_at", "starred_by",
            "star_count", "is_starred", "starred_by_names",
        ]
        read_only_fields = ["id"]

    def validate_title(self, value):
        value = strip_tags(value).strip()
        if not value:
            raise serializers.ValidationError("Title cannot be empty.")
        return value

    def validate_description(self, value):
        return strip_tags(value)

    def validate_tech_stack(self, value):
        return strip_tags(value)

    def update(self, instance, validated_data):
        many_to_many = {}
        for field in instance._meta.many_to_many:
            if field.name in validated_data:
                many_to_many[field.name] = validated_data.pop(field.name)

        for field_name, value in validated_data.items():
            setattr(instance, field_name, value)

        if validated_data:
            instance.save(update_fields=list(validated_data))

        for field_name, value in many_to_many.items():
            getattr(instance, field_name).set(value)

        return instance

    def get_star_count(self, obj):
        return obj.starred_by.count()

    def get_is_starred(self, obj):
        request = self.context.get("request")
        if request is None or not request.user.is_authenticated:
            return False
        return request.user in obj.starred_by.all()

    def get_starred_by_names(self, obj):
        return ", ".join(user.username for user in obj.starred_by.all())
