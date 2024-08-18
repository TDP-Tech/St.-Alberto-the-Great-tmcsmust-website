from django.db import models
from django_ckeditor_5.fields import CKEditor5Field
from AuthenticationApp.models import TmcsMember

# Choices for Gender field
GENDER_CHOICES = [
    ('MALE', 'Male'),
    ('FEMALE', 'Female'),
]
# Choices for Gender field
SACRAMENT_CHOICES = [
    ('nimepata', 'NIMEPATA'),
    ('sijapata', 'SIJAPATA'),
]
# Choices for Education Level field
EDUCATION_LEVEL_CHOICES = [
    ('O-level', 'O-level'),
    ('A-level', 'A-level'),
    ('Veta', 'Veta'),
    ('Diploma', 'Diploma'),
    ('Bachelor', 'Bachelor'),
]
# Choices for Courses field
COURSES_CHOICES = [
    ('Doctor of Philosophy in Information Science and Engineering', 'Doctor of Philosophy in Information Science and Engineering'),
    ('Doctor of Philosophy in Mechanical Engineering', 'Doctor of Philosophy in Mechanical Engineering'),
    ('Doctor of Philosophy in Civil Engineering', 'Doctor of Philosophy in Civil Engineering'),
    ('Postgraduate Diploma in Technical Education', 'Postgraduate Diploma in Technical Education'),
    ('Masters of Science in Civil Engineering', 'Masters of Science in Civil Engineering'),
    ('Master of Engineering in Renewable Energy', 'Master of Engineering in Renewable Energy'),
    ('Masters of Science in Energy Engineering', 'Masters of Science in Energy Engineering'),
    ('Masters of Science in Information Technology', 'Masters of Science in Information Technology'),
    ('Masters of Engineering in Clean Energy Technology', 'Masters of Engineering in Clean Energy Technology'),
    ('Masters of Biodiversity Conservation', 'Masters of Biodiversity Conservation'),
    ('Bachelor of Computer Engineering', 'Bachelor of Computer Engineering'),
    ('Bachelor of Electrical and Electronics Engineering', 'Bachelor of Electrical and Electronics Engineering'),
    ('Bachelor of Mechanical Engineering', 'Bachelor of Mechanical Engineering'),
    ('Bachelor of Technology in Architecture', 'Bachelor of Technology in Architecture'),
    ('Bachelor of Civil Engineering', 'Bachelor of Civil Engineering'),
    ('Bachelor of Business Administration', 'Bachelor of Business Administration'),
    ('Bachelor of Laboratory Sciences and Technology', 'Bachelor of Laboratory Sciences and Technology'),
    ('Bachelor of Science with Education', 'Bachelor of Science with Education'),
    ('Bachelor of Engineering in Telecommunication Systems', 'Bachelor of Engineering in Telecommunication Systems'),
    ('Bachelor of Computer Science', 'Bachelor of Computer Science'),
    ('Bachelor of Science in Information and Communication Technology', 'Bachelor of Science in Information and Communication Technology'),
    ('Bachelor of Technology in Landscape Architecture', 'Bachelor of Technology in Landscape Architecture'),
    ('Bachelor of Technical Education in Electrical and Electronics Engineering', 'Bachelor of Technical Education in Electrical and Electronics Engineering'),
    ('Bachelor of Technical Education in Mechanical Engineering', 'Bachelor of Technical Education in Mechanical Engineering'),
    ('Bachelor of Technical Education in Civil Engineering', 'Bachelor of Technical Education in Civil Engineering'),
    ('Bachelor of Technical Education in Architectural Technology', 'Bachelor of Technical Education in Architectural Technology'),
    ('Bachelor of Engineering in Data Science', 'Bachelor of Engineering in Data Science'),
    ('Bachelor of Food Science and Technology', 'Bachelor of Food Science and Technology'),
    ('Bachelor of Science in Natural Resources Conservation', 'Bachelor of Science in Natural Resources Conservation'),
    ('Bachelor of Agribusiness Management and Technology', 'Bachelor of Agribusiness Management and Technology'),
    ('Diploma in Architecture', 'Diploma in Architecture'),
    ('Diploma in Biomedical Equipment Engineering', 'Diploma in Biomedical Equipment Engineering'),
    ('Diploma in Business Administration', 'Diploma in Business Administration'),
    ('Diploma in Civil Engineering', 'Diploma in Civil Engineering'),
    ('Diploma in Computer Engineering', 'Diploma in Computer Engineering'),
    ('Diploma in Electrical and Electronic Engineering', 'Diploma in Electrical and Electronic Engineering'),
    ('Diploma in Electronics and Telecommunication Engineering', 'Diploma in Electronics and Telecommunication Engineering'),
    ('Diploma in Highway Engineering', 'Diploma in Highway Engineering'),
    ('Diploma in Mechanical Engineering', 'Diploma in Mechanical Engineering'),
    ('Diploma in Mechatronics Engineering', 'Diploma in Mechatronics Engineering'),
    ('Diploma in Mining Engineering', 'Diploma in Mining Engineering'),
    ('Diploma in Computer Science', 'Diploma in Computer Science'),
    ('Diploma in Information and Communication Technology', 'Diploma in Information and Communication Technology'),
    ('Diploma in Laboratory Science and Technology', 'Diploma in Laboratory Science and Technology'),
    ('Diploma in Food Science and Technology', 'Diploma in Food Science and Technology'),
    ('Diploma in Agribusiness with Technology', 'Diploma in Agribusiness with Technology'),
    ('Diploma in Mechanical Engineering with Industrial Safety and Occupational Health', 'Diploma in Mechanical Engineering with Industrial Safety and Occupational Health'),
    ('Diploma of Technical Education in Civil Engineering', 'Diploma of Technical Education in Civil Engineering'),
    ('Diploma of Technical Education in Electrical and Electronics Engineering', 'Diploma of Technical Education in Electrical and Electronics Engineering'),
    ('Diploma of Technical Education in Architectural Technology', 'Diploma of Technical Education in Architectural Technology'),
    ('Diploma of Technical Education in Mechanical Engineering', 'Diploma of Technical Education in Mechanical Engineering'),
    ('Diploma of Business Administration in Accounting and Finance', 'Diploma of Business Administration in Accounting and Finance'),
    ('Diploma of Business Administration in Marketing and Entrepreneurship', 'Diploma of Business Administration in Marketing and Entrepreneurship'),
    ('Diploma in Mechatronic Engineering', 'Diploma in Mechatronic Engineering'),
    ('Diploma in Business Computing', 'Diploma in Business Computing'),
    ('Diploma in Automotive and Autoelectrical Engineering', 'Diploma in Automotive and Autoelectrical Engineering'),
    ('Certificate in Agribusiness with Technology', 'Certificate in Agribusiness with Technology'),
    ('Certificate in Business Administration', 'Certificate in Business Administration')
]
# Choices for Department field
DEPARTMENT_CHOICES = [
    ('Department of Construction Management and Technology', 'Department of Construction Management and Technology'),
    ('Department of Architecture and Art Design', 'Department of Architecture and Art Design'),
    ('Department of Urban Planning and Real Estate Studies', 'Department of Urban Planning and Real Estate Studies'),
    ('Department of Information System and Technology', 'Department of Information System and Technology'),
    ('Department of Computer Science and Engineering', 'Department of Computer Science and Engineering'),
    ('Department of Electronics and Telecommunication Engineering', 'Department of Electronics and Telecommunication Engineering'),
    ('Department of Content Engineering and Multimedia Technology', 'Department of Content Engineering and Multimedia Technology'),
    ('Department of Informatics', 'Department of Informatics'),
    ('Department of Civil Engineering', 'Department of Civil Engineering'),
    ('Department of Geoscience and Mining Technology', 'Department of Geoscience and Mining Technology'),
    ('Department of Electrical and Power Engineering', 'Department of Electrical and Power Engineering'),
    ('Department of Mechanical and Industrial Engineering', 'Department of Mechanical and Industrial Engineering'),
    ('Department of Chemical Processing and Environmental Engineering','Department of Chemical Processing and Environmental Engineering'),
    ('Department of Applied Science', 'Department of Applied Science'),
    ('Department of Mathematics and Statistics', 'Department of Mathematics and Statistics'),
    ('Department of Natural Science', 'Department of Natural Science'),
    ('Department of Medical Science and Technology', 'Department of Medical Science and Technology'),
    ('Department of Technical Education', 'Department of Technical Education'),
    ('Department of Earth Sciences','Department of Earth Sciences'),
    ('Department of Business Management', 'Department of Business Management'),
    ('Department of Humanities', 'Department of Humanities'),
    ('Department of Law','Department of Law'),
    ('Department of Agricultural Engineering', 'Department of Agricultural Engineering'),
    ('Department of Crop Science and Horticulture', 'Department of Crop Science and Horticulture'),	
    ('Department of Food Science and Technology', 'Department of Food Science and Technology'),	
    ('Department of Natural Resources', 'Department of Natural Resources'),	
    ('Department of Veterinary Medicine and Animal Science', 'Department of Veterinary Medicine and Animal Science'),
    ('Department of Agronomy and Soil Science', 'Department of Agronomy and Soil Science'),
    
    
]
COLLEGE_CHOICES = [
    ('College of Engineering and Technology', 'College of Engineering and Technology (CET)'),
    ('College of Science and Technical Education', 'College of Science and Technical Education (CoSTE)'),
    ('College of Humanities and Business Studies', 'College of Humanities and Business Studies (CoHBS)'),
    ('College of Architecture and Construction Technology', 'College of Architecture and Construction Technology (CoACT)'),
    ('College of Information and Communication Technology', 'College of Information and Communication Technology (CoICT)'),
    ('College of Agricultural Sciences and Technology', 'College of Agricultural Sciences and Technology (CoAST)'),
]
# Choices for Level of Study field
LEVEL_OF_STUDY_CHOICES = [
    ('CERTIFICATE', 'Certificate'),
    ('DIPLOMA', 'Diploma'),
    ('BACHELOR', 'Bachelor'),
    ('MASTERS', 'Masters'),
]
# Choices for Level of Study field
JUMUIYA = [
    ('Mt. Anthony wa Padua', 'JMT. ANTHONY WA PADUA'),
    ('Mt. Bikira Maria wa Fatima', 'JMT. B.MARIA WA FATIMA'),
    ('Mt. Stephano', 'JMT. STEPHANO'),
    ('Mt. Gabriel', 'JMT. GABRIEL'),
    ('Mt. Francisco wa Asizi', 'JMT. FRANCISCO WA ASIZI'),
    ('Mt. Don Bosco', 'JMT. DON BOSCO'),
]
VYAMA_VYA_KITUME = [
    ('LEGIO MARIA','LEGIO MARIA'),
    ('KARISMATIKI','KARISMATIKI'),
    ('KWAYA','KWAYA'),
    ('MOYO MT. WA YESU','MOYO MTAKATIFU WA YESU'),
    ('WATUMISHI WA ALTARE','WATUMISHI WA ALTARE'),
    ('WASOMA MASOMO','CHAMA CHA WASOMA MASOMO'),
]
KAMATI = [
    ('KAMATI KUU','KAMATI KUU'),
    ('LITRUJIA','LITRUJIA'),
    ('MIPANGO NA FEDHA','MIPANGO NA FEDHA'),
    ('SHEREHE NA MAAFA','SHEREHE NA MAAFA'),
    ('ELIMU USHAURI NA NIDHAMU','ELIMU USHAURI NA NIDHAMU'),
    ('AFYA USAFI NA MAPAMBO','AFYA USAFI NA MAPAMBO'),
    ('KWAYA','KWAYA'),
    ('MUZIKI','MUZIKI'),
    ('MICHEZO','MICHEZO'),
]


