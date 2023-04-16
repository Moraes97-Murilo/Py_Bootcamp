def styling(style):
    def wrapped_function(*args):   
        final = args[1]
        for i in args[0]:
            final = f"<{i}>" + final + "</{i}>"

        return final
    return wrapped_function

