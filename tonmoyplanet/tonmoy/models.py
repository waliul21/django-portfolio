from django.db import models


#Home section
class Home(models.Model):
    name=models.CharField(max_length=250)
    greetings_1=models.CharField(max_length=250)
    greetings_2=models.CharField(max_length=250)
    hire_me=models.URLField(max_length=200,blank=True)
    contact_me=models.URLField(max_length=200,blank=True)
    picture=models.ImageField(upload_to='picture/')
    updated=models.DateTimeField( auto_now=True)

    def __str__(self):
        return self.name
#about section
class About(models.Model):
    heading=models.CharField(max_length=250)
    expeirence = models.CharField(max_length=250)
    description=models.TextField(blank=False)
    profile_img=models.ImageField(upload_to='profile/')
    updated=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.expeirence
class Profile(models.Model):
    about=models.ForeignKey(About,on_delete=models.CASCADE)
    social_name=models.CharField(max_length=250)
    link=models.URLField(max_length=200)
    

#to do list
class Workprocess(models.Model):
    name=models.CharField(max_length=50)
    heading=models.CharField(max_length=50)
    heading_1=models.CharField(max_length=50)
    description_1=models.TextField()
    heading_2=models.CharField(max_length=50)
    description_2=models.TextField()
    heading_3=models.CharField(max_length=50)
    description_3=models.TextField()
    heading_4=models.CharField(max_length=50)
    description_4=models.TextField()
    updated=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
#skills section
class Category(models.Model):
    name=models.CharField(max_length=250)
    updated=models.DateTimeField(auto_now=True)
    class Meta():
        verbose_name='Skill'
        verbose_name_plural='Skills'

    def __str__(self):
        return self.name
#RESUME START



class Portfolio(models.Model):
    image=models.ImageField(upload_to='portfolio/')
    link=models.URLField(max_length=200)


    def __str__(self):
        return f'portfolio{self.id}'


class Education(models.Model):
    fname=models.CharField(max_length=50)
    school=models.CharField(max_length=50)
    school_description=models.TextField()
    school_time=models.DateTimeField()
    collage=models.CharField(max_length=50)
    collage_description=models.TextField()
    collage_time=models.DateTimeField()
    university=models.CharField(max_length=50)
    university_description=models.TextField()
    university_time=models.DateTimeField()
    webdesign=models.CharField(max_length=50)
    web_description=models.TextField()
    webdesign_time=models.DateTimeField()
    webdevelopment=models.CharField(max_length=50)
    webdevelopment_description=models.TextField()
    webdevelopment_time=models.DateTimeField()
    updated=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.fname


class Contact(models.Model):
    cname=models.CharField(max_length=50)
    address=models.CharField(max_length=50)
    phone=models.IntegerField(blank=True)
    gmail=models.URLField(max_length=200,blank=True)
    facebook=models.URLField(max_length=200,blank=True)
    youtube=models.URLField(max_length=200,blank=True)
    github=models.URLField(max_length=200,blank=True)
    linkdin=models.URLField(max_length=200,blank=True)
    instra=models.URLField(max_length=200,blank=True)
    author_name=models.CharField(max_length=50,blank=True)
    updated=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.cname