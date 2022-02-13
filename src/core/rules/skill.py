from functools import wraps


def normal_atk(count=1):
    '''
    普通攻击
    '''
    def decorate(func):
        @wraps(func)
        def wapper(*args, **kwargs):
            print("\t\tTRIGGER BEFORE NORMAL ATK")
            result = func(*args, **kwargs)
            print("\t\tTRIGGER AFTER NORMAL ATK")
            return result
        return wapper
    return decorate

def elem_skill(count=1):
    '''
    元素战技
    '''
    def decorate(func):
        @wraps(func)
        def wapper(*args, **kwargs):
            print("\t\tTRIGGER BEFORE ELEM SKILL")
            result = func(*args, **kwargs)
            print("\t\tTRIGGER AFTER ELEM SKILL")
            return result
        return wapper
    return decorate

def elem_burst(count=1):
    '''
    元素爆发
    '''
    def decorate(func):
        @wraps(func)
        def wapper(*args, **kwargs):
            print("\t\tTRIGGER BEFORE ELEM BURST")
            result = func(*args, **kwargs)
            print("\t\tTRIGGER AFTER ELEM BURST")
            return result
        return wapper
    return decorate