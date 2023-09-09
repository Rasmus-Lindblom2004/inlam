def prime_tal(n):
    prime=[]

    # En loop som börjar på 2(första prim talet) och går till n inklusivt
    for tal in range(2,n+1):
        is_prime = True

        # går i genom all hittills funna prim tal 
        # och kollar om tal är ett primtal
        for prim in prime:
            if tal % prim == 0:
                is_prime = False
                break
        
        # om tal är ett primtal så läggs det till i prime listan
        if is_prime:
            prime.append(tal)
        
    return " ".join(map(str, prime))