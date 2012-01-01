
from setuptools import setup, find_packages

REQUIREMENTS = (
    'django>=1.3',
)
TEST_REQUIREMENTS = (
    'south',
    'mock',
    'django-debug-toolbar',
)

from ckeditor import VERSION

setup(
    name="django-admin-ckeditor",
    version=VERSION,
    author="Aaron Madison",
    description="Ckeditor integration with Django admin.",
    long_description=open('README', 'r').read(),
    url="https://github.com/madisona/django-admin-ckeditor",
    packages=find_packages(exclude=["example"]),
    include_package_data=True,
    install_requires=REQUIREMENTS,
    tests_require=TEST_REQUIREMENTS,
    zip_safe=False,
    classifiers = [
        "Development Status :: 4 - Beta",
        "Environment :: Web Environment",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Software Development",
        "Topic :: Software Development :: Libraries :: Application Frameworks",
    ],
)