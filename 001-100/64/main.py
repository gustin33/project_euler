count = 4
for m in range(14, 10_000+1):
    if (m**(0.5) != int(m**0.5)):
        print(m)
        dcn = [(0, 1)]
        while True:
            dn, cn = dcn[-1]
            bn = int((m**0.5+dn)/cn)
            dnplus1 = int(cn*bn - dn)
            cnplus1 = int((m - dnplus1**2)/cn)
            dcnplus1 = (dnplus1, cnplus1)
            if dcnplus1 in dcn:
                index = dcn.index(dcnplus1)
                period = len(dcn)-index
                break
            dcn.append((int(dnplus1), int(cnplus1)))
        if period % 2 == 1:
            count += 1
print(f"count: {count}")
