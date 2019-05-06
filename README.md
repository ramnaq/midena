# MIDENA

A tool for dealing with Regular Languages and Free Context Languages. Midena Implements some algorithm arounD grammars, regular Expressions aNd finite Automata.

Project developed for class INE5421 - Formal Languages and Compilers at UFSC.
Students: Diogo Junior and Ramna Sidharta
Programming Language: Python

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

```I'm so tired
I haven't slept a wink
I'm so tired
My mind is on the blink
I wonder should I get up
and fix myself a drink
No, no no...

But it's no joke, it's doing me harm
You know I can't sleep, I can't stop my brain
You know it's three weeks, I'm going insane
You know I'd give you everything I've got
for a little peace of mind
```

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

...
