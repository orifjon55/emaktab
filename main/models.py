from django.db import models
from django.contrib.auth.models import AbstractUser,User
from django.core.exceptions import ValidationError
from django.utils.timezone import now

class School(models.Model):  # Maktab
    fullname = models.CharField(
        max_length=100, 
        verbose_name="Maktab nomi", 
        help_text="Maktabning to‘liq nomini kiriting (masalan, Andijon 1-maktabi)."
    )
    about = models.TextField(
        verbose_name="Maktab haqida", 
        blank=True, 
        help_text="Maktab haqida qisqacha ma’lumot."
    )
    established_year = models.PositiveIntegerField(
        verbose_name="Tashkil etilgan yil", 
        null=True, 
        blank=True, 
        help_text="Maktab tashkil etilgan yili (masalan, 1995)."
    )
    principal_name = models.CharField(
        max_length=50, 
        verbose_name="Direktor ismi", 
        blank=True, 
        help_text="Maktab direktorining to‘liq ismi."
    )
    address = models.CharField(
        max_length=200, 
        verbose_name="Manzil", 
        blank=True, 
        help_text="Maktab manzili (masalan, Andijon, Izboskan tumani)."
    )
    phone_number = models.CharField(
        max_length=15, 
        verbose_name="Telefon raqami", 
        blank=True, 
        help_text="Maktab telefon raqami (masalan, +998901234567)."
    )
    email = models.EmailField(
        verbose_name="Elektron pochta", 
        blank=True, 
        help_text="Maktabning elektron pochta manzili."
    )
    is_active = models.BooleanField(
        default=True, 
        verbose_name="Faolmi?", 
        help_text="Maktab faol yoki faol emasligini belgilaydi."
    )

    class Meta:
        verbose_name = "Maktab"
        verbose_name_plural = "Maktablar"
        ordering = ['fullname']

    def __str__(self):
        return f"Name:{self.fullname}"

    def get_contact_info(self):
        return f"Telefon: {self.phone_number or 'Mavjud emas'}, Email: {self.email or 'Mavjud emas'}"

    def get_full_address(self):
        return self.address or "Manzil kiritilmagan"
    
    class Meta:
        ordering = ['-id']
# ===============================================    
class Rating(models.Model):  #baho
    price = models.CharField(max_length=30)

    def __str__(self):
        return self.price
    
    class Meta:
        ordering = ['-id']
# ===============================================
class Grade(models.Model): #sinf
    grade = models.CharField(max_length=10)
    
    def __str__(self):
        return self.grade
    
    class Meta:
        ordering = ['-id']
# ===============================================
class Diary(models.Model): #kundalik
    rating = models.ManyToManyField(Rating)

    def __str__(self):
        return str (self.rating)
    
    class Meta:
        ordering = ['-id']
# ===============================================
class TaskTable(models.Model): #dars jadvali
    table = models.FileField(upload_to='table/') 

    def __str__(self):
        return str(self.table) 
    
    class Meta:
        ordering = ['-id']
# ===============================================
class Principal(models.Model): #zamdiriktor
    fullname = models.CharField(max_length=100)
    create_data = models.DateField(auto_now_add=True)
    table = models.ManyToManyField(TaskTable)


    def __str__(self):
        return self.fullname
    
    class Meta:
        ordering = ['-id']
# ===============================================   
class Student(models.Model): #o'quvchi
    fullname = models.CharField(max_length=150)
    age = models.PositiveIntegerField()
    interest = models.TextField()
    grade = models.ForeignKey(Grade,on_delete=models.SET_NULL,null=True)
    school = models.ForeignKey(School,on_delete=models.SET_NULL,null=True)
    diary = models.ForeignKey(Diary,on_delete=models.CASCADE,null=True)
    tasktable = models.ForeignKey(TaskTable,on_delete=models.CASCADE,null=True)
    
    def __str__(self):
     return f"Fullname: {self.fullname}"
    
    def clean(self):
        if self.age > 18:
            raise ValidationError("O'quvchi 18 yoshdan kichik bo'lishi kerak.")
    
    class Meta:
        ordering = ['-id']
