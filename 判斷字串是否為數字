#判斷字串是否為數字
def is_number(s):
    try:
    	float(s)
    	return True
    except ValueError:
        pass

    try:
        import unicodedata #載入模塊
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
    	pass

    return False
    
#測試

print(is_number('foo'))
print(is_number('1'))
print(is_number('1.3'))
print(is_number('-1.37'))
print(is_number('1e3'))

#測試unicode
print(is_number('四'))    	

            	
