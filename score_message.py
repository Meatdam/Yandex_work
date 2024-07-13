from jinja2 import Environment, FileSystemLoader

min_score = 100
test_name = 'Yandex Score'

users = [
    {"event": "mission_complete", "id": 123,  "points": 100, },
    {"event": "mission_failed", "id": 124, "points": 87},
    {"event": "mission_failed", "id": 125, "points": 92},
    {"event": "mission_failed", "id": 126, "points": 40},
    {"event": "mission_failed", "id": 127, "points": 75},
]

environment = Environment(loader=FileSystemLoader("templates/"))

results_filename = "yandex_results.html"
results_template = environment.get_template("2.html")
context = {
    "users": users,
    "test_name": test_name,
    "min_score": min_score,
}
with open(results_filename, mode="w", encoding="utf-8") as results:
    results.write(results_template.render(context))
    print(f"... wrote {results_filename}")
