
def dag2html(dag, is_obj=False):
    if not is_obj:
        dag = eval(dag)
