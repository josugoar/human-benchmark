# Server Build Setup

```bash
# [auth]
$ python manage.py changepassword
$ python manage.py createsuperuser

# [contenttypes]
$ python manage.py remove_stale_contenttypes

# [django]
$ python manage.py check
$ python manage.py compilemessages
$ python manage.py createcachetable
$ python manage.py dbshell
$ python manage.py diffsettings
$ python manage.py dumpdata
$ python manage.py flush
$ python manage.py inspectdb
$ python manage.py loaddata
$ python manage.py makemessages
$ python manage.py makemigrations
$ python manage.py migrate
$ python manage.py sendtestemail
$ python manage.py shell
$ python manage.py showmigrations
$ python manage.py sqlflush
$ python manage.py sqlmigrate
$ python manage.py sqlsequencereset
$ python manage.py squashmigrations
$ python manage.py startapp
$ python manage.py startproject
$ python manage.py test
$ python manage.py testserver

# [sessions]
$ python manage.py clearsessions

# [staticfiles]
$ python manage.py collectstatic
$ python manage.py findstatic
$ python manage.py runserver
```
