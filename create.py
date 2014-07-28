#!/usr/bin/env python
'''
This script has only been tested on Ubuntu with django 1.6.
'''
import os
from os.path import realpath, dirname, join

# check os system
if os.name != 'posix':
   raise Exception('This script can only be used on POSIX system.')

BSE_PATH = dirname(realpath(__file__))
SRS_PATH = join(BSE_PATH, 'samples')

# locate path
os.chdir(dirname(BSE_PATH))

# create a new project
projname = raw_input("Project name: ")
os.system('django-admin.py startproject %s' % projname)

TAR_PATH = join(dirname(BSE_PATH), projname)

# create an app name
os.chdir(TAR_PATH)
appname = raw_input('App name: ')
os.system('python manage.py startapp %s' % appname)

# update views.py
os.system('cp %s %s' % (join(SRS_PATH, 'app', 'views.py'), join(TAR_PATH, appname)))

# update urls.py
os.system('cp %s %s' % (join(SRS_PATH, 'core', 'urls.py'), join(TAR_PATH, projname)))

# modify urls.py
os.system("sed -i 's/__APPNAME__/%s/g' %s" % (appname, join(TAR_PATH, projname, 'urls.py')))

# create template page
os.system('mkdir -p %s' % join(TAR_PATH, 'templates', appname))
os.system('cp %s %s' % (join(SRS_PATH, 'templates', 'index.html'), join(TAR_PATH, 'templates', appname)))

# set STATIC path
os.system('mkdir -p %s' % join(TAR_PATH, 'static', 'img'))
os.system('cp %s %s' % (join(SRS_PATH, 'static', 'logo_round.png'), join(TAR_PATH, 'static', 'img')))
msg_static = '''STATICFILES_DIRS = (
    os.path.join(os.path.dirname(os.path.dirname(__file__)),'static'),
)
'''
os.system('''echo "%s" >> %s''' % (msg_static, join(TAR_PATH, projname, 'settings.py')))

# add template path to settings.py
msg_template = '''
#TEMPLATE PATH
TEMPLATE_DIRS = [os.path.join(BASE_DIR, 'templates/%s')]
''' % appname
os.system('''echo "%s" >> %s''' % (msg_template, join(TAR_PATH, projname, 'settings.py')))

# update settings.py
#os.system('''awk '/INSTALLED_APPS = \(/{print;print "\047""TEST""\047";next}1' %s''' % join(TAR_PATH, projname, 'settings.py')) --> doesn't work...
with open(join(TAR_PATH, projname, 'settings.py')) as sf:
    script = sf.readlines()
    script.insert(script.index('INSTALLED_APPS = (\n')+1, "    '%s',\n" % appname)
with open(join(TAR_PATH, projname, 'settings.py'), 'w') as sf:
    for i in script:
        sf.write(i)

