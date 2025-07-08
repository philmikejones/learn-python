from ex25 import break_words, sort_words
from ex25 import print_first_word, print_last_word
from ex25 import sort_sentence
from ex25 import print_first_and_last, print_first_and_last_sorted

def test_break_words():
    assert break_words("Beans on toast") == ['Beans', 'on', 'toast']

def test_sort_words():
    assert sort_words(['toast', 'beans', 'on']) == ['beans', 'on', 'toast']

def test_print_first_word():
    assert print_first_word(['beans', 'on', 'toast']) == 'beans'

def test_print_last_word():
    assert print_last_word(['beans', 'on', 'toast']) == 'toast'

def test_sort_sentence():
    assert sort_sentence('beans and cheese on toast') == 'and beans cheese on toast'

def test_print_first_and_last():
    assert print_first_and_last('beans and cheese on toast') == ('beans', 'toast')

def test_print_first_and_last_sorted():
    assert print_first_and_last_sorted('beans and cheese on toast') == ('and', 'toast')
