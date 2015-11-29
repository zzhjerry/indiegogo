import models

def parse_obj(obj, cls):
    model = getattr(models, cls)()
    for k, v in obj.items():
        setattr(model, k, v)
    return model

def parse_list(lst, cls):
    result = []
    for js_obj in lst:
        obj = parse_obj(js_obj, cls)
        result.append(obj)

    return result
