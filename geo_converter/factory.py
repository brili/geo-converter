import logging
from pathlib import Path

from geo_converter.converters.tiff import TiffConverter

CONVERTERS = {
    "tif": TiffConverter,
    "tiff": TiffConverter,
}

ALLOWED_OUTPUT_FORMATS = ['csv']
DEFAULT_OUTPUT = 'csv'


class GeoConverterFactory:
    def __init__(self, input_file, output_file):
        self._converters = CONVERTERS
        self.input_file = input_file
        logging.info("Conversion started, input file: %s", self.input_file)
        self.output_file_type = \
            self.get_file_type(output_file) if output_file else DEFAULT_OUTPUT
        if self.output_file_type not in ALLOWED_OUTPUT_FORMATS:
            raise ValueError(
                f"Output format {self.output_file_type} not supported"
            )
        self.output_file = \
            output_file or f'{Path(input_file).stem}.{self.output_file_type}'

    @staticmethod
    def get_file_type(name):
        return name.split('.')[-1]

    def register_converter(self, file_type, converter):
        self._converters[file_type] = converter

    def get_converter(self):
        file_type = self.get_file_type(self.input_file)
        converter = self._converters.get(file_type)

        if not converter:
            raise ValueError(
                f"Converter for file type {file_type} doesn't exist"
            )

        return converter(self.input_file, self.output_file)
