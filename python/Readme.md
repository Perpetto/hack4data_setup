# Install Dependencies
```
sudo pip install -r requirements.txt
```

# Run Python Console
```
python
```

# Elasticsearch setup
```
from elasticsearch import Elasticsearch
es = Elasticsearch()
```

## Searching
```
client.search(index: 'profiles', type: 'session', body: {})
```

## Counting
```
client.count(index: 'profiles', type: 'session', body: {query: {term: {domain_id: 1}}})
```

## Iterating over documents in index with a given type
```
# the body parameter accepts a query
r = client.search(index: 'profiles', type: 'session', search_type: 'scan', scroll: '50s', body: {})
while r = client.scroll(scroll_id: r['_scroll_id'], scroll: '50s') and not r['hits']['hits'].empty? do
  r['hits']['hits'].each { |hit|
    # puts hit
  }
end
```

## Additional Resources
- [Elasticsearch Python SDK](https://elasticsearch-py.readthedocs.io/en/master/)
- [PredictionIO EventServer REST API](http://predictionio.incubator.apache.org/datacollection/eventapi/)
