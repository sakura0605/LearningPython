class Constant:
    def __int__(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name


class Instance:
    def __init__(self, name):
        self.name = name
        self.constants = []

    def get_name(self):
        return self.name

    def get_constants(self):
        return self.constants

    def set_name(self, name):
        self.name = name

    def add_constants(self, constant):
        self.constants.append(constant)


class Component:
    def __init__(self):
        self.constants = []
        self.instances = []

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def add_constants(self, constant):
        self.constants.append(constant)

    def add_instances(self, instance):
        self.instances.append(instance)

    def get_constants(self):
        return self.constants

    def get_instances(self):
        return self.instances


class Components:
    def __init__(self):
        self.components = []

    def add_component(self, component):
        self.components.append(component)

    def get_components(self):
        return self.components