# ===============================================
class Teacher(models.Model): #oqituvchi
    fullname = models.CharField(max_length=50)
    grade = models.ForeignKey(Grade,on_delete=models.CASCADE,null=True)
    lessontable = models.FileField(upload_to='lesson_table/') 
    lesson = models.FileField(upload_to='lesson_table/') 
    tasktable = models.ManyToManyField(TaskTable)
    subject = models.CharField(max_length=100)

    def __str__(self):
        return self.fullname
    
    class Meta:
        ordering = ['-id']
# ===============================================
class Assignment(models.Model):  # Vazifa modeli
    student = models.ManyToManyField(Student)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='assignments')
    title = models.CharField(max_length=200)
    description = models.TextField()
    deadline = models.DateField()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-id']
# ===============================================
class AssignmentStatus(models.Model):  # Vazifa holati modeli
    student = models.ForeignKey(Student, on_delete=models.CASCADE)  # Yagona talaba
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE)  # Yagona vazifa
    completed = models.BooleanField(default=False)

    def __str__(self):
        return (
            f"{self.student.fullname} - {self.assignment.title} - "
            f"{'Bajarildi' if self.completed else 'Bajarilmagan'}"
        )

    def clean(self):
        # Bir talaba uchun bir xil vazifa allaqachon mavjudligini tekshirish
        if AssignmentStatus.objects.filter(student=self.student, assignment=self.assignment).exists():
            raise ValidationError(
                f"{self.student.fullname} uchun '{self.assignment.title}' vazifasi allaqachon mavjud."
            )

    class Meta:
        ordering = ['-id']
        unique_together = ('student', 'assignment')  # Bir talaba uchun bitta vazifa faqat bir marta qayd etiladi
# ===============================================   
class Family(models.Model): #ota ona
    fullname = models.CharField(max_length=100)
    student = models.ManyToManyField(Student)
    rating = models.ForeignKey(Rating, on_delete=models.CASCADE, null=True)
    school = models.ForeignKey(School,on_delete=models.CASCADE, null=True)
    assignment = models.ManyToManyField(AssignmentStatus)
    teacher = models.ManyToManyField(Teacher)
    principal = models.ForeignKey(Principal, on_delete=models.CASCADE, null=True)
    tasktable = models.ManyToManyField(TaskTable)
    diary = models.ForeignKey(Diary, on_delete=models.CASCADE, null = True)
    grade = models.ForeignKey(Grade, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.fullname
    
    class Meta:
        ordering = ['-id']
# ===============================================
class AuditLog(models.Model):  #Xatolik
    action_type = models.CharField(max_length=50)
    action_description = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
# ===============================================
def get_science_month(): #oylik fanlar
    science_month = {
        'yanvar': 'ona tili',
        'fevral': 'matematika',
        'mart': 'fizika',
        'aprel': 'kimyo',
        'may': 'biologiya',
        'iyun': 'informatika',
        'iyul': 'tarix',
        'avgust': 'geografiya',
        'sentyabr': 'adabiyot',
        'oktyabr': 'ijtimoiy fanlar',
        'noyabr': 'chet tili',
        'dekabr': 'sanʼat'
    }
    return [(key, value) for key, value in science_month.items()]
# ===============================================
class ScienceMonth(models.Model):
    MONTH_CHOICES = get_science_month()

    body = models.CharField(
        max_length=20,
        choices=MONTH_CHOICES,
        verbose_name="Oylik fan"
    )

    def __str__(self):
        return self.body

    class Meta:
        ordering = ['-id']
# ===============================================
class EMaktabPayment(models.Model): #tolov emaktab
    school = models.ForeignKey(
        School,on_delete=models.SET_NULL,null=True
    )
    
    student = models.ForeignKey(
        Student,on_delete=models.SET_NULL,null=True
    )

    email = models.EmailField(
        verbose_name="Elektron pochta",
        help_text="Foydalanuvchining elektron pochta manzili."
    )
    phone_number = models.CharField(
        max_length=15,
        verbose_name="Telefon raqami",
        blank=True,
        help_text="Foydalanuvchining telefon raqami (masalan, +998901234567)."
    )
    is_paid = models.BooleanField(
        default=False,
        verbose_name="Pul to'langanmi?",
        help_text="To'lov holatini belgilaydi."
    )
