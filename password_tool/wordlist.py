import itertools
from typing import List, Set

LEET_MAP = {
    'a': ['a', '@', '4'],
    'e': ['e', '3'],
    'i': ['i', '1', '!'],
    'o': ['o', '0'],
    's': ['s', '$', '5'],
    't': ['t', '7']
}

DEFAULT_SUFFIXES = ["!", "@", "123", "2024", "2025"]

def _case_variants(word: str) -> Set[str]:
    return {word.lower(), word.upper(), word.title()}

def _leet_variants(word: str) -> Set[str]:
    variants = [""]
    for ch in word.lower():
        if ch in LEET_MAP:
            choices = LEET_MAP[ch]
        else:
            choices = [ch]
        variants = [prev + c for prev in variants for c in choices]
    return set(variants)

def generate_wordlist(seeds: List[str], max_items: int = 1000) -> List[str]:
    words = set()
    for seed in seeds:
        words.update(_case_variants(seed))
        words.update(_leet_variants(seed))

    wordlist = []
    for w in words:
        wordlist.append(w)
        for suffix in DEFAULT_SUFFIXES:
            wordlist.append(w + suffix)
        if len(wordlist) >= max_items:
            break

    return wordlist[:max_items]
