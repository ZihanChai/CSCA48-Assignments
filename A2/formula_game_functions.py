"""
# Copyright Nick Cheng, Mars Chai 2016
# Distributed under the terms of the GNU General Public License.
#
# This file is part of Assignment 2, CSCA48, Winter 2017
#
# This is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This file is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this file.  If not, see <http://www.gnu.org/licenses/>.
"""

# Do not change this import statement, or add any of your own!
from formula_tree import FormulaTree, Leaf, NotTree, AndTree, OrTree

# Do not change any of the class declarations above this comment

# Add your functions here.
"""
# Copyright Nick Cheng, 2016
# Distributed under the terms of the GNU General Public License.
#
# This file is part of Assignment 2, CSCA48, Winter 2017
#
# This is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This file is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this file.  If not, see <http://www.gnu.org/licenses/>.
"""

# Do not change this import statement, or add any of your own!
from formula_tree import FormulaTree, Leaf, NotTree, AndTree, OrTree

# Do not change any of the class declarations above this comment

# Add your functions here.
def build_tree_helper(formula):
    '''(str)-->list
    This function takes a string formula and returns the list
    of the input and check if the input is not in correct
    formate then return formula
    else return None
    >>>build_tree_helper('(x*y)')
    ['(', 'x', '*', 'y', ')']
    >>> build_tree_helper('((x+y)*(-x*y))')
    ['(', '(', 'x', '+', 'y', ')', '*', '(', '-', 'x', '*', 'y', ')', ')']
    >>> build_tree_helper('-((x+y)*(-x*y))')
    ['-', '(', '(', 'x', '+', 'y', ')', '*', '(', '-', 'x', '*', 'y', ')', ')']
    '''
    # Set the counters for '(', ')', and '+' and '*' signs
    left_nums = 0
    right_nums = 0
    AO_signs = 0
    # using for loop to check the format of input
    for i in range(len(formula)):
        # input should nothave space
        if formula[i] == ' ':
            return None
        # lowwer case letter and count the breakets
        elif formula[i].isalpha() is True:
            if(formula[i].isupper() is True):
                return None
            elif((formula[i-1] == ")") and (formula[i+1] == '(')):
                return None
            elif((formula[i-1] == "(") and (formula[i+1] == ')')):
                return None
        elif (formula[i] == "(") or (formula[i] == ")"):
            if(formula[i] == "("):
                left_nums += 1
            else:
                right_nums += 1
        # check if the AND or OR signs have breaket round it
        elif(formula[i] == '*') or (formula[i] == '+'):
            if (formula[i-1].isalpha() is True)and\
            (formula[i+1].isalpha() is True):
                if(formula[i-2] == '-'):
                    if(formula[i-3] != '(') or (formula[i+2] != ')'):
                        return None
                try:
                    ((formula[i-2] != '(') and (formula[i+2] != ')')) == False
                except IndexError:
                    return None
            elif(formula[i-1].isalpha() is True)and\
            (formula[i+2].isalpha() is True):
                if(formula[i-2] == '-') and (formula[i+1] == '-'):
                    if(formula[i-3] != '(') or (formula[i+2] != ')'):
                        return None
                elif(formula[i+1] == '-'):
                    if(formula[i-2] != '(') or (formula[i+2] != ')'):
                        return None
                try:
                    ((formula[i-2] != '(') and\
                     (formula[i+3] != ')')) == False
                except IndexError:
                    return None
            AO_signs += 1
        # check if the NOT signs have breaket round it
        elif(formula[i] == '-'):
            if(formula[i-1] == '(') and (formula[i+2] == ')'):
                return None
        else:
            return None
    # check if the counters have the same number
    if (AO_signs != left_nums) and (left_nums != right_nums):
        return None
    return list(formula)

