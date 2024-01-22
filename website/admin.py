from django.contrib import admin

from website.models import Country, Category, Trainer ,Course


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ["name"]
    list_filter = ["name"]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name"]
    list_filter = ["name"]


@admin.register(Trainer)
class TrainerAdmin(admin.ModelAdmin):
    list_display = ["first_name", "last_name", "category",]
    list_filter = ["category"]


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ["title", "country", "course_date", "category",]
    list_filter = ["category", "country"]
