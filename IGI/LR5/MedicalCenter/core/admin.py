from django.contrib import admin
from .models import *

class ClientAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone', 'birth_date')
    search_fields = ('user__username', 'phone')

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    filter_horizontal = ('specializations', 'services')  # Добавляем services
    list_display = ('full_name', 'department', 'experience')
    search_fields = ('full_name', 'license_number')
    
    fieldsets = (
        (None, {
            'fields': ('user', 'full_name', 'photo', 'phone', 'email', 'experience')
        }),
        ('Профессиональная информация', {
            'fields': ('department', 'specializations', 'services', 'license_number')
        }),
        ('Даты', {
            'fields': ('start_date',),
            'classes': ('collapse',)
        }),
    )

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'publish_date')

# Убрали дублирующиеся модели из списка
admin.site.register([Employee, Vacancy])  # PromoCode и Review убраны

@admin.register(GlossaryTerm)
class GlossaryAdmin(admin.ModelAdmin):
    list_display = ('term', 'date_added')
    search_fields = ('term', 'definition')

# Регистрируем оставшиеся модели
admin.site.register(Client, ClientAdmin)
admin.site.register(Department)
admin.site.register(Specialization)
admin.site.register(Service)
admin.site.register(Appointment)

@admin.register(PromoCode)
class PromoCodeAdmin(admin.ModelAdmin):
    list_display = ('code', 'discount', 'valid_until', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('code',)

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('user', 'rating', 'date')
    list_filter = ('rating', 'date')