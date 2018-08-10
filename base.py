import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from google.protobuf.json_format import MessageToJson
import json



_DB_USER_NAME=os.environ.get('DB_USER')
_DB_PASSWORD=os.environ.get('DB_PASSWORD')
_DB_HOST='localhost'
_DB_PORT='3306'
_DB_NAME='blogdata'
_DB_URL=f'mysql+mysqldb://{_DB_USER_NAME}:{_DB_PASSWORD}@{_DB_HOST}:{_DB_PORT}/{_DB_NAME}'
#print(_DB_URL)

engine=create_engine(_DB_URL,echo=False)
Base=declarative_base()
Base.metadata.bind=engine


def getSession():
	Base.metadata.create_all(engine)
	Session =sessionmaker(bind=engine)
	return Session()


def protobuf_to_json(message, including_default_value_fields=True,preserving_proto_field_name=True):
	message.DiscardUnknownFields()
	data = json.loads(MessageToJson(message, including_default_value_fields,
 	preserving_proto_field_name))
	return {k: v for k, v in data.items() if str(v)}




	
