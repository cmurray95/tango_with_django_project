import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'tango_with_django_project.settings')
import django
django.setup()
from rango.models import Category, Page


def populate():
    """
    First, create lists of dictionaries containing
    pages we which to add into each category.
    Next, create dictionary of dictionaries for
    our categories.
    """

    python_pages = [
        {
            'title': 'Official Python Tutorial',
            'url': 'http://docs.pythpn/3/tutorial/'
        },
        {
             'title': 'How to Think like a Computer Scientist',
             'url': 'http://www.greenteapress.com/thinkpython/'
        },
        {
             'title': 'Learn Python in 10 Minutes',
             'url': 'http://www.korokithakis.net/tutorials/python/'
        }
    ]

    django_pages = [
        {
             'title': 'Official Django Tutorial',
             'url': 'http://docs.djangoproject.com/en/2.1/intro/tutorial01/'
        },
        {
             'title': 'Django Rocks',
             'url': 'http://www.djangorocks.com/'
        },
        {
             'title': 'How to Tango with Django',
             'url': 'http://www.tangowithdjango.com/'
        },
    ]

    other_pages = [
        {
             'title': 'Bottle',
             'url': 'http://www.bottlepy.org/docs/dev/'
        },
        {
             'title': 'Flask',
             'url': 'http://www.flask.pocoo.org'
        }
    ]

    cats = {'Python': {'pages': python_pages,
                       'likes': 64,
                       'views': 128},
            'Django': {'pages': django_pages,
                       'likes': 32,
                       'views': 64},
            'Other Frameworks': {'pages': other_pages,
                                 'likes': 16,
                                 'views': 32}
            }

    # Add each category alongside associated pages
    for cat, cat_data in cats.items():
        c = add_cat(cat, cat_data['views'], cat_data['likes'])
        for p in cat_data['pages']:
            add_page(c, p['title'], p['url'])

    # Print categories
    for c in Category.objects.all():
        for p in Page.objects.filter(category=c):
            print(f'-{c}: {p}')


def add_page(cat, title, url, views=0):
    p = Page.objects.get_or_create(category=cat, title=title)[0]
    p.url = url
    p.views = views
    p.save()
    return p


def add_cat(name, views=0, likes=0):
    c = Category.objects.get_or_create(name=name, views=views, likes=likes)[0]
    c.likes = likes
    c.views = views
    c.save()
    return c


if __name__ == '__main__':
    print('Starting Rango population script...')
    populate()
