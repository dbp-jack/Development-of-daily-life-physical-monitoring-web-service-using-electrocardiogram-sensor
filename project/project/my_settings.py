MY_SECRET = {
    'SECRET_KEY' : 'django-insecure-0(zp#!9a&!5%5uoov5lhj32@&#=wu$qj11dfd4keucw_pv=39c'
}

MY_DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'ecg_test',
        'USER': 'root',
        'PASSWORD': '1111',
        'HOST': 'localhost',
        'PORT': '3306',
       'OPTIONS' : {
           'init_command' : "SET sql_mode='STRICT_TRANS_TABLES'",
       }
    }
}