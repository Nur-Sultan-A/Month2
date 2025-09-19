import frappe

items = frappe.get_all("Item", fields=["name", "item_name", "stock_uom"])
for i in items:
    print(i)