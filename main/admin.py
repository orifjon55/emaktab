from django.contrib import admin
from .import models
from unfold.admin import ModelAdmin

@admin.register(models.School)
class School (ModelAdmin):
    list_display = ['id','fullname']
# ===============================================
@admin.register(models.Principal)
class Principal (ModelAdmin):
    list_display = ['id','fullname']
# ===============================================
@admin.register(models.Student)
class Student (ModelAdmin):
    list_display = ['id','fullname','grade']
# ===============================================
@admin.register(models.Teacher)
class Teacher (ModelAdmin):
    list_display = ['id','fullname']
# ===============================================
@admin.register(models.Rating)
class Rating (ModelAdmin):
    list_display = ['id','price']
# ===============================================
@admin.register(models.Grade)
class Grade (ModelAdmin):
    list_display = ['id','grade']
# ===============================================
@admin.register(models.Diary)
class Diary (ModelAdmin):
    list_display = ['id']
# ===============================================
@admin.register(models.TaskTable)
class TaskTable (ModelAdmin):
    list_display = ['id']
# ===============================================
@admin.register(models.Assignment)
class Assignment (ModelAdmin):
    list_display = ['id','deadline']
# ===============================================
@admin.register(models.AssignmentStatus)
class AssignmentStatus (ModelAdmin):
    list_display = ['id','completed']
# ===============================================
@admin.register(models.Family)
class Family (ModelAdmin):
    list_display = ['id','fullname']
# ===============================================
@admin.register(models.ScienceMonth)
class ScienceMont (ModelAdmin):
    list_display = ['id','body']
# ===============================================
@admin.register(models.EMaktabPayment)
class Payment (ModelAdmin):
    list_display = ['id','is_paid']