def build_tree_helper1(formula):
    '''(list)-> list
    Return the formula tree in the list
    >>>build_tree_helper1(['(', 'x', '*', 'y', ')'])
    [AndTree(Leaf('x'), Leaf('y'))]
    >>>build_tree_helper1(['(', '(', 'x', '+', 'y', ')', '*', 
    '(', '-', 'x', '*', 'y', ')', ')'])
    [AndTree(OrTree(Leaf('x'), Leaf('y')), AndTree(NotTree(Leaf('x')), Leaf('y')))]
    '''
    # return itself if just a variable inside list
    if len(formula) == 1:
        return formula
    else:
        # find the first ')'
        for i in range(len(formula)):
            if formula[i] == ')':
                break
        # find the first'(' in the list from the first ')'
        for k in range(i,-1, -1):
            if formula[k] == '(':
                break
        # find the AND or OR sign between the '()'
        for m in range(k,i+1):
            if (formula[m] == '*') or (formula[m] == '+'):
                break
        # set the default of left and right child as Leaf
        left_node = Leaf(formula[m-1])
        right_node = Leaf(formula[i-1])
        # if the right or left child is already a formulatree then
        # itself is the child and it is not leaf
        if type(formula[m-1]) != str:
            left_node = formula[m-1]
        if type(formula[i-1]) != str:
            right_node = formula[i-1]
        # find NOT sign if it exist and call Not_tree_helper() function
        # to converte it to formatetree
        if((formula[m-2]) == '-'):
            left_node = NotTree(Not_tree_helper(formula[k+2:m]))
        if((formula[m+1]) == '-'):
            right_node = NotTree(Not_tree_helper(formula[m+2:i]))
        # find the sign and use the right formatetree class to converte it
        if(formula[m] == '*'):
            formula[k:i+1] = [AndTree(left_node,right_node)]
            formula = build_tree_helper1(formula[:])
        elif(formula[m] == '+'):
            formula[k:i+1] = [OrTree(left_node,right_node)]
            formula = build_tree_helper1(formula[:])
        return formula
        
def Not_tree_helper(formula):
    '''(list) -> FormateTree
    Return the formateTree form by inputing just the NOT signs and it variable
    
    >>>Not_tree_helper(['-', '(', 'x', '*', 'y', ')'])
    Leaf('y')
    '''
    # find all '-'s and usinf recursion to get the Formulatree format 
    for n in range(0,len(formula),1):
        if formula[n] == '-':
            result = NotTree(Not_tree_helper(formula[n+1:]))
        elif(type(formula[n])) != str:
            result = formula[n]
        elif(formula[n].isalpha() is True):
            result = Leaf(formula[n])
    return result

def build_tree(formula):
    '''(str)-->FormulaTree
    This function takes a string formula and returns the list
    that represents the formulaTree. if the input is not in correct
    formate then return formula
    else return None
    >>>build_tree('(x*y)')
    AndTree(Leaf('x'), Leaf('y'))
    >>> build_tree('((x+y)*(-x*y))')
    AndTree(OrTree(Leaf('x'), Leaf('y')), AndTree(NotTree\
    (Leaf('x')), Leaf('y')))
    >>> build_tree('-((x+y)*(-x*y))')
    NotTree(AndTree(OrTree(Leaf('x'), Leaf('y')), AndTree(NotTree(\
    Leaf('x')), Leaf('y'))))
    '''
    # set a bool to see if the formula has "()"
    have_breaket = False
    # using build_tree_helper() to check the format
    if type(formula) == str:
        formula = build_tree_helper(formula)
        if formula == None:
            return None
        for i in range(len(formula)):
            if formula[i] == '(':
                have_breaket = True
    # if there is breaket call build_tree_helper1() to get the format tree
        if have_breaket == True:
            formula = build_tree_helper1(formula)
        else:
    # if there is no breaket call Not_tree_helper() to get the format tree
            formula = Not_tree_helper(formula)
    else:
        return None
    
    return formula[0]

