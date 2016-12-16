# Hello, and welcome to HackFMI 8 - Hack for data!

Today you will deal with the following technologies:
- [Elasticsearch](https://www.elastic.co/products/elasticsearch)
- [Apache Spark](http://spark.apache.org/) + [PredictionIO](http://predictionio.incubator.apache.org/)
- [Apache Hbase](https://hbase.apache.org/)

We have set up a server for you guys with some e-commerce data.

What you can do (these are **suggestions** - you can do **anything you like, really**!):
* Familiarize yourself with  [PredictionIO](http://predictionio.incubator.apache.org/) machine learning framework and [Spark](http://spark.apache.org/). Download a few of the example machine learning engines below and try to get them up and running:
  - [Similar Product](https://github.com/apache/incubator-predictionio-template-similar-product)
  - [Ecommerce Recommendation](https://github.com/apache/incubator-predictionio-template-ecom-recommender)
  - [Frequent Pattern Mining](https://github.com/goliasz/pio-template-fpm)
  - [Complementary Purchase](https://github.com/PredictionIO/template-scala-parallel-complementarypurchase)
  - [Product Ranking](https://github.com/PredictionIO/template-scala-parallel-productranking)
  
  When you try and use the templates, you can change engine.json as follows to utilize the e-commerce dataset we have prepared for you:
  
  - If the file contains an 'appId' key, change it to 1.
  - If the file contains an 'appName' key, change it to 'perpetto'.
  
* Get familiar with Elasticsearch by running aggregations and gathering statistics. Some examples ay be:
  - Most Popoular Categories / Brands by Sessions
  - Most Popular Categories / Brands by Orders
  - Most Popular Items
  - Most Active Users
  - Months with the Most Orders
  - Most Effective Slots by Viewed Recommendations (ask us for details on this one)





The server contains the following:



I.Elasticsearch instance, containing e-commerce data as follows:

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
$set events are used to set properties for entities.

view / buys events are used to store relationships between users and items.

'pid' is the profile id for a profile document in elasticsearch.

'iid' is the item id for an item document in elasticsearch.


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
