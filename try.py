try:
    var1,var2= 0,0  
    print(var2/var1)
except ZeroDivisionError:
    print("ocurre una excepcion") 
except TypeError:
    print("esta poniendo un string")     