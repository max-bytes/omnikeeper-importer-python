from typing import Union

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
