class Generator:
    """Generates permutations to be tried in the site"""

    @staticmethod
    def generate(from_set, limit):
        import itertools
        var = list(map("".join, itertools.permutations(str(from_set), limit)))
        print "Generated " + str(len(var)) + " Passwords"
        return var
