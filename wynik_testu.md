============================= test session starts ==============================
platform linux -- Python 3.12.3, pytest-7.4.4, pluggy-1.4.0
rootdir: /home/odpluskwiacz/Szablony/TestDrivenDevelopment
collected 19 items

Inżynieria_Oprogramowania_TDD.py .....F.F....FFFF...                     [100%]

=================================== FAILURES ===================================
_______________________________ test_is_even_odd _______________________________

    def test_is_even_odd():
>       assert is_even(11)
E       assert 0
E        +  where 0 = is_even(11)

Inżynieria_Oprogramowania_TDD.py:31: AssertionError
_______________________________ test_is_even_big _______________________________

    def test_is_even_big():
>       assert is_even(9999999)
E       assert 0
E        +  where 0 = is_even(9999999)

Inżynieria_Oprogramowania_TDD.py:37: AssertionError
_____________________________ test_factorial_small _____________________________

    def test_factorial_small():
>       assert factorial(3)

Inżynieria_Oprogramowania_TDD.py:70: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

n = -964

    def factorial(n):
>       return n * factorial(n - 1)
E       RecursionError: maximum recursion depth exceeded

Inżynieria_Oprogramowania_TDD.py:65: RecursionError
______________________________ test_factorial_big ______________________________

    def test_factorial_big():
>       assert factorial(10)

Inżynieria_Oprogramowania_TDD.py:73: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

n = -957

    def factorial(n):
>       return n * factorial(n - 1)
E       RecursionError: maximum recursion depth exceeded

Inżynieria_Oprogramowania_TDD.py:65: RecursionError
___________________________ test_factorial_negative ____________________________

    def test_factorial_negative():
>       assert factorial(-5)

Inżynieria_Oprogramowania_TDD.py:76: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

n = -972

    def factorial(n):
>       return n * factorial(n - 1)
E       RecursionError: maximum recursion depth exceeded

Inżynieria_Oprogramowania_TDD.py:65: RecursionError
____________________________ test_factorial_bigbig _____________________________

    def test_factorial_bigbig():
>       assert factorial(14)

Inżynieria_Oprogramowania_TDD.py:79: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
Inżynieria_Oprogramowania_TDD.py:65: in factorial
    return n * factorial(n - 1)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

n = -953

    def factorial(n):
>       return n * factorial(n - 1)
E       RecursionError: maximum recursion depth exceeded

Inżynieria_Oprogramowania_TDD.py:65: RecursionError
=========================== short test summary info ============================
FAILED Inżynieria_Oprogramowania_TDD.py::test_is_even_odd - assert 0
FAILED Inżynieria_Oprogramowania_TDD.py::test_is_even_big - assert 0
FAILED Inżynieria_Oprogramowania_TDD.py::test_factorial_small - RecursionErro...
FAILED Inżynieria_Oprogramowania_TDD.py::test_factorial_big - RecursionError:...
FAILED Inżynieria_Oprogramowania_TDD.py::test_factorial_negative - RecursionE...
FAILED Inżynieria_Oprogramowania_TDD.py::test_factorial_bigbig - RecursionErr...
========================= 6 failed, 13 passed in 1.07s =========================
