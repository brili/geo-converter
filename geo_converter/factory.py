import logging

from pathlib import Path

from .converters.netcdf import NetcdfConverter
from .converters.tiff import TiffConverter
from .utils import get_file_type

CONVERTERS = {
    "tif": TiffConverter,
    "tiff": TiffConverter,
    "nc": NetcdfConverter
}

ALLOWED_OUTPUT_FORMATS = ['csv', 'parquet']
DEFAULT_OUTPUT = 'parquet'


class GeoConverterFactory:
    def __init__(self, input_file, output_file):
        self._converters = CONVERTERS
        self.input_file = input_file
        logging.info("Conversion started, input file: %s", self.input_file)
        self.output_file_type = \
            get_file_type(output_file) if output_file else DEFAULT_OUTPUT
        if self.output_file_type not in ALLOWED_OUTPUT_FORMATS:
            raise ValueError(
                f"Output format {self.output_file_type} not supported"
            )
        self.output_file = \
            output_file or f'{Path(input_file).stem}.{self.output_file_type}'

    def register_converter(self, file_type, converter):
        self._converters[file_type] = converter

    def get_converter(self):
        file_type = get_file_type(self.input_file)
        converter = self._converters.get(file_type)

        if not converter:
            raise ValueError(
                f"Converter for file type {file_type} doesn't exist"
            )

        return converter(self.input_file, self.output_file)
