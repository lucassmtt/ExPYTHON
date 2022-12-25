def my_repr(self):
    name_class = self.__class__.__name__
    name_dict = self.__dict__
    result_repr = f'{name_dict}({name_class})'
    return result_repr


def add_repr(random_class):
    random_class.__repr__ = my_repr
    return random_class


@add_repr
class Team:
    def __init__(self, name_team):
        self.name = name_team



time_pos_10 = Team('Bahia')
print(time_pos_10)