class CommitteeMember(models.Model):
    nafasi_ya_uongozi = models.CharField(max_length=255)
    jina_la_kiongozi = models.CharField(max_length=255)
    picha_ya_kiongozi = models.ImageField(upload_to='committee_members/')
    kozi_anayosoma = models.CharField(max_length=200, null=False, blank=False)
    phone_number = models.CharField(max_length=12, null=False, blank=False)
    
    def __str__(self):
        return self.jina_la_kiongozi
    
    class Meta:
        verbose_name = "Viongozi Kamati Kuu"
        verbose_name_plural = "Viongozi Kamati Kuu"
 
class SaintLife(models.Model):
    name_of_saint = models.CharField(max_length=100, verbose_name='Saint Name')
    birth_date = models.DateField(null=True, blank=True, verbose_name='Date of Birth')
    death_date = models.DateField(null=True, blank=True, verbose_name='Date of Death')
    biography = CKEditor5Field(blank=True, null=True, config_name='extends')
    image = models.ImageField(upload_to='saint_images/', null=True, blank=True, verbose_name='Image')

    def __str__(self):
        return self.name_of_saint

    class Meta:
        verbose_name = "Maisha ya Watakatifu"
        verbose_name_plural = "Maisha ya Watakatifu"   

class Community(models.Model):
    community_name = models.CharField(max_length=255)
    description = CKEditor5Field(blank=True, null=True, config_name='extends')
    community_image = models.ImageField(upload_to='community_images/', blank=True, null=True)
    patron_saint = models.ForeignKey(SaintLife, on_delete=models.SET_NULL, null=True, blank=True, related_name='communities')
    
    def __str__(self):
        return self.community_name
    
    class Meta:
        verbose_name = "Community"
        verbose_name_plural = "Community"
    
