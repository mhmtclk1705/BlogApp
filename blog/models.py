from sre_constants import CATEGORY
from django.db import models
from django.contrib.auth.models import User



class Post(models.Model):
    STATUS = (
        (0,"Draft"),
        (1,"Publish")
    )
    CATEGORY = (
        ("FE","Frontend"),
        ("BE","Backend"),
        ("FS","Fullstack"),
    )
    title = models.CharField(max_length=200, unique=True)
    content = models.TextField()
    image = models.ImageField(upload_to='images',blank=True)
    author = models.ForeignKey(User, on_delete= models.CASCADE)
    publish_date = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now= True)
    category = models.CharField(choices=CATEGORY, default="FS",blank=True, max_length=50)
    status = models.IntegerField(choices=STATUS, default=0)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    # views = models.IntegerField(default=0)
    # comments = models.IntegerField(default=0)
    # likes = models.ManyToManyField(User, related_name='blog_posts')
    

    
    class Meta:
        ordering = ['publish_date']

    def __str__(self):
        return self.title
    
    def views_count(self):
        return self.postview_set.all().count()

    def comment_count(self):
        return self.comment_set.all().count()

    def like_count(self):
        return self.like_set.all().count()



class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    time_stamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField()

    def __str__(self):
        return self.content

class PostView(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    time_stamp = models.DateTimeField(auto_now_add=True)
    # views = models.IntegerField(default=0)

    def __str__(self):
        return self.post.title

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return self.post.title

