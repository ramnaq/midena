class Group():
    def __init__(self, states=None):
        if states is None:
            self.states = set()
        elif isinstance(states, list):
            self.states = set(states)
        else:
            self.states = states

    def __str__(self):
        return str(self.states)

    def __contains__(self, a):
        r = a in self.states
        return r

    def __eq__(self, other):
        return self.states == other.states

    def __hash__(self):
        h = hash(tuple(sorted(self.states)))
        return h

    def __iter__(self):
        return iter(self.states)

    def __next__(self):
        return next(self.states)

    def add(self, elem):
        self.states.add(elem)

    def pop(self):
        return self.states.pop()


class Partition():

    def __init__(self, groups=None):
        self.groups = groups if groups is not None else set()

    def __str__(self):
        return f'{[str(g) for g in self.groups]}'.replace('"', '')

    def has(self, elem):
        return (self.group_of(elem) is not None)

    def group_of(self, elem):
        for group in self.groups:
            if elem in group:
                return group
        return None

    def add(self, g: Group):
        self.groups.add(g)

    def remove(self, g: Group):
        self.groups.remove(g)

    def pop(self):
        return self.groups.pop()

    def __eq__(self, other):
        if not isinstance(other, Partition):
            return False
        return self.groups == other.groups

    def __iter__(self):
        return iter(self.groups)

    def __next__(self):
        return next(self.groups)

    def __hash__(self):
        return hash(tuple(sorted(self.groups)))

    def __contains__(self, g):
        return g in self.groups
