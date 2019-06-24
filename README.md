# Midena

A tool for dealing with regular languages and context-free languages. Midena implements some grammar, regular expression and finite automata algorithms.

Project developed for class INE5421 - Formal Languages and Compilers at UFSC.  
Students: Diogo Junior and Ramna Sidharta  
Programming Language: Python  
Framework for UI: PyQt 5.12

## Installation

Pre-requisites:
- git
- python 3.7
- pipenv

Clone (or download) the repository:
```git clone https://github.com/ramnasidharta/midena.git```

Install:
```pipenv install```

## Running Application

```pipenv run python app.py```

## Using

### Finite Automata

A finite automata in Midena is modeled by the class `FiniteAutomata`,
and it can represent a deterministic or non-deterministic automata.
It consists of:
* a set `sigma` of characters of the language, e.g. ['a', 'b', '&']
* an `initial` state, e.g. "q0"
* a set of `accepting` states, e.g.["q1", "q2"]
* a `table` of transitions, represented by a hashtable/dict,
    e.g. {
            "q0": {'a': ["q1"], 'b': ["q2"]},
            "q1": {'a': ["q1"], 'b': ["q3"]}
            ...
         }
Each instance of a FA also contains a name that identifies it,
and when converted it keeps a record of its grammar and regex representation.

The user can create a new automata clicking at respective button and then entering
the transition table data that is updated interactively.
The FA can be saved to a text file and be imported at any time.
If it's a non-deterministic finite automata, it can also be determinized. And it can
be converted to a regular grammar.
One can also test if a sentence pertences to the language represented by the automata.


### Regular Grammar

No specific library was used for that too. A regular grammar is represented in
Midena by the class `RegularGrammar`, which is instantiated with:
* a set `symbols` that are the non-terminal elements of productions
* a set `sigma` that contains the terminal elements
* an array of tuples (`productions`), that represents the relation between the
other grammar elements. Each tuple represent a production in the form ALPHA -> BETA,
where BETA is an array of "symbols" and "sigmas"
* a `root` symbol, that is the initial symbol of a grammar


### Regular Expression

For the first deadline of this project we didn't need to implement any algorithms for regular expressions,
so it was represented just as a string.
