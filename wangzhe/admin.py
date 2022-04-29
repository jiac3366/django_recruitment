from django.contrib import admin

# Register your models here.
from .models import HerosPlay, Heros


class ReadOnlyAdmin(admin.ModelAdmin):  # 目的:禁止掉Django后台的一些增删改功能
    readonly_fields = []  # 此列表中的字段都是只读的

    def get_list_display(self, request):  # 不用每个一个个写啦草！全部展示！
        return [field.name for field in self.model._meta.concrete_fields]

    def get_readonly_fields(self, request, obj=None):  # 加到readonly_fields
        return list(self.readonly_fields) + \
               [field.name for field in obj._meta.fields] + \
               [field.name for field in obj._meta.many_to_many]  # 追加

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False


# @admin.register(Heros)
# class HeroAdmin(ReadOnlyAdmin):
#     search_fields = ('name', 'role_main',)
#
#
# @admin.register(HerosPlay)
# class HerosPlayAdmin(ReadOnlyAdmin):
#     def get_list_display(self, request):  # 不用每个一个个写啦草！全部展示！
#         filter_field = [field.name for field in self.model._meta.concrete_fields]
#         filter_field.remove('game_id')
#         return filter_field

    # exclude = ('game_id', 'creator_id')
    # list_display = (
    #     'hero_name', 'game_id', 'player_name', 'kda_k', 'kda_d', 'kda_a', 'money', 'damage_input', 'damage_output',
    #     'win')
