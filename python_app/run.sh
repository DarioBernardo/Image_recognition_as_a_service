#!/usr/bin/env bash
source activate flask_tensorflow
python maybe_download_and_extract.py
gunicorn -w 4 --bind :8080 main:app