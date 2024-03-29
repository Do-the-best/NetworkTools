VALID_MASKS = {'255.255.255.255', '255.255.255.254', '255.255.255.252', '255.255.255.248',
               '255.255.255.240', '255.255.255.224', '255.255.255.192', '255.255.255.128',
               '255.255.255.0', '255.255.254.0', '255.255.252.0', '255.255.248.0',
               '255.255.240.0', '255.255.224.0', '255.255.192.0', '255.255.128.0',
               '255.255.0.0', '255.254.0.0', '255.252.0.0', '255.248.0.0',
               '255.240.0.0', '255.224.0.0', '255.192.0.0', '255.128.0.0',
               '255.0.0.0', '254.0.0.0', '252.0.0.0', '248.0.0.0',
               '240.0.0.0', '224.0.0.0', '192.0.0.0', '128.0.0.0', '0.0.0.0'}

EXIT_COMMANDS = {'quit', 'exit', 'q'}


def mask_verify(func):
    def inner(_mask: int | str):
        if isinstance(_mask, int):
            if 0 <= _mask <= 32:
                return func(_mask)
            else:
                raise ValueError('输入掩码范围应为 0 ~ 32')
        elif isinstance(_mask, str):
            # 检测点分十进制掩码是否符合规范
            if _mask in VALID_MASKS:
                return func(_mask)
            else:
                raise ValueError('输入的掩码不符合规范')
    return inner


@mask_verify
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


@mask_verify
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
    while True:
        mask = input('> ')
        if mask in EXIT_COMMANDS:
            print('Bye!')
            break

        try:
            mask = int(mask)
        except:
            pass

        if isinstance(mask, int):
            try:
                result = inter_to_dotted_decimal(mask)
                print(result)
            except ValueError as error:
                print(error)
        elif isinstance(mask, str):
            try:
                result = dotted_decimal_to_integer(mask)
                print(result)
            except ValueError as error:
                print(error)
        else:
            result = None