from django.db import models

# Create your models here.

#Contact Model to Store Data from Contact Page
class Contact(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=100)
    desc = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.name +" - " + self.email

#Model to store Politician Profiles
class Politician(models.Model):
    no = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to="politician", height_field=None, width_field=None, max_length=100)
    score = models.IntegerField()
    post = models.CharField(max_length=100)
    since = models.DateField()
    party = models.ForeignKey('Party', on_delete=models.CASCADE)
    slug = models.CharField(max_length=130, default="")
    status = models.BooleanField()

    def __str__(self):
        return self.name

#Model to store Politicial Party Profiles
class Party(models.Model):
    no = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    logo = models.ImageField(upload_to="party", height_field=None, width_field=None, max_length=100)
    score = models.IntegerField()
    leader = models.CharField(max_length=50)
    ruling = models.ManyToManyField('State', blank=True)
    slug = models.CharField(max_length=130, default="")
    status = models.BooleanField()

    class Meta:
        verbose_name_plural = "Parties"

    def __str__(self):
        return self.name

#State Model to Store Region of Promise Made
class State(models.Model):
    no = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

#Promise Model to Store Actual Promises
class Promise(models.Model):
    Not_Completed = 'NC'
    Completed = 'C'
    Pending = 'P'
    Abandoned = 'A'
    PROMISE_CHOICES = [
        (Not_Completed, 'Not Completed'),
        (Completed, 'Completed'),
        (Pending, 'Pending'),
        (Abandoned, 'Abandoned'),
    ]
    no = models.AutoField(primary_key=True)
    name = models.TextField()
    by = models.ForeignKey('Politician', on_delete=models.CASCADE)
    party = models.ForeignKey('Party', on_delete=models.CASCADE)
    region = models.ForeignKey('State', on_delete=models.CASCADE)
    category = models.CharField(max_length=30)
    rating = models.CharField(max_length=15, default='')
    source = models.TextField()
    slug = models.CharField(max_length=130, default="Null")
    status = models.CharField(
        max_length=2,
        choices=PROMISE_CHOICES,
        default=Not_Completed
    )
    proof = models.TextField()
    p_source = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.name 
    