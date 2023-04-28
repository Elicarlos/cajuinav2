from django.db import models
from tinymce.models import HTMLField
from django.utils import timezone
from django.utils.text import slugify

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, editable=False)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.id:
            # Se for uma nova instância, gera o slug
            self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

class Tag(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, editable=False)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.id:
            # Se for uma nova instância, gera o slug
            self.slug = slugify(self.name)
        super(Tag, self).save(*args, **kwargs)

class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, editable=False)
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
    )
    body = HTMLField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
        related_name='posts'
    )
    tags = models.ManyToManyField(Tag, related_name='posts')

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.id:
            # Se for uma nova instância, gera o slug
            self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def get_absolute_url(self):
        return reverse('post_detail', args=[self.published_date.year, self.published_date.month, self.published_date.day, self.slug])
