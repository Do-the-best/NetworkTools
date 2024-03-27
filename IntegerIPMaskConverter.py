def inter_to_dotted_decimal(mask_integer: int) -> str:
    """将整数掩码转换为点分十进制掩码.

    :param mask_integer: 整数类型掩码
    :return: 点分十进制类型掩码
    """
    binary_mask = list()
    # 换成二进制列表
    for i in range(32):
        if i < mask_integer:
            binary_mask.append('1')
        else:
            binary_mask.append('0')
        if (i + 1) % 8 == 0 and i != 31:
            binary_mask.append('.')

    # 换成点分二进制掩码
    _mask = ''.join(binary_mask).split('.')
    return f"{int(_mask[0], 2)}.{int(_mask[1], 2)}.{int(_mask[2], 2)}.{int(_mask[3], 2)}"


def dotted_decimal_to_integer(mask_dotted_decimal: str) -> int:
    """将点分十进制掩码转换为整数掩码.

    :param mask_dotted_decimal:
    :return:
    """
    _mask = ''
    for _ in (mask_dotted_decimal.split('.')):
        # 将点分十进制转二进制
        _mask += bin(int(_))[2:]
    # 计算二进制中1的个数并返回
    return _mask.count('1')


if __name__ == '__main__':
    # TODO: 装饰器校验int类型数据，范围
    # TODO: 校验用户输入的x.x.x.x的完整性
    mask = input('> ')
    try:
        mask = int(mask)
    except ValueError as error:
        print(error)
    else:
        if 1 <= mask <= 32:
            pass
        else:
            raise ValueError('掩码值非法')

    if isinstance(mask, int):
        result = inter_to_dotted_decimal(mask)
    elif isinstance(mask, str):
        result = dotted_decimal_to_integer(mask)
    else:
        result = None

    print(result)
