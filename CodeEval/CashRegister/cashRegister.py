register = {0.01:'PENNY', 0.05:'NICKEL', 0.10:'DIME', 0.25:'QUARTER', 0.50:'HALF DOLLAR', 1.00:'ONE', 2.00:'TWO',5.00:'FIVE', 10.00:'TEN', 20.00:'TWENTY', 50.00: 'FIFTY', 100.00:'ONE HUNDRED'}
filename = "test_cashregister.txt"
with open(filename) as f:
    for test in f:
        print test
        test = test.strip().split(";")
        cost = float(test[0])
        paid = float(test[1])
        if paid < cost:
            print "ERROR"
            continue
        if paid == cost:
            print "ZERO"
            continue
        change = paid - cost
        print change
        res = [] 
        units = sorted(register.keys())[::-1]
        for unit in units: 
            change = round(change, 2)
            if change == 0:
                break
            if change >= unit:
                mult = int(change/unit)
                res.extend([register[unit]] * mult )
                change = change - mult*unit
        print ",".join(res)
