from addressbook import AddressBook


class Operation:
    def __init__(self, book: AddressBook):
        self.book = book
        self.commands = {
            'hello': HelloCommand(self),
            'add': AddPhoneCommand(self),
            'change': ChangeCommand(self),
            'phone': PhoneCommand(self),
            'show': ShowCommand(self),
            'delete': DeleteCommand(self),
            'birth': BirthdayCommand(self),
            'email': EmailCommand(self),
            'address': AddressCommand(self),
            'nxbirth': NextBirthdayCommand(self),
            'sear': SearchCommand(self),
            'info': InfoCommand(self)
        }

    def hello(self):
        return "How can I help you?\n"

    def add(self):
        """Adding a contact and phone, if there is a contact, it adds the phone"""
        pass

    def change(self):
        pass

    def phone(self):
        pass

    def show(self):
        pass

    def delete(self):
        pass

    def birth(self):
        pass

    def email(self):
        pass

    def address(self):
        pass

    def nxbirth(self):
        pass

    def sear(self):
        pass

    def info(self):
        pass

    def execute(self, command_name):
        return self.commands[command_name].execute()


class HelloCommand:
    def __init__(self, ops: Operation):
        self.ops = ops

    def execute(self):
        return self.ops.hello()


class AddPhoneCommand:
    def __init__(self, ops: Operation):
        self.ops = ops

    def execute(self):
        return self.ops.add()


class ChangeCommand:
    def __init__(self, ops: Operation):
        self.ops = ops

    def execute(self):
        return self.ops.change()


class PhoneCommand:
    def __init__(self, ops: Operation):
        self.ops = ops

    def execute(self):
        return self.ops.phone()


class ShowCommand:
    def __init__(self, ops: Operation):
        self.ops = ops

    def execute(self):
        return self.ops.show()


class DeleteCommand:
    def __init__(self, ops: Operation):
        self.ops = ops

    def execute(self):
        return self.ops.delete()


class BirthdayCommand:
    def __init__(self, ops: Operation):
        self.ops = ops

    def execute(self):
        return self.ops.birth()


class EmailCommand:
    def __init__(self, ops: Operation):
        self.ops = ops

    def execute(self):
        return self.ops.email()


class AddressCommand:
    def __init__(self, ops: Operation):
        self.ops = ops

    def execute(self):
        return self.ops.address()


class NextBirthdayCommand:
    def __init__(self, ops: Operation):
        self.ops = ops

    def execute(self):
        return self.ops.nxbirth()


class SearchCommand:
    def __init__(self, ops: Operation):
        self.ops = ops

    def execute(self):
        return self.ops.sear()


class InfoCommand:
    def __init__(self, ops: Operation):
        self.ops = ops

    def execute(self):
        return self.ops.info()


if __name__ == '__main__':
    op = Operation(10, 5)
    r = op.execute('add')
    print(r)
    r = op.execute('sub')
    print(r)
