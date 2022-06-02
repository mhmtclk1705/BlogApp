from django.db.models.signals import pre_save
from django.dispatch import receiver
from blog.models import Post
from django.template.defaultfilters import slugify
from .utils import get_random_code

@receiver(pre_save, sender=Post)
def create_slug(sender,instance,**kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.title+' '+get_random_code())


