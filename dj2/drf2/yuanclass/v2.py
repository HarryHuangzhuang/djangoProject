class SerializerMetaclass(type):
    def __new__(cls,name,bases,attrs):
        data_dict = {}
        for k,v in list(attrs.items()):      # 防止循环删除是 漏 掉    {"v1":123,"v2":456,"v3":"hahhaha"}
            if isinstance(v,int):
                data_dict[k] =attrs.pop(k)
        attrs["_declared_fields"] = data_dict
        
        return super().__new__(cls,name,bases,attrs)
    



class BaseSerializes(object):
    pass

class Serializes(BaseSerializes, metaclass = SerializerMetaclass):
    pass

class ModelSerializes(Serializes):
    pass

class UserSerializes(ModelSerializes):
    v1 =123
    v2 =456
    v3 = "hahhaha"

print(UserSerializes.v3)
print(UserSerializes._declared_fields)