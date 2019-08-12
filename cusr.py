import sqlite3
class Customer:
    def __init__(self, **kwargs):
        if len(kwargs):
            for param in kwargs:
                if param == 'Cust_id':
                    self.Cust_id = kwargs[param]
                if param == 'Cust_Name':
                    self.Cust_Name = kwargs[param]
                if param == 'Cust_phno':
                    self.Cust_phno = kwargs[param]
                if param == 'Cr_date':
                    self.Cr_date = kwargs[param]
                if param == 'Md_date':
                    self.Md_date = kwargs[param]
                if param == 'Cr_user':
                    self.Cr_user = kwargs[param]
                if param == 'Md_user':
                    self.Md_user = kwargs[param]

class Address:
    def __init__(self, **kwargs):
        if len(kwargs):
            for param in kwargs:
                if param == 'Cust_id':
                    self.Cust_id = kwargs[param]
                if param == 'Add_id':
                    self.Add_id = kwargs[param]
                if param == 'Add_type':
                    self.Add_type = kwargs[param]
                if param == 'Add1':
                    self.Add1 = kwargs[param]
                if param == 'Add2':
                    self.Add2 = kwargs[param]
                if param == 'Add3':
                    self.Add3 = kwargs[param]
                if param == 'State':
                    self.State = kwargs[param]
                if param == 'Country':
                    self.Country = kwargs[param]
                if param == 'Pincode':
                    self.Pincode = kwargs[param]
                if param == 'Isdefault':
                    self.Isdefault = kwargs[param]
                if param == 'Cr_date':
                    self.Cr_date = kwargs[param]
                if param == 'Cr_user':
                    self.Cr_user = kwargs[param]
                if param == 'Md_date':
                    self.Md_date = kwargs[param]
                if param == 'Md_user':
                    self.Md_user = kwargs[param]

class Payment:
    def __init__(self, **kwargs):
        if len(kwargs):
            for param in kwargs:
                if param == 'Cust_id':
                    self.Cust_id = kwargs[param]
                if param == 'Payment_id':
                    self.Payment_id = kwargs[param]
                if param == 'Payment_type':
                    self.Payment_type = kwargs[param]
                if param == 'Card_No':
                    self.Card_No = kwargs[param]
                if param == 'Card_Expiry_date':
                    self.Card_Expiry_date = kwargs[param]
                if param == 'Cr_date':
                    self.Cr_date = kwargs[param]
                if param == 'Md_date':
                    self.Md_date = kwargs[param]
                if param == 'Cr_user':
                    self.Cr_user = kwargs[param]
                if param == 'Md_user':
                    self.Md_user = kwargs[param]
