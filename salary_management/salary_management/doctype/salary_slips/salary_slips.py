# Copyright (c) 2021, gokul and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class salary_slips(Document):
	def validate(self):
		print(self.total_salary,self.per_day_salary,self.number_of_leave_days)
		if(self.number_of_leave_days!=0):
			self.net_pay=(self.total_salary)-(self.per_day_salary * self.number_of_leave_days)	
		else:
			self.net_pay=self.total_salary	
