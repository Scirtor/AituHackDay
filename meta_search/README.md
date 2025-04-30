# PenSearch

PenSearch is a web application designed to simplify advanced search queries using filters like specific websites (`site:`) and file types (`filetype:`). It leverages the DuckDuckGo search API to fetch results, including text and images, and provides a clean, user-friendly interface.

---

## Features

- **Search Filters**:
  - Filter results by specific websites (e.g., `site:example.com`).
  - Filter results by file types (e.g., `filetype:pdf`).
- **Image Search**: Fetch images related to the query.
- **Text Search**: Perform text-based searches with detailed results.
- **Rate Limiting**: Prevent abuse by limiting the number of requests per user.
- **Responsive Design**: Clean and user-friendly interface.

---

## Installation

1. **Clone the Repository**:
   
   git clone https://github.com/your-username/meta_search.git
   cd pensearch

2. **Set up a Virtual Environment**:

    python -m venv venv
    source venv/bin/activate

3. **Install dependencies**:

    pip install -r requirements.txt

4. **Run the Application**:

    python app.py

5. **Access the application**:

    Open your browser and navigate to http://127.0.0.1:5000.

Usage:
1. Enter your search query in the input field.
2. Use the filter buttons to: 
 * Search for images.
 * Seatch for specific file types.
 * Search within specific websites.
3. Click "Search" to view the results.

Project Structure

meta_search/
│
├── [app.py]                 # Main application logic
├── [requirements.txt]       # Python dependencies
├── templates/
│   └── [index.html]         # HTML template for the UI
├── static/
│   └── [style.css]         # CSS for styling the application
├── [License.txt]
├── [README.md]
└── [README.txt]

Dependencies
Flask: Web framework for Python.
Flask-Limiter: For rate limiting requests.
duckduckgo-search: Library for fetching search results from DuckDuckGo.
Install all dependencies using:
    pip install-r requirements.txt

License
This project is licensed under the MIT License. See the License.txt

