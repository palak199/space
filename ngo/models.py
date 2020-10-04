from django.db import models
from django.contrib.auth.models import User
# Create your models here.


ngo_scope=(
    ('rural','rural'),
    ('urban','urban'),
    ('national','national'),
    ('international','international'),
)

class Ngo(models.Model):
    user        = models.OneToOneField(User, on_delete=models.CASCADE)
    name        = models.CharField(max_length=35)
    objective   = models.CharField(max_length=50)
    description = models.TextField()    
    scope       = models.CharField(max_length=30,choices=ngo_scope)
    reg_no      = models.IntegerField()
    website     = models.URLField()
    email       = models.EmailField()
    contribution= models.TextField()
    image     = models.ImageField(default = 'ngo_default.jpg',upload_to= 'images/ngo')


choices = (
    ('not at all','not at all'),
    ('to some extent','to some extent'),
    ('a lot','a lot'),

)     
travel  = (
    ('public','public'),
    ('private','private'),
    ('carpool','carpool'),
)
diet = (
    ('veg','veg'),
    ('non_veg','non_veg'),
    ('mostly veg','mostly veg'),
)
yes_no = (
    ('yes','yes'),
    ('no','no'),
)

energy = (
    ('conventional','conventional'),
    ('non_conventional','non_conventional'),
    ('mix','mix'),
)
waste = (
    ('recyclabe','recyclabe'),
    ('non_recyclabe','non_recyclabe'),
    ('partial_recyclable','partial_recyclable'),
    ('nearly_null','nearly_null'),
)

water = (
    ('River/lake','River/lake'),
    ('Ground water','Ground water'),
    ('Rain water','Rain water'),
    ('Municipal water','Municipal water'),
)
effluent = (
    ('air','air'),
    ('water','water'),
    ('soil','soil'),
    ('not_applied','not_applied')
)
effluent_q =(
    ('>50%','>50%'),
    ('30%','30%'),
    ('20%','20%'),
    ('5%','5%'),
    ('1%','1%'),

)


class Individual(models.Model):
    user         = models.OneToOneField(User, on_delete=models.CASCADE)
    tank_cap     = models.IntegerField(default=0)
    member       = models.IntegerField(default=0)
    garbage      = models.TextField(max_length=30,choices=choices)
    waste_water  = models.TextField(max_length=30,choices=choices)
    biodegradable= models.TextField(max_length=30,choices=choices)
    recycle      = models.TextField(max_length=35,choices=choices)
    govt         = models.TextField(max_length=35 ,choices=choices)
    disposal     = models.TextField(max_length=35,choices=choices)
    energy       = models.TextField(max_length=35,choices=choices)
    bulb         = models.TextField(max_length=30,choices=yes_no)
    cfc          = models.TextField(max_length=35,choices=yes_no)
    news         = models.TextField(max_length=35 ,choices=yes_no)
    plant        = models.TextField(max_length=35,choices=yes_no)
    travel       = models.TextField(max_length=30,choices=travel)
    diet         = models.TextField(max_length=35 , choices=diet)


class Industry(models.Model):

    user                = models.OneToOneField(User, on_delete=models.CASCADE)
    name                = models.CharField(max_length=50)
    turnover            = models.IntegerField()

    pollution           = models.CharField(max_length=35, choices=yes_no)
    sustainibility      = models.CharField(max_length=35, choices=yes_no)
    csr_def             = models.CharField(max_length=35, choices=yes_no)
    plant               = models.CharField(max_length=35,choices=yes_no)
    untreated_sewage    = models.CharField(max_length=35,choices=yes_no)
    emp_month           = models.CharField(max_length=35,choices=yes_no)
    env_audit           = models.CharField(max_length=35,choices=yes_no)

    garbage             = models.CharField(max_length=35,choices=choices)
    employment          = models.CharField(max_length=35,choices=choices)
    health              = models.CharField(max_length=35,choices=choices)
    recycle             = models.CharField(max_length=35,choices=choices)
    responsibility      = models.CharField(max_length=35,choices=choices)
    energy              = models.CharField(max_length=35,choices=energy)
    water_source        = models.CharField(max_length=35,choices=water)
    effluent            = models.CharField(max_length=35,choices=effluent) 
    effluent_q          = models.CharField(max_length=35,choices=effluent_q)
    nature_waste        = models.CharField(max_length=35,choices=waste)