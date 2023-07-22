# Priority SeeClickFix
SeeClickFix 311 CRM by CivicPlus® is a 311 solution that empowers residents to report issues, identify repair needs, share feedback, and ask questions of their local government leaders. The result is collaborative experiences between governments and residents that co-create clean, safe, and happy communities.

Everyday numerous issues are reported and the implementation of a prioritizing system could help to better distribute the resources and attend the issues with a higher impact on the community. 

This project uses Apache NiFi to extract and process new reports from SeeClickFix API, assigns the reports a priority level using OpenAI API, stores the data in ElasticSearch and offers a visualization Dashboard in Kibana.
