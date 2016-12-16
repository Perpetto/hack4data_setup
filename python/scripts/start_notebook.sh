#!/bin/bash
cd notebook
PYSPARK_DRIVER_PYTHON=ipython PYSPARK_DRIVER_PYTHON_OPTS="notebook --ip 0.0.0.0" ~/PredictionIO-0.10.0-incubating/vendors/spark-1.5.1-bin-hadoop2.6/bin/pyspark
