import frappe


def _next_sequence(prefix: str) -> int:
    series_key = f"{prefix}-.######"
    return int(frappe.model.naming.make_autoname(series_key).replace(f"{prefix}-", ""))


def _extract_seq(code: str, prefix: str) -> int | None:
    if not code:
        return None
    code = code.strip()
    if code.startswith(prefix) and code[len(prefix):].isdigit():
        return int(code[len(prefix):])
    return None


def before_insert_cliente(doc, method=None):
    lead_doc = None
    if getattr(doc, "lead_origin", None):
        lead_doc = frappe.get_doc("Lead Eleva", doc.lead_origin)

    if not doc.sys_id:
        if lead_doc and lead_doc.sys_id:
            doc.sys_id = lead_doc.sys_id
        else:
            seq = _next_sequence("SYS")
            doc.sys_id = f"SYS{seq:06d}"

    if not doc.client_code:
        seq = None
        if lead_doc and lead_doc.lead_code:
            seq = _extract_seq(lead_doc.lead_code, "LD")
        if seq is None:
            seq = _next_sequence("CL")
        doc.client_code = f"CL{seq:06d}"

    if doc.tipo_cadastro == "PJ":
        doc.documento_principal = (doc.cnpj_raiz or "").strip()
        base_name = (doc.nome_fantasia or doc.razao_social or doc.nome_principal or doc.client_code or "").strip()
    else:
        doc.documento_principal = (doc.cpf or "").strip()
        base_name = (doc.nome_pf or doc.nome_principal or doc.client_code or "").strip()

    if not doc.display_label:
        doc.display_label = base_name or doc.client_code

    if lead_doc:
        doc.convertido_de_lead = 1

    if not doc.status:
        doc.status = "Ativo"
