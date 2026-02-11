import json
import sys
from pathlib import Path
from datetime import datetime
#-------------------------------------------------------------------
# Configuração
DATA_FILE = Path(__file__).parent.parent / "data" / "timeline_events.json"


# Utilitários
def error(msg):
    print(f"[ERRO] {msg}")
    sys.exit(1)

def info(msg):
    print(f"[OK] {msg}")

def load_events():
    if not DATA_FILE.exists():
        error(f"Arquivo não encontrado: {DATA_FILE}")

    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_events(data):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

def validate_date(date_str):
    try:
        datetime.fromisoformat(date_str)
    except ValueError:
        error("Data inválida. Use o formato YYYY-MM-DD")

# =========================
# Entrada do usuário
# =========================

def prompt(msg, required=True):
    value = input(msg).strip()
    if required and not value:
        error(f"Campo obrigatório não informado: {msg}")
    return value

# =========================
# Main
# =========================

def main():
    print("=== Adicionar novo evento ===")

    events_data = load_events()
    events = events_data.get("events", {})

    event_id = prompt("ID do evento (ex: event_1969_apollo_11): ")
    if event_id in events:
        error("Já existe um evento com esse ID")

    title = prompt("Título: ")
    date = prompt("Data (YYYY-MM-DD): ")
    validate_date(date)

    importance = prompt("Importância (1–10): ")
    if not importance.isdigit() or not (1 <= int(importance) <= 10):
        error("Importância deve ser um número entre 1 e 10")

    categories = prompt("Categorias (separadas por vírgula): ", required=False)
    tags = prompt("Tags (separadas por vírgula): ", required=False)
    content_ref = prompt("ContentRef (ex: events/apollo_11.md): ", required=False)

    events[event_id] = {
        "id": event_id,
        "title": title,
        "date": date,
        "importance": int(importance),
        "categories": [c.strip() for c in categories.split(",") if c.strip()],
        "tags": [t.strip() for t in tags.split(",") if t.strip()],
    }

    if content_ref:
        events[event_id]["contentRef"] = content_ref

    events_data["events"] = events
    save_events(events_data)

    info(f"Evento '{event_id}' adicionado com sucesso.")

    
#-------------------------------------------------------------------
if __name__ == "__main__":
    main()