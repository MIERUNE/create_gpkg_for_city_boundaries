#!/bin/bash

pipenv run python 01_download_shps.py
pipenv run python 02_merge_shp_to_gpkg.py
pipenv run python 03_add_zone_to_city_boundary.py