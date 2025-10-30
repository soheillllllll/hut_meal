from django.contrib import admin

from hut_meal_menu.models import Menu, Meals

# Register your models here.
class MenuAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'get_categories', 'get_meals', 'price']

    def get_categories(self, obj):
        return "\n".join([p.title for p in obj.categories.all()])

    def get_meals(self, obj):
        return "\n".join([p.title for p in obj.meals.all()])


    class Meta:
        Model = Menu


admin.site.register(Menu, MenuAdmin)
admin.site.register(Meals)