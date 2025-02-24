# Generated by Django 5.0.7 on 2025-02-06 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0022_alter_gsmpmember_workplace_activity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gsmpmember',
            name='workplace_activity',
            field=models.TextField(blank=True, choices=[('ორივე - კლინიკური/კვლევითი', 'ორივე - კლინიკური/კვლევითი'), ('ადმინისტრაციული', 'ადმინისტრაციული'), ('ფინანსები, მარკეტინგი, გაყიდვები', 'ფინანსები, მარკეტინგი, გაყიდვები'), ('კვლევა', 'კვლევა'), ('კლინიკური/სამედიცინო სერვისი', 'კლინიკური/სამედიცინო სერვისი'), ('სხვა', 'სხვა'), ('საგანმანათლებო', 'საგანმანათლებო')], verbose_name='სამუშაო აქტიობა'),
        ),
    ]
