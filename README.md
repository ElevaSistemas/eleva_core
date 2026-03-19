# Eleva Core

Aplicativo inicial do Frappe para o ERP da Eleva.

## Escopo desta primeira versão
- Módulo 1: Cadastros e Controles
- Lead Eleva
- Cliente Eleva
- Métodos de contato do lead
- Contatos do cliente
- Endereços do cliente
- Subcadastros PJ
- Regras iniciais de geração de SYS_ID, LEAD_CODE e CLIENT_CODE
- Conversão básica Lead -> Cliente

## Instalação no Frappe Cloud
1. Suba esta pasta para um repositório GitHub privado ou público.
2. No Frappe Cloud, no Bench privado, clique em `+ Add App`.
3. Escolha `Add from GitHub`.
4. Informe:
   - Repository: URL do repositório
   - Branch: `main`
5. Adicione o app ao bench.
6. Depois, no Site, em `Apps`, instale `eleva_core`.
7. Execute `bench migrate` se o ambiente solicitar.

## Instalação via CLI
Dentro do bench:

```bash
bench get-app https://github.com/SEU_USUARIO/eleva_core.git --branch main
bench --site SEU_SITE install-app eleva_core
bench --site SEU_SITE migrate
```

## Observações
- Este pacote foi preparado para Frappe v16.
- Os nomes visuais estão em português, mas o app segue a convenção técnica do Frappe em inglês para nomes de pacotes.
