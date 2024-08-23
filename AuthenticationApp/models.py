from django.db import models
from django.db import models
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager
from multiselectfield import MultiSelectField

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
    ('Masters', 'Masters'),
]
# Choices for Courses field
COURSES_CHOICES = [
    #### 2 years
    ('Doctor of Philosophy in Information Science and Engineering', 'Doctor of Philosophy in Information Science and Engineering'),
    #### 3 years
    ('Doctor of Philosophy in Mechanical Engineering', 'Doctor of Philosophy in Mechanical Engineering'),
    #### 3 years
    ('Doctor of Philosophy in Civil Engineering', 'Doctor of Philosophy in Civil Engineering'),
    #### 1 year
    ('Postgraduate Diploma in Technical Education', 'Postgraduate Diploma in Technical Education'),
    #### 2 years
    ('Masters of Science in Civil Engineering', 'Masters of Science in Civil Engineering'),
    ('Master of Engineering in Renewable Energy', 'Master of Engineering in Renewable Energy'),
    ('Masters of Science in Energy Engineering', 'Masters of Science in Energy Engineering'),
    ('Masters of Science in Information Technology', 'Masters of Science in Information Technology'),
    ('Masters of Engineering in Clean Energy Technology', 'Masters of Engineering in Clean Energy Technology'),
    ('Masters of Biodiversity Conservation', 'Masters of Biodiversity Conservation'),
    #### 3 years
    ('Bachelor of Science with Education', 'Bachelor of Science with Education'),
    ('Bachelor of Science in Natural Resources Conservation', 'Bachelor of Science in Natural Resources Conservation'),
    ('Bachelor of Science in Information and Communication Technology', 'Bachelor of Science in Information and Communication Technology'),
    ('Bachelor of Laboratory Sciences and Technology', 'Bachelor of Laboratory Sciences and Technology'),
    ('Bachelor of Food Science and Technology', 'Bachelor of Food Science and Technology'),
    ('Bachelor of Computer Science', 'Bachelor of Computer Science'),
    ('Bachelor of Business Administration', 'Bachelor of Business Administration'),
    ('Bachelor of Agribusiness Management and Technology', 'Bachelor of Agribusiness Management and Technology'),
    #### 4 years
    ('Bachelor of Computer Engineering', 'Bachelor of Computer Engineering'),
    ('Bachelor of Electrical and Electronics Engineering', 'Bachelor of Electrical and Electronics Engineering'),
    ('Bachelor of Mechanical Engineering', 'Bachelor of Mechanical Engineering'),
    ('Bachelor of Technology in Architecture', 'Bachelor of Technology in Architecture'),
    ('Bachelor of Civil Engineering', 'Bachelor of Civil Engineering'),
    ('Bachelor of Engineering in Telecommunication Systems', 'Bachelor of Engineering in Telecommunication Systems'),
    ('Bachelor of Technology in Landscape Architecture', 'Bachelor of Technology in Landscape Architecture'),
    ('Bachelor of Technical Education in Electrical and Electronics Engineering', 'Bachelor of Technical Education in Electrical and Electronics Engineering'),
    ('Bachelor of Technical Education in Mechanical Engineering', 'Bachelor of Technical Education in Mechanical Engineering'),
    ('Bachelor of Technical Education in Civil Engineering', 'Bachelor of Technical Education in Civil Engineering'),
    ('Bachelor of Technical Education in Architectural Technology', 'Bachelor of Technical Education in Architectural Technology'),
    ('Bachelor of Engineering in Data Science', 'Bachelor of Engineering in Data Science'),
    #### 3 years
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
    #### 1 year
    ('Certificate in Agribusiness with Technology', 'Certificate in Agribusiness with Technology'),
    ('Certificate in Business Administration', 'Certificate in Business Administration')
]
# Dictionary mapping each course to its abbreviation
COURSE_ABBREVIATIONS = {
    'Doctor of Philosophy in Information Science and Engineering': 'PHD_ISE',
    'Doctor of Philosophy in Mechanical Engineering': 'PHD_ME',
    'Doctor of Philosophy in Civil Engineering': 'PHD_CE',
    'Postgraduate Diploma in Technical Education': 'PGD_TE',
    'Masters of Science in Civil Engineering': 'MSc_CE',
    'Master of Engineering in Renewable Energy': 'ME_RE',
    'Masters of Science in Energy Engineering': 'MSc_EE',
    'Masters of Science in Information Technology': 'MSc_IT',
    'Masters of Engineering in Clean Energy Technology': 'ME_CET',
    'Masters of Biodiversity Conservation': 'MSc_BC',
    'Bachelor of Computer Engineering': 'BCE',
    'Bachelor of Electrical and Electronics Engineering': 'BEEE',
    'Bachelor of Mechanical Engineering': 'BME',
    'Bachelor of Technology in Architecture': 'BTA',
    'Bachelor of Civil Engineering': 'BCE_1',
    'Bachelor of Business Administration': 'BBA',
    'Bachelor of Laboratory Sciences and Technology': 'BLST',
    'Bachelor of Science with Education': 'BS_ED',
    'Bachelor of Engineering in Telecommunication Systems': 'BETS',
    'Bachelor of Computer Science': 'BCS',
    'Bachelor of Science in Information and Communication Technology': 'BSc_ICT',
    'Bachelor of Technology in Landscape Architecture': 'BTLA',
    'Bachelor of Technical Education in Electrical and Electronics Engineering': 'BTEE',
    'Bachelor of Technical Education in Mechanical Engineering': 'BTME',
    'Bachelor of Technical Education in Civil Engineering': 'BTCE',
    'Bachelor of Technical Education in Architectural Technology': 'BTEAT',
    'Bachelor of Engineering in Data Science': 'BEDS',
    'Bachelor of Food Science and Technology': 'BFST',
    'Bachelor of Science in Natural Resources Conservation': 'BSc_NRC',
    'Bachelor of Agribusiness Management and Technology': 'BAMT',
    'Diploma in Architecture': 'DA',
    'Diploma in Biomedical Equipment Engineering': 'DBEEE',
    'Diploma in Business Administration': 'DBA',
    'Diploma in Civil Engineering': 'DCE',
    'Diploma in Computer Engineering': 'DCE_1',
    'Diploma in Electrical and Electronic Engineering': 'DEEE',
    'Diploma in Electronics and Telecommunication Engineering': 'DETE',
    'Diploma in Highway Engineering': 'DHE',
    'Diploma in Mechanical Engineering': 'DME',
    'Diploma in Mechatronics Engineering': 'DME_1',
    'Diploma in Mining Engineering': 'DME_2',
    'Diploma in Computer Science': 'DCS',
    'Diploma in Information and Communication Technology': 'DICT',
    'Diploma in Laboratory Science and Technology': 'DLST',
    'Diploma in Food Science and Technology': 'DFST',
    'Diploma in Agribusiness with Technology': 'DABT',
    'Diploma in Mechanical Engineering with Industrial Safety and Occupational Health': 'DME_ISOH',
    'Diploma of Technical Education in Civil Engineering': 'DTE_CE',
    'Diploma of Technical Education in Electrical and Electronics Engineering': 'DTE_EEE',
    'Diploma of Technical Education in Architectural Technology': 'DTE_AT',
    'Diploma of Technical Education in Mechanical Engineering': 'DTE_ME',
    'Diploma of Business Administration in Accounting and Finance': 'DBA_AF',
    'Diploma of Business Administration in Marketing and Entrepreneurship': 'DBA_ME',
    'Diploma in Mechatronic Engineering': 'DME_3',
    'Diploma in Business Computing': 'DBC',
    'Diploma in Automotive and Autoelectrical Engineering': 'DAAE',
    'Certificate in Agribusiness with Technology': 'CABT',
    'Certificate in Business Administration': 'CBA'
}

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
    ('Doctor of Philosophy', 'Doctor of Philosophy'),
    ('Postgraduate Diploma', 'Postgraduate Diploma'),
    ('Masters', 'Masters'),
    ('Bachelor\'s Degree', 'Bachelor\'s Degree'),
    ('Diploma', 'Diploma'),
    ('Certificate', 'Certificate')
]
# Choices for Level of Study field
JUMUIYA = [
    ('Mt. Anthony wa Padua', 'JMT. ANTHONY WA PADUA'),
    ('Mt. Bikira Maria wa Fatima', 'JMT. B.MARIA WA FATIMA'),
    ('Mt. Stephano', 'JMT. STEPHANO'),
    ('Mt. Gabriel', 'JMT. GABRIEL'),
    ('Mt. Francisco wa Asizi', 'JMT. FRANCISCO WA ASIZI'),
    ('Mt. Don Bosco', 'JMT. DON BOSCO'),
    ('Mt. Padre Pio', 'JMT. PADRE PIO'),
]

