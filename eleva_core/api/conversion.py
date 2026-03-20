import frappe


@frappe.whitelist()
def convert_lead_to_cliente(lead_name: str, tipo_cadastro: str, nome_principal: str = None):
    lead = frappe.get_doc("Lead Eleva", lead_name)

    cliente = frappe.new_doc("Cliente Eleva")
    cliente.sys_id = lead.sys_id
    cliente.lead_origin = lead.name
    cliente.tipo_cadastro = tipo_cadastro
    cliente.convertido_de_lead = 1
    cliente.nome_principal = nome_principal or lead.nome_comercial or lead.display_label or lead.name

    if tipo_cadastro == "PJ":
        cliente.razao_social = cliente.nome_principal
        cliente.nome_fantasia = cliente.nome_principal
    else:
        cliente.nome_pf = cliente.nome_principal

    for row in lead.contact_methods or []:
        cliente.append("contatos", {
            "contact_type": row.contact_type,
            "contact_value": row.contact_value,
            "contact_name": lead.nome_comercial or lead.display_label,
            "contact_role": "Principal" if row.is_primary else "Outro",
            "is_primary": row.is_primary,
            "is_verified": getattr(row, "is_verified", 0),
            "notes": getattr(row, "notes", None),
        })

    cliente.insert(ignore_permissions=True)

    lead.status = "Convertido"
    lead.etapa_funil = "Convertido"
    lead.cliente_vinculado = cliente.name
    lead.save(ignore_permissions=True)

    return {
        "cliente": cliente.name,
        "client_code": cliente.client_code,
        "sys_id": cliente.sys_id,
    }
