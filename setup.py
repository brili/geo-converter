import subprocess
from setuptools import setup, find_packages  # type: ignore

# Send to pypi
# python3 setup.py sdist bdist_wheel
# twine upload dist/*

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

GDAL_VERSION=subprocess.getoutput("gdal-config --version")

setup(
    name='geo_converter',
    packages=find_packages(),
    version='0.0.1',
    python_requires=">=3.8",
    description='Convert various geo formats (tiff, netcdf into csv)',
    author='Brilant Kasami',
    author_email='brilant@mit.edu',
    url='https://github.mit.edu/MCSC-DataHub/geo_converter',
    keywords=['tiff', 'netcdf', 'geoTIFF'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: MIT License",
    ],
    install_requires=[
        'cftime',
        "pyproj",
        "zarr",
        "numpy",
        "h3",
        'dask',
        'pandas',
        f'pygdal=={GDAL_VERSION}.*',
        'netCDF4',
        'xarray',
        'pyarrow',
    ],
    entry_points={
        'console_scripts': ['geo-converter=geo_converter.__main__:main'],
    }
)
