# -*- coding: utf-8 -*-
#
# colletor: willowj
#
# One-line Tree in Python
# ref https://gist.github.com/hrldcpr/2012250
# https://en.wikipedia.org/wiki/Autovivification#Python

from __future__ import unicode_literals
from __future__ import print_function

from collections import defaultdict

#----method 1 ##->----------------------------------------
# https://gist.github.com/hrldcpr/2012250

class mydefaultdict(defaultdict):

    def __getattr__(self, attr):
        return self[attr]

    def __setattr__(self, attr, val):
        self[attr] = val


def tree(): return mydefaultdict(tree)

#----method 2 ##->----------------------------------------
# https://en.wikipedia.org/wiki/Autovivification#Python


class Tree(dict):
    """docstring for Tree"""

    def __missing__(self, key):
        value = self[key] = type(self)()
        return value

    def __getattr__(self, attr):
        return self[attr]

    def __setattr__(self, attr, val):
        self[attr] = val
#----##->----------------------------------------

taxonomy = Tree()  # or tree()


taxonomy.Animalia.Chordata.Mammalia.Carnivora.Felidae.Felis.cat
taxonomy.Animalia.Chordata.Mammalia.Carnivora.Felidae['Panthera']['lion']
taxonomy.Animalia.Chordata.Mammalia.Carnivora['Canidae']['Canis']['dog']
taxonomy.Animalia.Chordata.Mammalia.Carnivora['Canidae']['Canis']['coyote']
taxonomy['Plantae']['Solanales']['Solanaceae']['Solanum']['tomato']
taxonomy['Plantae']['Solanales']['Solanaceae']['Solanum']['potato']
taxonomy['Plantae']['Solanales']['Convolvulaceae']['Ipomoea']['sweet potato']


def add(t, path):
    for node in path:
        t = t[node]

add(taxonomy,
    'Animalia>Chordata>Mammalia>Cetacea>Balaenopteridae>Balaenoptera>blue whale'.split('>'))

#----##->----------------------------------------

def ptratree(t, depth=0):
    """ print a tree """
    for k in t.keys():
        print("%s %2d %s" % (" "*4*depth, depth, k))
        depth += 1
        ptratree(t[k], depth)
        depth -= 1

ptratree(taxonomy)
import pprint
pprint.pprint (taxonomy)

#----#->----------------------------------------
'''###for method 1
def dicts(t): return {k: dicts(t[k]) for k in t}

print(dicts(taxonomy))
'''

