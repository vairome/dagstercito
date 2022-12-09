from dagster import op
import pandas as pd


@op
def load_data(context, data_path):
    # Code for loading the data goes here
    data = pd.read_csv(data_path)
    context.log.info(f"Loaded data with shape {data.shape}")
    return data
