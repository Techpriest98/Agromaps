# Generated by Django 2.1.1 on 2018-12-13 20:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Corp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('email', models.EmailField(max_length=32)),
                ('phone', models.CharField(max_length=12)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('datetime', models.DateTimeField()),
                ('content', models.TextField(max_length=10000)),
            ],
        ),
        migrations.CreateModel(
            name='Preview',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('image', models.ImageField(max_length=255, upload_to='galery/')),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='preview',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='main.Preview'),
        ),
    ]