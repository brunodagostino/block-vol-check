from setuptools import setup, find_packages

setup(
    name='block_vol_check',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'block_vol_check=block_vol_check.main:main',
        ],
    },
)
