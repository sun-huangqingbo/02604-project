from Bio import Phylo
from Bio.Phylo.Consensus import *
import pylab


# n = 23

maj_trees = []

for n in [5, 16, 23]:
    tree1 = Phylo.read(r"bacteria {}S Maximum Likelihood tree.nwk".format(n), "newick")
    tree2 = Phylo.read(r"bacteria {}S Maximum Parsimony tree.nwk".format(n), "newick")
    tree3 = Phylo.read(r"bacteria {}S Minimum Evolution tree.nwk".format(n), "newick")
    tree4 = Phylo.read(r"bacteria {}S Neighbor-Joining tree.nwk".format(n), "newick")
    tree5 = Phylo.read(r"bacteria {}S UPGMA tree.nwk".format(n), "newick")

    trees = [tree1, tree2, tree3, tree4, tree5]
    strict_tree = strict_consensus(trees)
    # Phylo.draw(strict_tree, branch_labels=lambda c: c.branch_length)
    majority_tree = majority_consensus(trees, 0.5)
    majority_tree.ladderize() 
    Phylo.draw_ascii(majority_tree)
    # Phylo.draw(majority_tree, branch_labels=lambda c: c.branch_length)
    adam_tree = adam_consensus(trees)
    # Phylo.draw(adam_tree, branch_labels=lambda c: c.branch_length)

    maj_trees.append(majority_tree)

majority_tree = majority_consensus(maj_trees, 0.5)
majority_tree.ladderize() 
Phylo.draw_ascii(majority_tree)
# Phylo.draw(majority_tree, branch_labels=lambda c: c.branch_length)