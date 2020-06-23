# Generated by Django 3.0.7 on 2020-06-22 15:57

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('username_en_us', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, null=True, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('username_es', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, null=True, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('first_name_en_us', models.CharField(blank=True, max_length=30, null=True, verbose_name='first name')),
                ('first_name_es', models.CharField(blank=True, max_length=30, null=True, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('last_name_en_us', models.CharField(blank=True, max_length=150, null=True, verbose_name='last name')),
                ('last_name_es', models.CharField(blank=True, max_length=150, null=True, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='AboutpageBody',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(max_length=500, verbose_name='Description')),
                ('description_en_us', models.TextField(max_length=500, null=True, verbose_name='Description')),
                ('description_es', models.TextField(max_length=500, null=True, verbose_name='Description')),
                ('thumbnail', models.ImageField(upload_to='About', verbose_name='Thumbnail')),
            ],
            options={
                'verbose_name': 'Aboutpage Body',
                'verbose_name_plural': 'Aboutpage Body',
            },
        ),
        migrations.CreateModel(
            name='AboutpageHeading',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('main_heading', models.CharField(max_length=50, verbose_name='Main Heading')),
                ('main_heading_en_us', models.CharField(max_length=50, null=True, verbose_name='Main Heading')),
                ('main_heading_es', models.CharField(max_length=50, null=True, verbose_name='Main Heading')),
                ('sub_heading', models.TextField(blank=True, max_length=500, verbose_name='Sub Heading')),
                ('sub_heading_en_us', models.TextField(blank=True, max_length=500, null=True, verbose_name='Sub Heading')),
                ('sub_heading_es', models.TextField(blank=True, max_length=500, null=True, verbose_name='Sub Heading')),
            ],
            options={
                'verbose_name': 'Aboutpage Heading',
                'verbose_name_plural': 'Aboutpage Heading',
            },
        ),
        migrations.CreateModel(
            name='HomepageBody',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(max_length=500, verbose_name='Description')),
                ('description_en_us', models.TextField(max_length=500, null=True, verbose_name='Description')),
                ('description_es', models.TextField(max_length=500, null=True, verbose_name='Description')),
                ('thumbnail', models.ImageField(upload_to='Homepage', verbose_name='Thumbnail')),
            ],
            options={
                'verbose_name': 'Homepage Body',
                'verbose_name_plural': 'Homepage Body',
            },
        ),
        migrations.CreateModel(
            name='HomepageHeading',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('main_heading', models.CharField(max_length=50, verbose_name='Main Heading')),
                ('main_heading_en_us', models.CharField(max_length=50, null=True, verbose_name='Main Heading')),
                ('main_heading_es', models.CharField(max_length=50, null=True, verbose_name='Main Heading')),
                ('sub_heading', models.TextField(blank=True, max_length=500, verbose_name='Sub Heading')),
                ('sub_heading_en_us', models.TextField(blank=True, max_length=500, null=True, verbose_name='Sub Heading')),
                ('sub_heading_es', models.TextField(blank=True, max_length=500, null=True, verbose_name='Sub Heading')),
            ],
            options={
                'verbose_name': 'Homepage Heading',
                'verbose_name_plural': 'Homepage Heading',
            },
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('name_en_us', models.CharField(max_length=100, null=True, verbose_name='Name')),
                ('name_es', models.CharField(max_length=100, null=True, verbose_name='Name')),
                ('age', models.IntegerField(verbose_name='Age')),
                ('age_en_us', models.IntegerField(null=True, verbose_name='Age')),
                ('age_es', models.IntegerField(null=True, verbose_name='Age')),
                ('gender', models.CharField(choices=[('O', 'Others'), ('M', 'Male'), ('F', 'Female')], max_length=1, verbose_name='Gender')),
                ('gender_en_us', models.CharField(choices=[('O', 'Others'), ('M', 'Male'), ('F', 'Female')], max_length=1, null=True, verbose_name='Gender')),
                ('gender_es', models.CharField(choices=[('O', 'Others'), ('M', 'Male'), ('F', 'Female')], max_length=1, null=True, verbose_name='Gender')),
                ('contact', models.IntegerField(verbose_name='Contact')),
                ('contact_en_us', models.IntegerField(null=True, verbose_name='Contact')),
                ('contact_es', models.IntegerField(null=True, verbose_name='Contact')),
                ('agent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Customer',
                'verbose_name_plural': 'Customers',
            },
        ),
    ]
