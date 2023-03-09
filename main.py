from veiws import CreatMixin, ReadMixin, UpdateMixin, DelateMixin

class Product(CreatMixin, ReadMixin, UpdateMixin, DelateMixin):
    def save(self):
        import json
        with open('data.json', 'w') as file:
            json.dump(self.objects, file, indent=4)
        return 'Saved!'

smartphones = Product()
print(smartphones.post(title='Rdmi Note-10', description='The best phone for own price', qty=10, price=250))
print(smartphones.post(title='Rdmi Note-20', description='The Flagman phone for own price', qty=5, price=600))
print(smartphones.post(title='Iphone', description='Good phone', qty=40, price=2000))
print(smartphones.post(title='Sumsung', description='The best phone for own price', qty=12, price=1000))
print(smartphones.post(title='Poco Phone 19', description='Cheap phone', qty=5, price=150))
print()
print(smartphones.list())
print('!!!!!!')
# print(smartphones.detail(5))
# print(smartphones.detail(15))
print(smartphones.patch(5, title='Poco Phone 20', price=500))
print()
print(smartphones.patch(15, title='Poco Phone 20'))
print()
print(smartphones.delete(5))
print()
print(smartphones.list())
print()
print(smartphones.save())