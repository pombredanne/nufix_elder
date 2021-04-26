from bayes_opt import BayesianOptimization

def test(x):
    x=x+1
    return x

def black_box_function(x, y):
    """Function with unknown internals we wish to maximize.

    This is just serving as an example, for all intents and
    purposes think of the internals of this function, i.e.: the process
    which generates its output values, as unknown.
    """
    for i in range(9):
        x=x+i+y
        print(x,i)

    return x






# Bounded region of parameter space
pbounds = {'x': (2, 4), 'y': (-3, 3)}

optimizer = BayesianOptimization(
    f=black_box_function,
    pbounds=pbounds,
    random_state=1,
)

# optimizer.probe(
#     params={"x": 0.5, "y": 0.7},
#     lazy=True,
# )

# optimizer.maximize(
#     init_points=2,
#     n_iter=3,
# )
optimizer.maximize(init_points=0, n_iter=0)