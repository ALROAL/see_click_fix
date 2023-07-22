# Priority SeeClickFix
SeeClickFix 311 CRM by CivicPlus® is a 311 solution that empowers residents to report issues, identify repair needs, share feedback, and ask questions of their local government leaders. The result is collaborative experiences between governments and residents that co-create clean, safe, and happy communities.

Everyday numerous issues are reported and the implementation of a prioritizing system could help to better distribute the resources and attend the issues with a higher impact on the community. 

This project uses Apache NiFi and Kafka to extract and process new reports from SeeClickFix API, assigns the reports a priority level using OpenAI API, stores the data in ElasticSearch and offers a visualization Dashboard in Kibana.

## Data pipeline

![data_pipeline](https://i.imgur.com/css4m4r.png)

## Kibana Dashboard

![kibana_dashboard](https://i.imgur.com/0aakdY0.png)

## NiFi Flow

![nifi_flow](https://i.imgur.com/erA02Eo.png)
