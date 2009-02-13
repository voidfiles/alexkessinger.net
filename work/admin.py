from django.contrib import admin
from resume.work.models import SimpleText,Picture,Skill,Project

class SimpleTextAdmin(admin.ModelAdmin):
    pass
class PictureAdmin(admin.ModelAdmin):
    pass
class SkillAdmin(admin.ModelAdmin):
    pass
class ProjectAdmin(admin.ModelAdmin):
    pass    
    
admin.site.register(SimpleText, SimpleTextAdmin)
admin.site.register(Picture, PictureAdmin)
admin.site.register(Skill, SkillAdmin)
admin.site.register(Project, ProjectAdmin)

