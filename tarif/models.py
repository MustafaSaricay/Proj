from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone   

class Tarif(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
class Post(models.Model):
    
    class PostObjects(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(status='instock')
    
    options = (
        ('', 'Draft'),
        ('published', 'Published'),
    )
    status = models.CharField(
        max_length=10, choices=options, default='instock')
    tarif = models.ForeignKey(
        Tarif, on_delete=models.PROTECT, default=1)
    title = models.CharField(max_length=250)
    excerpt = models.TextField(null=True)
    content = models.TextField()
    slug = models.SlugField(max_length=250, unique_for_date='published')
    published = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='ingredient_posts')
    postobjects = PostObjects()
    objects = models.Manager()
    
    class Meta:
        ordering = ('-published',)
        
    def __str__(self):
        return self.title
    
class React(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='reacts')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    class ReactType(models.TextChoices):
        LIKE = 'LIKE', 'Like'
        LOVE = 'LOVE', 'Love'
        HAHA = 'HAHA', 'Haha'
        WOW = 'WOW', 'Wow'
        SAD = 'SAD', 'Sad'
        ANGRY = 'ANGRY', 'Angry'
        
    react_type = models.CharField(
        max_length=10, choices=ReactType.choices)
    
    def __str__(self):
        return f'{self.user} {self.react_type} {self.post}'