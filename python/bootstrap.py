import pandas as pd
import json

#return a data frame of the results
def rows_to_df(rows):
    return pd.DataFrame(map(lambda e: e.asDict(), rows))

# return the result as a list of dictionaries
def rows_to_dict(rows):
    return map(lambda e: e.asDict(), rows)

# return an array of the n-th column of the results
def get_column(column_index, rows):
    data = []
    for row in summary:
        data.append(row[column_index])
    return data

# writes the result to a JSON file in the format {"data": [{...}, {...}, ... {...}]}
def write_to_json(file_name, rows):
    with open(file_name, 'w') as outfile:
        json.dump(dict(data = rows_to_dict(rows)), outfile)
    outfile.close()

from pyspark.sql import SQLContext
sqlc = SQLContext(sc)
