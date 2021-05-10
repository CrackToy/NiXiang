# -*- coding: utf-8 -*-
"""
首先要了解一遍dex的原理，为什么要去分析这个dex，这对之后的脱壳，dex混淆有很大的帮助
"""


class StructHeaderItemDexHeader:
    struct_dex_magic_magic = None
    uint_checksum = None
    SHA1_signature = None
    uint_file_size = None
    uint_header_size = None
    uint_endian_tag = None
    uint_link_size = None
    uint_link_off = None
    uint_map_off = None
    uint_string_ids_size = None
    uint_string_ids_off = None
    uint_type_ids_size = None
    uint_type_ids_off = None
    uint_proto_ids_size = None
    uint_proto_ids_off = None
    uint_field_ids_size = None
    uint_field_ids_off = None
    uint_method_ids_size = None
    uint_method_ids_off = None
    uint_class_defs_size = None
    uint_class_defs_off = None
    uint_data_size = None
    uint_data_off = None


class DEXParser:
    def __init__(self, filename):
        with open(filename, 'rb')as f:
            self.dex_buffer = f.read()
        self.StructHeaderItemDexHeader = StructHeaderItemDexHeader()

    def parse_header(self):
        self._header = self.dex_buffer[0:0x70]
        self.StructHeaderItemDexHeader.struct_dex_magic_magic = self._header[0:0x8]
        self.StructHeaderItemDexHeader.uint_checksum = self._header[0x8:0xC]
        self.StructHeaderItemDexHeader.SHA1_signature = self._header[0xC:0x20]
        self.StructHeaderItemDexHeader.uint_file_size = self._header[0x20:0x24]
        self.StructHeaderItemDexHeader.uint_header_size = self._header[0x24:0x28]
        self.StructHeaderItemDexHeader.uint_endian_tag = self._header[0x28:0x2C]
        self.StructHeaderItemDexHeader.uint_link_size = self._header[0x2C:0x30]
        self.StructHeaderItemDexHeader.uint_link_off = self._header[0x30:0x34]
        self.StructHeaderItemDexHeader.uint_map_off = self._header[0x34:0x38]
        self.StructHeaderItemDexHeader.uint_string_ids_size = self._header[0x38:0x3C]
        self.StructHeaderItemDexHeader.uint_string_ids_off = self._header[0x3C:0x40]
        self.StructHeaderItemDexHeader.uint_type_ids_size = self._header[0x40:0x44]
        self.StructHeaderItemDexHeader.uint_type_ids_off = self._header[0x44:0x48]
        self.StructHeaderItemDexHeader.uint_proto_ids_size = self._header[0x48:0x4C]
        self.StructHeaderItemDexHeader.uint_proto_ids_off = self._header[0x4C:0x50]
        self.StructHeaderItemDexHeader.uint_field_ids_size = self._header[0x50:0x54]
        self.StructHeaderItemDexHeader.uint_field_ids_off = self._header[0x54:0x58]
        self.StructHeaderItemDexHeader.uint_method_ids_size = self._header[0x58:0x5C]
        self.StructHeaderItemDexHeader.uint_method_ids_off = self._header[0x5C:0x60]
        self.StructHeaderItemDexHeader.uint_class_defs_size = self._header[0x60:0x64]
        self.StructHeaderItemDexHeader.uint_class_defs_off = self._header[0x64:0x68]
        self.StructHeaderItemDexHeader.uint_data_size = self._header[0x68:0x6C]
        self.StructHeaderItemDexHeader.uint_data_0ff = self._header[0x6C:0x70]
        print(self._header)


dex = DEXParser("example.dex")
dex.parse_header()
