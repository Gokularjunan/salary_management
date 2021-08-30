# Copyright (c) 2021, gokul and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class salary_structure(Document):
	def validate(self):
		
		a=self.basic_pay=100
		b=self.insurance=50
		c=self.pf=50
		self.total_salary=a+b+c
		self.monthly_payable=(a+b+c)*30
		
	def on_submit(self):
		if frappe.db.exists("salary_slip",				{'employee_name':self.employee_name}):
			frappe.throw(" employee already exit")

		else:
			d=frappe.new_doc("salary_slip")
			d.employee_name=self.employee_name
			d.total_salary=self.monthly_payable
			d.save()

