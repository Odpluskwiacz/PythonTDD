
## Zadanie 1 Testowanie funkcji dodawania
def add_numbers(a,b):
    return a + b

## Testy

def test_positive():
    assert add_numbers(1,2) == 3

def test_positive_negative():
    assert add_numbers(2,-2) == 0

def test_negative():
    assert add_numbers(-2, -2) == -4

def test_zero():
    assert add_numbers(0,1) == 1

## Zadanie 2 Testowanie funkcji sprawdajacej parzystość

def is_even(n):
    return int(n % 2 == 0)   

## Testy

def test_is_even_par():
    assert is_even(10)

def test_is_even_odd():
    assert is_even(11)

def test_is_even_zero():
    assert is_even(0)

def test_is_even_big():
    assert is_even(9999999)


## Zadanie 3 Testowanie funkcji konwertującej temperature

def celsius_to_fahrenheit(celsius):
    return celsius * 9 / 5 + 32

## Testy

def test_freezing_point():
    assert celsius_to_fahrenheit(0) == 32

def test_boiling_point():
    assert celsius_to_fahrenheit(100) == 212

def test_negative_temperature():
    assert celsius_to_fahrenheit(-10) == 14

def test_large_value():
    assert celsius_to_fahrenheit(1000) == 1832

def test_zero():
    assert celsius_to_fahrenheit(0) == 32

## Zadanie 4 Testowanie funkcji obliczającej silnie

def factorial(n):
    return n * factorial(n - 1)

## Testy

def test_factorial_small():
    assert factorial(3)

def test_factorial_big():
    assert factorial(10)

def test_factorial_negative():
    assert factorial(-5)

def test_factorial_bigbig():
    assert factorial(14)

## Zadanie 5 Testowanie funkcji sprawdzającej czy liczba jest pierwsza

def is_prime(n):
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def test_is_prime():
    assert is_prime(7)

def test_is_priem_odd():
    assert is_prime(9)

def test_is_priem_2(): 
    assert is_prime(1)

def test_is_prime():
    assert is_prime(89)


