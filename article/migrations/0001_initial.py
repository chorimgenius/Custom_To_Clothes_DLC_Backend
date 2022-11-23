# Generated by Django 4.1.3 on 2022-11-23 11:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Draft',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('style', models.CharField(max_length=50)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Style',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='style/')),
            ],
        ),
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.CharField(max_length=50)),
                ('stock', models.IntegerField(default=999)),
                ('price', models.IntegerField()),
                ('color', models.CharField(max_length=50)),
                ('draft', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='draft_set', to='article.draft')),
            ],
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(max_length=255, null=True, upload_to='result/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('draft', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='article.draft')),
                ('likes', models.ManyToManyField(related_name='user_likes', to=settings.AUTH_USER_MODEL)),
                ('style', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='article.style')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
