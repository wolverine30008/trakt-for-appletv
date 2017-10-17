# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: UpdateContentItemMessage.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import ProtocolMessage_pb2 as ProtocolMessage__pb2
from . import ContentItem_pb2 as ContentItem__pb2
from . import PlayerPath_pb2 as PlayerPath__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='UpdateContentItemMessage.proto',
  package='',
  syntax='proto2',
  serialized_pb=_b('\n\x1eUpdateContentItemMessage.proto\x1a\x15ProtocolMessage.proto\x1a\x11\x43ontentItem.proto\x1a\x10PlayerPath.proto\"_\n\x18UpdateContentItemMessage\x12\"\n\x0c\x63ontentItems\x18\x01 \x03(\x0b\x32\x0c.ContentItem\x12\x1f\n\nplayerPath\x18\x02 \x01(\x0b\x32\x0b.PlayerPath:M\n\x18updateContentItemMessage\x12\x10.ProtocolMessage\x18< \x01(\x0b\x32\x19.UpdateContentItemMessage')
  ,
  dependencies=[ProtocolMessage__pb2.DESCRIPTOR,ContentItem__pb2.DESCRIPTOR,PlayerPath__pb2.DESCRIPTOR,])


UPDATECONTENTITEMMESSAGE_FIELD_NUMBER = 60
updateContentItemMessage = _descriptor.FieldDescriptor(
  name='updateContentItemMessage', full_name='updateContentItemMessage', index=0,
  number=60, type=11, cpp_type=10, label=1,
  has_default_value=False, default_value=None,
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  options=None)


_UPDATECONTENTITEMMESSAGE = _descriptor.Descriptor(
  name='UpdateContentItemMessage',
  full_name='UpdateContentItemMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='contentItems', full_name='UpdateContentItemMessage.contentItems', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='playerPath', full_name='UpdateContentItemMessage.playerPath', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=94,
  serialized_end=189,
)

_UPDATECONTENTITEMMESSAGE.fields_by_name['contentItems'].message_type = ContentItem__pb2._CONTENTITEM
_UPDATECONTENTITEMMESSAGE.fields_by_name['playerPath'].message_type = PlayerPath__pb2._PLAYERPATH
DESCRIPTOR.message_types_by_name['UpdateContentItemMessage'] = _UPDATECONTENTITEMMESSAGE
DESCRIPTOR.extensions_by_name['updateContentItemMessage'] = updateContentItemMessage
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

UpdateContentItemMessage = _reflection.GeneratedProtocolMessageType('UpdateContentItemMessage', (_message.Message,), dict(
  DESCRIPTOR = _UPDATECONTENTITEMMESSAGE,
  __module__ = 'UpdateContentItemMessage_pb2'
  # @@protoc_insertion_point(class_scope:UpdateContentItemMessage)
  ))
_sym_db.RegisterMessage(UpdateContentItemMessage)

updateContentItemMessage.message_type = _UPDATECONTENTITEMMESSAGE
ProtocolMessage__pb2.ProtocolMessage.RegisterExtension(updateContentItemMessage)

# @@protoc_insertion_point(module_scope)