class Cust_Controller:
    def __init__(self):
        self._db = sqlite3.connect ('custo.db')
        self._cur = self._db.cursor()
       # self._table = 'Cust_Master'

    def GetCustomer(self,filter_cond='',Cust_id=''):
      #abc = []
      cust_list = []
      cust = dict()
      sql = 'SELECT * FROM Cust_Master'
      sql += f" WHERE {filter_cond}"
     # if len(Cust_id):
     #     sql += (f" WHERE Cust_id = '{Cust_id}'")
      print (sql)
      self._cur.execute(sql)
      rows = self._cur.fetchall()
      for row in rows:
        cust = dict ({"Cust_id": row[0], "Cust_Name": row[1], "Cust_phno": row[2], "Cr_date": row[3], "Md_date": row[4], "Cr_user": row[5], "Md_user" : row[6]})
        cust_list.append(cust)
      #print (cust_list)
      return cust_list
    def GetAddress(self, Cust_id='', Add_id=''):
      abc = []
      addt = dict()
      sql = 'SELECT * FROM Address'
      if len(Cust_id):
        sql += (f" WHERE Cust_id = '{Cust_id}' and Add_id ='{Add_id}'")
      #print(sql)
      self._cur.execute(sql)
      rows = self._cur.fetchall()
      for row in rows:
          addt = dict(
              {"Cust_id": row[0], "Add_id": row[1], "Add_type": row[2],
               "Add1": row[3], "Add2": row[4], "Add3": row[5], "State": row[6], "Country": row[7],
            "pincode": row[8], "Isdefault": row[9],"Cr_date": row[10], "Md_date": row[11], "Cr_user": row[12], "Md_user" : row[13] })
          abc.append(addt)
      #print(abc)
      return abc

    def GetPayment(self, Cust_id='', Payment_id=''):
      abcd=[]
      payt = dict()
      sql = 'SELECT * FROM Payment'
      if len(Cust_id):
          sql += (f" WHERE Cust_id = '{Cust_id}'")
      #print(sql)
      self._cur.execute(sql)
      rows = self._cur.fetchall()
      for row in rows:
          payt = dict(
              {"Cust_id": row[0], "Payment_id": row[1], "Payment_type": row[2],"Card_No": row[3], "Card_Expiry_date": row[4],  "Cr_date": row[5], "Md_date": row[6], "Cr_user": row[7],
               "Md_user": row[8]})
          abcd.append(payt)
      return abcd
      #print(abcd)

    def SaveCustomer(self, custobj):
        existingcust = self.GetCustomer(custobj.Cust_id)
        print(existingcust)
        if not existingcust:
           print (" Record to be insert")
           self.__InsertCustomer(custobj)
        else:
            self.__UpdateCustomer(custobj)
            print("record is updated")

    def __InsertCustomer(self, customer):
        self.cust = customer
        sql = (
            f"INSERT INTO Cust_Master (Cust_id, Cust_Name, Cust_phno, Cr_date, Md_date, Cr_user, Md_user) "
            f"VALUES ('{self.cust.Cust_id}', '{self.cust.Cust_Name}', '{self.cust.Cust_phno}', '{self.cust.Cr_date}', '{self.cust.Md_date}', '{self.cust.Cr_user}','{self.cust.Md_user}')")
        print(sql)
        self._cur.execute(sql)
        self._db.commit()

    def __UpdateCustomer(self, customer):
        self.cust = customer
        sql = (
            f"Update Cust_Master SET Cust_id = '{self.cust.Cust_id}',Cust_Name = '{self.cust.Cust_Name}',"
            f"Cust_phno = '{self.cust.Cust_phno}',Cr_date = '{self.cust.Cr_date}', Md_date ='{self.cust.Md_date}', Cr_user = '{self.cust.Cr_user}',Md_user = '{self.cust.Md_user}' where Cust_id = '{self.cust.Cust_id}'")
        print(sql)
        self._cur.execute(sql)
        self._db.commit()

    def SaveAddress(self, addobj):
        existingadd = self.GetAddress(addobj.Cust_id, addobj.Add_id)
        print(existingadd)
        if not existingadd:
           print (" Record to be insert")
           self.__InsertAddress(addobj)
           print("Record is inserted")
        else:
            self.__UpdateAddress(addobj)
            print("record is updated")
    def __InsertAddress(self, address):
        self.addt = address
        sql = (
            f"INSERT INTO Address(Cust_id,Add_id,Add_type,Add1,Add2,Add3,State,Country,Pincode,Isdefault,Cr_date,Md_date,Cr_user,Md_user ) "
            f"VALUES ('{self.addt.Cust_id}','{self.addt.Add_id}','{self.addt.Add_type}','{self.addt.Add1}','{self.addt.Add2}','{self.addt.Add3}','{self.addt.State}','{self.addt.Country}','{self.addt.Pincode}','{self.addt.Isdefault}', '{self.addt.Cr_date}', '{self.addt.Md_date}', '{self.addt.Cr_user}','{self.addt.Md_user}')")
        print(sql)
        self._cur.execute(sql)
        self._db.commit()

    def __UpdateAddress(self, address):
        self.addt = address
        sql = (
            f"Update Address SET Cust_id = '{self.addt.Cust_id}',Add_id = '{self.addt.Add_id}',Add_type ='{self.addt.Add_type}',Add1 = '{self.addt.Add1}',Add2 = '{self.addt.Add2}',Add3='{self.addt.Add3}',State ='{self.addt.State}',Country ='{self.addt.Country}',Pincode='{self.addt.Pincode}',Isdefault='{self.addt.Isdefault}',"
            f"Cr_date = '{self.addt.Cr_date}', Md_date ='{self.addt.Md_date}', Cr_user = '{self.addt.Cr_user}',Md_user = '{self.addt.Md_user}' where Cust_id = '{self.addt.Cust_id}' and Add_id ='{self.addt.Add_id}'")
        print(sql)
        self._cur.execute(sql)
        self._db.commit()
    def SavePayment(self, payobj):
        existingpay = self.GetPayment(payobj.Cust_id, payobj.Payment_id)
        print(existingpay)
        if not existingpay:
           print (" Record to be insert")
           self.__InsertPayment(payobj)
           print("Record is inserted")
        else:
            self.__UpdatePayment(payobj)
            print("record is updated")
    def __InsertPayment(self, payment):
        self.payt = payment
        sql = (
            f"INSERT INTO Payment(Cust_id,Payment_id,Payment_type,Card_No,Card_Expiry_date,Cr_date,Md_date,Cr_user,Md_user ) "
            f"VALUES ('{self.payt.Cust_id}','{self.payt.Payment_id}','{self.payt.Payment_type}','{self.payt.Card_No}','{self.payt.Card_Expiry_date}', '{self.payt.Cr_date}', '{self.payt.Md_date}', '{self.payt.Cr_user}','{self.payt.Md_user}')")
        print(sql)
        self._cur.execute(sql)
        self._db.commit()

    def __UpdatePayment(self, payment):
        self.payt = payment
        sql = (
            f"Update Payment SET Cust_id = '{self.payt.Cust_id}',Payment_id = '{self.payt.Payment_id}',Payment_type ='{self.payt.Payment_type}',Card_No = '{self.payt.Card_No}',Card_Expiry_date = '{self.payt.Card_Expiry_date}',"
            f"Cr_date = '{self.payt.Cr_date}', Md_date ='{self.payt.Md_date}', Cr_user = '{self.payt.Cr_user}',Md_user = '{self.payt.Md_user}' where Cust_id = '{self.payt.Cust_id}' and Payment_id ='{self.payt.Payment_id}'")
        print(sql)
        self._cur.execute(sql)
        self._db.commit()
cc = Cust_Controller()
#cc.GetCustomer('0001')
#cc.GetAddress('0002',1)
#addt = Address(Cust_id='0002', Add_id=2, Add_type='HOM1',Add1='BA',Add2='C',Add3='U',State='TN',Country='IN',Pincode='600100',Isdefault='N',Cr_date='209',Md_date='',Cr_user='',Md_user='')
#cc.SaveAddress(addt)
#cust = Customer(Cust_id = '0007', Cust_Name = 'subuRaman', Cust_phno = 9789345337, Cr_date = '2019-07-06', Md_date = '', Cr_user = 'Rama', Md_user = '')
#cc.SaveCustomer(cust)
#cc.GetPayment('0001',1)
#payt = Payment(Cust_id='0002', Payment_id=2, Payment_type='Credit',Card_No='8432-09493-001',Card_Expiry_date='2020-09-01',Cr_date='2019-08-03',Md_date='',Cr_user='',Md_user='Balaji')
#cc.SavePayment(payt)


