# Install Dependencies
```
bundle install
```

# Run Ruby Console
```
bundle exec irb
```

# Elasticsearch setup
```
require 'elasticsearch'

client = Elasticsearch::Client.new log: true
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
- [Elasticsearch Ruby SDK](http://www.rubydoc.info/gems/elasticsearch-api)
- [PredictionIO EventServer REST API](http://predictionio.incubator.apache.org/datacollection/eventapi/)
