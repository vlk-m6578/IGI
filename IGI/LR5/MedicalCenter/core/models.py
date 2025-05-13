from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, RegexValidator, MaxValueValidator
from django.core.exceptions import ValidationError
import datetime
from django.db import models
from django.utils import timezone

class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    phone = models.CharField(
        max_length=20,
        validators=[
            RegexValidator(
                regex=r'^\+375 \(\d{2}\) \d{3}-\d{2}-\d{2}$',
                message="Номер должен быть в формате +375 (29) XXX-XX-XX"
            )
        ]
    )
    birth_date = models.DateField()
    address = models.TextField()
    
    @property
    def age(self):
        return (datetime.date.today() - self.birth_date).days // 365
    
    def clean(self):
        if self.age < 18:
            raise ValidationError("Клиент должен быть старше 18 лет")

class Department(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

class Specialization(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    specializations = models.ManyToManyField(Specialization)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    license_number = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='doctors/', blank=True, null=True)  # Добавили фото
    experience = models.PositiveIntegerField(verbose_name="Опыт работы (лет)")  # Новое поле
    full_name = models.CharField(max_length=200, verbose_name="Полное ФИО")  # Новое поле
    start_date = models.DateField(verbose_name="Дата начала практики", default=timezone.now)  # Для автоматического расчета стажа
    services = models.ManyToManyField(
        'Service',
        related_name='doctors',
        verbose_name='Оказываемые услуги'
    )
    phone = models.CharField(
        max_length=20,
        validators=[
            RegexValidator(
                regex=r'^\+375\(\d{2}\)\d{3}-\d{2}-\d{2}$',
                message="Номер должен быть в формате +375 (29) XXX-XX-XX"
            )
        ],
        verbose_name="Телефон"
    )
    email = models.EmailField(verbose_name="Email")

    @property
    def experience_calculated(self):
        """Автоматический расчет стажа на основе даты начала"""
        today = timezone.now().date()
        delta = today - self.start_date
        return delta.days // 365

    def __str__(self):
        return self.full_name

class Service(models.Model):
    name = models.CharField(max_length=200, verbose_name="Название")
    short_description = models.CharField(
        max_length=200, 
        verbose_name="Краткое описание"
    )
    full_description = models.TextField(verbose_name="Полное описание")
    price = models.DecimalField(
        max_digits=10, 
        decimal_places=2, 
        verbose_name="Стоимость"
    )
    duration = models.DurationField(verbose_name="Продолжительность")
    
    def duration_formatted(self):
        total_seconds = int(self.duration.total_seconds())
        hours = total_seconds // 3600
        minutes = (total_seconds % 3600) // 60
        return f"{hours:02d}:{minutes:02d}" if hours > 0 else f"{minutes} мин."

    def __str__(self):
        return self.name

class Appointment(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    date_time = models.DateTimeField()
    services = models.ManyToManyField(Service)

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)])
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

class PromoCode(models.Model):
    code = models.CharField(max_length=20, unique=True, verbose_name="Код")
    discount = models.PositiveIntegerField(verbose_name="Скидка (%)")
    valid_until = models.DateField(verbose_name="Действует до")
    is_active = models.BooleanField(default=True, verbose_name="Активен")

    class Meta:
        ordering = ['-valid_until']
        verbose_name = 'Промокод'
        verbose_name_plural = 'Промокоды'

    def __str__(self):
        return f"{self.code} ({self.discount}%)"

class News(models.Model):
    title = models.CharField(max_length=200)
    short_content = models.CharField(max_length=200)
    full_content = models.TextField()
    image = models.ImageField(upload_to='news/')
    publish_date = models.DateTimeField(auto_now_add=True)

class GlossaryTerm(models.Model):
    term = models.CharField(max_length=200, verbose_name="Термин")
    definition = models.TextField(verbose_name="Определение")
    date_added = models.DateField(auto_now_add=True, verbose_name="Дата добавления")

    class Meta:
        ordering = ['-date_added']
        verbose_name = 'Термин'
        verbose_name_plural = 'Глоссарий'

    def __str__(self):
        return self.term

class Employee(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='employees/')
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    description = models.TextField()

class Vacancy(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date_posted = models.DateField(auto_now_add=True)