# Generated by Django 2.2.1 on 2019-06-03 19:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailredirects', '0006_redirect_increase_max_length'),
        ('library', '0003_remove_libraryitem_authored_by'),
        ('magazine', '0007_auto_20190520_1941'),
        ('wagtailforms', '0003_capitalizeverbose'),
        ('wagtailcore', '0041_group_collection_permissions_verbose_name_plural'),
        ('contact', '0010_remove_meetingindexpage_body'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Contact',
        ),
    ]