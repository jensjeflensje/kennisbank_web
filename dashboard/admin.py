from django.contrib import admin

from .models import Guild, GuildChannel, Question

admin.site.register(Guild)
admin.site.register(GuildChannel)
admin.site.register(Question)
