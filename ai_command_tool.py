import requests

# ---------------------------
# SIMPLE TEXT PROCESSING
# ---------------------------

def summarize(text):
    sentences = text.split(".")
    if len(sentences) > 1:
        return sentences[0].strip() + "."
    else:
        words = text.split()
        return " ".join(words[:12]) + "..."

import requests

def get_quote():
    apis = [
        {
            "url": "https://api.adviceslip.com/advice",
            "type": "advice"
        },
        {
            "url": "https://zenquotes.io/api/random",
            "type": "zen"
        }
    ]

    for api in apis:
        try:
            res = requests.get(api["url"], timeout=10)
            data = res.json()

            # API 1 (AdviceSlip)
            if api["type"] == "advice":
                if "slip" in data:
                    return data["slip"]["advice"]

            # API 2 (ZenQuotes)
            if api["type"] == "zen":
                return data[0]["q"] + " — " + data[0]["a"]

        except Exception:
            continue

    return "All APIs failed — network issue"

# ---------------------------
# MAIN LOOP (COMMAND SYSTEM)
# ---------------------------

data = {
    "text": ""
}

print("AI COMMAND TOOL STARTED")
print("Commands: input / summarize / quote / show / exit")

while True:
    command = input("\nEnter command: ")

    # take input text
    if command == "input":
        data["text"] = input("Enter your text: ")
        print("Text saved!")

    # summarize text
    elif command == "summarize":
        if data["text"] == "":
            print("No text found. Use 'input' first.")
        else:
            result = summarize(data["text"])
            print("Summary:", result)

    # API call
    elif command == "quote":
        print("Quote:", get_quote())

    # show stored data
    elif command == "show":
        print("Stored Data:", data)

    # exit program
    elif command == "exit":
        print("Exiting tool...")
        break

    else:
        print("Invalid command")