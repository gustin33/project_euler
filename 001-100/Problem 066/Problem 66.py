from time import time
start = time()


def cont_frac_rep__and__period_of_sqrt(n):  # returns (period, representation)
    if int(n**0.5) == n**0.5:
        return 0, [n**0.5]
    a_b_c = [(int(n**0.5), int(n**0.5), n - int(n**0.5)**2)]  # a_0,b_0,c_0
    while a_b_c[-1][2] != 1:  # see paper for formulas
        a_n = int((a_b_c[0][0]+a_b_c[-1][1])/(a_b_c[-1][2]))  # 0 for a, 1 for b, 2 for c
        b_n = a_n * a_b_c[-1][2] - a_b_c[-1][1]
        c_n = (n-b_n**2)//(a_b_c[-1][2])
        a_b_c.append((a_n, b_n, c_n))
    representation = [a_b_c[j][0] for j in range(len(a_b_c))]
    representation.append(int((a_b_c[0][0]+a_b_c[-1][1])/(a_b_c[-1][2])))
    return len(representation)-1, representation


def mth_convergent_sqrt_(m, n):  # returns (p_n, q_n)
    m -= 1
    periodic_part = cont_frac_rep__and__period_of_sqrt(n)[1]
    a_1 = periodic_part[0]
    del periodic_part[0]
    b = m//(len(periodic_part))
    c = m % len(periodic_part)
    an_list = periodic_part*b + [periodic_part[num] for num in range(c)]
    pn_qn = [(1, 0), (a_1, 1)]
    num = 2
    while num <= m+1:
        pn_qn.append((an_list[num-2] * pn_qn[-1][0] + pn_qn[-2][0], an_list[num-2] * pn_qn[-1][1] + pn_qn[-2][1]))
        num += 1
    return pn_qn[-1][0], pn_qn[-1][1]



def least_solution_pells_eq(n, b):  # x^2-n*y^2 = b; b  1, -1
    period = cont_frac_rep__and__period_of_sqrt(n)[0]
    if int(n**0.5) == n**0.5:
        if b == 1:
            return 1, 0
        else:
            return 0, 1
    elif period % 2 == 0:
        if b == -1:
            return -1, -1  # we´ll use this as a flag for no solutions
        else:
            return mth_convergent_sqrt_(cont_frac_rep__and__period_of_sqrt(n)[0], n)
    else:
        if b == -1:
            return mth_convergent_sqrt_(cont_frac_rep__and__period_of_sqrt(n)[0], n)
        else:
            return mth_convergent_sqrt_(2*cont_frac_rep__and__period_of_sqrt(n)[0], n)



def max_x_given_n(n):
    if int(n**0.5) == n**0.5:
        return 0
    non_square_list = [num for num in range(2, n+1) if num**0.5 != int(num**0.5)]
    x_list = []
    d_list = []
    for d in non_square_list:
        x_list.append(least_solution_pells_eq(d, 1))
        d_list.append(d)
    return d_list[x_list.index(max(x_list))]


print(max_x_given_n(1000))
print(time()-start)
