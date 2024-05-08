from django.contrib import admin
from .models import Profile, Skill, Education, Block, Connection, ConnectionRequest

# Register your models here.
admin.site.register(Profile)
admin.site.register(Skill)
admin.site.register(Education)
admin.site.register(Block)
admin.site.register(Connection)
admin.site.register(ConnectionRequest)