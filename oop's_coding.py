# # 1 . domain
# # --Banking--
# # --Entity-- account_details
# #
# # ---account details--
# #
# #    1. STATE:
# #     ---------
# # variable: Attributes: account_number, holder_name,  account_type,  address,  ph_number, mail_id
#
# class Account_details:
#     Bank_name = "SBI"  # class variable
#
#     def __init__(self, holder_name, account_type, address, ph_number, mail_id):
#         self._prot = "protected_instance_variable"
#         self.__private = "private instance variable"
#         self.holder_name = holder_name
#         self.account_type = account_type
#         self.address = address
#         self.phone_number = ph_number
#         self.mail_id = mail_id
#
#     def account_opening(self, acc_number):
#         return (
#             f"share \n customer_name: {self.holder_name} \n account_type: {self.account_type} \n account_number: {acc_number}"
#             f" \n contact_number: {self.phone_number} \n address: {self.address}")
#
#     def update_contact_number(self, ph_number):
#         return (
#             f"share \n customer_name: {self.holder_name} \n account_type: {self.account_type} \n New_contact_number: {ph_number} \n "
#             f"address: {self.address}")
#
#     @classmethod
#     def class_meth(cls):
#         return f"from class method {cls.Bank_name}"
#
#     @staticmethod
#     def utility(x,y):    # this is not a behaviour#no self no cls method
#         res = x+y
#         return res
#
#     @property
#     def c_id(self):
#         return " property c_id"
#
#
#
#
# ram_obj = Account_details("ram", "savings", "bengaluru", 9874562589, "abc@gmail.com")
# sham_obj = Account_details("sham", "current", "bengaluru", 9987456589, "bbc@gmail.com")

# print(ram_obj.holder_name)
# print(ram_obj.account_type)
# print(ram_obj.address)
# print(ram_obj.phone_number)
# print(ram_obj.mail_id)
# print(ram_obj.account_opening(15525))
# print(ram_obj.update_contact_number(9999999999))
# print(Account_details.Bank_name)
# print(ram_obj.utility(54,63))
# print(ram_obj._Account_details__private)
# print(ram_obj.c_id)
# print(ram_obj.utility(10,58))
# print(ram_obj.class_meth())


# # 2. domain
# # --E-commerce--
# # --Entity--order_details
#
# # 1. STATE:
# #     ---------
# # # variable: Attributes: customer_id, order_id,  quantity,  product_name,  delivery_address, price
# #
# class order_details:
#     e_commerce_provider = "Flipkart"
#
#     def __init__(self, customer_id, order_id, price):
#         self._prot = "protected_instance_variable"
#         self.__private = "private instance variable"
#         self.customer_id = customer_id
#         self.order_id = order_id
#         self.price = price
#
#     def prod_spec(self, product_name, colour, quantity, address):
#         return f"name of a product: {product_name}  colour is : {colour} quantity is: {quantity} address is: {address} "
#
#     def tracking(self, status, type_of_delivery, delivery_status):
#         return (f"customer_id: {self.customer_id}\norder_id: {self.order_id}\nin{status} \ndelivery type is {type_of_delivery}\n"
#                 f"product is {delivery_status} {})
#
#     @classmethod
#     def class_meth(cls):
#         return f"from class method {cls.e_commerce_provider}"
#
#     @staticmethod
#     def utility(x, y):  # this is not a behaviour#no self no cls method
#         res = x + y
#         return res
#
#     @property
#     def order(self):
#         return " property order_id"
#
#
# sham_obj = order_details(100, 1, 10000)
#
# print(order_details.e_commerce_provider)
# print(sham_obj.order_id)
# print(sham_obj.customer_id)
# print(sham_obj.prod_spec("moto","red",2,"bengaluru"))
# print(sham_obj.tracking("transit","cash on delivery","yet to deliver"))
# print(sham_obj.class_meth())
# print(sham_obj.utility(85,25))
# print(sham_obj.order)
# print(sham_obj._prot)


#
# # 3. domain
# # --Banking--
# # --Entity--KYC

# class Kyc:
#     bank_name="SBI"
#     def __init__(self,c_name,c_acc_type,addhar_no,phone_number,pan_no):
#
#         self.phone_number = phone_number
#         self.addhar_no = addhar_no
#         self.c_name=c_name
#         self._prot = "protected instance variable"
#         self.__private = "private instance variable"
#         self.c_acc_type = c_acc_type
#         self.pan_no = pan_no
#     def update_kyc(self,addhar_no):
#         return (f"{addhar_no} is updated to {self.c_name},{self._prot},{self.__private},"
#                 f"{self.__private_inst_meth()},{self._prot_inst_meth()}")
#
#     def show_customer(self):
#         return (f"name is {self.c_name},account type is {self.c_acc_type},addhar is {self.addhar_no}"
#                 f",phone number {self.phone_number},"
#                 f"pan number {self.pan_no}")
#     def _prot_inst_meth(self):
#         return "from _prot_inst_meth "
#
#     def __private_inst_meth(self):
#         return "from __private_inst_meth"
#
#     @classmethod
#     def class_meth(cls):
#         return f"from class method {cls.bank_name}"
#
#     @staticmethod
#     def utility(a, b):
#         res = a + b
#         return res
#
#     @property
#     def ifsccode(self):
#         return "SBIN0001234"
#
#
#
# ram_obj=Kyc("ram","savings",12345678987,9049713246,"Dopamf9k")
# raj_obj=Kyc("raj","loan",678987143574,9049778126,"Dovkad3e")
# print(ram_obj.pan_no)
# print(ram_obj.update_kyc(895812347896))
# print(ram_obj.show_customer())
# print(ram_obj.ifsccode)
# print(ram_obj.update_kyc(895812347896))
# print(ram_obj.bank_name)
# print(Kyc.bank_name)
# # print(ram_obj._prot_inst_meth())
# # print(ram_obj._Kyc__private_inst_meth())
# print(ram_obj.ifsccode)


