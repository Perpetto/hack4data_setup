# Install Dependencies
```
sudo pip install -r requirements.txt
```

# Run Python Console
```
python
# do stuff with elasticsearch
```

# Play around with Spark (Web-based, can daw histograms, save as PDF, etc!)
```
scripts/start_notebook.sh
# Note the port number where it's running, then in a separate terminal, create a tunnel:

ssh -A -L 8888:localhost:<port> <user>@ptto-hackfmi.westeurope.cloudapp.azure.com
```

# Play around with Spark (Shell-based)
```
scripts/start_ipython.sh
# !! IMPORTANT: paste the commands below one per line or it won't work
%run -i 'bootstrap.py'

# load a dump of our HBASE data
# You now have an RDD that you can apply transofmrations to. See the Spark programming guide link below.
rdd = sqlc.read.parquet("/tmp/perpetto-dump-new.parquet")

# You now have a Hive table that you can use to run queries against the data.
rdd.registerTempTable("events")

# Execute a Query
summary = sqlc.sql("SELECT "
                   "entityType, event, targetEntityType, COUNT(*) AS c "
                   "FROM events "
                   "GROUP BY entityType, event, targetEntityType").collect()

# Visualize Result as Table
rows_to_df(summary)

# Save Result to File (Locally)
write_to_json("results.json", summary)
```


## Additional Resources
- [Spark Programming Guide](http://spark.apache.org/docs/1.6.2/programming-guide.html) (Look at Python examples)
- [Elasticsearch Python SDK](https://elasticsearch-py.readthedocs.io/en/master/)
- [PredictionIO EventServer REST API](http://predictionio.incubator.apache.org/datacollection/eventapi/)
