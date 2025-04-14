from django.contrib import admin
from .models import Client, Domain

class DomainInline(admin.TabularInline):
    model = Domain
    extra = 1

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'paid_until', 'on_trial', 'created_on')
    search_fields = ('name',)
    inlines = [DomainInline]

@admin.register(Domain)
class DomainAdmin(admin.ModelAdmin):
    list_display = ('domain', 'tenant', 'is_primary')
    search_fields = ('domain',)