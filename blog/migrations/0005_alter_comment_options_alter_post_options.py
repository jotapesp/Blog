# Generated by Django 4.2 on 2023-04-24 20:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0004_comment_post"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="comment", options={"ordering": ["date", "post"]},
        ),
        migrations.AlterModelOptions(
            name="post", options={"ordering": ["date", "title"]},
        ),
    ]