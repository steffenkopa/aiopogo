# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/data/logs/action_log_entry.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pogoprotos.data.logs import catch_pokemon_log_entry_pb2 as pogoprotos_dot_data_dot_logs_dot_catch__pokemon__log__entry__pb2
from pogoprotos.data.logs import fort_search_log_entry_pb2 as pogoprotos_dot_data_dot_logs_dot_fort__search__log__entry__pb2
from pogoprotos.data.logs import buddy_pokemon_log_entry_pb2 as pogoprotos_dot_data_dot_logs_dot_buddy__pokemon__log__entry__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/data/logs/action_log_entry.proto',
  package='pogoprotos.data.logs',
  syntax='proto3',
  serialized_pb=_b('\n+pogoprotos/data/logs/action_log_entry.proto\x12\x14pogoprotos.data.logs\x1a\x32pogoprotos/data/logs/catch_pokemon_log_entry.proto\x1a\x30pogoprotos/data/logs/fort_search_log_entry.proto\x1a\x32pogoprotos/data/logs/buddy_pokemon_log_entry.proto\"\x8a\x02\n\x0e\x41\x63tionLogEntry\x12\x14\n\x0ctimestamp_ms\x18\x01 \x01(\x03\x12\r\n\x05sfida\x18\x02 \x01(\x08\x12\x43\n\rcatch_pokemon\x18\x03 \x01(\x0b\x32*.pogoprotos.data.logs.CatchPokemonLogEntryH\x00\x12?\n\x0b\x66ort_search\x18\x04 \x01(\x0b\x32(.pogoprotos.data.logs.FortSearchLogEntryH\x00\x12\x43\n\rbuddy_pokemon\x18\x05 \x01(\x0b\x32*.pogoprotos.data.logs.BuddyPokemonLogEntryH\x00\x42\x08\n\x06\x41\x63tionb\x06proto3')
  ,
  dependencies=[pogoprotos_dot_data_dot_logs_dot_catch__pokemon__log__entry__pb2.DESCRIPTOR,pogoprotos_dot_data_dot_logs_dot_fort__search__log__entry__pb2.DESCRIPTOR,pogoprotos_dot_data_dot_logs_dot_buddy__pokemon__log__entry__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_ACTIONLOGENTRY = _descriptor.Descriptor(
  name='ActionLogEntry',
  full_name='pogoprotos.data.logs.ActionLogEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='timestamp_ms', full_name='pogoprotos.data.logs.ActionLogEntry.timestamp_ms', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sfida', full_name='pogoprotos.data.logs.ActionLogEntry.sfida', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='catch_pokemon', full_name='pogoprotos.data.logs.ActionLogEntry.catch_pokemon', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='fort_search', full_name='pogoprotos.data.logs.ActionLogEntry.fort_search', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='buddy_pokemon', full_name='pogoprotos.data.logs.ActionLogEntry.buddy_pokemon', index=4,
      number=5, type=11, cpp_type=10, label=1,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='Action', full_name='pogoprotos.data.logs.ActionLogEntry.Action',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=224,
  serialized_end=490,
)

_ACTIONLOGENTRY.fields_by_name['catch_pokemon'].message_type = pogoprotos_dot_data_dot_logs_dot_catch__pokemon__log__entry__pb2._CATCHPOKEMONLOGENTRY
_ACTIONLOGENTRY.fields_by_name['fort_search'].message_type = pogoprotos_dot_data_dot_logs_dot_fort__search__log__entry__pb2._FORTSEARCHLOGENTRY
_ACTIONLOGENTRY.fields_by_name['buddy_pokemon'].message_type = pogoprotos_dot_data_dot_logs_dot_buddy__pokemon__log__entry__pb2._BUDDYPOKEMONLOGENTRY
_ACTIONLOGENTRY.oneofs_by_name['Action'].fields.append(
  _ACTIONLOGENTRY.fields_by_name['catch_pokemon'])
_ACTIONLOGENTRY.fields_by_name['catch_pokemon'].containing_oneof = _ACTIONLOGENTRY.oneofs_by_name['Action']
_ACTIONLOGENTRY.oneofs_by_name['Action'].fields.append(
  _ACTIONLOGENTRY.fields_by_name['fort_search'])
_ACTIONLOGENTRY.fields_by_name['fort_search'].containing_oneof = _ACTIONLOGENTRY.oneofs_by_name['Action']
_ACTIONLOGENTRY.oneofs_by_name['Action'].fields.append(
  _ACTIONLOGENTRY.fields_by_name['buddy_pokemon'])
_ACTIONLOGENTRY.fields_by_name['buddy_pokemon'].containing_oneof = _ACTIONLOGENTRY.oneofs_by_name['Action']
DESCRIPTOR.message_types_by_name['ActionLogEntry'] = _ACTIONLOGENTRY

ActionLogEntry = _reflection.GeneratedProtocolMessageType('ActionLogEntry', (_message.Message,), dict(
  DESCRIPTOR = _ACTIONLOGENTRY,
  __module__ = 'pogoprotos.data.logs.action_log_entry_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.data.logs.ActionLogEntry)
  ))
_sym_db.RegisterMessage(ActionLogEntry)


# @@protoc_insertion_point(module_scope)
