def bad_obfuscated_cc(cc):
    return cc[:4] + ["*"] * 8 + cc[12:]

def obfuscated_cc(cc):
    cc_len = len(cc)
    start = slice(4)
    end = slice(-4, None)

    return cc[start] + ['*'] * (cc_len - 8) + cc[end]

def other_obfuscated_cc(cc):
    mask = ['*'] * 8
    middle = slice(4, -4)
    cc[middle] = mask

    return cc

cc = list(range(16))

print(bad_obfuscated_cc(cc))
print(obfuscated_cc(cc))
print(other_obfuscated_cc(cc))
