from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from django.conf import settings
from resume.work.models import Project,Skill
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^resume/', include('resume.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
    (r'^index.html',  
        direct_to_template, {
            'template': 'base.html',
            "extra_context":{
                "projects":Project.objects.all()[0:10],
                "skills":Skill.objects.all()[0:10]
            }
        }
    ),
    
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    
)
