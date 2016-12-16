# Hello, and welcome to HackFMI 8 - Hack for data!

Today you will deal with the following technologies:
- Elasticsearch
- Spark + PredictionIO
- Hbase

We have set up a server for you guys with some e-commerce data.
The server contins the following

I.Elasticsearch instance, containing the following:

- profiles (index)
  - profile (type) - contains profile data
  - session (type) - contains profile session data. Each session is basically a collection of visits on the e-commerce site wihtin a 24-hour interval.
  - order (type) - contains profile cart/order data. A cart whill have a paid: true property if it has been purchased.
- items (index)
  - item (type) - contains item data


II.Hbase / PredictionIO instance, containing e-commerce data in the form of events:
```
eventType    entityType    entityId    targetEntityType    targetEntityId    eventTime         properties
'$set'       'user'        <pid>       -                   -                 (ignore)          -
'$set'       'item'        <iid>       -                   -                 (ignore)          <item props from elasticsearch>
'buy'        'user'        <pid>       'item'              <iid>             <ISO 8601 date>   -
'view'        'user'       <pid>       'item'              <iid>             <ISO 8601 date>   -
```
$set events are used to set properties for entities
view /buys events are used to store relationships between users and items.
<pid> is the profile id for a profile document in elasticsearch
<iid> is the item id for an item document in elasticsearch


# Elasticsearch setup
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
