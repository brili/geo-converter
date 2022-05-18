# Geo Converter
Convert various geo formats (tiff, netcdf into csv)

### Dependencies
Installing this package is as easy as:

Ubuntu:
```console
sudo apt-get install libgdal-dev
```

Mac:
```console
brew install gdal
```

### Installation

Install python dependencies
```console
pip install .
```

### Usage
```console
geo-converter -i dem.tif -o output.csv
```
`-i` is mandatory, `-o` is optional and if ommited will take the name of the input file

#### Making the GeoTiff object

```python
factory = GeoConverterFactory(args.input, args.output)
converter = factory.get_converter()
converter.parse()
converter.to_csv()
```


#### Create new converter

Create a new converter class extending BaseConverter and register it:

```python
factory = GeoConverterFactory(args.input, args.output)
factory.register_converter(file_type, converter_class)
```


### Project Road Map

#### Core Features

- [x] Convert tiff files to csv
- [ ] Convert netcdf files to csv


### Troubleshhoot

If there are issues while installing gdal run and make sure you have the same gdal version in setup.py
```console
gdal-config --version
```
