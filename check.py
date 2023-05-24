class Meta(type):
    def __new__(meta, class_name, supers, class_dict):
        print("meta", meta) # Meta class
        print(class_name) # User - child class name
        print(supers) # parent classner@
        print(class_dict) # User class attibutes
        return type.__new__(meta, class_name, supers, class_dict)


class SpaceMan:
    pass

class User(SpaceMan, metaclass = Meta):
    name = 'Jarvis'


jarvis = User()