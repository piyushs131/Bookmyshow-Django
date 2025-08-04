from django.contrib import admin
from .models import Review

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('user', 'content_type', 'get_title', 'rating', 'created_at')
    list_filter  = ('content_type', 'rating', 'created_at')
    search_fields = ('user__username', 'movie__title', 'event__title', 'comment')

    def get_title(self, obj):
        return obj.movie.title if obj.content_type == 'movie' else obj.event.title
    get_title.short_description = 'Item Title'

