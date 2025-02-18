#
# Licensed to the Apache Software Foundation (ASF) under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# The ASF licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: spark/connect/expressions.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pyspark.sql.connect.proto import types_pb2 as spark_dot_connect_dot_types__pb2
from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\x1fspark/connect/expressions.proto\x12\rspark.connect\x1a\x19spark/connect/types.proto\x1a\x19google/protobuf/any.proto"\xf0\x17\n\nExpression\x12=\n\x07literal\x18\x01 \x01(\x0b\x32!.spark.connect.Expression.LiteralH\x00R\x07literal\x12\x62\n\x14unresolved_attribute\x18\x02 \x01(\x0b\x32-.spark.connect.Expression.UnresolvedAttributeH\x00R\x13unresolvedAttribute\x12_\n\x13unresolved_function\x18\x03 \x01(\x0b\x32,.spark.connect.Expression.UnresolvedFunctionH\x00R\x12unresolvedFunction\x12Y\n\x11\x65xpression_string\x18\x04 \x01(\x0b\x32*.spark.connect.Expression.ExpressionStringH\x00R\x10\x65xpressionString\x12S\n\x0funresolved_star\x18\x05 \x01(\x0b\x32(.spark.connect.Expression.UnresolvedStarH\x00R\x0eunresolvedStar\x12\x37\n\x05\x61lias\x18\x06 \x01(\x0b\x32\x1f.spark.connect.Expression.AliasH\x00R\x05\x61lias\x1a\xa3\x10\n\x07Literal\x12\x1a\n\x07\x62oolean\x18\x01 \x01(\x08H\x00R\x07\x62oolean\x12\x10\n\x02i8\x18\x02 \x01(\x05H\x00R\x02i8\x12\x12\n\x03i16\x18\x03 \x01(\x05H\x00R\x03i16\x12\x12\n\x03i32\x18\x05 \x01(\x05H\x00R\x03i32\x12\x12\n\x03i64\x18\x07 \x01(\x03H\x00R\x03i64\x12\x14\n\x04\x66p32\x18\n \x01(\x02H\x00R\x04\x66p32\x12\x14\n\x04\x66p64\x18\x0b \x01(\x01H\x00R\x04\x66p64\x12\x18\n\x06string\x18\x0c \x01(\tH\x00R\x06string\x12\x18\n\x06\x62inary\x18\r \x01(\x0cH\x00R\x06\x62inary\x12\x1e\n\ttimestamp\x18\x0e \x01(\x03H\x00R\ttimestamp\x12\x14\n\x04\x64\x61te\x18\x10 \x01(\x05H\x00R\x04\x64\x61te\x12\x14\n\x04time\x18\x11 \x01(\x03H\x00R\x04time\x12l\n\x16interval_year_to_month\x18\x13 \x01(\x0b\x32\x35.spark.connect.Expression.Literal.IntervalYearToMonthH\x00R\x13intervalYearToMonth\x12l\n\x16interval_day_to_second\x18\x14 \x01(\x0b\x32\x35.spark.connect.Expression.Literal.IntervalDayToSecondH\x00R\x13intervalDayToSecond\x12\x1f\n\nfixed_char\x18\x15 \x01(\tH\x00R\tfixedChar\x12\x46\n\x08var_char\x18\x16 \x01(\x0b\x32).spark.connect.Expression.Literal.VarCharH\x00R\x07varChar\x12#\n\x0c\x66ixed_binary\x18\x17 \x01(\x0cH\x00R\x0b\x66ixedBinary\x12\x45\n\x07\x64\x65\x63imal\x18\x18 \x01(\x0b\x32).spark.connect.Expression.Literal.DecimalH\x00R\x07\x64\x65\x63imal\x12\x42\n\x06struct\x18\x19 \x01(\x0b\x32(.spark.connect.Expression.Literal.StructH\x00R\x06struct\x12\x39\n\x03map\x18\x1a \x01(\x0b\x32%.spark.connect.Expression.Literal.MapH\x00R\x03map\x12#\n\x0ctimestamp_tz\x18\x1b \x01(\x03H\x00R\x0btimestampTz\x12\x14\n\x04uuid\x18\x1c \x01(\x0cH\x00R\x04uuid\x12-\n\x04null\x18\x1d \x01(\x0b\x32\x17.spark.connect.DataTypeH\x00R\x04null\x12<\n\x04list\x18\x1e \x01(\x0b\x32&.spark.connect.Expression.Literal.ListH\x00R\x04list\x12=\n\nempty_list\x18\x1f \x01(\x0b\x32\x1c.spark.connect.DataType.ListH\x00R\temptyList\x12:\n\tempty_map\x18  \x01(\x0b\x32\x1b.spark.connect.DataType.MapH\x00R\x08\x65mptyMap\x12R\n\x0cuser_defined\x18! \x01(\x0b\x32-.spark.connect.Expression.Literal.UserDefinedH\x00R\x0buserDefined\x12\x1a\n\x08nullable\x18\x32 \x01(\x08R\x08nullable\x12\x38\n\x18type_variation_reference\x18\x33 \x01(\rR\x16typeVariationReference\x1a\x37\n\x07VarChar\x12\x14\n\x05value\x18\x01 \x01(\tR\x05value\x12\x16\n\x06length\x18\x02 \x01(\rR\x06length\x1aS\n\x07\x44\x65\x63imal\x12\x14\n\x05value\x18\x01 \x01(\x0cR\x05value\x12\x1c\n\tprecision\x18\x02 \x01(\x05R\tprecision\x12\x14\n\x05scale\x18\x03 \x01(\x05R\x05scale\x1a\xce\x01\n\x03Map\x12M\n\nkey_values\x18\x01 \x03(\x0b\x32..spark.connect.Expression.Literal.Map.KeyValueR\tkeyValues\x1ax\n\x08KeyValue\x12\x33\n\x03key\x18\x01 \x01(\x0b\x32!.spark.connect.Expression.LiteralR\x03key\x12\x37\n\x05value\x18\x02 \x01(\x0b\x32!.spark.connect.Expression.LiteralR\x05value\x1a\x43\n\x13IntervalYearToMonth\x12\x14\n\x05years\x18\x01 \x01(\x05R\x05years\x12\x16\n\x06months\x18\x02 \x01(\x05R\x06months\x1ag\n\x13IntervalDayToSecond\x12\x12\n\x04\x64\x61ys\x18\x01 \x01(\x05R\x04\x64\x61ys\x12\x18\n\x07seconds\x18\x02 \x01(\x05R\x07seconds\x12"\n\x0cmicroseconds\x18\x03 \x01(\x05R\x0cmicroseconds\x1a\x43\n\x06Struct\x12\x39\n\x06\x66ields\x18\x01 \x03(\x0b\x32!.spark.connect.Expression.LiteralR\x06\x66ields\x1a\x41\n\x04List\x12\x39\n\x06values\x18\x01 \x03(\x0b\x32!.spark.connect.Expression.LiteralR\x06values\x1a`\n\x0bUserDefined\x12%\n\x0etype_reference\x18\x01 \x01(\rR\rtypeReference\x12*\n\x05value\x18\x02 \x01(\x0b\x32\x14.google.protobuf.AnyR\x05valueB\x0e\n\x0cliteral_type\x1a\x46\n\x13UnresolvedAttribute\x12/\n\x13unparsed_identifier\x18\x01 \x01(\tR\x12unparsedIdentifier\x1a\x63\n\x12UnresolvedFunction\x12\x14\n\x05parts\x18\x01 \x03(\tR\x05parts\x12\x37\n\targuments\x18\x02 \x03(\x0b\x32\x19.spark.connect.ExpressionR\targuments\x1a\x32\n\x10\x45xpressionString\x12\x1e\n\nexpression\x18\x01 \x01(\tR\nexpression\x1a\x10\n\x0eUnresolvedStar\x1aU\n\x12QualifiedAttribute\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12+\n\x04type\x18\x02 \x01(\x0b\x32\x17.spark.connect.DataTypeR\x04type\x1ax\n\x05\x41lias\x12-\n\x04\x65xpr\x18\x01 \x01(\x0b\x32\x19.spark.connect.ExpressionR\x04\x65xpr\x12\x12\n\x04name\x18\x02 \x03(\tR\x04name\x12\x1f\n\x08metadata\x18\x03 \x01(\tH\x00R\x08metadata\x88\x01\x01\x42\x0b\n\t_metadataB\x0b\n\texpr_typeB"\n\x1eorg.apache.spark.connect.protoP\x01\x62\x06proto3'
)


_EXPRESSION = DESCRIPTOR.message_types_by_name["Expression"]
_EXPRESSION_LITERAL = _EXPRESSION.nested_types_by_name["Literal"]
_EXPRESSION_LITERAL_VARCHAR = _EXPRESSION_LITERAL.nested_types_by_name["VarChar"]
_EXPRESSION_LITERAL_DECIMAL = _EXPRESSION_LITERAL.nested_types_by_name["Decimal"]
_EXPRESSION_LITERAL_MAP = _EXPRESSION_LITERAL.nested_types_by_name["Map"]
_EXPRESSION_LITERAL_MAP_KEYVALUE = _EXPRESSION_LITERAL_MAP.nested_types_by_name["KeyValue"]
_EXPRESSION_LITERAL_INTERVALYEARTOMONTH = _EXPRESSION_LITERAL.nested_types_by_name[
    "IntervalYearToMonth"
]
_EXPRESSION_LITERAL_INTERVALDAYTOSECOND = _EXPRESSION_LITERAL.nested_types_by_name[
    "IntervalDayToSecond"
]
_EXPRESSION_LITERAL_STRUCT = _EXPRESSION_LITERAL.nested_types_by_name["Struct"]
_EXPRESSION_LITERAL_LIST = _EXPRESSION_LITERAL.nested_types_by_name["List"]
_EXPRESSION_LITERAL_USERDEFINED = _EXPRESSION_LITERAL.nested_types_by_name["UserDefined"]
_EXPRESSION_UNRESOLVEDATTRIBUTE = _EXPRESSION.nested_types_by_name["UnresolvedAttribute"]
_EXPRESSION_UNRESOLVEDFUNCTION = _EXPRESSION.nested_types_by_name["UnresolvedFunction"]
_EXPRESSION_EXPRESSIONSTRING = _EXPRESSION.nested_types_by_name["ExpressionString"]
_EXPRESSION_UNRESOLVEDSTAR = _EXPRESSION.nested_types_by_name["UnresolvedStar"]
_EXPRESSION_QUALIFIEDATTRIBUTE = _EXPRESSION.nested_types_by_name["QualifiedAttribute"]
_EXPRESSION_ALIAS = _EXPRESSION.nested_types_by_name["Alias"]
Expression = _reflection.GeneratedProtocolMessageType(
    "Expression",
    (_message.Message,),
    {
        "Literal": _reflection.GeneratedProtocolMessageType(
            "Literal",
            (_message.Message,),
            {
                "VarChar": _reflection.GeneratedProtocolMessageType(
                    "VarChar",
                    (_message.Message,),
                    {
                        "DESCRIPTOR": _EXPRESSION_LITERAL_VARCHAR,
                        "__module__": "spark.connect.expressions_pb2"
                        # @@protoc_insertion_point(class_scope:spark.connect.Expression.Literal.VarChar)
                    },
                ),
                "Decimal": _reflection.GeneratedProtocolMessageType(
                    "Decimal",
                    (_message.Message,),
                    {
                        "DESCRIPTOR": _EXPRESSION_LITERAL_DECIMAL,
                        "__module__": "spark.connect.expressions_pb2"
                        # @@protoc_insertion_point(class_scope:spark.connect.Expression.Literal.Decimal)
                    },
                ),
                "Map": _reflection.GeneratedProtocolMessageType(
                    "Map",
                    (_message.Message,),
                    {
                        "KeyValue": _reflection.GeneratedProtocolMessageType(
                            "KeyValue",
                            (_message.Message,),
                            {
                                "DESCRIPTOR": _EXPRESSION_LITERAL_MAP_KEYVALUE,
                                "__module__": "spark.connect.expressions_pb2"
                                # @@protoc_insertion_point(class_scope:spark.connect.Expression.Literal.Map.KeyValue)
                            },
                        ),
                        "DESCRIPTOR": _EXPRESSION_LITERAL_MAP,
                        "__module__": "spark.connect.expressions_pb2"
                        # @@protoc_insertion_point(class_scope:spark.connect.Expression.Literal.Map)
                    },
                ),
                "IntervalYearToMonth": _reflection.GeneratedProtocolMessageType(
                    "IntervalYearToMonth",
                    (_message.Message,),
                    {
                        "DESCRIPTOR": _EXPRESSION_LITERAL_INTERVALYEARTOMONTH,
                        "__module__": "spark.connect.expressions_pb2"
                        # @@protoc_insertion_point(class_scope:spark.connect.Expression.Literal.IntervalYearToMonth)
                    },
                ),
                "IntervalDayToSecond": _reflection.GeneratedProtocolMessageType(
                    "IntervalDayToSecond",
                    (_message.Message,),
                    {
                        "DESCRIPTOR": _EXPRESSION_LITERAL_INTERVALDAYTOSECOND,
                        "__module__": "spark.connect.expressions_pb2"
                        # @@protoc_insertion_point(class_scope:spark.connect.Expression.Literal.IntervalDayToSecond)
                    },
                ),
                "Struct": _reflection.GeneratedProtocolMessageType(
                    "Struct",
                    (_message.Message,),
                    {
                        "DESCRIPTOR": _EXPRESSION_LITERAL_STRUCT,
                        "__module__": "spark.connect.expressions_pb2"
                        # @@protoc_insertion_point(class_scope:spark.connect.Expression.Literal.Struct)
                    },
                ),
                "List": _reflection.GeneratedProtocolMessageType(
                    "List",
                    (_message.Message,),
                    {
                        "DESCRIPTOR": _EXPRESSION_LITERAL_LIST,
                        "__module__": "spark.connect.expressions_pb2"
                        # @@protoc_insertion_point(class_scope:spark.connect.Expression.Literal.List)
                    },
                ),
                "UserDefined": _reflection.GeneratedProtocolMessageType(
                    "UserDefined",
                    (_message.Message,),
                    {
                        "DESCRIPTOR": _EXPRESSION_LITERAL_USERDEFINED,
                        "__module__": "spark.connect.expressions_pb2"
                        # @@protoc_insertion_point(class_scope:spark.connect.Expression.Literal.UserDefined)
                    },
                ),
                "DESCRIPTOR": _EXPRESSION_LITERAL,
                "__module__": "spark.connect.expressions_pb2"
                # @@protoc_insertion_point(class_scope:spark.connect.Expression.Literal)
            },
        ),
        "UnresolvedAttribute": _reflection.GeneratedProtocolMessageType(
            "UnresolvedAttribute",
            (_message.Message,),
            {
                "DESCRIPTOR": _EXPRESSION_UNRESOLVEDATTRIBUTE,
                "__module__": "spark.connect.expressions_pb2"
                # @@protoc_insertion_point(class_scope:spark.connect.Expression.UnresolvedAttribute)
            },
        ),
        "UnresolvedFunction": _reflection.GeneratedProtocolMessageType(
            "UnresolvedFunction",
            (_message.Message,),
            {
                "DESCRIPTOR": _EXPRESSION_UNRESOLVEDFUNCTION,
                "__module__": "spark.connect.expressions_pb2"
                # @@protoc_insertion_point(class_scope:spark.connect.Expression.UnresolvedFunction)
            },
        ),
        "ExpressionString": _reflection.GeneratedProtocolMessageType(
            "ExpressionString",
            (_message.Message,),
            {
                "DESCRIPTOR": _EXPRESSION_EXPRESSIONSTRING,
                "__module__": "spark.connect.expressions_pb2"
                # @@protoc_insertion_point(class_scope:spark.connect.Expression.ExpressionString)
            },
        ),
        "UnresolvedStar": _reflection.GeneratedProtocolMessageType(
            "UnresolvedStar",
            (_message.Message,),
            {
                "DESCRIPTOR": _EXPRESSION_UNRESOLVEDSTAR,
                "__module__": "spark.connect.expressions_pb2"
                # @@protoc_insertion_point(class_scope:spark.connect.Expression.UnresolvedStar)
            },
        ),
        "QualifiedAttribute": _reflection.GeneratedProtocolMessageType(
            "QualifiedAttribute",
            (_message.Message,),
            {
                "DESCRIPTOR": _EXPRESSION_QUALIFIEDATTRIBUTE,
                "__module__": "spark.connect.expressions_pb2"
                # @@protoc_insertion_point(class_scope:spark.connect.Expression.QualifiedAttribute)
            },
        ),
        "Alias": _reflection.GeneratedProtocolMessageType(
            "Alias",
            (_message.Message,),
            {
                "DESCRIPTOR": _EXPRESSION_ALIAS,
                "__module__": "spark.connect.expressions_pb2"
                # @@protoc_insertion_point(class_scope:spark.connect.Expression.Alias)
            },
        ),
        "DESCRIPTOR": _EXPRESSION,
        "__module__": "spark.connect.expressions_pb2"
        # @@protoc_insertion_point(class_scope:spark.connect.Expression)
    },
)
_sym_db.RegisterMessage(Expression)
_sym_db.RegisterMessage(Expression.Literal)
_sym_db.RegisterMessage(Expression.Literal.VarChar)
_sym_db.RegisterMessage(Expression.Literal.Decimal)
_sym_db.RegisterMessage(Expression.Literal.Map)
_sym_db.RegisterMessage(Expression.Literal.Map.KeyValue)
_sym_db.RegisterMessage(Expression.Literal.IntervalYearToMonth)
_sym_db.RegisterMessage(Expression.Literal.IntervalDayToSecond)
_sym_db.RegisterMessage(Expression.Literal.Struct)
_sym_db.RegisterMessage(Expression.Literal.List)
_sym_db.RegisterMessage(Expression.Literal.UserDefined)
_sym_db.RegisterMessage(Expression.UnresolvedAttribute)
_sym_db.RegisterMessage(Expression.UnresolvedFunction)
_sym_db.RegisterMessage(Expression.ExpressionString)
_sym_db.RegisterMessage(Expression.UnresolvedStar)
_sym_db.RegisterMessage(Expression.QualifiedAttribute)
_sym_db.RegisterMessage(Expression.Alias)

if _descriptor._USE_C_DESCRIPTORS == False:

    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b"\n\036org.apache.spark.connect.protoP\001"
    _EXPRESSION._serialized_start = 105
    _EXPRESSION._serialized_end = 3161
    _EXPRESSION_LITERAL._serialized_start = 613
    _EXPRESSION_LITERAL._serialized_end = 2696
    _EXPRESSION_LITERAL_VARCHAR._serialized_start = 1923
    _EXPRESSION_LITERAL_VARCHAR._serialized_end = 1978
    _EXPRESSION_LITERAL_DECIMAL._serialized_start = 1980
    _EXPRESSION_LITERAL_DECIMAL._serialized_end = 2063
    _EXPRESSION_LITERAL_MAP._serialized_start = 2066
    _EXPRESSION_LITERAL_MAP._serialized_end = 2272
    _EXPRESSION_LITERAL_MAP_KEYVALUE._serialized_start = 2152
    _EXPRESSION_LITERAL_MAP_KEYVALUE._serialized_end = 2272
    _EXPRESSION_LITERAL_INTERVALYEARTOMONTH._serialized_start = 2274
    _EXPRESSION_LITERAL_INTERVALYEARTOMONTH._serialized_end = 2341
    _EXPRESSION_LITERAL_INTERVALDAYTOSECOND._serialized_start = 2343
    _EXPRESSION_LITERAL_INTERVALDAYTOSECOND._serialized_end = 2446
    _EXPRESSION_LITERAL_STRUCT._serialized_start = 2448
    _EXPRESSION_LITERAL_STRUCT._serialized_end = 2515
    _EXPRESSION_LITERAL_LIST._serialized_start = 2517
    _EXPRESSION_LITERAL_LIST._serialized_end = 2582
    _EXPRESSION_LITERAL_USERDEFINED._serialized_start = 2584
    _EXPRESSION_LITERAL_USERDEFINED._serialized_end = 2680
    _EXPRESSION_UNRESOLVEDATTRIBUTE._serialized_start = 2698
    _EXPRESSION_UNRESOLVEDATTRIBUTE._serialized_end = 2768
    _EXPRESSION_UNRESOLVEDFUNCTION._serialized_start = 2770
    _EXPRESSION_UNRESOLVEDFUNCTION._serialized_end = 2869
    _EXPRESSION_EXPRESSIONSTRING._serialized_start = 2871
    _EXPRESSION_EXPRESSIONSTRING._serialized_end = 2921
    _EXPRESSION_UNRESOLVEDSTAR._serialized_start = 2923
    _EXPRESSION_UNRESOLVEDSTAR._serialized_end = 2939
    _EXPRESSION_QUALIFIEDATTRIBUTE._serialized_start = 2941
    _EXPRESSION_QUALIFIEDATTRIBUTE._serialized_end = 3026
    _EXPRESSION_ALIAS._serialized_start = 3028
    _EXPRESSION_ALIAS._serialized_end = 3148
# @@protoc_insertion_point(module_scope)
