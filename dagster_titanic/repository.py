from dagster import load_assets_from_package_module, repository

from dagster_titanic import assets


@repository
def dagster_titanic():
    return [load_assets_from_package_module(assets)]