COURSE_JUMUIYA_MAPPING = {
    'Doctor of Philosophy in Information Science and Engineering': 'JMT. ANTHONY WA PADUA',
    'Doctor of Philosophy in Mechanical Engineering': 'JMT. ANTHONY WA PADUA',
    'Doctor of Philosophy in Civil Engineering': 'JMT. ANTHONY WA PADUA',
    'Postgraduate Diploma in Technical Education': 'JMT. ANTHONY WA PADUA',
    'Masters of Science in Civil Engineering': 'JMT. ANTHONY WA PADUA',
    'Master of Engineering in Renewable Energy': 'JMT. ANTHONY WA PADUA',
    'Masters of Science in Energy Engineering': 'JMT. ANTHONY WA PADUA',
    'Masters of Science in Information Technology': 'JMT. ANTHONY WA PADUA',
    'Masters of Engineering in Clean Energy Technology': 'JMT. ANTHONY WA PADUA',
    'Masters of Biodiversity Conservation': 'JMT. B.MARIA WA FATIMA',
    'Bachelor of Computer Engineering': 'JMT. B.MARIA WA FATIMA',
    'Bachelor of Electrical and Electronics Engineering': 'JMT. B.MARIA WA FATIMA',
    'Bachelor of Mechanical Engineering': 'JMT. B.MARIA WA FATIMA',
    'Bachelor of Technology in Architecture': 'JMT. PADRE PIO',
    'Bachelor of Civil Engineering': 'JMT. PADRE PIO',
    'Bachelor of Business Administration': 'JMT. PADRE PIO',
    'Bachelor of Laboratory Sciences and Technology': 'JMT. PADRE PIO',
    'Bachelor of Science with Education': 'JMT. PADRE PIO',
    'Bachelor of Engineering in Telecommunication Systems': 'JMT. GABRIEL',
    'Bachelor of Computer Science': 'JMT. GABRIEL',
    'Bachelor of Science in Information and Communication Technology': 'JMT. GABRIEL',
    'Bachelor of Technology in Landscape Architecture': 'JMT. FRANCISCO WA ASIZI',
    'Bachelor of Technical Education in Electrical and Electronics Engineering': 'JMT. FRANCISCO WA ASIZI',
    'Bachelor of Technical Education in Mechanical Engineering': 'JMT. STEPHANO',
    'Bachelor of Technical Education in Civil Engineering': 'JMT. STEPHANO',
    'Bachelor of Technical Education in Architectural Technology': 'JMT. STEPHANO',
    'Bachelor of Engineering in Data Science': 'JMT. DON BOSCO',
    'Bachelor of Food Science and Technology': 'JMT. DON BOSCO',
    'Bachelor of Science in Natural Resources Conservation': 'JMT. DON BOSCO',
    'Bachelor of Agribusiness Management and Technology': 'JMT. DON BOSCO',
    'Diploma in Architecture': 'JMT. STEPHANO',
    'Diploma in Biomedical Equipment Engineering': 'JMT. PADRE PIO',
    'Diploma in Business Administration': 'JMT. PADRE PIO',
    'Diploma in Civil Engineering': 'JMT. PADRE PIO',
    'Diploma in Computer Engineering': 'JMT. PADRE PIO',
    'Diploma in Electrical and Electronic Engineering': 'JMT. PADRE PIO',
    'Diploma in Electronics and Telecommunication Engineering': 'JMT. PADRE PIO',
    'Diploma in Highway Engineering': 'JMT. PADRE PIO',
    'Diploma in Mechanical Engineering': 'JMT. PADRE PIO',
    'Diploma in Mechatronics Engineering': 'JMT. PADRE PIO',
    'Diploma in Mining Engineering': 'JMT. PADRE PIO',
    'Diploma in Computer Science': 'JMT. PADRE PIO',
    'Diploma in Information and Communication Technology': 'JMT. PADRE PIO',
    'Diploma in Laboratory Science and Technology': 'JMT. PADRE PIO',
    'Diploma in Food Science and Technology': 'JMT. PADRE PIO',
    'Diploma in Agribusiness with Technology': 'JMT. PADRE PIO',
    'Diploma in Mechanical Engineering with Industrial Safety and Occupational Health': 'JMT. PADRE PIO',
    'Diploma of Technical Education in Civil Engineering': 'JMT. PADRE PIO',
    'Diploma of Technical Education in Electrical and Electronics Engineering': 'JMT. PADRE PIO',
    'Diploma of Technical Education in Architectural Technology': 'JMT. PADRE PIO',
    'Diploma of Technical Education in Mechanical Engineering': 'JMT. PADRE PIO',
    'Diploma of Business Administration in Accounting and Finance': 'JMT. PADRE PIO',
    'Diploma of Business Administration in Marketing and Entrepreneurship': 'JMT. PADRE PIO',
    'Diploma in Mechatronic Engineering': 'JMT. PADRE PIO',
    'Diploma in Business Computing': 'JMT. PADRE PIO',
    'Diploma in Automotive and Autoelectrical Engineering': 'JMT. PADRE PIO',
    'Certificate in Agribusiness with Technology': 'JMT. PADRE PIO',
    'Certificate in Business Administration': 'JMT. PADRE PIO'
}

