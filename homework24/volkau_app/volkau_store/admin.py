from django.contrib import admin
from volkau_store.models import Category, Games

# Register your models here.

class GamesInCategory(admin.StackedInline):
    model = Games

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'view_game', 'show_average')
    inlines = (
        GamesInCategory,
    )

    @admin.display(description='games')
    def view_game(self,obj):
        from django.utils.html import format_html
        from django.urls import reverse
        from django.utils.http import urlencode
        count = obj.games_set.count()
        url = (
            reverse('admin:volkau_store_games_changelist')
            + '?'
            + urlencode({'category_id': f'{obj.id}'})
        )
        return format_html('<a href="{}">{} Games</a>', url, count)

    @admin.display(description='avg price')
    def show_average(self, obj):
        from django.db.models import Avg
        result = Games.objects.filter(category=obj).aggregate(Avg('price'))
        return result['price__avg']

@admin.register(Games)
class GamesAdmin(admin.ModelAdmin):
    date_hierarchy = 'release_date'
    list_editable = ('release_date',)
    sortable_by = ('name', 'release_date', 'full_price')
    list_filter = ('category',)
    search_fields = ('category__title', 'name')
    list_display = (
        'name',
        'game_img',
        'release_date',
        'full_price'
    )

    actions = ('export_as_csv', )

    @admin.display(description='price')
    def full_price(self, obj):
        return f'{obj.price} $'
    
    @admin.display(description='image')
    def game_img(self,obj):
        from django.utils.html import mark_safe
        return mark_safe(f'<img src="{obj.game_image.url}" width="150px" height="200px"/>')


    @admin.action(description="Download table")
    # def export_as_csv(self, request, queryset):
    #     from django.core import serializers
    #     from django.http import FileResponse
    #     import io
    #     from datetime import datetime

    #     csvdata = list(serializers.serialize('csv', queryset).encode('utf-8'))
    #     response = FileResponse(
    #         io.BytesIO(csvdata),
    #         as_attachment=True,
    #         filename=f'file-{datetime.now()}.csv'
    #     )
    #     return response
    def export_as_csv(self, request, queryset):
        import csv
        from django.http import HttpResponse

        meta = self.model._meta
        field_names = [field.name for field in meta.fields]

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
        writer = csv.writer(response)

        writer.writerow(field_names)
        for obj in queryset:
            row = writer.writerow([getattr(obj, field) for field in field_names])

        return response