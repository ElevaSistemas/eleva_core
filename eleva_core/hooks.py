app_name = "eleva_core"
app_title = "Eleva Core"
app_publisher = "Eduardo Vessio / OpenAI"
app_description = "Modulo 1 - Cadastros e Controles da Eleva"
app_email = "eduardovessio@hotmail.com"
app_license = "MIT"

app_include_css = "/assets/eleva_core/css/eleva_core.css"
app_include_js = "/assets/eleva_core/js/eleva_core.js"

fixtures = []

after_install = "eleva_core.install.after_install"

doc_events = {
    "Lead Eleva": {
        "before_insert": "eleva_core.api.lead.before_insert_lead"
    },
    "Cliente Eleva": {
        "before_insert": "eleva_core.api.cliente.before_insert_cliente"
    }
}
