import xarray as xr
import pandas as pd
 
def read_noaa(filename: str) -> xr.Dataset:
    """Read the netCDF file downloaded using `download_noaa`.
 
    Parameters
    ----------
    filename : str
        The name of the file to read as `xarray.Dataset`
 
    Returns
    -------
    `xarray.Dataset`
    """
    return xr.open_dataset(filename)
 
def get_noaa_timeseries(
        xarr: xr.Dataset, 
        lon: Union[int, float], 
        lat: Union[int, float]
    ) -> xr.Dataset:
    """Get the annual temperature anomaly time series from NOAA data.
 
    Parameters
    ----------
    xarr : xr.Dataset
        `xarray.Dataset` containing the monthly anomalies.
    lon : Union[int, float]
        Longitude in decimal degrees. It will return the closest timeseries
        to this location.
    lat : Union[int, float]
        Latitude in decimal degrees. It will return the closest timeseries
        to this location.
 
    Returns
    -------
    `xarray.Dataset`.
    """
    data = xarr.sel(lon=lon, lat=lat, z=0, method='nearest')
    df = data.to_dataframe()['anom']
    ts = df * df.index.days_in_month
    ts = (     
        ts.groupby(pd.Grouper(freq='Y')).mean()      
        /      
        ts.groupby(pd.Grouper(freq='Y')).count() 
    )
    return ts