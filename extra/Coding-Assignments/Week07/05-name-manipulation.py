def correct_name(name):
    result = ''
    names = name.split()
    
    last_name=names[len(names)-1]
    
    for n in range(0, len(names)-1):
        if len(result) > 0:
            result += ' '
        result += f'{names[n][0]}.'
        
    result += f' {last_name}'
    
    return result


print (correct_name('Asit Kumar Sarkar'))