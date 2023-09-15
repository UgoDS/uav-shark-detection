from kedro.config import ConfigLoader
from kedro.io import DataCatalog

# Initialise a ConfigLoader
conf_loader = ConfigLoader("conf")

# Load the data catalog configuration from catalog.yml
conf_catalog = conf_loader.get("catalog.yml")

# Create the DataCatalog instance from the configuration
catalog = DataCatalog.from_config(conf_catalog)

# Load the dataset and print the output
df = catalog.load("example_iris_data")
print(df.head())