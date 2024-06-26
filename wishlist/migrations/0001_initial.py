# Generated by Django 5.0.2 on 2024-03-01 00:17

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('member', '0002_auto_20240301_0005'),
        ('teenplay_server', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Wishlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('is_private', models.BooleanField(default=1)),
                ('wishlist_content', models.TextField()),
                ('status', models.BooleanField(default=1)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='teenplay_server.category')),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='member.member')),
            ],
            options={
                'db_table': 'tbl_wishlist',
            },
        ),
        migrations.CreateModel(
            name='WishListLike',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('status', models.BooleanField(default=1)),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='member.member')),
                ('wishlist', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='wishlist.wishlist')),
            ],
            options={
                'db_table': 'tbl_wishlist_like',
            },
        ),
        migrations.CreateModel(
            name='WishlistReply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('reply_content', models.TextField()),
                ('status', models.BooleanField(default=1)),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='member.member')),
                ('wishlist', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='wishlist.wishlist')),
            ],
            options={
                'db_table': 'tbl_wishlist_reply',
            },
        ),
        migrations.CreateModel(
            name='WishlistTag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('tag_name', models.TextField()),
                ('status', models.BooleanField(default=1)),
                ('wishlist', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='wishlist.wishlist')),
            ],
            options={
                'db_table': 'tbl_wishlist_tag',
            },
        ),
    ]