def draw_formula_tree(root):
    '''(FormulaTree)-->str
    Return a string that represent the diagram of input FormulaTree
    REQ: MUST HAVE THE CORRECT VARIBALE TYPE
    >>>draw_formula_tree(build_tree('((-x+y)*-(-y+x))'))
    '* - + x\n  - y\n  + y\n  - x'
    >>>draw_formula_tree(build_tree('(-y+x)'))
    '+ x\n  - y'
    '''
    result = ''
    # set the counter to count spaces needed
    counter = 0
    result += root.symbol
    counter += 1
    # if root is AND or OR
    if(root.symbol == '*') or (root.symbol == '+'):
        # the len on children is not 0
        if(len(root.children) != 0):
            # result and counter are adding a space, b/c it has one children
            result += ' '
            counter += 1
            # call the right of node by recursion
            result += draw_formula_tree(root.children[1])
            # switch to next line
            result += '\n'
            # count the space need for next line
            for k in range(0, counter):
                result += ' '
            # call the left of node by recursion
            result += draw_formula_tree(root.children[0])    
    # if root is NOT
    elif(root.symbol == '-'):
        # if the root has children
        if len(root.children) != 0:
            result += ' '
            counter += 1
            # call the left side of node by using recusion
            result += draw_formula_tree(root.children[0])

    return result

def evaluate(root, variables, values):
    '''
    (root, str, str)-->int
     takes a formula as represented by the FormulaTree
     rooted at root, along with a string variables containing the variables in
     the formula and a string values (of 1’s and 0’s) containing
     the corresponding truth values for the variables, and
     returns the truth value (1 or 0) of the formula.
    >>> evaluate(AndTree(Leaf('x'), Leaf('y')), 'xy', '11')
    1
    >>> evaluate(AndTree(Leaf('x'), Leaf('y')), 'xy', '10')
    0
    >>> evaluate(OrTree(OrTree(Leaf('x'), Leaf('y')),\
    OrTree(Leaf('x'), Leaf('y'))), 'xy', '11')
    1
    '''
    # setup the dictionary and result
    var_dict = {}
    result = 1
    # using for loop to get the var and val by key and val formate
    for i in range(0, len(variables)):
        var_dict[variables[i]] = values[i]
    # if root is a Leaf
    if(isinstance(root, Leaf)):
        for key in var_dict:
            # if key is equal to root
            if(key == root.symbol):
                result = int(var_dict.get(key))
    # if root is NOT
    if(isinstance(root, NotTree)):
    # using recursion to get the children of left
        child = evaluate(root.children[0], variables, values)
    # reverse 1 and 0
        if(child == 1):
            result = 0
        else:
            result = 1
    # if root is AND
    elif(isinstance(root, AndTree)):
        # if there is no child
        if(len(root.children) != "0"):
            # using recursion setup the return of right and left
            rightchild = evaluate(root.children[1], variables, values)
            leftchild = evaluate(root.children[0], variables, values)
            # if right and left is 1 or do not exist
            if(rightchild == 1 and leftchild == 1):
                result = 1
            else:
                result = 0
    
    # if root is OR
    elif(isinstance(root, OrTree)):
        # get the right and left children
        rightchild = evaluate(root.children[1], variables, values)
        leftchild = evaluate(root.children[0], variables, values)
        # if all children is 0s then return 0
        if(rightchild == 0 and leftchild == 0):
            result = 0
        # else all var are 1s
        else:
            result = 1
    return result

def play2win(root, turns, variables, values):
    '''(FormatTree, int, str, int)->str
    which takes the formula game configuration given
    by (root, turns, variables, values), and returns the best next move
    for the player whose turn is next. The formula part of the
    configuration is represented by the FormulaTree rooted
    at root. Implement this so that if there is a winning strategy
    for that player, then the corresponding
    “winning” move is returned. If there is no winning strategy,
    or if choosing either 1 or 0 would lead to winning, then 1 is
    returned if it is player E’s turn, and 0 is returned if it is
    player A’s turn. (root, turns, variables, values) must form a
    valid formula game configuration, and length
    of turns must be greater than length of values —
    i.e., there must be a next move.
    '''
    