# Generated by Django 5.0.7 on 2025-02-06 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0021_alter_gsmpmember_country_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gsmpmember',
            name='workplace_activity',
            field=models.TextField(blank=True, choices=[('საგანმანათლებო', 'საგანმანათლებო'), ('სხვა', 'სხვა'), ('ფინანსები, მარკეტინგი, გაყიდვები', 'ფინანსები, მარკეტინგი, გაყიდვები'), ('ადმინისტრაციული', 'ადმინისტრაციული'), ('კლინიკური/სამედიცინო სერვისი', 'კლინიკური/სამედიცინო სერვისი'), ('კვლევა', 'კვლევა'), ('ორივე - კლინიკური/კვლევითი', 'ორივე - კლინიკური/კვლევითი')], verbose_name='სამუშაო აქტიობა'),
        ),
    ]
