from django.contrib import admin

from .models import Home,About,Profile,Portfolio,Workprocess,Education,Contact
#home
admin.site.register(Home)

#about
class ProfileInline(admin.TabularInline):
    model=Profile
    extra=1
@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    inlines=[
        ProfileInline
    ]
#education
admin.site.register(Education)

#portfolio
admin.site.register(Portfolio)
admin.site.register(Contact)
admin.site.register(Workprocess)


