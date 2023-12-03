from source.Clause import Clause


class KnowledgeBase:
    def __init__(self):
        self.KB = []

    def add_clause(self, clause):
        self.KB.append(clause)

    def length(self):
        return len(self.KB)

    @staticmethod
    def convert_str_list_to_KB(string_clause_list):
        KB = KnowledgeBase()
        for string_clause in string_clause_list:
            temp_clause = Clause.convert_str_to_clause(string_clause)
            temp_clause.clean()
            KB.add_clause(temp_clause)
        return KB
