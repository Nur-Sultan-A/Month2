import frappe

doc = frappe.get_doc({
    "doctype": "Stock Entry",
    "stock_entry_type": "Material Receipt",
    "items": [
        {
            "item_code": "TEST-ITEM",
            "qty": 10,
            "uom": "Nos",
            "t_warehouse": "Main Warehouse - ERP"
        }
    ]
})
doc.insert()
doc.submit()