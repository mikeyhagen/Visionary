from django.db import models
from account.models import Account
from django.urls import reverse
# Create your models here.
class Project(models.Model):

    name = models.CharField(max_length=70, null=False, blank=False)
    user = models.ForeignKey(Account, related_name="projects" , on_delete=models.CASCADE)
    description = models.CharField(max_length=500,null=True,blank=True)
    target_completion = models.DateField(null=True,blank=True)
    date_created = models.DateField(verbose_name="date created", auto_now_add=True)
    completion_date = models.DateTimeField(verbose_name="completion_date", null=True,blank=True )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("project:project_detail",kwargs={'pk':self.pk})

class Stage(models.Model):
    DESIGN = "DESIGN"
    QUOTE = "QUOTE"
    DEPOSIT = "DEPOSIT"
    SCREENSHARE = "SCREENSHARE"
    DIGITAL_PROOF = "DIGITAL_PROOF"
    SAMPLE_PRODUCTION = "SAMPLE_PRODUCTION"
    WHOLESALE_PRODUCTION = "WHOLESALE_PRODUCTION"
    SHIPPING = "SHIPPING"
    STAGE_TYPE_CHOICES=[
    (DESIGN,'Design'),
    (QUOTE,'Quote'),
    (DEPOSIT,'Deposit'),
    (SCREENSHARE,'Screenshare'),
    (DIGITAL_PROOF,"Digital Proof"),
    (SAMPLE_PRODUCTION,"Sample Production"),
    (WHOLESALE_PRODUCTION,"Wholesale Production"),
    (SHIPPING,"Shipping")
    ]
    project=models.ForeignKey(Project, related_name="stages", on_delete=models.CASCADE)
    type = models.CharField(max_length=30, choices=STAGE_TYPE_CHOICES,)
    target_completion = models.DateField(null=True,blank=True)
    info = models.CharField(max_length=300, null=True,blank=True)
    completion_date = models.DateTimeField(verbose_name="completion_date", null=True,blank=True )


    def __str__(self):
        return str(self.project) + " " + str(self.type)

    def get_absolute_url(self):
        return reverse("project:project_detail",kwargs={'pk':self.project.pk})

class Stageupdate(models.Model):
    stage = models.ForeignKey(Stage, related_name="stageupdates", on_delete=models.CASCADE)
    text = models.CharField(max_length = 300, blank=False, null=False)
    date_created = models.DateField(verbose_name="date created", auto_now_add=True)

    def __str__(self):
        return str(self.stage) +" " + str(self.text[:20]) + "..."

    def get_absolute_url(self):
        return reverse("project:project_detail",kwargs={'pk':self.stage.project.pk})
