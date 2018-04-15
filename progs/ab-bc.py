
import abc
class Context(object):
    """
    Define the interface of interest to clients.
    Maintain a reference to a Strategy object.
    """
    def __init__(self, strategy):
        self._strategy = strategy

    def context_interface(self, person):
        self._strategy.output_interface(person)

class Person(object):
    def __init__(self, name, age, city , mob_num):
        self.name = name
        self.age = age
        self.city = city
        self.mob_num = mob_num
    
class Strategy(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def output_interface(self, person):
        raise NotImplementedError


class TextOutput(Strategy):
    """
    Implement the algorithm using the Strategy interface.
    """
    def output_interface(self, person):
        print "Text Output"
        for key,val in person.__dict__.items():
            print val


class PDFOutput(Strategy):
    """
    Implement the algorithm using the Strategy interface.
    """
    def output_interface(self):
        pass


if __name == "__main__":
    name = raw_input("Enter the name:")
    age = raw_input("Enter the age:")    
    mobile_number = raw_input("Enter the mobile number:")
    city = raw_input("Enter the mobile city:")
    export_type = raw_input("Enter the export type: pdf | text")

    
    person = Person(name, age, city , mobile_number)
    text_output = TextOutput()
    context = Context(text_output)
    context.context_interface(person)
