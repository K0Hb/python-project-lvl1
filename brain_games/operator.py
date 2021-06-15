import operator


def eval_binary_expr(op1, oper, op2,
                     get_operator_fn={
                         '+' : operator.add,
                         '-' : operator.sub,
                         '*' : operator.mul,
                         }.get):
    op1,op2 = int(op1), int(op2)
    return get_operator_fn(oper)(op1, op2)
