def search ( x , seq ) :
    if ( list ( seq ) == [ ] ) :
        return 0
    elif ( x > seq [ ( - 1 ) ] ) :
        return len ( seq )
    else :
        for ref_num in range ( len ( seq ) ) :
            if ( x > seq [ ref_num ] ) :
                continue
            elif ( x <= seq [ ref_num ] ) :
                return ref_num
    return 0
