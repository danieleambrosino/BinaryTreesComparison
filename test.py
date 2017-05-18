import random
import trees
from timeit import default_timer as timer
from sys import version_info

assert version_info[0] == 2

sizes = (10, 100, 995)


def insertion_test():
    for size in sizes:
        print "\nSIZE:", size

        ####################
        # SEQUENTIAL TREES #
        ####################

        bin_search_tree = trees.BinarySearchTree()
        red_black_tree = trees.RedBlackTree()

        for i in xrange(size):
            bin_search_tree.insert(i)
            red_black_tree.insert(i)

        print "SEQUENTIAL TREES:"
        print "Binary Search Tree height:", bin_search_tree.height()
        print "Red-Black Tree height:", red_black_tree.height()
        time = timer()
        bin_search_tree.insert(100000)
        time = timer() - time
        print "Binary Search Tree insertion time:", time
        time = timer()
        red_black_tree.insert(100000)
        time = timer() - time
        print "Red-Black Tree insertion time:", time

        ################
        # RANDOM TREES #
        ################

        bin_search_tree = trees.BinarySearchTree()
        red_black_tree = trees.RedBlackTree()

        values = random.sample(xrange(size), size)

        # Random-filling trees
        for value in values:
            bin_search_tree.insert(value)
            red_black_tree.insert(value)

        print "---"
        print "RANDOM TREES:"
        print "Binary Search Tree height:", bin_search_tree.height()
        print "Red-Black Tree height:", red_black_tree.height()
        time = timer()
        bin_search_tree.insert(100000)
        time = timer() - time
        print "Binary Search Tree insertion time:", time
        time = timer()
        red_black_tree.insert(100000)
        time = timer() - time
        print "Red-Black Tree insertion time:", time


def max_min_test():
    for size in sizes:
        print "\nSIZE:", size

        ####################
        # SEQUENTIAL TREES #
        ####################
        print "\nSEQUENTIAL TREES:\n"

        bin_search_tree = trees.BinarySearchTree()
        red_black_tree = trees.RedBlackTree()

        for i in xrange(size):
            bin_search_tree.insert(i)
            red_black_tree.insert(i)

        time = timer()
        bin_search_tree.maximum()
        time = timer() - time
        print "Binary Search Tree maximum search time:", time

        time = timer()
        red_black_tree.maximum()
        time = timer() - time
        print "Red-Black Tree maximum search time:", time

        time = timer()
        bin_search_tree.minimum()
        time = timer() - time
        print "Binary Search Tree minimum search time:", time

        time = timer()
        red_black_tree.minimum()
        time = timer() - time
        print "Red-Black Tree minimum search time:", time

        ################
        # RANDOM TREES #
        ################
        print "\nRANDOM TREES:\n"

        bin_search_tree = trees.BinarySearchTree()
        red_black_tree = trees.RedBlackTree()

        values = random.sample(xrange(size), size)

        # Random-filling trees
        for value in values:
            bin_search_tree.insert(value)
            red_black_tree.insert(value)

        time = timer()
        bin_search_tree.maximum()
        time = timer() - time
        print "Binary Search Tree maximum search time:", time

        time = timer()
        red_black_tree.maximum()
        time = timer() - time
        print "Red-Black Tree maximum search time:", time

        time = timer()
        bin_search_tree.minimum()
        time = timer() - time
        print "Binary Search Tree minimum search time:", time

        time = timer()
        red_black_tree.minimum()
        time = timer() - time
        print "Red-Black Tree minimum search time:", time


if __name__ == '__main__':
    insertion_test()
    max_min_test()
