from __future__ import unicode_literals
from frappe import _

import frappe


def execute(filters=None):
    return get_columns(), get_data(filters)


def get_columns():
    columns = [
        {
            "fieldname":"Work Order",
            "label":("Work Order"),
            "fieldtype": "Link",
            "options":"Work Order",
            "width": 200,
            "reqd":0,
        },
        {
            "fieldname": "Date",
            "label": ("Date"),
            "fieldtype": "Date",
            "width": 100,
            "reqd": 1,
        },
        {
            "fieldname":"Item Code",
            "label":("Item Code"),
            "fieldtype": "Link",
            "options":"Item",
            "width": 100,
            "reqd":0,
        },
        {
            "fieldname":"Project",
            "label":("project"),
            "fieldtype": "Data",
            "width": 100,
            "reqd": 0,
        },
        {
            "fieldname":"Operation",
            "label":("Operation"),
            "fieldtype": "Data",
            "width": 100,
            "reqd": 0,
        },
        {
            "fieldname":"Warehouse",
            "label":("Warehouse"),
            "fieldtype": "Data",
            "width": 100,
            "reqd": 0,
        },
        {
            "fieldname":"Workstation",
            "label":("Workstation"),
            "fieldtype": "Data",
            "width": 100,
            "reqd": 0,
        },
        {
            "fieldname":"Qty To Manufacture",
            "label":("Qty To Manufacture"),
            "fieldtype": "Flot",
            "width": 100,
            "reqd": 0,
        },
        {
            "fieldname":"Material Transferred for Manufacturing",
            "label":("Material Transferred For Manufacturing"),
            "fieldtype": "Data",
            "width": 100,
            "reqd": 0,
        },
        {
            "fieldname":"JB Qty To Manufacture",
            "label":("JB Qty To Manufacture"),
            "fieldtype": "Flot",
            "width": 100,
            "reqd": 0,
        },
        {
            "fieldname":"Valuation Rate",
            "label":("Valuation Rates"),
            "fieldtype": "Data",
            "width": 100,
            "reqd": 0,
        }
        
	]
    return columns



def get_data(filters):
    conditions="1=1"
    print("Conditions:", conditions)  # Print conditions for debugging

	
    query = """
    SELECT 
    name as 'Work Order',
    custom_date as 'Date',
    production_item as 'Item Code',
    custom_project_ AS 'Project',
    operation AS 'Operation',
    wip_warehouse AS 'Warehouse',
    workstation_name AS 'Workstation',
    qty AS 'Qty To Manufacture',
    material_transferred_for_manufacturing AS 'Material Transferred for Manufacturing',
    for_quantity AS 'JB Qty To Manufacture',
    ROUND(total_rate + total_outgoing_value, 2) AS 'Valuation Rate'
FROM
(
    SELECT 
        wo.name,
        wo.custom_date,
        wo.production_item,
        wo.custom_project_,
        jb.operation,
        wo.wip_warehouse,
        ws.workstation_name,
        wo.qty,
        jb.for_quantity,
        wo.material_transferred_for_manufacturing,
        tl.time_in_mins,
        ws.hour_rate,
        se.total_outgoing_value,
        SUM(tl.time_in_mins*ws.hour_rate/60) OVER (PARTITION BY wo.name) AS 'total_rate',
        ROW_NUMBER() OVER (PARTITION BY wo.name ORDER BY tl.to_time DESC) AS row_num
    FROM 
        `tabWork Order` wo
    INNER JOIN 
        `tabStock Entry` se ON wo.name = se.work_order
    INNER JOIN 
        `tabJob Card` jb ON wo.name = jb.work_order
    INNER JOIN 
        `tabJob Card Time Log` tl ON jb.name = tl.parent
    INNER JOIN 
        `tabWorkstation` ws ON jb.workstation = ws.name
    WHERE  
        se.stock_entry_type = 'Material Transfer for Manufacture'
    AND
        jb.docstatus = 1
    AND
        wo.status != 'Completed'
    
) AS temp_table
WHERE 
	temp_table.row_num = 1  AND {0}
GROUP BY 
	temp_table.name
    """.format(conditions)

    data = frappe.db.sql(query, as_dict=True)
    return data

    

