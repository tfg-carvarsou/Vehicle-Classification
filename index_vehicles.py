
from elasticsearch import Elasticsearch

class RoboflowVehiclesIndex:
    INDEX_NAME = 'roboflow-vehicles'
    INDEX_SETTINGS = {
        "mappings": {
            "properties": {
                "filename": {
                    "type": "text"
                },
                "size": {
                    "type": "text"
                },
                "vehicles": {
                    "type": "text"
                }
            }
        }
    }

    def index_image(es: Elasticsearch, index_name: str, image_dict: dict):
        res = es.index(index=index_name, id=image_dict['filename'], document=image_dict)
        print(res)

    def reset_index(es: Elasticsearch, index_name: str, index_settings: dict):
        if es.indices.exists(index=index_name):
            es.indices.delete(index=index_name)
        es.indices.create(index=index_name, body=index_settings)
