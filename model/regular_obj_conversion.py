from model.RegularGrammar import RegularGrammar
from model.FiniteAutomata import FiniteAutomata

def rg_to_fa(grammar):
    name = grammar.name + "FiniteAutomata"
    initial = grammar_symbol_form(grammar.root)
    table = {}
    sigma = set()
    acceptingState = "X"
    for prod in grammar.productions:
        state = prod[0]
        table[state] = {}
        for beta in prod[1]:
            symbol = beta[0]
            sigma.add(symbol)

            if symbol not in table[state]:
                table[state][symbol] = set()

            if len(beta) == 1:
                table[state][symbol].add(acceptingState)
            else:
                table[state][symbol].add(beta[1])

    table[acceptingState] = {}
    for t in sigma:
        table[acceptingState][t] = []

    for state in table.keys():
        for symbol in table[state]:
            table[state][symbol] = list(table[state][symbol])

    return FiniteAutomata(list(sigma), table, initial, [acceptingState])

def fa_to_rg(automata):
    name = automata.name + "Grammar"
    root = grammar_symbol_form(automata.initial)
    sigma = set(automata.sigma)

    faStates = automata.states()
    grammarStates = list(map(lambda s: grammar_symbol_form(s), faStates))
    symbols = set(grammarStates)

    productions = []

    for state in faStates:
        stateTransictions = automata.table[state]
        alpha = grammar_symbol_form(state)
        beta = []
        for symbol in automata.sigma:
            if symbol in stateTransictions.keys():
                nextStates =\
                        next_states_separated(stateTransictions, symbol)
                beta += list(map(
                            lambda ns: symbol + grammar_symbol_form(ns),\
                            nextStates)
                        )
                add_terminal_symbol(
                        symbol, beta, nextStates, automata.accepting)
        productions.append((alpha, beta))

    return RegularGrammar(symbols, sigma, productions, root, name)

def add_terminal_symbol(symbol, beta, nextStates, accepting):
    if list(filter(lambda s: s in accepting, nextStates)):
        beta.append(symbol)

def grammar_symbol_form(state):
    return "_".join(state.upper())

def next_states_separated(transitions, symbol):
    nextStates = []
    for ns in transitions[symbol]:
        nextStates += ns.split(", ")
    return nextStates

