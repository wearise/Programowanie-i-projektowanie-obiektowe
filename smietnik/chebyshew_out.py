def chebyshev_out(k):
    if k==0:
        return [1]
    elif k==1:
        return [1,0]
    else:
        T_k_1 = chebyshev_out(k-1)
        T_k_1 = [2 * x for x in T_k_1] #mnoze liste *2
        T_k_1.append(0) #dodaje 0 na koncu - podnosze potege (*x)
        T_k_2 = chebyshev_out(k-2)
        T_k_2 = [0,0] + T_k_2 #dodaje dwa zera na poczatku zeby byly zgodne wymiary
        return [T_k_1[i]-T_k_2[i] for i in range(len(T_k_1))]