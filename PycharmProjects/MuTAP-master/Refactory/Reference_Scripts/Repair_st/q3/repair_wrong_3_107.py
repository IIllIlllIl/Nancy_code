def remove_extras ( lst ) :
    result = [ ]
    for item in lst :
        if ( item in result ) :
            continue
        else :
            result += ( item , )
    return result
