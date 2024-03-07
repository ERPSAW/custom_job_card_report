// Copyright (c) 2024, varsha and contributors
// For license information, please see license.txt

frappe.query_reports["Job card report"] = {
	"filters": [
		{
			"fieldname": "name",
            "label": __("Work Order"),
            "fieldtype": "Link",
            "options": "Work Order",  // Set the doctype for which you want to fetch the names
            "get_query": function() {
                return {
                    query: "custom_job_card_report.report_filter_api.get_work_order_names"  // Replace with your actual module and script
                };
            },
            "width": 100,
            "reqd": 0,
        },
		{
            "fieldname": "production_item",
            "label": __("Item Code"),
            "fieldtype": "Link",
            "options": "Item",
            "width": 100,
            "reqd": 0,  
            
        },
        
        {
            "fieldname": "custom_date",
            "label": ("Date"),
            "fieldtype": "DateRange",
            "width": 100,
            "reqd": 0,
        },
        {
        
			"fieldname": "operation",
            "label": __("Operation"),
            "fieldtype": 'Select',
            "options": ["", ...getOperationOptions()],
            "width": 100,
            "reqd": 0,
        },
       

	]
};

function getItemCode() {
    // Write a server call to fetch options from the database query
    var options = [];
    frappe.call({
        method: 'custom_job_card_report.report_filter_api.get_item_code',
        async: false,
        callback: function (r) {
            if (r.message) {
                options = r.message;
            }
        }
    });
    return options;
}

function getDate() {
    // Write a server call to fetch options from the database query
    var options = [];
    frappe.call({
        method: 'custom_job_card_report.report_filter_api.get_date',
        async: false,
        callback: function (r) {
            if (r.message) {
                options = r.message;
            }
        }
    });
    return options;
}



function getOperationOptions() {
    // Write a server call to fetch options from the database query
    var options = [];
    frappe.call({
        method: 'custom_job_card_report.report_filter_api.get_operation_options',
        async: false,
        callback: function (r) {
            if (r.message) {
                options = r.message;
            }
        }
    });
    return options;
}
