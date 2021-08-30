# Copyright (c) 2021, gokul and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.utils import date_diff

class salary_slip(Document):
	def validate(self):
    		fromdate=self.from_date
    		todate=self.to_date
    		tot=date_diff(fromdate, todate)
    		self.total_days=abs(int(tot))
    		self.net_pay=abs(int(tot))*200
		
		
