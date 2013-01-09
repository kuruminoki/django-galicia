import os
from setuptools import setup

README = open(os.path.join(os.path.dirname(__file__), 'README.rst')).read()

setup(
    name = 'django-localflavor-es-ga',
    version = '0.1',
    description = 'Country-specific Django helpers for Galicia (Spain).',
    long_description = README,
    author = 'Afonso Fernandez Nogueira',
    author_email = 'fonzzo+localflavor-es-ga@gmail.com',
    license='BSD',
    url = 'https://bitbucket.org/fonso/django-localflavor-es-ga',
    packages = ['django_localflavor_es_ga'],
    include_package_data = True,
    classifiers = [
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
    install_requires=[
        'Django>=1.4',
    ]
)