def search ( x , seq ) :
    for ref_k in range ( len ( seq ) ) :
        if ( x <= seq [ ref_k ] ) :
            return ref_k
        if ( x > seq [ ref_k ] ) :
            continue
    return len ( seq )
