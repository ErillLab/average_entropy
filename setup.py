from setuptools import setup, find_packages

setup(
    name='average_entropy',
    version='1.0.0',
    packages=["average_entropy"],
    package_dir={'':'src'},
    description='XXX',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Elia Mascolo',
    author_email='eliamascolo94@gmail.com',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)