class Rozary(models.Model):
    rozary_name = models.CharField(max_length=255)
    description = CKEditor5Field(blank=True, null=True, config_name='extends')
    # description = models.TextField()
    rozary_image = models.ImageField(upload_to='rozary_images/', blank=True, null=True)
    # Add other fields as needed
    
    def __str__(self):
        return self.rozary_name
    
    class Meta:
        verbose_name = "Rozary"
        verbose_name_plural = "Rozary"
    
class Novena(models.Model):
    novena_name = models.CharField(max_length=255)
    description = CKEditor5Field(blank=True, null=True, config_name='extends')
    # description = models.TextField()
    novena_image = models.ImageField(upload_to='novena_images/', blank=True, null=True)
    # Add other fields as needed
    
    def __str__(self):
        return self.novena_name
    
    class Meta:
        verbose_name = "Novena"
        verbose_name_plural = "Novena"
    

     
class Image(models.Model):
    user = models.ForeignKey(TmcsMember, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='gallery_images/')
    title = models.CharField(max_length=255, blank=False)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name} - {self.uploaded_at}"
    
    class Meta:
        verbose_name = "Galery events"
        verbose_name_plural = "Galery events"

class MaswalinaMajibu(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    swali = CKEditor5Field(null=True, blank=True, config_name='extends')
    jibu = CKEditor5Field(null=True, blank=True, config_name='extends')

    def __str__(self):
        return self.swali[:50]
    
    class Meta:
        verbose_name = "Maswali na Majibu"
        verbose_name_plural = "Maswali na Majibu"

class MasomoyaDominika(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    dominika = models.CharField(max_length=300)
    somo_la1 = CKEditor5Field(null=True, blank=True, config_name='extends')
    somo_la2 = CKEditor5Field(null=True, blank=True, config_name='extends')
    injili = CKEditor5Field(null=True, blank=True, config_name='extends')

    def __str__(self):
        return f"MASOMO YA MISA, JUMAPILI, {self.date.strftime('%B %d, %Y')}, DOMINIKA {self.dominika}"
    
    class Meta:
        verbose_name = "Masomo ya Misa"
        verbose_name_plural = "Masomo ya Misa"

class NewsItem(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Matangazo"
        verbose_name_plural = "Matangazo"
    
class Quote(models.Model):
    text_quote = models.TextField()
    author_of_quote = models.CharField(max_length=100)

    def __str__(self):
        return self.text_quote
    
class Event(models.Model):
    title = models.CharField(max_length=300, help_text="Event Title")
    event_date = models.DateField(help_text="Event Date")
    image = models.ImageField(upload_to='events/')
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Matukio yajayo"
        verbose_name_plural = "Matukio yajayo"

class CalenderYaTMCSTawiPDF(models.Model):
    pdf_title = models.CharField(max_length=100, default="Calender Ya TMCS Tawi")
    pdf_file = models.FileField(upload_to='calender_ya_tawi/')

    def __str__(self):
        return self.pdf_title
    
    class Meta:
        verbose_name = "Calenda ya Tawi"
        verbose_name_plural = "Calenda ya Tawi"
    
class Feedback(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    date_submitted = models.DateTimeField(auto_now_add=True)
    


class ContactMessage(models.Model):
    user_name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user_name


class LeadersTeamMember(models.Model):
    LEVEL_CHOICES = [
        ('National Leader', 'National Leader'),
        ('Zonal Leader', 'Zonal Leader'),
        ('Branch Leader', 'Branch Leader'),
    ]

    leader_name = models.CharField(max_length=100)
    leader_position = models.CharField(max_length=100)
    image = models.ImageField(upload_to='team_images/')
    level = models.CharField(max_length=50, choices=LEVEL_CHOICES)
    start_year = models.PositiveIntegerField(default=2024)  # Adding start year
    end_year = models.PositiveIntegerField(default=2024)  # Adding end year
    contact_info = models.CharField(max_length=255)  # Adding contact information

    def __str__(self):
        return self.leader_name

