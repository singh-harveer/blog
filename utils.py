from google.protobuf.json_format import MessageToJson
import json

def message_to_Json(message):
	return MessageToJson(message)
