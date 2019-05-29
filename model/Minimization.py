class Group():
    def __init__(self, states=set()):
        if isinstance(states, list):
            self.states = set(states)
        else:
            self.states = states

    def __str__(self):
        return str(self.states)

    def __contains__(self, a):
        return a in self.states

    def __eq__(self, other):
        return self.states == other.states

    def __hash__(self):
        return hash(tuple(sorted(self.states)))

    def __iter__(self):
        return iter(self.states)

    def __next__(self):
        return next(self.states)

    def pop(self):
        return self.states.pop()


class Partition():

    def __init__(self, groups):
        self.groups = groups

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
        if len(self.groups) != len(other.groups):
            return False
        for group in self.groups:
            if group not in other.groups:
                return False
        return True

    def __iter__(self):
        return iter(self.groups)

    def __next__(self):
        return next(self.groups)

    def __hash__(self):
        return hash(tuple(self.states))


if __name__ == '__main__':
    p = Partition()
    final = Group(['q1', 'q3'])
    non = Group(['q2', 'q4', 'q5', 'q6'])
    p.add(final)
    p.add(non)
    print(f'Partition: {p}')
    for g in p:
        print(f'Group: {g}')
    print(p == Partition(set()))
