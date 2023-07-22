from elasticsearch import Elasticsearch
from confluent_kafka import Consumer

import json
import time

import logging

from .openai_utils import get_priority_and_explanation


def KafkatoElasticSearch():

    es = Elasticsearch("http://localhost:9200")
    consumer = Consumer({
                'bootstrap.servers': 'localhost:9092,localhost:9093,localhost:9094',
                'group.id': 'group_1',
                'auto.offset.reset': 'earliest',
                'max.poll.interval.ms': 1000000
                })
    
    # Subscribe to topic
    topic = "scf"
    consumer.subscribe([topic])

    try:
        while True:
            msg = consumer.poll(1.0)
            if msg is None:
                # Initial message consumption may take up to
                # `session.timeout.ms` for the consumer group to
                # rebalance and start consuming
                logging.info('Waiting...')
            elif msg.error():
                logging.error("ERROR: %s".format(msg.error()))
            else:
                str_msg = msg.value().decode("utf-8")
                doc = json.loads(str_msg)

                title = doc.get("request_type.title.keyword") 
                title = title if title else "No title"

                description = doc.get("description") 
                description = description if description else "No description"

                priority, explanation = get_priority_and_explanation(title, description)

                doc["priority"] = priority
                doc["priority_explanation"] = explanation

                actions = [{"_index": "users",
                    "_doc": "doc",
                    "_source": doc}]
        
                res = es.update(
                            index="scf_priority",
                            id=doc["id"],
                            body={
                                "doc": doc, 
                                "doc_as_upsert": True
                            }
                        )
                logging.info(res["result"])

                time.sleep(450) # Necessary to avoid hitting the rate limit from OpenAI

    except KeyboardInterrupt:
        pass
    finally:
        # Leave group and commit final offsets
        consumer.close()

if __name__ == "__main__":
    KafkatoElasticSearch()