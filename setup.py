from setuptools import setup, find_packages

setup(
        name='profilegrab',
        version='0.1',
        author="Charlie Hack",
        author_email="charlie@205consulting.com",
        description="Very simple social media scraping for Python.",
        packages=find_packages(),
        include_package_data=True,
        install_requires=[
            'pattern',
            'python-twitter',
        ]
)

