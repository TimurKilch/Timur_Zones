import struct
import numpy as np
#from dataclasses import dataclass


DTYPES = ['uint8', 'int32', 'float32']
ENCODE_DTYPE = {n: i for i, n in enumerate(DTYPES)}
MAGIC = b'RMAP'


#@dataclass
class GeoPoint:
    def __init__(self, lat: float, lon: float):
        self.latitude = lat
        self.longitude = lon


#@dataclass
class GeoRect:
    def __init__(self, left_top: GeoPoint, right_bottom: GeoPoint):
        self.left_top = left_top
        self.right_bottom = right_bottom


#@dataclass
class Map:
    def __init__(self, data: np.ndarray, geo_rect: GeoRect):
        self.data = data
        self.geo_rect = geo_rect


def save_int(x: int) -> bytes:
    return x.to_bytes(4, byteorder='big')


def save_float(x: float) -> bytes:
    return struct.pack('>f', x)


def load_int(b: bytes) -> int:
    return int.from_bytes(b, byteorder='big')


def load_float(b: bytes) -> float:
    return struct.unpack('>f', b)


def to_bytes(x: Map) -> bytes:
    chan, rows, cols = x.data.shape
    x_bytes = x.data.flatten().astype(x.data.dtype.newbyteorder('>')).tobytes()
    ret = bytearray(MAGIC)
    ret.extend(save_int(chan))
    ret.extend(save_int(rows))
    ret.extend(save_int(cols))
    ret.extend(save_int(ENCODE_DTYPE[x.data.dtype.name]))
    ret.extend(save_float(x.geo_rect.left_top.latitude))
    ret.extend(save_float(x.geo_rect.left_top.longitude))
    ret.extend(save_float(x.geo_rect.right_bottom.latitude))
    ret.extend(save_float(x.geo_rect.right_bottom.longitude))
    ret.extend(x_bytes)
    return bytes(ret)


def from_bytes(b: bytes) -> Map:
    magic = b[:4]
    if magic != MAGIC:
        raise ValueError('d')#f'Magic value is {magic}, must be {MAGIC}')
    chan = load_int(b[4:8])
    rows = load_int(b[8:12])
    cols = load_int(b[12:16])
    stored_dtype = np.dtype(DTYPES[load_int(b[16:20])]).newbyteorder('>')
    ret_dtype = stored_dtype.newbyteorder('=')
    #print('type = ', ret_dtype)
    geo_rect = GeoRect(
        GeoPoint(load_float(b[20:24]), load_float(b[24:28])),
        GeoPoint(load_float(b[28:32]), load_float(b[32:36])))
    data = np.frombuffer(b[36:], dtype=stored_dtype)
    data = data.astype(ret_dtype).reshape((chan, rows, cols))
    return Map(data, geo_rect)


def to_file(x: Map, path) -> None:
    x_bytes = to_bytes(x)
    with open(path, 'wb') as fd:
        fd.write(x_bytes)


def from_file(path) -> Map:
    with open(path, 'rb') as fd:
        x_bytes = fd.read()
    return from_bytes(x_bytes)
