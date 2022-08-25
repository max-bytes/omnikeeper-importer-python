from typing import Union
from numpy import array
from requests.structures import CaseInsensitiveDict
import requests

def build_temp_id(*parts) -> str:
    return ' - '.join(parts)

def build_attribute(name: str, values: 'Union[list[str],str]', type: str = "Text", isArray: bool = False) -> dict:
    return {
        "name":name,
        "value":{
            "type": type,
            "isArray": isArray,
            "values": values if isinstance(values, list) else [values]
        }
    }

def build_id_method_data(attributes: dict) -> dict:
    return {"type": "OKPluginGenericJSONIngest.InboundIDMethodByData, OKPluginGenericJSONIngest", "attributes": attributes}

def build_id_method_attribute(attribute: dict) -> dict:
    return {
        "type": "OKPluginGenericJSONIngest.InboundIDMethodByAttribute, OKPluginGenericJSONIngest",
        "attribute": attribute,
        "modifiers": {
            "caseInsensitive": False
        }}

def build_id_method_intersect(inner: array) -> dict:
    return {
        "type": "OKPluginGenericJSONIngest.InboundIDMethodByIntersect, OKPluginGenericJSONIngest",
        "inner": inner
    }


def build_id_method_union(inner: array) -> dict:
    return {
        "type": "OKPluginGenericJSONIngest.InboundIDMethodByUnion, OKPluginGenericJSONIngest",
        "inner": inner
    }

def build_id_method_related_temp_id(tempID: str, outgoing: bool, predicateID: str) -> dict:
    return {
        "type": "OKPluginGenericJSONIngest.InboundIDMethodByRelatedTempID, OKPluginGenericJSONIngest",
        "tempID": tempID,
        "outgoingRelation": outgoing,
        "predicateID": predicateID
    }

def ingest(config: dict, cis: array, relations: array, access_token: str):
    api_url = f"%s/api/v1/ingest/genericJSON/data" % (config["url"])
    data = {
        "cis": cis,
        "relations": relations
    }
    params={
        "readLayerIDs": config["read_layer_ids"],
        "writeLayerID": config["write_layer_id"]
    }
    headers = CaseInsensitiveDict()
    headers["Authorization"] = f"Bearer %s" % access_token

    resp = requests.post(api_url, params=params, json=data, verify=False, headers=headers, timeout=config["timeout_seconds"])
    if resp.status_code != 200:
        raise Exception(f"Expected return code 200, received {resp.status_code}")
