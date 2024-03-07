# your_module/your_script.py
from frappe import _
import frappe

@frappe.whitelist()
def get_work_order_names(doctype, txt, searchfield, start, page_len, filters):
    return frappe.get_all("Work Order", filters={"docstatus": 1}, fields=["name"], as_list=True)

# @frappe.whitelist()
# def get_item_codes(doctype, txt, searchfield, start, page_len, filters):
#     result = frappe.get_all("Work Order", filters={"docstatus": 1}, fields=["production_item"], as_list=True)
#     print(result)
#     return result

   

@frappe.whitelist()
def get_item_code():
    try: 
        options = frappe.get_all('Work Order', filters={}, pluck='production_item')


        return options
    except Exception as e:
        frappe.log_error(f"Error in get_operation_options: {e}")
        return []


@frappe.whitelist()
def get_date():
    try:
        # Your database query to fetch options
        options = frappe.get_all('Job Card', filters={}, pluck='custom_date', distinct=True)


        return options
    except Exception as e:
        frappe.log_error(f"Error in get date: {e}")
        return []
    


@frappe.whitelist()
def get_operation_options():
    try:
        # Your database query to fetch options
        options = frappe.get_all('Job Card', filters={}, pluck='operation', distinct=True)


        return options
    except Exception as e:
        frappe.log_error(f"Error in get_operation_options: {e}")
        return []
    

