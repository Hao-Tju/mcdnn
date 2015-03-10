# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto/request.proto

from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)




DESCRIPTOR = _descriptor.FileDescriptor(
  name='proto/request.proto',
  package='uw.syhan.mcdnn',
  serialized_pb='\n\x13proto/request.proto\x12\x0euw.syhan.mcdnn\"T\n\nDNNRequest\x12)\n\x04type\x18\x01 \x02(\x0e\x32\x1b.uw.syhan.mcdnn.RequestType\x12\r\n\x05layer\x18\x02 \x01(\x05\x12\x0c\n\x04\x64\x61ta\x18\x03 \x01(\x0c\"?\n\x0b\x44NNResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x0f\n\x07latency\x18\x02 \x01(\x01\x12\x0e\n\x06result\x18\x03 \x01(\x05*\x17\n\x0bRequestType\x12\x08\n\x04\x46\x41\x43\x45\x10\x01')

_REQUESTTYPE = _descriptor.EnumDescriptor(
  name='RequestType',
  full_name='uw.syhan.mcdnn.RequestType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='FACE', index=0, number=1,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=190,
  serialized_end=213,
)

RequestType = enum_type_wrapper.EnumTypeWrapper(_REQUESTTYPE)
FACE = 1



_DNNREQUEST = _descriptor.Descriptor(
  name='DNNRequest',
  full_name='uw.syhan.mcdnn.DNNRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='uw.syhan.mcdnn.DNNRequest.type', index=0,
      number=1, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='layer', full_name='uw.syhan.mcdnn.DNNRequest.layer', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='data', full_name='uw.syhan.mcdnn.DNNRequest.data', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=39,
  serialized_end=123,
)


_DNNRESPONSE = _descriptor.Descriptor(
  name='DNNResponse',
  full_name='uw.syhan.mcdnn.DNNResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='success', full_name='uw.syhan.mcdnn.DNNResponse.success', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='latency', full_name='uw.syhan.mcdnn.DNNResponse.latency', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='result', full_name='uw.syhan.mcdnn.DNNResponse.result', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=125,
  serialized_end=188,
)

_DNNREQUEST.fields_by_name['type'].enum_type = _REQUESTTYPE
DESCRIPTOR.message_types_by_name['DNNRequest'] = _DNNREQUEST
DESCRIPTOR.message_types_by_name['DNNResponse'] = _DNNRESPONSE

class DNNRequest(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _DNNREQUEST

  # @@protoc_insertion_point(class_scope:uw.syhan.mcdnn.DNNRequest)

class DNNResponse(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _DNNRESPONSE

  # @@protoc_insertion_point(class_scope:uw.syhan.mcdnn.DNNResponse)


# @@protoc_insertion_point(module_scope)