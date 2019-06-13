# encoding=utf-8
"""
@author huxujun
@date 2019-06-03
"""


def parse_args_to_dict(args: list, default_dict=None) -> dict:
    if default_dict is None:
        default_dict = {}
    args_dict = {}
    for ii in range(2, len(args), 2):
        args_dict[args[ii - 1]] = args[ii]
    for k, v in default_dict.items():
        if k not in args_dict.keys():
            args_dict[k] = v
    return args_dict


if __name__ == '__main__':
    pass
