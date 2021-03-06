# Generated by Django 3.2.3 on 2021-05-30 20:39

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ByUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100, verbose_name='username')),
                ('rating', models.IntegerField(default=0, verbose_name="user's answer rating")),
            ],
        ),
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, verbose_name='Title')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Date Created')),
            ],
        ),
        migrations.CreateModel(
            name='Answers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer_text', models.CharField(max_length=255, verbose_name='Answer Text')),
                ('likes', models.IntegerField(default=0, verbose_name='total likes')),
                ('dislikes', models.IntegerField(default=0, verbose_name='total dislikes')),
                ('byUser', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='faq.byuser', verbose_name='answered by')),
                ('questions', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='answers', to='faq.questions')),
            ],
            managers=[
                ('getanswer', django.db.models.manager.Manager()),
            ],
        ),
    ]
