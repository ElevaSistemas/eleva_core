import frappe


def _next_sequence(prefix: str) -> int:
    series_key = f"{prefix}-.######"
    return int(frappe.model.naming.make_autoname(series_key).replace(f"{prefix}-", ""))


def before_insert_lead(doc, method=None):
    if not doc.sys_id:
        seq = _next_sequence("SYS")
        doc.sys_id = f"SYS{seq:06d}"

    if not doc.lead_code:
        seq = _next_sequence("LD")
        doc.lead_code = f"LD{seq:06d}"

    if not doc.display_label:
        doc.display_label = (doc.nome_comercial or doc.lead_code or "").strip()

    if not doc.status:
        doc.status = "Novo"
