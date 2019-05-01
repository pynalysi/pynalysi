def generate_random_str(randomlength=32):
    """
    生成一个指定长度的随机字符串
    """
    random_str = ''
    base_str = '0123456789abcdefghigklmnopqrstuvwxyz'
    length = len(base_str) - 1
    for i in range(randomlength):
        random_str += base_str[random.randint(0, length)]
    return random_str
