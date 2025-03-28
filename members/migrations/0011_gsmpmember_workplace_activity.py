# Generated by Django 5.0.7 on 2025-01-22 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0010_gsmpmember_academic_position'),
    ]

    operations = [
        migrations.AddField(
            model_name='gsmpmember',
            name='workplace_activity',
            field=models.TextField(blank=True, choices=[('ადმინისტრაციული', 'ადმინისტრაციული'), ('ფინანსები, მარკეტინგი, გაყიდვები', 'ფინანსები, მარკეტინგი, გაყიდვები'), ('საგანმანათლებო', 'საგანმანათლებო'), ('კვლევა', 'კვლევა'), ('სხვა', 'სხვა'), ('ორივე - კლინიკური/კვლევითი', 'ორივე - კლინიკური/კვლევითი'), ('კლინიკური/სამედიცინო სერვისი', 'კლინიკური/სამედიცინო სერვისი')], verbose_name='სამუშაო აქტიობა'),
        ),
    ]
