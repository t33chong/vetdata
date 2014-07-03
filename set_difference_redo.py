redone = set([line.strip() for line in open('redo.txt')])
top5k = set([line.strip() for line in open('top5k.txt')])

todo = list(top5k - redone)

with open('top5k_minus_redone.txt', 'w') as f:
    f.write('\n'.join(todo))
