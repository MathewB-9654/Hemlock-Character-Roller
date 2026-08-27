# Hemlock Character Roller

A data-heavy, object-oriented desktop companion application for tabletop role-playing games (TTRPGs), specifically Hemlock. This tool handles character state management and incorporates automated game mechanics, similar to platforms like D&D Beyond.

## 🚀 Project Status: Active Refactoring
This project is under active development. The original backend was heavily influenced by my learning, and as such, is being rewritten into a much more usable form, as a precursor to transitioning to a CustomTkinter UI.

*   **`main` branch:** Contains the stable, fully operational terminal/print-based version.
*   **`dev` branch:** Contains active work migrating the layout to a modern desktop GUI.

---

## ✨ Features (Stable on `main`)
*   **Automated Dice Engine:** Built-in dice roller for the Hemlock system, including full support for many modifiers. More details found in overview.txt, which is accessible within the app.
*   **Object-Oriented Architecture:** Scalable Python classes managing character statistics and modifiers.
*   **Dynamic Calculations:** Real-time calculation of modifiers based on raw attribute inputs.

---

## 🛠️ Tech Stack & Tools
*   **Language:** Python 3.x
*   **UI Frameworks:** Standard I/O (Current Stable) ➔ Migrating to **CustomTkinter (CTK)** (In Progress)
*   **Version Control:** Git & GitHub

---

## 🗺️ Development Roadmap

### Phase 1: Core Mechanics 🔄 *COMPLETE*
- [x] Design object classes for character sheets.
- [x] Implement mathematical logic for dice rolls and modifier calculations.
- [x] Validate application state stability via terminal inputs.
- [x] JSON serialization integration for data persistence, to save and load character data.


### Phase 2: GUI Migration ⏳ *IN PROGRESS*
- [ ] Migrate application engine from console inputs to standard windows.
- [ ] Implement custom styling and dark mode themes using **CustomTkinter**.
- [ ] Build interactive visual dice widgets.

### Phase 3: Data Persistence 📅 *FUTURE*
- [ ] Integrate game rules and information for fully in-app character creation.

---

## ⚙️ How to Run the Stable Version

### Prerequisites
Ensure you have Python 3 installed on your system.

### Installation & Execution
1. Download files through GitHub

2. Open main.py through an IDE or run with Python.

3. Use the menu to access the **overview** for detailed explanations.
