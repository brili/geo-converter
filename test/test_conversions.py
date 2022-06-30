import os
import hashlib

from pathlib import Path
from tempfile import NamedTemporaryFile
from geo_converter.factory import GeoConverterFactory

test_data_path = os.path.join('test', 'data')
test_tiff_file = os.path.join(test_data_path, 'dem.tif')
test_tiff_file_sha256 = 'c4bd9e26d3d485a6c395af032b5d697fc4fdf86313642fcded4e254a64b29474'
test_tiff_to_csv_sha256 = '53eaf714225c38103435cb723b0f1523e9e4321a754a546dc02fc361f62347fe'

test_netcdf_file = os.path.join(test_data_path, 'sresa1b_ncar_ccsm3-example.nc')
test_netcdf_file_sha256 = '2c2047ee329654f3bebf0a4b0d99eada50f1183728a3c7c129b0bc50d404511b'
test_netcdf_to_csv_sha256 = '4b46700979661f577e05048bbb2bb22004fcaef236d2996149448f55deeee217'


class TestConverter:
    def test_tiff_integrity(self):
        file_sha256 = hashlib.sha256(Path(test_tiff_file).read_bytes()).hexdigest()
        assert file_sha256 == test_tiff_file_sha256

    def test_convert_tiff(self):
        with NamedTemporaryFile(suffix='.csv') as tmp:
            factory = GeoConverterFactory(test_tiff_file, tmp.name)
            converter = factory.get_converter()
            converter.convert()

            assert hashlib.sha256(Path(tmp.name).read_bytes()).hexdigest() \
                   == test_tiff_to_csv_sha256

    def test_convert_netcdf(self):
        with NamedTemporaryFile(suffix='.csv') as tmp:
            factory = GeoConverterFactory(test_netcdf_file, tmp.name)
            converter = factory.get_converter()
            converter.convert()

            assert hashlib.sha256(Path(tmp.name).read_bytes()).hexdigest() \
                   == test_netcdf_to_csv_sha256
