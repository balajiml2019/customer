import cusr as CM
srch = CM.Cust_Controller()
class Srch_Cust_Param:
    def __init__(self, **kwargs):
        if len(kwargs):
            for param in kwargs:
                if param == "Cust_id":
                    self.Cid = kwargs[param]
                if param == "Cust_Name":
                    self.Cname = kwargs[param]
                if param == "Cust_phno":
                    self.Cphno = kwargs[param]

def Cust_Search(Cust_val):
    Cust_filter = False
    filter_cond = ''
    if Cust_val.Cid != '':
        filter_cond = f" Cust_id like '%{Cust_val.Cid}%'"
        Cust_filter = True
    if Cust_val.Cname != '':
        if Cust_filter:
            filter_cond += f" OR "
        filter_cond += f" Cust_Name like '%{Cust_val.Cname}%'"
        Cust_filter = True
    if Cust_val.Cphno != '':
        if Cust_filter:
            filter_cond += f" OR "
        filter_cond += f" Cust_phno like '%{Cust_val.Cphno}%'"
        print(filter_cond)
        Cust_filter = True
    Cust_srch = srch.GetCustomer(filter_cond)
    print(*Cust_srch, sep="\n")
    #return Cust_srch
srch1 = Srch_Cust_Param(Cust_id = '0001', Cust_Name = 'z', Cust_phno=1)
Cust_Search(srch1)