from django.db import models

class SimpleText(models.Model):
    """chunks of simple text"""
    name = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    text = models.TextField()
    link = models.URLField(blank=True)

    def __unicode__(self):
        return self.title
    def get_absolute_url(self):
        return "/simpletext/%s" % self.name
        
class Picture(models.Model):
    """ simple picture model"""
    from django.conf import settings
    name = models.CharField(blank=True, max_length=100)
    text = models.TextField(blank=True)
    image = models.ImageField(upload_to=settings.IMG_DIR)

       
    def __unicode__(self):
        return self.image.name
    def get_absolute_url(self):
        
        return "%s" % self.image
        
class Skill(models.Model):
    """Skils"""

    title = models.CharField(max_length=220)
    slug = models.SlugField(max_length=240)
    text = models.TextField(blank=True)
    date_added = models.DateField(auto_now_add=True)
    images = models.ManyToManyField(Picture,blank=True)

    def __unicode__(self):
        return self.title
        
    def get_absolute_url(self):
        return "/skill/%s.html" % self.slug
        
class Project(models.Model):
    """Simple model of a project"""
    
    title = models.CharField( max_length=200)
    slug = models.SlugField(max_length=240)
    short_desc = models.TextField(blank=True)
    long_desc = models.TextField(blank=True)
    start_date = models.DateField()
    end_date = models.DateField()
    images = models.ManyToManyField(Picture,blank=True)
    skills = models.ManyToManyField(Skill,blank=True)

    def __unicode__(self):
        return "%s %s - %s" % (self.title,self.start_date,self.end_date)
        

    def get_absolute_url(self):
        return "/project/%s.html" % self.slug
        


from django.db.models.signals import post_save

from staticgenerator import quick_delete

def delete(sender = None, instance = None,**kwargs):
    quick_delete(instance, '/index.html',"/")

post_save.connect(delete, sender=Skill)
post_save.connect(delete, sender=Project)
post_save.connect(delete, sender=SimpleText)



