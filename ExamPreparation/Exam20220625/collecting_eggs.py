from collections import deque


def take_input():
    return deque([int(x) for x in input().split(', ')])


def swap_paper_pieces(pieces: deque):
    first_paper = pieces.popleft()
    last_paper = pieces.pop()
    pieces.appendleft(last_paper)
    pieces.append(first_paper)
    return pieces


def printer(eggs_deque, paper_pieces, box_with_wrapped_eggs):
    if box_with_wrapped_eggs > 0:
        print(f"Great! You filled {box_with_wrapped_eggs} boxes.")
    else:
        print("Sorry! You couldn't fill any boxes!")

    if len(eggs_deque) > 0:
        left_eggs = ', '.join([str(x) for x in eggs_deque])
        print(f'Eggs left: {left_eggs}')

    if len(paper_pieces) > 0:
        left_paper = ', '.join([str(x) for x in paper_pieces])
        print(f'Pieces of paper left: {left_paper}')


def main(eggs_deque: deque, paper_pieces: deque):
    box_with_wrapped_eggs = 0
    while eggs_deque and paper_pieces:
        egg = eggs_deque.popleft()

        # Check egg freshness
        if egg <= 0:
            continue

        # Check for egg 13
        if egg == 13:
            # Swap first and last paper
            paper_pieces = swap_paper_pieces(paper_pieces)
            continue

        paper = paper_pieces.pop()

        # Fill the box
        if (egg + paper) <= 50:
            box_with_wrapped_eggs += 1

    return eggs_deque, paper_pieces, box_with_wrapped_eggs


if __name__ == '__main__':
    eggs_deque = take_input()
    paper_pieces = take_input()
    eggs_deque, paper_pieces, box_with_wrapped_eggs = main(eggs_deque, paper_pieces)
    printer(eggs_deque, paper_pieces, box_with_wrapped_eggs)
