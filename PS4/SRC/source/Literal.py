class Literal:
    def __init__(self, name, negative):
        self.name = name
        self.negative = negative

    def negate(self):
        self.negative = not self.negative

    def __repr__(self):
        if self.negative:
            return str('-' + self.name)
        return str(self.name)

    def __eq__(self, other):
        return self.name == other.name and self.negative == other.negative

    def __hash__(self):
        if self.negative:
            return hash('-' + self.name)
        return hash(self.name)
    
    def __lt__(self, other):
        if self.name != other.name:
            return self.name < other.name
        return self.negative < other.negative

    def clone(self):
        clone = Literal(self.name, self.negative)
        return clone
    
    def is_negative(self):
        return self.negative

    def is_opposite(self, other):
        if self.name == other.name:
            if self.negative != other.negative:
                return True
        return False

    def is_same(self, other):
        return self.name == other.name & self.negative == other.negative

    @staticmethod
    def convert_str_to_literal(string):
        string = string.strip()
        if string[0] == '-':
            literal = Literal(string[1], True)
        else:
            literal = Literal(string[0], False)
        return literal
