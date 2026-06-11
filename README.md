# Python Projects

A collection of Python learning and development projects showcasing various concepts, libraries, and best practices.

---

## 📋 Projects Overview

### 1. **Number Guessing Game** ✅

**What it does:** A simple yet engaging number guessing game where players attempt to guess a randomly generated number within a specified range. The game provides feedback on each guess and tracks attempts.

**Features:**
- Random number generation
- Input validation
- Guess feedback (too high/too low/correct)
- Attempt counter
- Replay functionality

**Technologies Used:**
- Python 3.x
- Built-in `random` module

**How to Run:**
```bash
cd "Number Guessing Game"
python main.py
```

**What I Learned:**
- User input handling and validation
- Control flow with loops and conditionals
- Random number generation
- Game loop implementation

**Location:** `/Number Guessing Game/`

---

### 2. **Password Generator** ✅

**What it does:** A secure password generation tool that creates strong, randomized passwords with customizable parameters. Includes user management capabilities and persistent storage using JSON.

**Features:**
- Generate secure passwords with configurable length
- Mix of uppercase, lowercase, numbers, and special characters
- User database management
- Save/retrieve user passwords
- User-friendly CLI interface

**Technologies Used:**
- Python 3.x
- JSON storage
- `random` and `string` modules

**How to Run:**
```bash
cd Password_Generator
python main.py
```

**What I Learned:**
- File I/O and JSON data persistence
- String manipulation
- Character set combinations
- User authentication basics
- CLI interface design

**Location:** `/Password_Generator/`

---

### 3. **Quiz Game** 🚧

**What it does:** An interactive quiz game application that tests user knowledge across various topics. Players answer multiple-choice questions and receive scored feedback based on their performance.

**Features:**
- Interactive quiz gameplay with multiple-choice questions
- Real-time question and answer system
- Score tracking and performance metrics
- User input validation
- Quiz completion summary

**Technologies Used:**
- Python 3.x
- Modular code architecture

**How to Run:**
```bash
cd Quiz_Game
python main.py
```

**What I Learned:**
- Game state management
- Data structure design (questions, answers, scoring)
- User experience and feedback
- Score calculation logic
- Code modularity and organization

**Status:** 🚧 In Progress
- ✅ Basic project structure created
- ⏳ Core game logic - in development
- ⏳ Question database - to be added
- ⏳ Scoring system - to be added

**Future Enhancements:**
- Add expandable question database/file
- Implement multiple difficulty levels
- Add timer functionality for timed quizzes
- Create interactive menu system with categories

**Location:** `/Quiz_Game/` | [View Project Details](./Quiz_Game/README.md)

---

### 4. **Task Tracker CLI** ✅

**What it does:** A command-line task management application that allows users to create, update, delete, and organize tasks with persistent JSON storage. Perfect for managing daily to-do lists and project tasks.

**Features:**
- Add, update, and delete tasks
- Task status management (pending, completed)
- Task listing and filtering
- Persistent storage with JSON
- Task priority levels
- Due date tracking

**Technologies Used:**
- Python 3.x
- JSON storage
- Command-line argument parsing

**How to Run:**
```bash
cd Task-Tracker-CLI
python main.py
```

**What I Learned:**
- File persistence and data structures
- CRUD operations (Create, Read, Update, Delete)
- CLI argument handling
- Data filtering and sorting
- Application state management

**Location:** `/Task-Tracker-CLI/`

---

### 5. **Web Scraping Project** 🚧

**What it does:** A web scraping tool that extracts and parses content from websites using BeautifulSoup. Currently scrapes the OpenCode.ai website to extract hero sections and feature information. Demonstrates HTML parsing with CSS selectors.

**Features:**
- Website content extraction using BeautifulSoup
- HTML parsing with CSS selectors
- Hero section and feature data extraction
- Headings and descriptions parsing
- List items extraction
- Robust error handling for missing sections

**Technologies Used:**
- Python 3.x
- BeautifulSoup 4 - HTML parsing
- Requests - HTTP requests
- lxml - XML/HTML processing

**Installation:**
```bash
pip install beautifulsoup4 requests lxml
```

**How to Run:**
```bash
cd Web_scrap
python main.py
```

**Current Website Target:**
- OpenCode.ai - Scraping hero section and features

**What I Learned:**
- HTTP requests and web APIs
- HTML structure and DOM traversal
- CSS selectors for targeted extraction
- Error handling in web operations
- Data parsing and cleaning
- Respecting website terms of service and robots.txt

**Status:** 🚧 In Progress
- ✅ Core scraping functionality implemented
- ⏳ Multi-site support - in development
- ⏳ Data storage to file - to be added

**Future Enhancements:**
- [ ] Add multiple website targets with configuration
- [ ] Save scraped data to file (JSON/CSV formats)
- [ ] Add JavaScript rendering support (Selenium/Puppeteer)
- [ ] Create data processing and transformation pipeline
- [ ] Implement logging and monitoring
- [ ] Add robots.txt and rate limiting compliance

**Important Notes:**
- Some websites require JavaScript rendering for full content access
- Always respect website's `robots.txt` and terms of service
- Implement appropriate request delays to avoid overloading servers

**Location:** `/Web_scrap/` | [View Project Details](./Web_scrap/README.md)

---

## 🚀 Getting Started

Each project has its own structure and dependencies. Follow these steps:

1. **Navigate to the project directory:**
   ```bash
   cd "Project_Name"
   ```

2. **Install project-specific dependencies (if any):**
   ```bash
   pip install -r requirements.txt
   ```

3. **Read the project README for detailed information**

4. **Run the project:**
   ```bash
   python main.py
   ```

## 📋 Requirements

- **Python 3.x** (3.8 or higher recommended)
- See individual project READMEs for specific dependencies

**Global Dependencies:**
- `beautifulsoup4` - For web scraping project
- `requests` - For web scraping project
- `lxml` - For web scraping project

## 📖 Legend

- ✅ **Completed** - Fully functional and tested
- 🚧 **In Progress** - Under active development
- 📚 **Learning Focus** - Demonstrates specific Python concepts

## 💡 Key Learning Outcomes

Across these projects, I've learned:
- **Core Python:** Variables, loops, conditionals, functions, data structures
- **File I/O:** Reading, writing, and managing files (especially JSON)
- **Web Technologies:** HTTP requests, HTML parsing, CSS selectors
- **Data Management:** CRUD operations, data persistence, JSON handling
- **User Interaction:** CLI interface design, input validation, error handling
- **Game Development:** Game loops, state management, scoring systems
- **Best Practices:** Code organization, modularity, documentation

## 📝 Notes

- All projects are for learning and development purposes
- Each project demonstrates different Python concepts and libraries
- Code is open for review, improvement, and learning
- Contributions and suggestions are welcome!

## 🔄 Development Workflow

1. Create project directory and initial structure
2. Build core functionality with basic features
3. Add error handling and validation
4. Implement data persistence (if needed)
5. Test and refine user experience
6. Document code and create comprehensive README
7. Plan and implement enhancements

## 📅 Last Updated

June 2026

---

**Feel free to explore each project, run them, and learn from the code!**
