# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: environmentvariables.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)




DESCRIPTOR = _descriptor.FileDescriptor(
  name='environmentvariables.proto',
  package='',
  serialized_pb='\n\x1a\x65nvironmentvariables.proto\"M\n\x0bVariableSet\x12\r\n\x05setid\x18\x01 \x02(\t\x12\x19\n\x11\x63hromedriver_path\x18\x02 \x01(\t\x12\x14\n\x0curl_to_watch\x18\x03 \x01(\t\"9\n\x14\x45nvironmentVariables\x12!\n\x0bvariableset\x18\x01 \x03(\x0b\x32\x0c.VariableSet')




_VARIABLESET = _descriptor.Descriptor(
  name='VariableSet',
  full_name='VariableSet',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='setid', full_name='VariableSet.setid', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='chromedriver_path', full_name='VariableSet.chromedriver_path', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='url_to_watch', full_name='VariableSet.url_to_watch', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
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
  serialized_start=30,
  serialized_end=107,
)


_ENVIRONMENTVARIABLES = _descriptor.Descriptor(
  name='EnvironmentVariables',
  full_name='EnvironmentVariables',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='variableset', full_name='EnvironmentVariables.variableset', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=109,
  serialized_end=166,
)

_ENVIRONMENTVARIABLES.fields_by_name['variableset'].message_type = _VARIABLESET
DESCRIPTOR.message_types_by_name['VariableSet'] = _VARIABLESET
DESCRIPTOR.message_types_by_name['EnvironmentVariables'] = _ENVIRONMENTVARIABLES

class VariableSet(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _VARIABLESET

  # @@protoc_insertion_point(class_scope:VariableSet)

class EnvironmentVariables(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _ENVIRONMENTVARIABLES

  # @@protoc_insertion_point(class_scope:EnvironmentVariables)


# @@protoc_insertion_point(module_scope)
