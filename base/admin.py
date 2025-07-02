from base.forms import UserCreationForm
from django.contrib import admin
from base.models import Item, Category, Tag, User, Profile, Order, Contact
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin

from django import forms  # 追記
import json  # 追記
 
 
class TagInline(admin.TabularInline):
    model = Item.tags.through
 
 
class ItemAdmin(admin.ModelAdmin):
    inlines = [TagInline]
    exclude = ['tags']
 
 
class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
 
 
class CustomUserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password',)}),
        (None, {'fields': ('is_active', 'is_admin',)}),
    )
 
    list_display = ('username', 'email', 'is_active',)
    list_filter = ()
    ordering = ()
    filter_horizontal = ()
 
    add_fieldsets = (
        (None, {'fields': ('username', 'email', 'is_active',)}),
    )
 
    add_form = UserCreationForm
 
    inlines = (ProfileInline,)

class CustomJsonField(forms.JSONField):  # 追記
    def prepare_value(self, value):  # 追記
        loaded = json.loads(value)  # 追記
        return json.dumps(loaded, indent=2, ensure_ascii=False)  # 追記
 
 
class OrderAdminForm(forms.ModelForm):  # 追記
    items = CustomJsonField()  # 追記
    shipping = CustomJsonField()  # 追記
 
 
class OrderAdmin(admin.ModelAdmin):  # 追記
    form = OrderAdminForm  # 追記
    
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_at')  # 一覧で表示したい項目
    search_fields = ('name', 'email', 'message')    # 検索機能
    readonly_fields = ('name', 'email', 'message', 'created_at')  # 誤操作防止で読み取り専用

 
 
admin.site.register(Order, OrderAdmin)  # OrderAdminを追記 
admin.site.register(Item, ItemAdmin)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(User, CustomUserAdmin)
admin.site.unregister(Group)
admin.site.register(Contact, ContactAdmin)
