import xarray as xr

from geo_converter.base import BaseConverter


class NetcdfConverter(BaseConverter):
    def parse(self):
        self._data = xr.open_dataset(self.input_file)
        self._dataframe = self._data.to_dask_dataframe()
