#Написать декоратор, который логирует вызов функции и прибавляет единицу
#   к возвращаемому значению. Пример:
#   @my_decorator
#   def function():
#       return 10

#   a = my_decorator()

#   должно вывести "функция вызвана" и переменная `a` должна равняться 11.

def my_decorator(func): # Получается, что декоратор это вложенная декоратор_функция, которая принимает любая_функция и вызывает в обертка_функция(вложенная функция my_decorator) любая_функция
    def inner_func():
        print("функция вызвына")
        b = func()
        return b + 1
         
    
    return inner_func

@my_decorator
def function():
    return 10

print(function())
