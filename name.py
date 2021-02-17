#სემოვიტანოთ ბიბლიოთეკები
import random
import math
#ავირჩიოთ ორი მარტივი p და q რიცხვი, რომლებიც არ არის ერთმანეთის ტოლი
 
p = int(input("p = \n"))
q = int(input("q = \n"))

#შემოწმება

#გამოვთვალოთ n რიცხვი, რომელიც ტოლი n = p * q
if ( p % 2 == 1 & q % 2 == 1):
    n = p * q

#გამოვთვალოთ f(n), რომელიც ტოლია f(n) = (p-1) * (q-1)

    fn = (p-1)*(q-1)

    print ('n =',n)
    print ('fn =',fn)

#ვიპოვოთ e რიცხვი, რომელიც თანამარტივია f(n)-თან, მეტია 1ზე და ნაკლებია f(n)-ზე
#რიცხვები რომლებიც თანამარტივია 
#ევკლიდეს ალგორითმი
    b = list(range(2,fn))

    em = []
    for num in b:
        if math.gcd(num, fn) == 1:
            em.append(num)

    print ("1-ზე მეტი და ",fn,'-ზე ნაკლები,',fn,'-თან თანამარტივი რიცხვებია ',em)

#შემთხვევითად ამოვირჩიოთ რიცხვი em მასივიდან , რომელიც მიენიჭება e-ს
    e = random.choice(em)
    # e = 13

    print ('რიცხვებიდან შემთხვევითად აღებულია , რიცხვი ',e)
    print ('საჯარო გასაღებია {',e,',',n,'}')

#გამოვთვალოთ d-ს მნიშვნელობა ფორმულით d = ((f(n) * i) + 1 ) / e
#ევკლიდეს გაფართოებული ალგორითმი



    i = 1
    while i !=0 :
        de = ((fn * i) + 1 ) / e
        i +=1
        if de == int(de):
            d = i - 1
            print (de)
            break
    print ("i ტოლია - ",d)
    print ("ვიპოვეთ მთელი რიცხვი d, რომელიც ტოლია ",de)

#შეიყვანეთ დასაშიფრი P , რომელიც წარმოადგენს დასაშიფრ სიმბოლოს, რათა ვიპოვოთ C
    P = int(input("შეიყვანეთ დასაშიფრი სიმბოლო \n"))
    print ("დასაშიფრი სიმბოლოა -",P)
#გამოვთვალოთ C , ანუ დავშიფროთ ტექსტი P
    C = (pow(P,e)) % n
    print ("დაშიფრული ტექსტია -",C)

#გავშიფროთ დაშიფრული ტექსტი C, ანუ გამოვთვალოთ P
    do = int(de)
    P1 = (pow(C,do)) % n


    print("p =",p)
    print("q =",q)
    print("n =",n)
    print("f(n) =",fn)
    print("e =",e)
    print("საჯარო გასაღებია {",e,',',n,'}')
    print("d =",d)
    print("პირადი გასაღებია {",d,',',n,'}')
    print("დაშიფრული ტექსტი -",C)
    print("დასაშიფრი და გაშიფრული ტექსტი -",P,' და ',P1)



else :
    print("p ან q არ არის თანამარტივი")