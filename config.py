import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or b'\xf8\xebf3;p\xfb\x03\xeb!K\x7f\x14p\x18\x8c' 
    # py -c "import os; print(os.urandom(16))" -->run in cmd
    
    MONGODB_SETTINGS= {'db' : 'UTA_Enrollment'}