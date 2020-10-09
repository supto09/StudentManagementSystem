# Register your models here.
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group

from apps.accounts.forms import UserAdminChangeForm, UserAdminCreationForm, TeacherAdminCreationForm, \
    StudentCreationForm, StudentAdminChangeForm, TeacherAdminChangeForm
from apps.accounts.models import User, Teacher, Student


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = UserAdminChangeForm
    add_form = UserAdminCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('email', 'type', 'admin')
    list_filter = ('admin',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        # ('Personal info', {'fields': ()}),
        ('Permissions', {'fields': ('admin',)}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'type', 'password1', 'password2')}
         ),
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ["email"]
    search_fields = ('email',)
    ordering = ('email',)

    def get_form(self, request, obj=None, **kwargs):
        # Proper kwargs are form, fields, exclude, formfield_callback
        if obj:
            self.form = TeacherAdminChangeForm
        else:
            self.form = TeacherAdminCreationForm
        return super(TeacherAdmin, self).get_form(request, obj, **kwargs)


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ["email"]
    search_fields = ('email',)
    ordering = ('email',)
    
    def get_form(self, request, obj=None, **kwargs):
        # Proper kwargs are form, fields, exclude, formfield_callback
        if obj:
            self.form = StudentAdminChangeForm
        else:
            self.form = StudentCreationForm
        return super(StudentAdmin, self).get_form(request, obj, **kwargs)


# Remove Group Model from admin. We're not using it.
admin.site.unregister(Group)
