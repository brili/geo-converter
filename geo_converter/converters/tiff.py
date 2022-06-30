import os

from tempfile import NamedTemporaryFile
import dask.dataframe as dd
from osgeo import gdal


from geo_converter.base import BaseConverter


class TiffConverter(BaseConverter):
    tmp = None

    def parse(self):
        self._data = gdal.Open(self.input_file)
        self.tmp = NamedTemporaryFile(suffix='.xyz', delete=False)
        gdal.Translate(self.tmp.name, self._data)
        self._dataframe = dd.read_csv(self.tmp.name, sep=" ", header=None)
        self._dataframe.columns = ["lat", "lng", 'value']

    def __del__(self):
        os.unlink(self.tmp.name)
