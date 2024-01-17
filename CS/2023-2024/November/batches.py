"""This is a bruteforce solution that does not employ any optimizations
it works in 2^(n^2) * n for 10pt"""

SET_SIZE = 4
BATCH_PARAM_POWER = [SET_SIZE, 1]

def is_batch(batch_cards):
    """Determines if set of cards forms a batch. This can easily be extended to handle any
    number of cards with any number of parameters"""
    if len(batch_cards) != SET_SIZE:
        return False

    N, S, C = set(), set(), set()
    for card in batch_cards:
        N.add(card[1])
        S.add(card[2])
        C.add(card[3])
    return len(N) in BATCH_PARAM_POWER and            len(S) in BATCH_PARAM_POWER and            len(C) in BATCH_PARAM_POWER

def is_valid_batchset(batches):
    """Determines if batchset contains the same card more than once."""
    used_cards = set()
    for batch in batches:
        for card in batch:
            if card[0] in used_cards: 
                return False
            used_cards.add(card[0])
    return True

def find_valid_batch_subset_size(batches):
    """Will try every combination starting with the most promising one. 
    worst case would work in 2^len(batches) * n"""
    if not batches:
        return 0
    if len(batches) == 1:
        return 1
    # Check subsets of all sizes, starting with the biggest one
    for test_n in range(len(batches), 1, -1):
        # Iterate over all subsets of size test_n
        for batch_set in combinations(batches, test_n):
            # Test if the subset contains the same card more than once. If not -- return it as bigest valid subset.
            if is_valid_batchset(batch_set):
                print(batch_set)
                return test_n
    # If we have not found valid batchset of size at least 2, then there is bathset of size 1.
    return 1

# This is a library function from itertools. You can import it like `from itertools import combinations`
# Read more about it here: https://docs.python.org/3/library/itertools.html#itertools.combinations
# More info on for/else: https://docs.python.org/3/tutorial/controlflow.html#break-and-continue-statements-and-else-clauses-on-loops
def combinations(iterable, r):
    # combinations('ABCD', 2) --> AB AC AD BC BD CD
    # combinations(range(4), 3) --> 012 013 023 123
    pool = tuple(iterable)
    n = len(pool)
    if r > n:
        return
    indices = list(range(r))
    yield tuple(pool[i] for i in indices)
    while True:
        for i in reversed(range(r)):
            if indices[i] != i + n - r:
                break
        else:
            return
        indices[i] += 1
        for j in range(i+1, r):
            indices[j] = indices[j-1] + 1
        yield tuple(pool[i] for i in indices)


if __name__ == "__main__":
    solve()