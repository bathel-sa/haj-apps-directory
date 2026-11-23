from django.contrib import admin
from config.admin_locale import ArabicAdminLabels
from .models import AssistantConversation


@admin.register(AssistantConversation)
class AssistantConversationAdmin(ArabicAdminLabels, admin.ModelAdmin):
    list_display = ['session_id', 'lang', 'selected_app', 'created_at']
    list_filter = ['lang', 'created_at']
    readonly_fields = ['session_id', 'created_at']
