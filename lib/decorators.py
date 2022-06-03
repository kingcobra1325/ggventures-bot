class Decorators:

    @staticmethod
    def conditional_function(condition=True):
        def decorator_func(func):
            def wrapper(*args, **kwargs):
                if condition:
                    return func(*args, **kwargs)
            return wrapper
        return decorator_func


    @staticmethod
    def exception_wrapper(exc_func,exc=Exception):
        def decorator_func(func):
            def wrapper(*args, **kwargs):
                try:
                    return func(*args, **kwargs)
                except exc as e:
                    exc_func(e)
            return wrapper
        return decorator_func

    @staticmethod
    def connection_retry(error=(ConnectionError,ConnectionResetError,ConnectionAbortedError,ConnectionResetError)):
        def decorator_func(func):
            def wrapper(*args, **kwargs):
                while True:
                    try:
                        return func(*args, **kwargs)
                    except error:
                        print(end=".")
            return wrapper
        return decorator_func

    @staticmethod
    def class_exception_wrapper(exc=Exception):
        def decorator_func(func):
            def wrapper(*args, **kwargs):
                try:
                    return func(*args, **kwargs)
                except exc as e:
                    args[0].exception_handler(e)
            return wrapper
        return decorator_func
    
    @staticmethod
    def gen_exception_wrapper(exc=Exception):
        def decorator_gen(gen):
            def wrapper(*args, **kwargs):
                try:
                    return (yield from gen(*args, **kwargs))
                except exc as e:
                    args[0].exception_handler(e)
            return wrapper
        return decorator_gen

    @staticmethod
    def selenium_popup_handler_gen(exc=Exception):
        def decorator_gen(gen):
            def wrapper(*args, **kwargs):
                try:
                    return (yield from gen(*args, **kwargs))
                except exc as e:
                    print(f"{e}")
                    args[0].handle_popup_alert()
                    return (yield from gen(*args, **kwargs))
            return wrapper
        return decorator_gen
    
    @staticmethod
    def selenium_popup_handler_fn(exc=Exception):
        def decorator_func(func):
            def wrapper(*args, **kwargs):
                try:
                    return func(*args, **kwargs)
                except exc as e:
                    print(f"{e}")
                    args[0].handle_popup_alert()
                    return func(*args, **kwargs)
            return wrapper
        return decorator_func



decorate = Decorators()