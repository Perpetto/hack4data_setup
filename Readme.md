# elasticsearch setup
```
require 'elasticsearch'

client = Elasticsearch::Client.new log: true
```

## searching
```
client.search(index: 'profiles', type: 'session', body: {})
```

## counting
```
client.count(index: 'profiles', type: 'session', body: {query: {term: {domain_id: 1}}})
```

## iterating over documents in index with a given type
```
# the body parameter accepts a query
r = client.search(index: 'profiles', type: 'session', search_type: 'scan', scroll: '50s', body: {})
while r = client.scroll(scroll_id: r['_scroll_id'], scroll: '50s') and not r['hits']['hits'].empty? do
  r['hits']['hits'].each { |hit|
    # puts hit
  }
end
```
