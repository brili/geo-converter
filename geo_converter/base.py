import logging

from .utils import get_file_type


class BaseConverter:
    _data = None
    _dataframe = None

    def __init__(self, input_file, output_file):
        self.input_file = input_file
        self.output_file = output_file
        self.output_file_type = get_file_type(output_file)

    def convert(self):
        self.parse()
        return getattr(self, f"to_{self.output_file_type}")()

    def parse(self):
        raise NotImplementedError

    # Dask dataframe to csv
    def to_csv(self):
        self._dataframe.to_csv(self.output_file, index=False, single_file=True)
        logging.info(
            "Conversion finished, output file: %s",
            self.output_file
        )
        return self.output_file

    def to_parquet(self):
        self._dataframe.to_parquet(self.output_file)
        return self.output_file
