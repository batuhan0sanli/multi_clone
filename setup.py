from setuptools import setup, find_packages

from os import path

# The directory containing this file
PATH = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(PATH, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='rclone-manager',
    version='0.3.2',
    description='Define multiple tasks using rclone',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/batuhan0sanli/rclone-manager',
    author='batuhan0sanli',
    author_email='batuhansanli@gmail.com',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ],
    keywords='rclone manager sync copy move file',
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    python_requires='>=3.8',
)
