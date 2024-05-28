import datetime
import hashlib
def sha256_hash(data):
    # 创建一个sha256哈希对象
    hash_object = hashlib.sha256()
    # 提供需要哈希的数据，必须是字节类型
    hash_object.update(data.encode('utf-8'))
    # 获取16进制格式的哈希值
    hashed_data = hash_object.hexdigest()
    return hashed_data
