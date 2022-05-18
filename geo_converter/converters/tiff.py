import logging
from tempfile import NamedTemporaryFile
import dask.dataframe as dd
from osgeo import gdal


from geo_converter.base import BaseConverter


class TiffConverter(BaseConverter):
    def parse(self):
        self.data = gdal.Open(self.input_file)

    def to_csv(self):
        with NamedTemporaryFile(suffix='.xyz') as tmp:
            gdal.Translate(tmp.name, self.data)
            ddf = dd.read_csv(tmp.name, sep=" ", header=None)
            ddf.columns = ["lat", "lng", 'elevation']
            ddf.to_csv(self.output_file, index=False, single_file=True)
            logging.info(
                "Conversion finished, output file: %s",
                self.output_file
            )
