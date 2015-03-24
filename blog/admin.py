from django.contrib import admin

from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    # list view
    date_hierarchy = 'pub_date'
    list_display = (
        'title', 'pub_date', 'tag_count')
    list_filter = ('pub_date',)
    search_fields = ('title', 'text')
    # form view
    fieldsets = (
        (None, {
            'fields': (
                'title', 'slug', 'author', 'text',
            )}),
        ('Related', {
            'fields': (
                'tags', 'startups')}),
    )
    filter_horizontal = ('tags', 'startups',)
    prepopulated_fields = {"slug": ("title",)}