VYAMA_VYA_KITUME = [
    ('LEGIO MARIA','LEGIO MARIA'),
    ('KARISMATIKI','KARISMATIKI'),
    ('KWAYA','KWAYA'),
    ('MOYO MTAKATIFU WA YESU','MOYO MTAKATIFU WA YESU'),
    ('WATUMISHI WA ALTARE','WATUMISHI WA ALTARE'),
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

# Define a dictionary mapping courses to their respective years of study
course_years_mapping = {
    # Courses with 2 years of study
    'Doctor of Philosophy in Information Science and Engineering': 2,
    'Master of Engineering in Renewable Energy': 2,
    'Masters of Science in Civil Engineering': 2,
    'Masters of Science in Energy Engineering': 2,
    'Masters of Science in Information Technology': 2,
    'Masters of Engineering in Clean Energy Technology': 2,
    'Masters of Biodiversity Conservation': 2,
    # Courses with 3 years of study
    'Doctor of Philosophy in Mechanical Engineering': 3,
    'Doctor of Philosophy in Civil Engineering': 3,
    'Bachelor of Science with Education': 3,
    'Bachelor of Science in Natural Resources Conservation': 3,
    'Bachelor of Science in Information and Communication Technology': 3,
    'Bachelor of Laboratory Sciences and Technology': 3,
    'Bachelor of Food Science and Technology': 3,
    'Bachelor of Computer Science': 3,
    'Bachelor of Business Administration': 3,
    'Bachelor of Agribusiness Management and Technology': 3,
    'Diploma in Architecture': 3,
    'Diploma in Biomedical Equipment Engineering': 3,
    'Diploma in Business Administration': 3,
    'Diploma in Civil Engineering': 3,
    'Diploma in Computer Engineering': 3,
    'Diploma in Electrical and Electronic Engineering': 3,
    'Diploma in Electronics and Telecommunication Engineering': 3,
    'Diploma in Highway Engineering': 3,
    'Diploma in Mechanical Engineering': 3,
    'Diploma in Mechatronics Engineering': 3,
    'Diploma in Mining Engineering': 3,
    'Diploma in Computer Science': 3,
    'Diploma in Information and Communication Technology': 3,
    'Diploma in Laboratory Science and Technology': 3,
    'Diploma in Food Science and Technology': 3,
    'Diploma in Agribusiness with Technology': 3,
    'Diploma in Mechanical Engineering with Industrial Safety and Occupational Health': 3,
    'Diploma of Technical Education in Civil Engineering': 3,
    'Diploma of Technical Education in Electrical and Electronics Engineering': 3,
    'Diploma of Technical Education in Architectural Technology': 3,
    'Diploma of Technical Education in Mechanical Engineering': 3,
    'Diploma of Business Administration in Accounting and Finance': 3,
    'Diploma of Business Administration in Marketing and Entrepreneurship': 3,
    'Diploma in Mechatronic Engineering': 3,
    'Diploma in Business Computing': 3,
    'Diploma in Automotive and Autoelectrical Engineering': 3,
    # Courses with 4 years of study
    'Bachelor of Computer Engineering': 4,
    'Bachelor of Electrical and Electronics Engineering': 4,
    'Bachelor of Mechanical Engineering': 4,
    'Bachelor of Technology in Architecture': 4,
    'Bachelor of Civil Engineering': 4,
    'Bachelor of Engineering in Telecommunication Systems': 4,
    'Bachelor of Technology in Landscape Architecture': 4,
    'Bachelor of Technical Education in Electrical and Electronics Engineering': 4,
    'Bachelor of Technical Education in Mechanical Engineering': 4,
    'Bachelor of Technical Education in Civil Engineering': 4,
    'Bachelor of Technical Education in Architectural Technology': 4,
    'Bachelor of Engineering in Data Science': 4,
    # Courses with 1 year of study
    'Postgraduate Diploma in Technical Education': 1,
    'Certificate in Agribusiness with Technology': 1,
    'Certificate in Business Administration': 1,
}

class CustomUserManager(UserManager):
    def _create_user(self, email, first_name, password, **extra_fields):
        if not email:
            raise ValueError("Provide the correct E-mail address")
        if not first_name:
            raise ValueError("Provide a First Name")
        
        email = self.normalize_email(email)
        user = self.model(email=email, first_name=first_name, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_user(self, email=None, first_name=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, first_name, password, **extra_fields)
    
    def create_superuser(self, email=None, first_name=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self._create_user(email, first_name, password, **extra_fields)
    #############################
    
    def create_mwenyekiti_tawi(self, email=None, first_name=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', False)
        extra_fields.setdefault('is_mwenyekiti_tawi', True)
        return self._create_user(email, first_name, password, **extra_fields)

    def create_katibu_tawi(self, email=None, first_name=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', False)
        extra_fields.setdefault('is_katibu_tawi', True)
        return self._create_user(email, first_name, password, **extra_fields)
    
    def create_mhazini_tawi(self, email=None, first_name=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', False)
        extra_fields.setdefault('is_mhazini_tawi', True)
        return self._create_user(email, first_name, password, **extra_fields)
    #############################

    def create_mwenyekiti_karismatiki(self, email=None, first_name=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', False)
        extra_fields.setdefault('is_mwenyekiti_karismatiki', True)
        return self._create_user(email, first_name, password, **extra_fields)

    def create_katibu_karismatiki(self, email=None, first_name=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', False)
        extra_fields.setdefault('is_katibu_karismatiki', True)
        return self._create_user(email, first_name, password, **extra_fields)
 
    def create_mhazini_karismatiki(self, email=None, first_name=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', False)
        extra_fields.setdefault('is_mhazini_karismatiki', True)
        return self._create_user(email, first_name, password, **extra_fields)

    #############################
   
    def create_mwenyekiti_legio(self, email=None, first_name=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', False)
        extra_fields.setdefault('is_mwenyekiti_legio', True)
        return self._create_user(email, first_name, password, **extra_fields)

    def create_katibu_legio(self, email=None, first_name=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', False)
        extra_fields.setdefault('is_katibu_legio', True)
        return self._create_user(email, first_name, password, **extra_fields)
    
    def create_mhazini_legio(self, email=None, first_name=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', False)
        extra_fields.setdefault('is_mhazini_legio', True)
        return self._create_user(email, first_name, password, **extra_fields)
 
    ##########################

        
    def create_mwenyekiti_kwaya(self, email=None, first_name=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', False)
        extra_fields.setdefault('is_mwenyekiti_kwaya', True)
        return self._create_user(email, first_name, password, **extra_fields)

    def create_katibu_kwaya(self, email=None, first_name=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', False)
        extra_fields.setdefault('is_katibu_kwaya', True)
        return self._create_user(email, first_name, password, **extra_fields)
    
    def create_mhazini_kwaya(self, email=None, first_name=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', False)
        extra_fields.setdefault('is_mhazini_kwaya', True)
        return self._create_user(email, first_name, password, **extra_fields)
    ############################
    
    def create_mwenyekiti_moyo_mtakatifu_wa_Yesu(self, email=None, first_name=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', False)
        extra_fields.setdefault('is_mwenyekiti_moyo_mtakatifu_wa_Yesu', True)
        return self._create_user(email, first_name, password, **extra_fields)

    def create_katibu_moyo_mtakatifu_wa_Yesu(self, email=None, first_name=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', False)
        extra_fields.setdefault('is_katibu_moyo_mtakatifu_wa_Yesu', True)
        return self._create_user(email, first_name, password, **extra_fields)
    
    def create_mhazini_moyo_mtakatifu_wa_Yesu(self, email=None, first_name=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', False)
        extra_fields.setdefault('is_mhazini_moyo_mtakatifu_wa_Yesu', True)
        return self._create_user(email, first_name, password, **extra_fields)
    ############################
    def create_kiongozi_wa_darasa(self, email=None, first_name=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', False)
        extra_fields.setdefault('is_kiongozi_wa_darasa', True)
        return self._create_user(email, first_name, password, **extra_fields)
    ############################
    def create_mwenyekiti_litrujia(self, email=None, first_name=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', False)
        extra_fields.setdefault('is_mwenyekiti_litrujia', True)
        return self._create_user(email, first_name, password, **extra_fields)

    def create_katibu_litrujia(self, email=None, first_name=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', False)
        extra_fields.setdefault('is_katibu_litrujia', True)
        return self._create_user(email, first_name, password, **extra_fields)
    
    ############# MIPANGO NA FEDHA ###############
    def create_mwenyekiti_mipango_na_fedha(self, email=None, first_name=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', False)
        extra_fields.setdefault('is_mwenyekiti_mipango_na_fedha', True)
        return self._create_user(email, first_name, password, **extra_fields)

    def create_katibu_mipango_na_fedha(self, email=None, first_name=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', False)
        extra_fields.setdefault('is_katibu_mipango_na_fedha', True)
        return self._create_user(email, first_name, password, **extra_fields)
    
    def create_mhazini_mipango_na_fedha(self, email=None, first_name=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', False)
        extra_fields.setdefault('is_mhazini_mipango_na_fedha', True)
        return self._create_user(email, first_name, password, **extra_fields)
    ############## MASS MEDIA ##############
    def create_mwenyekiti_mas_media(self, email=None, first_name=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', False)
        extra_fields.setdefault('is_mwenyekiti_mas_media', True)
        return self._create_user(email, first_name, password, **extra_fields)

    def create_katibu_mas_media(self, email=None, first_name=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', False)
        extra_fields.setdefault('is_katibu_mas_media', True)
        return self._create_user(email, first_name, password, **extra_fields)
    
    def create_mhazini_mas_media(self, email=None, first_name=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', False)
        extra_fields.setdefault('is_mhazini_mas_media', True)
        return self._create_user(email, first_name, password, **extra_fields)
    ############# SHEREHE NA MAAFA###############
    def create_mwenyekiti_sherehe_na_maafa(self, email=None, first_name=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', False)
        extra_fields.setdefault('is_mwenyekiti_sherehe_na_maafa', True)
        return self._create_user(email, first_name, password, **extra_fields)

    def create_katibu_sherehe_na_maafa(self, email=None, first_name=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', False)
        extra_fields.setdefault('is_katibu_sherehe_na_maafa', True)
        return self._create_user(email, first_name, password, **extra_fields)
    
    def create_mhazini_sherehe_na_maafa(self, email=None, first_name=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', False)
        extra_fields.setdefault('is_mhazini_sherehe_na_maafa', True)
        return self._create_user(email, first_name, password, **extra_fields)
    ############ MICHEZO NA BURUDANI ################
    def create_mwenyekiti_michezo_na_burudani(self, email=None, first_name=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', False)
        extra_fields.setdefault('is_mwenyekiti_michezo_na_burudani', True)
        return self._create_user(email, first_name, password, **extra_fields)

    def create_katibu_michezo_na_burudani(self, email=None, first_name=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', False)
        extra_fields.setdefault('is_katibu_michezo_na_burudani', True)
        return self._create_user(email, first_name, password, **extra_fields)
    
    def create_mhazini_michezo_na_burudani(self, email=None, first_name=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', False)
        extra_fields.setdefault('is_mhazini_michezo_na_burudani', True)
        return self._create_user(email, first_name, password, **extra_fields)
    ############# MUZIKI ###############
    def create_mwenyekiti_muziki(self, email=None, first_name=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', False)
        extra_fields.setdefault('is_mwenyekiti_muziki', True)
        return self._create_user(email, first_name, password, **extra_fields)

    def create_katibu_muziki(self, email=None, first_name=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', False)
        extra_fields.setdefault('is_katibu_muziki', True)
        return self._create_user(email, first_name, password, **extra_fields)
    
    def create_mhazini_muziki(self, email=None, first_name=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', False)
        extra_fields.setdefault('is_mhazini_muziki', True)
        return self._create_user(email, first_name, password, **extra_fields)
    ############# ELIMU USHAURI NA NIDHAMU ###############
    def create_mwenyekiti_elimu_ushauri_na_nidhamu(self, email=None, first_name=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', False)
        extra_fields.setdefault('is_mwenyekiti_elimu_ushauri_na_nidhamu', True)
        return self._create_user(email, first_name, password, **extra_fields)

    def create_katibu_elimu_ushauri_na_nidhamu(self, email=None, first_name=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', False)
        extra_fields.setdefault('is_katibu_elimu_ushauri_na_nidhamu', True)
        return self._create_user(email, first_name, password, **extra_fields)
    
    def create_mhazini_elimu_ushauri_na_nidhamu(self, email=None, first_name=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', False)
        extra_fields.setdefault('is_mhazini_elimu_ushauri_na_nidhamu', True)
        return self._create_user(email, first_name, password, **extra_fields)
    ######## REGISTRATION COMMITEE ###########
    def create_registration_committee(self, email=None, first_name=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', False)
        extra_fields.setdefault('is_registration_committee', True)
        return self._create_user(email, first_name, password, **extra_fields)


class TmcsMember(AbstractBaseUser, PermissionsMixin):
    # Personal Information
    first_name = models.CharField(max_length=50, verbose_name='First Name')
    middle_name = models.CharField(max_length=50, blank=True, verbose_name='Middle Name')
    last_name = models.CharField(max_length=50, verbose_name='Last Name')
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)   
    # Contact Information
    namba_ya_mwanafunzi = models.CharField(max_length=20, verbose_name='Simu Student')
    email = models.EmailField(max_length=100, verbose_name='Your E-mail', unique=True)
    namba_ya_mzazi = models.CharField(max_length=20, verbose_name='Simu Parent')
    # Sacraments
    ubatizo = models.CharField(max_length=50,null=False, blank=False,choices=SACRAMENT_CHOICES, verbose_name='Ubatizo')
    kipaimara = models.CharField(max_length=50,null=False, blank=False,choices=SACRAMENT_CHOICES, verbose_name='Kipaimara')
    ndoa_au_daraja = models.CharField(max_length=50, blank=False,choices=SACRAMENT_CHOICES, verbose_name='Daraja')
    # Education
    elimu_uliyonayo = models.CharField(max_length=50, verbose_name='Elimu uliyonayo', choices=EDUCATION_LEVEL_CHOICES)
    # Parish and Diocese
    parokia = models.CharField(max_length=100, verbose_name='Parokia')
    jimbo_kuu = models.CharField(max_length=100, verbose_name='Jimbo')
    # Course and Department
    course = models.CharField(max_length=100, verbose_name='Course', choices=COURSES_CHOICES)
    department = models.CharField(max_length=100, verbose_name='Department', choices=DEPARTMENT_CHOICES)
    college = models.CharField(max_length=100, verbose_name='College', choices=COLLEGE_CHOICES)
    # Academic Level
    level_of_study = models.CharField(max_length=20, verbose_name='Level unayosoma', choices=LEVEL_OF_STUDY_CHOICES)
    # Apostolic Associations
    # vyama_vya_kitume = models.CharField(max_length=100, blank=True, verbose_name='Utume', choices=VYAMA_VYA_KITUME)
    vyama_vya_kitume = MultiSelectField(max_length=100, blank=True, verbose_name='Utume', choices=VYAMA_VYA_KITUME)
    vinginevyo = models.CharField(max_length=100, blank=True, verbose_name='Vinginevyo')
    tarehe_aliyosajiliwa = models.DateTimeField(auto_now_add=True)
    # Years of Study
    years_of_study = models.IntegerField(verbose_name='Years of Study', blank=True, null=True)
    # Registration Year
    # registration_year = models.IntegerField(verbose_name='Registration Year', choices=(), blank=True, null=True)
    #Permissions    
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    ###
    is_mwenyekiti_tawi = models.BooleanField(default=False)
    is_katibu_tawi = models.BooleanField(default=False)
    is_mhazini_tawi = models.BooleanField(default=False)
    ###
    is_mwenyekiti_legio = models.BooleanField(default=False)
    is_katibu_legio = models.BooleanField(default=False)
    is_mhazini_legio = models.BooleanField(default=False)
    ###
    is_mwenyekiti_kwaya = models.BooleanField(default=False)
    is_katibu_kwaya = models.BooleanField(default=False)
    is_mhazini_kwaya = models.BooleanField(default=False)
    ###
    is_mwenyekiti_karismatiki = models.BooleanField(default=False)
    is_katibu_karismatiki = models.BooleanField(default=False)
    is_mhazini_karismatiki = models.BooleanField(default=False)
    ###
    is_mwenyekiti_moyo_mtakatifu_wa_Yesu = models.BooleanField(default=False)
    is_katibu_moyo_mtakatifu_wa_Yesu = models.BooleanField(default=False)
    is_mhazini_moyo_mtakatifu_wa_Yesu = models.BooleanField(default=False)
    ###
    is_kiongozi_wa_darasa = models.BooleanField(default=False)
    ###
    is_mwenyekiti_litrujia = models.BooleanField(default=False)
    is_katibu_litrujia = models.BooleanField(default=False)
    ###
    is_mwenyekiti_mipango_na_fedha = models.BooleanField(default=False)
    is_katibu_mipango_na_fedha = models.BooleanField(default=False)
    is_mhazini_mipango_na_fedha = models.BooleanField(default=False)
    ###
    ###
    is_mwenyekiti_mas_media = models.BooleanField(default=False)
    is_katibu_mas_media = models.BooleanField(default=False)
    is_mhazini_mas_media = models.BooleanField(default=False)
    ###
    ###
    is_mwenyekiti_sherehe_na_maafa = models.BooleanField(default=False)
    is_katibu_sherehe_na_maafa = models.BooleanField(default=False)
    is_mhazini_sherehe_na_maafa = models.BooleanField(default=False)
    ###
    ###
    is_mwenyekiti_michezo_na_burudani = models.BooleanField(default=False)
    is_katibu_michezo_na_burudani = models.BooleanField(default=False)
    is_mhazini_michezo_na_burudani = models.BooleanField(default=False)
    ###
    ###
    is_mwenyekiti_muziki = models.BooleanField(default=False)
    is_katibu_muziki = models.BooleanField(default=False)
    is_mhazini_muziki = models.BooleanField(default=False)
    ###
    ###
    is_mwenyekiti_elimu_ushauri_na_nidhamu = models.BooleanField(default=False)
    is_katibu_elimu_ushauri_na_nidhamu = models.BooleanField(default=False)
    is_mhazini_elimu_ushauri_na_nidhamu = models.BooleanField(default=False)
    ###
    is_registration_committee = models.BooleanField(default=False)
    
    
    objects = CustomUserManager()
    
    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name']
    
    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Tmcs Members'
    
    
    def __str__(self):
        return f"{self.first_name} {self.middle_name} {self.last_name}"
    
    def generate_member_id(self):
        # Extract Jumuiya abbreviation based on course
        jumuiya_abbreviation = COURSE_JUMUIYA_MAPPING.get(self.course, '')
        # Extract course abbreviation
        course_abbreviation = COURSE_ABBREVIATIONS.get(self.course, '')
        # Extract academic level abbreviation
        academic_level_abbreviation = self.level_of_study[:4].upper()
        # Extract registration year
        registration_year = str(self.tarehe_aliyosajiliwa.year)
        # registration_year = str(self.registration_year)
        # Concatenate parts to form member ID
        member_id = f'{jumuiya_abbreviation}/{course_abbreviation}/{academic_level_abbreviation}/{registration_year}{self.id}'
        return member_id
    
    def save(self, *args, **kwargs):
        # Automatically set the years of study based on the selected course
        if self.course:# Set the years of study based on the selected course
            self.years_of_study = course_years_mapping.get(self.course, None)
        super().save(*args, **kwargs)
        

