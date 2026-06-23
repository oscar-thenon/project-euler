counter = 0

h = 0
while (h <= 1):
    if 200*h <= 200:
        g = 0
        while (g <= 2):
            if 200*h+100*g <= 200:
                f = 0
                while (f <= 4):
                    if 200*h+100*g+50*f <= 200:
                        e = 0
                        while (e <= 10):
                            if 200*h+100*g+50*f+20*e <= 200:
                                d = 0
                                while (d <= 20):
                                    if 200*h+100*g+50*f+20*e+10*d <= 200:
                                        c = 0
                                        while (c <= 40):
                                            if 200*h+100*g+50*f+20*e+10*d+5*c <= 200:
                                                b = 0
                                                while (b <= 100):
                                                    if 200*h+100*g+50*f+20*e+10*d+5*c+2*b <= 200:
                                                        a = 0
                                                        while (a <= 200):
                                                            if 200*h+100*g+50*f+20*e+10*d+5*c+2*b+a == 200:
                                                                counter += 1
                                                                print a,b,c,d,e,f,g,h
                                                            a += 1
                                                    b += 1
                                            c += 1
                                    d += 1
                            e += 1
                    f += 1
            g += 1
    h += 1

print "Answer is", counter