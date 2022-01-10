from django.contrib import admin
from apps.base.models import CustomUser, Worker, Store, Visit


@admin.register(CustomUser)
class UserAdmin(admin.ModelAdmin):
    list_display = ["id", "username"]
    search_fields = ["id", "username"]

    model = CustomUser


@admin.register(Worker)
class WorkerAdmin(admin.ModelAdmin):
    list_display = ["name", "phone"]
    search_fields = ["name", "phone"]

    model = Worker


@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    list_display = ["worker", "title"]
    search_fields = ["worker", "title"]
    autocomplete_fields = ("worker",)

    model = Store


@admin.register(Visit)
class VisitAdmin(admin.ModelAdmin):
    list_display = ["store", "date", "latitude", "longitude"]
    search_fields = ["store", "date", "latitude", "longitude"]
    readonly_fields = ["store", "date", "latitude", "longitude"]

    model = Visit
    save_as_continue = False

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False
