from setuptools import setup  # type: ignore

# Send to pypi
# python3 setup.py sdist bdist_wheel
# twine upload dist/*

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='geo_converter',
    packages=['geo_converter'],
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
        'gdal==3.0.4',
        'netCDF4',
        'xarray',
    ],
    entry_points={
        'console_scripts': ['geo-converter=geo_converter.__main__:main'],
    }
)
