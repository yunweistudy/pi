import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myproject.settings")
import django
django.setup()
def main():
    from myapp.models import User
    f=open('in.txt')
    for line in f:
        id,name=line.split(',')
        blog=User(id=id,name=name)
        #BlogList.append(blog)
        User.objects.get_or_create(id=id,name=name)
    f.close()

if __name__ == "__main__":
    main()
    print('Done')

