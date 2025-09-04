💎 Gem Tripper
**Your AI-powered travel companion for trips, food, weather, and stays—all from your terminal.**
✨ Features
🏛️ Location Guide (Image Input)
- Upload an image of a landmark, and Gem Tripper will:
  - Identify the place
  - Show location details
  - Suggest nearby attractions
✈️ Trip Planner (Text Input)
- Enter a destination and number of days
- Get a day-by-day itinerary with:
  - Best time to visit
  - Hidden gems
  - Mid-range accommodation suggestions
🌤️ Weather Forecast
- Get a 7-day weather forecast for your travel destination
- See conditions, temperatures, rain probability, and wind speed in a clean table format
🍴 Dining & Accommodation
- Get 3 dining suggestions (budget, mid-range, fine dining)
- Get 3 hotel suggestions (budget, mid-range, luxury)
- Prices are shown in the local currency
🚀 Tech Stack
- Python 3.8+ – Core programming language
- Google Generative AI – AI-powered responses
- Rich – Beautiful CLI UI with tables, panels, markdown
- python-dotenv – Environment variable management
🏗️ Application Architecture

Gem Tripper (CLI)
├── Location Guide (Image Input)
│   └── Place details & attractions
├── Trip Planner (Text Input)
│   └── Itinerary, hidden gems, stays
├── Weather Forecast
│   └── 7-day forecast table
└── Dining & Accommodation
    ├── Restaurants by budget
    └── Hotels by budget

🛠️ Installation & Setup
### Prerequisites
- Python 3.8 or higher
- Google API key for Gemini AI
1. Clone the Repository:
   git clone https://github.com/yourusername/gem-tripper.git
   cd gem-tripper
2. Create Virtual Environment:
   python -m venv venv
   source venv/bin/activate (macOS/Linux)
   venv\Scripts\activate (Windows)
3. Install Dependencies:
   pip install -r requirements.txt
4. Setup Environment:
   Create a .env file in the root directory:
   GOOGLE_API_KEY=your_google_api_key_here
5. Run the Program:
   python main.py
📱 Usage
Once started, you’ll see a menu:

1. 📸 Location Guide (Image Input)
2. ✈️ Trip Planner (Text Input)
3. ☀️ Weather Forecast (Text Input)
4. 🍴 Dining & Accommodation (Text Input)
0. 🚪 Exit
📖 Example
### Trip Planning

Enter location & days (e.g., 'Goa 4 days')

Output:
Destination: Goa
Trip Duration: 4 Days

Best Time to Visit: November - February

Itinerary:
Day 1: Beaches & Shacks
Day 2: Old Goa Churches & Museums
Day 3: Spice Plantation & Local Markets
Day 4: Water Sports & Sunset Cruise

Hidden Gem: Divar Island
Accommodation: Casa Boutique Hotel
📦 Dependencies
google-generativeai
python-dotenv
rich

Install with:
pip install google-generativeai python-dotenv rich
🤝 Contributing
Contributions are always welcome!

- Fork this repo
- Create your branch (git checkout -b feature/your-feature)
- Commit (git commit -m 'Added amazing feature')
- Push (git push origin feature/your-feature)
- Open a Pull Request
📄 License
This project is licensed under the MIT License – see the LICENSE file for details.
🙏 Acknowledgments
Google AI for powering the intelligence
Rich for beautiful terminal UI
Open-source community for tools and inspiration
