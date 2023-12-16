# Generated by Django 4.2.7 on 2023-12-07 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0003_alter_contestmodel_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grademodel',
            name='grade',
            field=models.CharField(blank=True, choices=[('Grade 1', 'Grade1'), ('Grade 2', 'Grade2'), ('Grade 3', 'Grade3'), ('Grade 4', 'Grade4'), ('Grade 5', 'Grade5'), ('Grade 6', 'Grade6'), ('Grade 7', 'Grade7'), ('Grade 8', 'Grade8'), ('Grade 9', 'Grade9'), ('Grade 10', 'Grade10'), ('Grade 11', 'Grade11'), ('Grade 12', 'Grade12')], max_length=20, unique=True),
        ),
        migrations.AlterField(
            model_name='usermodel',
            name='grade',
            field=models.CharField(choices=[('Grade 1', 'Grade1'), ('Grade 2', 'Grade2'), ('Grade 3', 'Grade3'), ('Grade 4', 'Grade4'), ('Grade 5', 'Grade5'), ('Grade 6', 'Grade6'), ('Grade 7', 'Grade7'), ('Grade 8', 'Grade8'), ('Grade 9', 'Grade9'), ('Grade 10', 'Grade10'), ('Grade 11', 'Grade11'), ('Grade 12', 'Grade12')], default='Grade 1', max_length=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='usermodel',
            name='section',
            field=models.CharField(choices=[('SECTION A', 'SECTION_A'), ('SECTION B', 'SECTION_B'), ('SECTION C', 'SECTION_C'), ('SECTION D', 'SECTION_D'), ('SECTION E', 'SECTION_E')], default='SECTION A', max_length=20),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='ContestModel',
        ),
        migrations.DeleteModel(
            name='QuestionModel',
        ),
    ]