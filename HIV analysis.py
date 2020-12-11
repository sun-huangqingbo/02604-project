from Bio import Phylo
from Bio.Phylo.Consensus import *
import pylab
import networkx

tree1 = Phylo.read(r"HIV Maximum Likelihood tree.nwk", "newick")
tree2 = Phylo.read(r"HIV Maximum Parsimony tree.nwk", "newick")
tree3 = Phylo.read(r"HIV Minimum Evolution tree.nwk", "newick")
tree4 = Phylo.read(r"HIV Neighbor-Joining tree.nwk", "newick")
tree5 = Phylo.read(r"HIV UPGMA tree.nwk", "newick")

trees = [tree1, tree2, tree3, tree4, tree5]
strict_tree = strict_consensus(trees)
Phylo.draw(strict_tree, branch_labels=lambda c: c.branch_length)
majority_tree = majority_consensus(trees, 0.5)
Phylo.draw(majority_tree, branch_labels=lambda c: c.branch_length)
# Phylo.draw_ascii(majority_tree)

adam_tree = adam_consensus(trees)
Phylo.draw(adam_tree, branch_labels=lambda c: c.branch_length)

