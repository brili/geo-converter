import os
import hashlib

from pathlib import Path
from tempfile import NamedTemporaryFile
from geo_converter.factory import GeoConverterFactory

test_data_path = os.path.join('test', 'data')
test_tiff_file = os.path.join(test_data_path, 'dem.tif')
test_tiff_file_sha256 = 'c4bd9e26d3d485a6c395af032b5d697fc4fdf86313642fcded4e254a64b29474'
test_tiff_to_csv_sha256 = '8fb4630797f6c9f554d6eee6de2cd8d9e64be55de3183714b8fff384e01679dd'


class TestConverter:
    def test_tiff_integrity(self):
        file_sha256 = hashlib.sha256(Path(test_tiff_file).read_bytes()).hexdigest()
        assert file_sha256 == test_tiff_file_sha256

    def test_convert_tiff(self):
        with NamedTemporaryFile(suffix='.csv') as tmp:
            factory = GeoConverterFactory(test_tiff_file, tmp.name)
            converter = factory.get_converter()
            converter.parse()
            converter.to_csv()

            assert hashlib.sha256(Path(tmp.name).read_bytes()).hexdigest() \
                   == test_tiff_to_csv_sha256
