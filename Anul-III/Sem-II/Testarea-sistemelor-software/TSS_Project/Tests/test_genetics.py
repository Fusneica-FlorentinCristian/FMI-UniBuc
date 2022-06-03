"""
Determinating genetics_main basic() equivalence classes:

N_POPULATION, N_SELECTED > 0
    N_POPULATION and N_SELECTED > 0
    N_POPULATION or N_SELECTED <= 0

N_POPULATION >= N_SELECTED
    2 classes: N_POPULATION >= N_SELECT and N_POPULATION < N_SELECT

0 ... 1 < MUTATION_PROBABILITY, i.e  0 <= MUTATION_PROBABILITY <= 1
    MUTATION_PROBABILITY <= 0
    0 < MUTATION_PROBABILITY <= 1 (if > 1, it is as MUTATION_PROBABILITY == 1)

target's chars must be in genes
    all of targets's chars are in genes
    not all of targets's chars are in genes

debug:
    either true or false
"""
import pytest
from genetics_main import basic as gen


def test_basic1():
    target_str = "This is a genetic algorithm to evaluate, combine, evolve, and mutate a string! Also, TSS is amazing!"
    genes_list = list(" ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz.,;!?+-*#@^'èéòà€ù=)(&%$£/\\")
    N_POPULATION = 200
    N_SELECTED = 50
    MUTATION_PROBABILITY = 0.5
    assert gen(target_str, genes_list, N_POPULATION, N_SELECTED, MUTATION_PROBABILITY, debug=False)


def test_basic2():
    target_str = "This is a genetic algorithm to evaluate, combine, evolve, and mutate a string! Also, TSS is amazing!"
    genes_list = list(" ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz.,;!?+-*#@^'èéòà€ù=)(&%$£/\\")
    N_POPULATION = 20
    N_SELECTED = 50
    MUTATION_PROBABILITY = 0.5
    with pytest.raises(ValueError):
        assert gen(target_str, genes_list, N_POPULATION, N_SELECTED, MUTATION_PROBABILITY, debug=False)


def test_basic3():
    target_str = "This is a genetic algorithm to evaluate, combine, evolve, and mutate a string! Also, TSS is amazing!"
    genes_list = list(" ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz.,;!?+-*#@^'èéòà€ù=)(&%$£/\\")
    N_POPULATION = 200
    N_SELECTED = -50
    MUTATION_PROBABILITY = 0.5
    with pytest.raises(ValueError):
        assert gen(target_str, genes_list, N_POPULATION, N_SELECTED, MUTATION_PROBABILITY, debug=False)


def test_basic4():
    target_str = "This is a genetic algorithm to evaluate, combine, evolve, and mutate a string! Also, TSS is amazing!"
    genes_list = list(" ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefgijklmnopqrstuvwxyz.,;!?+-*#@^'èéòà€ù=)(&%$£/\\")
    # genes_list has no letter "h"
    N_POPULATION = 200
    N_SELECTED = 50
    MUTATION_PROBABILITY = 0.5
    with pytest.raises(ValueError):
        assert gen(target_str, genes_list, N_POPULATION, N_SELECTED, MUTATION_PROBABILITY, debug=False)


def test_basic5():
    target_str = "This is a genetic algorithm to evaluate, combine, evolve, and mutate a string! Also, TSS is amazing!"
    genes_list = list(" ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz.,;!?+-*#@^'èéòà€ù=)(&%$£/\\")
    N_POPULATION = 200
    N_SELECTED = 50
    MUTATION_PROBABILITY = -5
    with pytest.raises(ValueError):
        assert gen(target_str, genes_list, N_POPULATION, N_SELECTED, MUTATION_PROBABILITY, debug=False)


def test_basic6():
    target_str = "This is a genetic algorithm to evaluate, combine, evolve, and mutate a string! Also, TSS is amazing!"
    genes_list = list(" ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz.,;!?+-*#@^'èéòà€ù=)(&%$£/\\")
    N_POPULATION = 200
    N_SELECTED = 50
    MUTATION_PROBABILITY = 0.5
    assert gen(target_str, genes_list, N_POPULATION, N_SELECTED, MUTATION_PROBABILITY, debug=False)


def test_basic7(capfd):
    target_str = "This is a genetic algorithm to evaluate, combine, evolve, and mutate a string! Also, TSS is amazing!"
    genes_list = list(" ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz.,;!?+-*#@^'èéòà€ù=)(&%$£/\\")
    N_POPULATION = 200
    N_SELECTED = 50
    MUTATION_PROBABILITY = 2

    gen(target_str, genes_list, N_POPULATION, N_SELECTED, MUTATION_PROBABILITY, debug=True)

    out, err = capfd.readouterr()

    assert out is not None and out != ""


def test_basic8(capfd):
    target_str = "This is a genetic algorithm to evaluate, combine, evolve, and mutate a string! Also, TSS is amazing!"
    genes_list = list(" ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz.,;!?+-*#@^'èéòà€ù=)(&%$£/\\")
    N_POPULATION = 200
    N_SELECTED = 50
    MUTATION_PROBABILITY = 0.7

    gen(target_str, genes_list, N_POPULATION, N_SELECTED, MUTATION_PROBABILITY, debug=False)

    out, err = capfd.readouterr()

    assert out is None or out == ""
