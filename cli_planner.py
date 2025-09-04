import os
from dotenv import load_dotenv
import google.generativeai as genai
from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt
from rich.progress import Progress
from rich.panel import Panel
from rich.markdown import Markdown

# Setup console
console = Console()

# Load API Key
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# --- Helper functions ---
def get_response_text(prompt, user_input):
    model = genai.GenerativeModel("gemini-1.5-flash")
    with Progress() as progress:
        task = progress.add_task("[cyan]🤔 Thinking...", total=None)
        # Combine the main prompt with the user's specific input
        full_prompt = f"{prompt}\n\nUSER REQUEST: {user_input}"
        resp = model.generate_content(full_prompt)
        progress.stop()
    return getattr(resp, "text", "").strip()

def get_response_image(image_parts, prompt):
    model = genai.GenerativeModel("gemini-1.5-flash")
    with Progress() as progress:
        task = progress.add_task("[cyan]🖼️ Analyzing image...", total=None)
        resp = model.generate_content([prompt, image_parts[0]])
        progress.stop()
    return getattr(resp, "text", "").strip()

def prep_image(path):
    if not os.path.exists(path):
        console.print("[red]❌ Image not found![/red]")
        return None
    with open(path, "rb") as f:
        # The model expects a list of parts
        return [{"mime_type": "image/jpeg", "data": f.read()}]

# --- Detailed & Structured Prompts ---

PROMPT_LOCATION = """
You are an expert travel guide identifying a location from an image. Provide a detailed summary in Markdown format.

**📍 Place Name:**
**🏙️ Location:** City, State, Country
**🌍 Coordinates:** Latitude, Longitude
**⭐ Known For:** A brief, one-sentence description.
**🏛️ Nearby Attractions (within 5 km):**
* **[Attraction 1]:** Brief description.
* **[Attraction 2]:** Brief description.
* **[Attraction 3]:** Brief description.

Respond only with the structured information as requested. Do not add any introductory text.
"""

PROMPT_TRIP = """
You are a master Tour Planner. Create a concise, practical itinerary based on the user's request for a location and number of days.

Provide the output in the following Markdown format.

**✈️ Destination:** [Location]
**⏳ Trip Duration:** [Number of Days]

**🗓️ Best Time to Visit:** [Month/Season] - [Brief reason why]
**🗺️ Suggested Itinerary:**
* **Day 1:** [Morning Activity], [Afternoon Activity]
* **Day 2:** [Morning Activity], [Afternoon Activity]
* ... (continue for the number of days specified)
**💎 Hidden Gem:** [Name of a less-known spot] - [Why it's worth visiting]
**🏨 Accommodation Suggestion (Mid-Range):** [Hotel Name] - [Briefly why it's a good choice]

Stick strictly to this format and do not add extra conversation.
"""

PROMPT_WEATHER = """
You are a Weather Forecaster. Provide a 7-day weather forecast for the specified location.
Use today's date as the starting point. Provide only the Markdown table in your response.

The table should have these columns: Day, Date, Condition, Temp (°C), Rain (%), Wind (km/h).

| Day       | Date      | Condition        | Temp (°C) | Rain (%) | Wind (km/h) |
|-----------|-----------|------------------|-----------|----------|-------------|
| Wednesday | Sep 3     | ☀️ Sunny         | 28-32     | 10       | 15          |
| Thursday  | Sep 4     | ☁️ Partly Cloudy | 27-31     | 20       | 12          |
| ...       | ...       | ...              | ...       | ...      | ...         |
"""

PROMPT_DINING = """
You are a local food and hotel expert. For the specified location, provide 3 recommendations for dining and 3 for hotels, categorized by budget.

Use the following Markdown format. Infer the local currency for prices.

### 🍴 Dining Recommendations

* **Budget:**
    * **Name:** [Restaurant Name]
    * **Cuisine:** [Type of Cuisine]
    * **Avg. Cost for Two:** [Estimated Price]
* **Mid-Range:**
    * **Name:** [Restaurant Name]
    * **Cuisine:** [Type of Cuisine]
    * **Avg. Cost for Two:** [Estimated Price]
* **Fine Dining:**
    * **Name:** [Restaurant Name]
    * **Cuisine:** [Type of Cuisine]
    * **Avg. Cost for Two:** [Estimated Price]

### 🏨 Accommodation Recommendations

* **Budget:**
    * **Name:** [Hotel Name]
    * **Avg. Price/Night:** [Estimated Price]
    * **Why Stay Here:** [Brief reason]
* **Mid-Range:**
    * **Name:** [Hotel Name]
    * **Avg. Price/Night:** [Estimated Price]
    * **Why Stay Here:** [Brief reason]
* **Luxury:**
    * **Name:** [Hotel Name]
    * **Avg. Price/Night:** [Estimated Price]
    * **Why Stay Here:** [Brief reason]

Provide only the information in this structured format.
"""

# --- Menu ---
def main():
    console.print("[bold magenta]🌍 Travel & Dining Planner CLI[/bold magenta]\n")

    while True:
        table = Table(title="Choose an Option", show_lines=True)
        table.add_column("Option", justify="center", style="cyan", no_wrap=True)
        table.add_column("Description", style="green")

        table.add_row("1", "📸 Location Guide (Image Input)")
        table.add_row("2", "✈️ Trip Planner (Text Input)")
        table.add_row("3", "☀️ Weather Forecast (Text Input)")
        table.add_row("4", "🍴 Dining & Accommodation (Text Input)")
        table.add_row("0", "🚪 Exit")

        console.print(table)

        choice = Prompt.ask("👉 Enter choice", choices=["0", "1", "2", "3", "4"], default="0")

        if choice == "0":
            console.print("[bold yellow]👋 Goodbye! Safe travels![/bold yellow]")
            break

        elif choice == "1":
            path = Prompt.ask("📸 Enter image path")
            image_data = prep_image(path)
            if image_data:
                out = get_response_image(image_data, PROMPT_LOCATION)
                console.print(Panel(Markdown(out), title="🏛️ Tour Bot", border_style="blue", expand=False))

        elif choice == "2":
            location = Prompt.ask("✈️ Enter location & days (e.g., 'Paris 5 days')")
            out = get_response_text(PROMPT_TRIP, location)
            console.print(Panel(Markdown(out), title="🗺️ Planner Bot", border_style="cyan", expand=False))

        elif choice == "3":
            location = Prompt.ask("☀️ Enter location for weather")
            out = get_response_text(PROMPT_WEATHER, location)
            console.print(Panel(Markdown(out), title="🌤️ Weather Bot", border_style="yellow", expand=False))

        elif choice == "4":
            location = Prompt.ask("🍴 Enter location for dining & stay")
            out = get_response_text(PROMPT_DINING, location)
            console.print(Panel(Markdown(out), title="🏨 Accommodation Bot", border_style="green", expand=False))

if __name__ == "__main__":
    main()