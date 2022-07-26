# Generated by Django 4.0.6 on 2022-08-07 04:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0004_video_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Nombre')),
            ],
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Categoría', 'verbose_name_plural': 'Categorías'},
        ),
        migrations.AddField(
            model_name='video',
            name='tags',
            field=models.ManyToManyField(to='videos.tag'),
        ),
    ]
