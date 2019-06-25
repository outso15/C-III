
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'DIVIDE MINUS NUMBER PLUS TIMESexpression : expression expression PLUSexpression : expression expression MINUSexpression : expression expression TIMESexpression : expression expression DIVIDEexpression : termterm : factorfactor : NUMBER'
    
_lr_action_items = {'DIVIDE':([1,2,3,5,6,7,8,9,],[-5,-7,-6,6,-4,-3,-1,-2,]),'NUMBER':([0,1,2,3,4,5,6,7,8,9,],[2,-5,-7,-6,2,2,-4,-3,-1,-2,]),'TIMES':([1,2,3,5,6,7,8,9,],[-5,-7,-6,7,-4,-3,-1,-2,]),'PLUS':([1,2,3,5,6,7,8,9,],[-5,-7,-6,8,-4,-3,-1,-2,]),'MINUS':([1,2,3,5,6,7,8,9,],[-5,-7,-6,9,-4,-3,-1,-2,]),'$end':([1,2,3,4,6,7,8,9,],[-5,-7,-6,0,-4,-3,-1,-2,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'term':([0,4,5,],[1,1,1,]),'expression':([0,4,5,],[4,5,5,]),'factor':([0,4,5,],[3,3,3,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> expression","S'",1,None,None,None),
  ('expression -> expression expression PLUS','expression',3,'p_expression_plus','parser_rules.py',5),
  ('expression -> expression expression MINUS','expression',3,'p_expression_minus','parser_rules.py',11),
  ('expression -> expression expression TIMES','expression',3,'p_expression_times','parser_rules.py',17),
  ('expression -> expression expression DIVIDE','expression',3,'p_expression_divide','parser_rules.py',23),
  ('expression -> term','expression',1,'p_expression_term','parser_rules.py',29),
  ('term -> factor','term',1,'p_term_factor','parser_rules.py',33),
  ('factor -> NUMBER','factor',1,'p_factor_num','parser_rules.py',37),
]
