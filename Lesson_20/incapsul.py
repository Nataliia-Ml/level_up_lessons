# class BaseClass:
#     def __init__(self):
#         # Public Attribute
#         self.public_attr = "I'm Public Attribute"
#         # Protected Attr (convention)
#         self._protected_attr = "I'm Protected Attribute"
#         # Private Attr (convention)
#         self.__private_attr = "I'm Private Attribute"
#         self.digit = 50

    # def get_private_attr(self):
    #     print(self.__private_attr)

    # def get_private_attr(self):
    #     print(self.digit)
    #
    # def set_private_attr(self, new_value):
    #     if type(new_value) is int and new_value > 0:
    #         self.digit = new_value
    #     else:
    #         print("Private attr must be positive integer")
    #
    # @property
#     def made_calculation(self):
#         return self.digit ** 2
#
#
# base = BaseClass()

# base._BaseClass__private_attr

import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property
    def area(self):
        return math.pi * self.radius **2

    @property
    def perimetr(self):
        return 2 * math.pi * self.radius

    @property   # radius
    def radius(self):
        print("Radius Getter")
        return self.__radius

    @radius.setter # radius =
    def radius(self, new_radius):
        print("Radius setter")
        if type(new_radius) is int and new_radius > 0:
            self.__radius = new_radius

    @radius.deleter # del radius
    def radius(self):
        print("You have no permission to delete this attribute")
