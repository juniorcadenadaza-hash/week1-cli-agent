import csv


INPUT_FILE = "tools.csv"
OUTPUT_FILE = "ai_output.csv"
SIMULATE_API_FAILURE = False


def build_prompt(row):
    prompt = f"Summarize this in one sentence: {row}"
    return prompt


def choose_article(word):
    first_letter = word[0].lower()

    if first_letter in ["a", "e", "i", "o", "u"]:
        return "an"

    return "a"


def send_to_ai(prompt, row):
    name = row["name"]
    category = row["category"]
    purpose = row["purpose"]
    article = choose_article(category)

    if SIMULATE_API_FAILURE and name == "Claude":
        raise Exception("Simulated API failure for testing.")

    response = f"{name} is {article} {category} tool. {purpose}."
    return response


def process_csv():
    with open(INPUT_FILE, "r", encoding="utf-8", newline="") as input_file:
        reader = csv.DictReader(input_file)

        with open(OUTPUT_FILE, "w", encoding="utf-8", newline="") as output_file:
            fieldnames = ["name", "category", "purpose", "summary"]

            writer = csv.DictWriter(output_file, fieldnames=fieldnames)

            writer.writeheader()

            for row in reader:
                prompt = build_prompt(row)
                try:
                    ai_response = send_to_ai(prompt, row)
                except Exception as e:
                    print(f"Error occurred while processing row: {e}")
                    ai_response = "Error occurred while generating summary."

                writer.writerow({
                    "name": row["name"],
                    "category": row["category"],
                    "purpose": row["purpose"],
                    "summary": ai_response
                })

    print(f"Done. Results saved to {OUTPUT_FILE}")


process_csv()