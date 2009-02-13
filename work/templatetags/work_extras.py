from django import template
register = template.Library()

@register.inclusion_tag('box.html')
def text_chunk(name,classes):
    extra_classes = classes.split(",")
    from resume.work.models import SimpleText
    chunk = SimpleText.objects.get(name=name)
    return {'chunk': chunk,"extra_classes":extra_classes}
    
text_chunk.is_safe = True

