from source.Literal import Literal

class Clause:
    def __init__(self):
        self.literal_list = []

    def is_empty(self):
        return (len(self.literal_list) == 0)
    
    def __repr__(self):
        if len(self.literal_list) == 0:
            return '{}'
        display = ' OR '.join(
            str(literal)
            for literal in self.literal_list
        )
        return display

    def clean(self):
        self.literal_list = sorted(set(self.literal_list))

    def has_2_literal_complementary(self):
        for i in range(len(self.literal_list) - 1):
            for j in range(i + 1, len(self.literal_list)):
                if self.literal_list[i].is_opposite(self.literal_list[j]):
                    return True
        return False

    def add_literal(self, literal):
        self.literal_list.append(literal)

    def negate(self):
        for literal in self.literal_list:
            literal.negate()

    def __lt__(self, other):
        if len(self.literal_list) != len(other.literal_list):
            return len(self.literal_list) < len(other.literal_list)
        for i in range(len(self.literal_list)):
            if self.literal_list[i] != other.literal_list[i]:
                return self.literal_list[i] < other.literal_list[i]
        return False

    def __eq__(self, other):
        if len(self.literal_list) != len(other.literal_list):
            return False
        for i in range(len(self.literal_list)):
            if self.literal_list[i] != other.literal_list[i]:
                return False
        return True

    def __hash__(self):
        return hash(tuple(self.literal_list))

    def is_child_of(self, parent_clause):
        return set(self.literal_list).issubset(set(parent_clause))

    @staticmethod
    def convert_str_to_clause(string_clause):
        clause = Clause()
        if 'OR' not in string_clause:
            temp_literal = Literal.convert_str_to_literal(string_clause)
            clause.add_literal(temp_literal)
            return clause

        string_literal_list = string_clause.strip().split('OR')
        for string_literal in string_literal_list:
            literal = Literal.convert_str_to_literal(string_literal)
            clause.add_literal(literal)

        clause.clean()
        return clause

    @staticmethod
    def merge_clause(clause1, clause2):
        clause = Clause()
        clause.literal_list = clause1.literal_list.copy() + clause2.literal_list.copy()
        clause.clean()
        return clause

    @staticmethod
    def PLResolve(Ci, Cj):
        is_empty = False
        set_resolve = set()
        for Li in Ci.literal_list:
            for Lj in Cj.literal_list:
                if Li.is_opposite(Lj):
                    new_clause = Clause.merge_clause(
                        Clause.create_clause_by_excepting(Ci, Li),
                        Clause.create_clause_by_excepting(Cj, Lj)
                    )
                    if new_clause.has_2_literal_complementary():
                        continue
                    if new_clause.is_empty():
                        is_empty = True
                    set_resolve.add(new_clause)
        return set_resolve, is_empty

    @staticmethod
    def create_clause_by_excepting(old_clause, remove_literal):
        new_clause = Clause()
        for literal in old_clause.literal_list:
            if literal != remove_literal:
                new_clause.add_literal(literal)
        return new_clause
    