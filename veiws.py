from search import search_object

class CreatMixin:
    def _get_or_set_objects_and_id(self):
        try:
            self.objects
            self.id
        except(NameError, AttributeError):
            self.objects = []
            self. id = 0
    
    def __init__(self) -> None:
        self._get_or_set_objects_and_id()
    
    def post(self, **kwargs):
        self.id += 1
        object_ = dict(id=self.id, **kwargs)
        self.objects.append(object_)
        return {'status': 201, 'msg': object_}

class ReadMixin:
    def list(self):
        res = []
        for obj in self.objects:
            res.append({'id': obj['id'], 'title': obj['title'], 'price': obj['price']})
        return {'status': 200, 'msg': res}

    @search_object
    def detail(self, id, **kwargs):
        obj = kwargs['object_']
        if obj:
            return {'status': 200, 'msg': obj}
        return {'statud': 404, 'msg': 'Not Found!'}

class UpdateMixin:
    @search_object
    def patch(self, id, **kwargs):
        obj = kwargs.pop('object_')
        if obj:
            obj.update(**kwargs)
            return {'status': 206, 'mgs': obj}
        return {'status': 404, 'msg': 'Not Found!'}

class DelateMixin:
    @search_object
    def delete(self, id, **kwargs):
        obj = kwargs.get('object_')
        if obj:
            self.objects.remove(obj)
            return {'status': 204, 'mgs': 'Deleted!'}
        return {'status': 404, 'msg': 'Not Found!'}

class Post():
    pass
class Comments():
    pass