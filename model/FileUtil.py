import json
from model.FiniteAutomata import FiniteAutomata
from model.ContextFreeGrammar import ContextFreeGrammar
from model.RegularGrammar import RegularGrammar
from model.RegularExpression import RegularExpression


def import_FA(path):
    data = json.load(open(path, 'r'))
    initial = data["initial"]
    accepting = data["accepting"]
    file_table = data["table"]
    sigma = []
    table = {}

    for state in file_table:
        if state not in table:
            table[state] = {}
        for symbol, transitions in file_table[state].items():
            if symbol not in sigma:
                sigma.append(symbol)
            if symbol not in table[state]:
                table[state][symbol] = []
            for i in transitions:
                table[state][symbol].append(i)
    fa = FiniteAutomata(sigma, table, initial, accepting)
    fa.name = data["name"]
    fa.regex_str = data["regex_str"]
    fa.grammar_str = data["grammar_str"]
    return fa


def export_FA(fa, path):
    fa_json = {}
    fa_json["name"] = fa.name
    fa_json["sigma"] = fa.sigma
    fa_json["table"] = fa.table
    fa_json["initial"] = fa.initial
    fa_json["accepting"] = fa.accepting
    fa_json["grammar_str"] = fa.grammar_str
    fa_json["regex_str"] = fa.regex_str

    with open(path, 'w') as outfile:
        json.dump(fa_json, outfile)

def importGrammar(path):
    data = json.load(open(path, 'r'))
    name = data["name"]
    root = data["root"]
    symbols = set(data["symbols"])
    sigma = set(data["sigma"])
    productions = [tuple(p) for p in data["productions"]]
    grammarType = data["type"]

    return createGrammar(symbols, sigma, productions, root, name)

def exportGrammar(g, path):
    gJson = {}
    gJson["name"] = g.name
    gJson["root"] = g.root
    gJson["symbols"] = list(g.symbols)
    gJson["sigma"] = list(g.sigma)
    gJson["productions"] = g.productions
    gJson["type"] = g.type

    with open(path, 'w') as outfile:
        json.dump(gJson, outfile)

def importRegEx(path):
    regex = None

    with open(path, 'r') as infile:
        regexStr = infile.readlines()[0]
 
    regex = RegularExpression(regexStr)
    return regex

def exportRegEx(re, path):
    with open(path, 'w') as outfile:
        outfile.write(str(re))

def createGrammar(symbols, sigma, productions, root, name):
    # TODO: evaluate the usage of parameter 'type' to instantiate the proper
    #       object.
    # Maybe some design pattern can be properly applyed to this case.
    grammar = None
    try:
        grammar = RegularGrammar(symbols, sigma, productions, root, name)
    except:
        grammar =\
            ContextFreeGrammar(symbols, sigma, productions, root, name)
    return grammar
