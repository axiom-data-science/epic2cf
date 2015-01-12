# epic2cf

#### A simple python library to find the CF standard name equivalent of an EPIC code.

[EPIC codes](http://www.epic.noaa.gov/epic/document/epickey.htm)
[CF standard names](http://cfconventions.org/Data/cf-standard-names/28/build/cf-standard-name-table.html)


## Installation

##### Stable

    pip install epic2cf

##### Development

    pip install git+https://github.com/axiom-data-science/epic2cf.git


## Usage


##### Return contents

A `dict` like object is returned from a call to `get` and contains the following:
```python
{
    'cell_methods': None,   # If there are any cell_methods associated with this variable
    'cf_units': None,       # The units of the CF standard name
    'convert': None,        # A function to convert values from EPIC to CF
    'long_name': None,      # A description of the variable
    'standard_name': None,  # The CF standard_name
    'units': None           # The EPIC units
}
```

##### Get a CF mapping from an EPIC code

```python
from epic2cf import mapping

mapping.get(18)
{
    'cell_methods': None,
    'cf_units': 'm',
    'convert': <function epic2cf.data.<lambda>>,
    'long_name': 'Sea Surface Height',
    'standard_name': 'sea_surface_height',
    'units': 'm'
}

mapping.get(26)
{
    'cell_methods': 'time: minimum',
    'cf_units': 'K',
    'convert': <function epic2cf.data.<lambda>>,
    'long_name': 'Water Temperature',
    'standard_name': 'sea_water_temperature',
    'units': 'degree_Celsius'
}
```

##### Convert existing EPIC values into CF values

###### Pass in a numpy array to the convert function

```python
import numpy as np
from epic2cf import mapping

epic = mapping.get(9)
print epic
{
    'cell_methods': None,
    'cf_units': 'dbar',
    'convert': <function epic2cf.data.<lambda>>,
    'long_name': 'Sea Water Pressure',
    'standard_name': 'sea_water_pressure',
    'units': 'mbar'
}

values = np.random.random(6)
print values  # EPIC values in 'mbar'
array([ 0.57136167,  0.98046873,  0.64963954,  0.39981203,  0.72433581, 0.16820297])

cf_values = epic.convert(values)
print cf_values  # CF values in 'dbar'
array([ 0.00571362,  0.00980469,  0.0064964 ,  0.00399812,  0.00724336, 0.00168203])
```

## Contributing

Not all EPIC codes have been mapped to CF standard names.  If you require
a mappnig that has not been done you can do one of the following:

1.  Create an issue with the EPIC code number you would like mapped and as much
information about the variable as possible (how it is used, the units, etc).
It may take some time for these to be included in `epic2cf`, especially if we
can not verify a correct mapping to CF.

2. Fork the repository and add the mapping yourself into `epic2cf/data.py`.
I will accept pull requests for updated mapping very quickly.
