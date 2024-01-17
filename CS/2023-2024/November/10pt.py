import batches as batch

def solve():

    cards = []
    with open('input.txt') as f:
        count = int(f.readline())
        # We store each card as a tuple with card index and 3 card parameters.
        for i in range(count):
            n, s, c = f.readline().split()
            cards.append((i,n,c,s))

    batches = []
    # Go over each combination of 4 cards, and save it in "batches" list if it is a batch
    for p in batch.combinations(cards, 4):
        if batch.is_batch(p):
            batches.append(p)

    with open('output.txt', 'w') as f:
        f.write(str(batch.find_valid_batch_subset_size(batches)))


if __name__ == "__main__":
    solve()