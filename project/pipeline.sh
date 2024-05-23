#!/bin/bash
python3 /project/pipeline.py


# IMPORTANT:
## Because the data pipeline is going to connect to kaggle, it is necessary that a kaggle API token is available on the
## local device under '~/.kaggle/kaggle.json' which extracts the data.
## The credintials must remain secret for the security messures 

