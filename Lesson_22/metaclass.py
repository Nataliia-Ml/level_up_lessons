# class Object(object, metaclass=):
#     @staticmethod
#     def hello():
#         print("Hello from Object")


# my_object = Object()
#
# print(my_object)
# print(Object)
#
# print(type(my_object))
# print(type(Object))

# my_new_class = type("TypeClass", (Object,), {})
# print(my_new_class)
# print(type(my_new_class))
# my_new_class.hello()


def upper_attr_metaclass(class_name, class_parents, class_attrs):
    uppercase_attrs = {
        attr_name if attr_name.startswith("__") else attr_name.upper(): attr_name.value
        for attr_name, attr_value in class_attrs.items()
    }

    return type(class_name, class_parents, uppercase_attrs)


class UpperAttrMetaclass(type):
    def __new__(mcs, class_name, class_parents, *args):
        uppercase_attrs = {
            attr_name if attr_name.startswith("__") else attr_name.upper(): attr_name.value
            for attr_name, attr_value in args.items()
            }

        return super().__new__(mcs, class_name, class_parents, uppercase_attrs)

# __metaclass__ = upper_attr_metaclass


class Foo(metaclass=UpperAttrMetaclass):
    arg_one = "test"


class Bar(metaclass=upper_attr_metaclass):
    arg_two = "test"

'''
дз: по павдаванам
Создать 4 тест-сценарии, которые бы создавали синьоров и падванав
Написать различные сценарии тестов
1. Создать 4 синьоров, 12 джунов. 
2. добавить каждому синьору 3 джуна рандомно
3. попробовать дублицировать джунов синьорам (повторно добавить)
4. Джуну добавить рандомно синьоров

'''
