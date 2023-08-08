import os
import contextlib, io
import importlib
import random
import ruamel.yaml

yaml = ruamel.yaml.YAML()

# set fixed seed for generating test cases
random.seed(123456789)

# locate evaldir
evaldir = os.path.join('..', 'evaluation')
if not os.path.exists(evaldir):
    os.makedirs(evaldir)

# locate solutiondir
solutiondir = os.path.join('..', 'solution')
if not os.path.exists(solutiondir):
    os.makedirs(solutiondir)

# load functionality defined in sample solution
module_name = 'solution'
file_path = os.path.join(solutiondir, 'solution.nl.py')
spec = importlib.util.spec_from_file_location(module_name, file_path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

def write_yaml( data:list ):
    """ A function to write YAML file"""
    with open(os.path.join('..', 'evaluation', 'tests.yaml'), 'w', encoding='utf-8') as f:
        yaml.dump(data, f)

# generate test data
ntests= 15
cases = [(6,8), ]
while len(cases) < ntests:
    cases.append( tuple(random.randint(1,10) for _ in range(2)) ) 

# generate unit tests for functions
yamldata = []
yamldata.append( {'tab': 'Feedback', 'testcases': []})
# input, expression, statement or stdin?
input = 'expression'
# output, stdout or return?
output = 'stdout'
for test in cases:
    # generate test expression
    expression_name = 'schaakbord( {}, {} )'.format( test[0], test[1] )
    
    f = io.StringIO()
    with contextlib.redirect_stdout( f ):
        module.schaakbord( test[0], test[1] )
    
    result = f.getvalue().strip() 
    
    # setup for return expressions
    testcase = { input: expression_name, output: ''+ result }
    yamldata[0]['testcases'].append( testcase )

write_yaml(yamldata)
