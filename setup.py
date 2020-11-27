from setuptools import find_packages, setup

setup(
    name='iq',
    version='1.1.2',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'flask',
        'wheel',
    ],
)
