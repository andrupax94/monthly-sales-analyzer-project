# Example data
data = [
    {"day": 1, "product_a": 202, "product_b": 142, "product_c": 164},
    {"day": 2, "product_a": 206, "product_b": 121, "product_c": 338},
    {"day": 3, "product_a": 120, "product_b": 152, "product_c": 271},
    {"day": 4, "product_a": 174, "product_b": 137, "product_c": 266},
    {"day": 5, "product_a": 199, "product_b": 153, "product_c": 301},
    {"day": 6, "product_a": 230, "product_b": 199, "product_c": 202},
    {"day": 7, "product_a": 101, "product_b": 137, "product_c": 307},
    {"day": 8, "product_a": 137, "product_b": 179, "product_c": 341},
    {"day": 9, "product_a": 287, "product_b": 70, "product_c": 310},
    {"day": 10, "product_a": 157, "product_b": 71, "product_c": 238},
    {"day": 11, "product_a": 148, "product_b": 108, "product_c": 319},
    {"day": 12, "product_a": 287, "product_b": 64, "product_c": 339},
    {"day": 13, "product_a": 289, "product_b": 100, "product_c": 257},
    {"day": 14, "product_a": 154, "product_b": 113, "product_c": 280},
    {"day": 15, "product_a": 150, "product_b": 184, "product_c": 170},
    {"day": 16, "product_a": 172, "product_b": 67, "product_c": 281},
    {"day": 17, "product_a": 188, "product_b": 109, "product_c": 163},
    {"day": 18, "product_a": 108, "product_b": 139, "product_c": 202},
    {"day": 19, "product_a": 229, "product_b": 133, "product_c": 241},
    {"day": 20, "product_a": 210, "product_b": 57, "product_c": 324}
]
#funciones para validar datos
def valid_days(data,start,end):
    if str(type(start))=="<class 'int'>" and str(type(end))=="<class 'int'>":
        if start>=1 and end<=len(data) and start<=end:
            return True
        else:
            print(f"Rango de dias invalido Maximo:{len(data)} dias")
            return False
    else:
        print("Los parametros start y end deben ser enteros")
        return False

def valid_product_key(data,product_key):
    
  
    if str(type(product_key))=="<class 'str'>":
       
        found=False
        if(len(product_key)==1 and product_key.isalpha()):
            print(f"Se Especifico \"{product_key}\" como parametro, Se usara \"product_{product_key}\" en su lugar")
            product_key=f"product_{product_key}"
        for sales in data:
            for sale in sales.keys():
                if(sale==product_key):
                    found=product_key
        if(found):
            return product_key
        else:
            print(f"El Producto {product_key} No Existe en el diccionario")
            return False

    else:
        print("El Parametro pasado no es un string")
        return False



#ejercicios
def total_sales_by_product(data, product_key,start=1,end=20,onlyValue=False):
    product_key=valid_product_key(data,product_key)
    validDays=valid_days(data,start,end)
    total=0
    if(product_key and validDays):
        for sales in range(start-1, end):
            sales=data[sales]
            for sale in sales.keys():
                if(sale==product_key):
                    total+=int(sales[sale])
        if(onlyValue):
            return total
        else:
            return f"Total Ventas del {product_key}: {total}"
    else:
        return False

def average_daily_sales(data, product_key,start=1,end=20):
    product_key=valid_product_key(data,product_key)
    total=total_sales_by_product(data,product_key,start,end,True)
    if(total):
        dias=end-start+1
        average=round(total/dias,2)
        return f"El Promedio De Ventas Del {product_key} Entre el dia {start} y {end} es: {average}"
    else:
        return False

def best_selling_day(data,start=1,end=20):
    validDays=valid_days(data,start,end)
    if(validDays):
        max_sales = 0
        best_day = ""
        for sales in range(start-1, end):
            sales=data[sales]
            total = 0
            for key, value in sales.items():
                if key.startswith("product_"): 
                    total += value
            if total > max_sales:
                max_sales = total
                best_day = sales["day"]
        return f"El dia con mayores ventas entre el {start} y el {end} fue el dia: {best_day} con un total de {max_sales}"
    else:
        return False

def days_above_threshold(data, product_key,threshold,start=1,end=20):
    product_key=valid_product_key(data,product_key)
    validDays=valid_days(data,start,end)
    days=0
    if(product_key and validDays):
        for sales in range(start-1, end):
            sales=data[sales]
            for key, value in sales.items():
                if key==product_key:
                    if(value>threshold):
                        days+=1
        return f"El {product_key} supero el umbral de {threshold} en un numero de {days} dias en el rango de dias de: {start} - {end}" 
    else:
        return False

def top_product(data,start=1,end=20):
    validDays=valid_days(data,start,end)
    if(validDays):
        totales={}
        max_sales = 0
        max_sales_product=""
        for sales in range(start-1, end):
            sales=data[sales]
            for key, value in sales.items():
                if key.startswith("product_"): 
                    if(key in totales):
                        totales[key] += value
                    else:
                        totales[key]=value
        for key,value in totales.items():
            if value>max_sales:
                max_sales_product=key
                max_sales=value
        return f"El {max_sales_product} fue el producto que vendio mas con: {max_sales} unidades entre los dias: {start} y {end}"
    else:
        return False



# Testeo De Funciones
print(total_sales_by_product(data, "a",1,20))
print(average_daily_sales(data, "product_b"))
print(best_selling_day(data,5,20))
print(days_above_threshold(data, "product_c",threshold=300))
print(top_product(data))
