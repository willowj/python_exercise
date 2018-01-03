#coding:utf8
#author: willowj
#license: MIT
#date: 2017-12-30 23:30:43

class ClassName(object):
    """rotate by 13 places
    """
    def __init__(self, arg=None):
        super(ClassName, self).__init__()
        self.arg = arg

    def code_rot(self, sts_, rot_step=13):
        new_ = []
        for x in sts_:
            ordx = ord(x)
            if 65 <= ordx < 91 or 97 <= ordx < 123:
                if ordx >= 97:
                    start = 97
                else:
                    start = 65
                new_ord = start + (ord(x) + rot_step - start) % 26
                new_.append(chr(new_ord))
                print (chr(new_ord))
            else:
                new_.append(x)

        return ''.join(new_)
