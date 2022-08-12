from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField('Nombre', max_length=50)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
    
    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField('Name', max_length=50)

    def __str__(self):
        return self.name


class Video(models.Model):
    title = models.CharField('Title', max_length=50)
    description = models.CharField('Description', max_length=50)
    private = models.BooleanField('Private', default=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)


    def __str__(self):
        return str(self.id) + " - " + self.title + " - " + self.description



