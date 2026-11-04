from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsPortfolioOwnerOrReadOnly(BasePermission):
    message = "Only the portfolio owner can change projects."

    def has_permission(self, request, view):
        return (
            request.method in SAFE_METHODS
            or request.user.is_superuser
        )


class IsPortfolioOwnerOrEditorOrReadOnly(BasePermission):
    """Public reads, Editor updates, and owner-only create/delete."""

    message = "Only an Editor or portfolio owner can update experiences."

    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        user = request.user
        if not user.is_authenticated:
            return False
        if user.is_superuser:
            return True
        return (
            request.method in ("PUT", "PATCH")
            and user.groups.filter(name="Editor").exists()
        )
