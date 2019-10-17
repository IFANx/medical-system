from setuptools import find_packages, setup

setup(
    name='medical-system',
    version='0.1',
    packages=find_packages,
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'flask',
        'Flask_SQLAlchemy'
    ],
)
