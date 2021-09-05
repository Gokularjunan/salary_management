# Copyright (c) 2021, gokul and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class leave_application(Document):
	def validate(self):
		if frappe.db.exists("salary_slips",{"employee_name":self.employee_name}):
			old_sal=frappe.db.get_value("salary_slips",{"employee_name":self.employee_name},"number_of_leave_days")
			name=frappe.db.get_value("salary_slips",{"employee_name":self.employee_name},"name")
			doc = frappe.get_doc("salary_slips", name)
			doc.number_of_leave_days = old_sal+self.number_of_days
			doc.save()
			
		else:
			frappe.db.set_value("salary_slips",{"employee_name":self.employee_name},"number_of_leave_days",self.number_of_days)
	







	#def validate(self):
	#leaves = frappe.db.sql(""" select count(*) from `tabLeaveApplication` where employee_name=employee_name and date between %s and %s""", from_date, to_date)
#a=leaves
#print(a)
#self.number_of_days=a