# 4 domain
# --HealthCare--
# --Entity--order_details

# 1. STATE:
#     ---------
# # variable: Attributes: patient_name, age,  hospital_name,  doctor_name,  token_no, diagnosis

# class hospital:
#     hospital_name = 'SNR'
#
#     def __init__(self, patient_name, age, doctor_name, fees, token_no, diagnosis):
#         self.diagnosis = diagnosis
#         self.patient_name = patient_name
#         self.doctor_name = doctor_name
#         self._fees = fees
#         self.age = age
#         self.token = token_no
#
#     def check_for_diagnosis(self):
#         return f"{self.patient_name} aged {self.age} having {self.diagnosis}"
#
#     def consultation(self):
#         return (f"patient having {self.diagnosis} has paid {self._fees}\nconsult {self.doctor_name} "
#                 f"and the token number is {self.token}")
#
#     @classmethod
#     def class_meth(cls):
#         return f"from class method {cls.hospital_name}"
#
#     @property
#     def charges(self):
#         return self._fees
#
#     @charges.setter
#     def charges(self, updated_fee):
#         if updated_fee > 1000 and isinstance(updated_fee, float):
#             self._fees = updated_fee
#         else:
#             print("standard charges for diabetes is greater than 1000")
#
#     @charges.deleter
#     def charges(self):
#         del self._fees
#
# @property
#     def fees(self):
#         return self._fees
#
#     @fees.setter
#     def fees(self, value):
#         self._fees = value
#
#
# patient_obj = hospital('Raj', 25, 'Dr.apollo', 800, 14, 'diabetes')

# print(patient_obj.patient_name)
# print(patient_obj.class_meth())
# print(patient_obj.check_for_diagnosis())
# print(patient_obj.consultation())
# print(patient_obj.charges)
# hospital.fees = 400
# print(patient_obj.fees)


# 5 domain
# --insurance--
# --Entity--bike_insurance

# 1. STATE:
#     ---------
# # variable: Attributes: owner_name, age,gender,  bike_model_name,  mfg_year,  type_of_insurance, bike_condition
# # #
# class Bike_insurance:
#     insurer = 'IFFCO_TOKIO'
#
#     def __init__(self, owner_name, age, gender, bike_model_name, mfg_year, type_of_insurance, non_accidental,
#                  issue_date):
#         self._owner_name = owner_name
#         self.age = age
#         self.gender = gender
#         self.bike_model_name = bike_model_name
#         self.mfg_year = mfg_year
#         self.type_of_insurance = type_of_insurance
#         self.bike_condition = non_accidental
#         self.issue_date = issue_date
#
#     def selling_insurance_for_new_bike(self, comprehension):
#         return (f"insurance has been issued to {self.bike_model_name}\n"
#                 f"manufactured year: {self.mfg_year}\n"
#                 f"owner_name: {self._owner_name}\n"
#                 f"{self.type_of_insurance}: {comprehension}\n"
#                 f"gender: {self.gender}\n"
#                 f"age: {self.age}\n"
#                 f"valid till one year from the: {self.issue_date}")
#
#     def selling_insurance_for_expired_policy(self, comprehension):
#         return (f"bike is in condition: {self.bike_condition}, Eligible to get a insurance\n"
#                 f"owner_name: {self._owner_name}\n"
#                 f"{self.type_of_insurance}:{comprehension}\n"
#                 f"gender: {self.gender}\n"
#                 f"age: {self.age}\n"
#                 f"valid till one year from the: {self.issue_date}")
#
#     @classmethod
#     def class_meth(cls):
#         return f"from class_meth {cls.insurer}"
#
#     @property
#     def owner_name(self):
#         return self._owner_name
#
#     @owner_name.getter      # function name and @name.getter should be an attribute
#     def owner_name(self):
#         return self._owner_name
#
#     @owner_name.setter
#     def owner_name(self, new_owner):
#         if not isinstance(new_owner, str):
#             raise TypeError("must be in str format")
#         self._owner_name = new_owner
#
#
# owner_obj = Bike_insurance('Dinesh', 25, 'male', 'Himalayan_411_BS4',
#                            2019, 'comprehension', 'yes', '30-08-2024')
#
# setattr(owner_obj, 'owner_name', "feri")

# print(owner_obj.owner_name())
# print(owner_obj.age())

# print(owner_obj.class_meth())
# print(owner_obj.selling_insurance_for_new_bike('yes'))
# print(owner_obj.selling_insurance_for_expired_policy('yes'))
# print(owner_obj.bike_condition)
# print(owner_obj.bike_model_name)
# print(owner_obj.gender)
# print(owner_obj._owner_name)

