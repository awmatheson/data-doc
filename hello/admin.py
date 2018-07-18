from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from .models import Profile

# Register your models here.
class ProfileInline(admin.StackedInline):
	model = Profile
	can_delete = False
	verbose_name_plural = 'profile'
	fk_name = 'user'

class CustomUserAdmin(UserAdmin):
	inlines = (ProfileInline, )
	list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'get_repository', 'get_dag_directory')
	list_select_related = ('profile', )

	def get_repository(self, instance):
		return instance.profile.repository
	get_repository.short_description = 'Repository URL'

	def get_dag_directory(self, instance):
		return instance.profile.dag_directory_name
	get_dag_directory.short_description = 'Dag Directory Name'

	def get_inline_instances(self, request, obj=None):
		if not obj:
			return list()
		return super(CustomUserAdmin, self).get_inline_instances(request, obj)


admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)