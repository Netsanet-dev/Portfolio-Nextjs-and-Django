import uuid
from django.db import models
from datetime import datetime

class CommonInfo(models.Model):
    name = models.CharField(max_length=100,  blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    
    class Meta:
        abstract = True
        
class Accounts(models.Model):
    acc_name = models.CharField(max_length=20, blank=True, null=True)
    acc_link = models.URLField(max_length=80, blank=True, null=True)
    acc_email = models.EmailField(max_length=50, blank=True, null=True, unique=True) 
    
    def __str__(self):
        return self.acc_name
    
class Education(models.Model):
    sch_name = models.CharField(max_length=50)
    sch_gpa = models.FloatField("GPA", default=0.0, blank=True, null=True)
    sch_field = models.CharField('Field of Study',max_length=100)
    sch_start_date = models.DateField(default=datetime.today)
    sch_End_date = models.DateField(default=datetime.today, blank=True, null=True)
    
    def __str__(self):
        return f'{self.sch_field} at {self.sch_name}'
    
class Project(CommonInfo):
    # project = models.ForeignKey(CommonInfo, on_delete=models.CASCADE, related_name="project")
    project_date = models.DateField(auto_created=True)
    project_client = models.CharField(max_length=50, null=True, default='personal', blank=True)
    project_created_at = models.DateTimeField(auto_now_add=True)
    project_updated_at = models.DateTimeField(auto_now=True)
    project_demo_link = models.ForeignKey(Accounts, on_delete=models.CASCADE)
    project_demo_file  = models.FileField(upload_to='uploads/')
    
    class Meta:
        db_table = "project_table"
     
    def __str__(self):
        return self.project
    
class Experiance(CommonInfo):
    # exp = models.ForeignKey(CommonInfo, on_delete=models.CASCADE, related_name="experiance")
    ex_company = models.CharField(max_length=200, null=True, blank=True)
    ex_start_date = models.DateField(auto_now=True, editable=True)
    ex_end_date = models.DateField(auto_now=True, editable=True)
    
    class Meta:
        db_table = "experiance_table"
        
    def __str__(self):
        return self.ex_role
    
    
class ContactMe(CommonInfo):
    contact_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # contact = models.ForeignKey(CommonInfo, on_delete=models.CASCADE, related_name="contact")
    contact_email = models.EmailField()
    
    class Meta:
        db_table = "contact_table"
        
    def __str__(self):
        return self.contact

class AboutMe(models.Model):
    my_first_name = models.CharField(max_length=10)
    my_last_name = models.CharField(max_length=10)
    my_phone = models.IntegerField(default=0)
    my_email =  models.ForeignKey(Accounts, on_delete=models.CASCADE, related_name="about")
    my_language = models.CharField(max_length=100)
    my_nationality = models.CharField(max_length=10, blank=True, null=True)
    my_social_Media = models.ForeignKey(Accounts, on_delete=models.CASCADE, related_name="aboutme",  blank=True, null=True)
    my_desc = models.TextField(blank=True, null=True)
    last_modified = models.DateTimeField(default=datetime.today)
    
    
    def __str__(self):
        return f"{self.my_first_name} {self.my_last_name}"
    
    

class HomePage(models.Model):
    home_photo = models.ImageField(upload_to='uploads/', default=None)
    

class Services(CommonInfo):
    # service = models.ForeignKey(CommonInfo, on_delete=models.CASCADE, related_name="service")
    serv_TechStack= models.CharField("service Tech Stack", max_length=200)
    
    class Meta:
        db_table = "services_table"
        
    def __str__(self):
        return self.service
    
class Skills(CommonInfo):
    # skill = models.ForeignKey(CommonInfo, on_delete=models.CASCADE, related_name="skill")
    skill_percentage = models.IntegerField()
    
    class Meta:
        db_table = "skills_table"
        
    def __str__(self):
        return self.skill
    

