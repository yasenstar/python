for f in (9,1,-1):
    for l in (9,0,-1):
        for y in (9,0,-1):
            for b in (9,0,-1):
                for u in (9,0,-1):
                    for g in (9,0,-1):
                        if (8 * (f*100000+l*10000+y*1000+f*100+l*10+y) == (b*100000+u*10000+g*1000+b*100+u*10+g)) :
                            print(f,l,y,b,u,g)