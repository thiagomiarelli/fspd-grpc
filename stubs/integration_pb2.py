# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: integration.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x11integration.proto\x12\x05unary\"G\n\x19RegisterIntegrationParams\x12\x0f\n\x07\x61\x64\x64ress\x18\x01 \x01(\t\x12\x0c\n\x04port\x18\x02 \x01(\x05\x12\x0b\n\x03ids\x18\x03 \x03(\x05\"-\n\x19RegisterIntegrationReturn\x12\x10\n\x08numOfIds\x18\x04 \x01(\x05\"\"\n\x14GetIntegrationParams\x12\n\n\x02id\x18\x05 \x01(\x05\"5\n\x14GetIntegrationReturn\x12\x0f\n\x07\x61\x64\x64ress\x18\x06 \x01(\t\x12\x0c\n\x04port\x18\x07 \x01(\x05\"\x1d\n\x1bStopIntegrationServerParams\"/\n\x1bStopIntegrationServerReturn\x12\x10\n\x08numOfIds\x18\x08 \x01(\x05\x32\x9b\x02\n\x0bIntegration\x12[\n\x13RegisterIntegration\x12 .unary.RegisterIntegrationParams\x1a .unary.RegisterIntegrationReturn\"\x00\x12L\n\x0eGetIntegration\x12\x1b.unary.GetIntegrationParams\x1a\x1b.unary.GetIntegrationReturn\"\x00\x12\x61\n\x15StopIntegrationServer\x12\".unary.StopIntegrationServerParams\x1a\".unary.StopIntegrationServerReturn\"\x00\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'integration_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _REGISTERINTEGRATIONPARAMS._serialized_start=28
  _REGISTERINTEGRATIONPARAMS._serialized_end=99
  _REGISTERINTEGRATIONRETURN._serialized_start=101
  _REGISTERINTEGRATIONRETURN._serialized_end=146
  _GETINTEGRATIONPARAMS._serialized_start=148
  _GETINTEGRATIONPARAMS._serialized_end=182
  _GETINTEGRATIONRETURN._serialized_start=184
  _GETINTEGRATIONRETURN._serialized_end=237
  _STOPINTEGRATIONSERVERPARAMS._serialized_start=239
  _STOPINTEGRATIONSERVERPARAMS._serialized_end=268
  _STOPINTEGRATIONSERVERRETURN._serialized_start=270
  _STOPINTEGRATIONSERVERRETURN._serialized_end=317
  _INTEGRATION._serialized_start=320
  _INTEGRATION._serialized_end=603
# @@protoc_insertion_point(module_scope)
