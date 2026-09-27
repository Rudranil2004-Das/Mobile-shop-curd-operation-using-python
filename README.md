# Mobile Shop Management

A simple command-line inventory management system for a mobile phone shop, built in Python. It lets you add, view, search, update, and delete mobile phone records through an interactive text menu.

## Features

- **Add Mobile** — Add a new mobile phone record with ID, brand, model, price, and quantity.
- **Display All Mobiles** — View all mobile records in a formatted table.
- **Search Mobile** — Look up a mobile by its ID.
- **Update Mobile** — Edit the details of an existing mobile.
- **Delete Mobile** — Remove a mobile from the inventory (with confirmation).
- **Exit** — Cleanly exit the application.

## Project Structure

```
.
├── app.py         # Entry point — launches the dashboard
├── Dashboard.py   # Main menu loop and user interaction
└── config.py      # Data storage and core operations (add/display/search/update/delete)
```

### How it works

- `app.py` is the entry point. Running it calls `dashboard()` from `Dashboard.py`.
- `Dashboard.py` displays a menu in a loop and routes the user's choice to the corresponding function.
- `config.py` holds the in-memory `mobiles` list (each mobile is stored as `[id, brand, model, price, quantity]`) along with the functions that operate on it.

## Requirements

- Python 3.10+ (uses `match` / `case` statements)

## Usage

1. Make sure `app.py`, `Dashboard.py`, and `config.py` are in the same directory.
2. Run the application:

   ```bash
   python app.py
   ```

3. Follow the on-screen menu to manage mobile records:

   ```
   =============================================
    MOBILE SHOP MANAGEMENT
   =============================================
   1. Add Mobile
   2. Display All Mobiles
   3. Search Mobile
   4. Update Mobile
   5. Delete Mobile
   6. Exit
   =============================================
   Enter your choice:
   ```

## Notes

- Data is stored **in memory only** — all records are lost when the program exits. There is no file or database persistence.
- Mobile IDs must be unique; attempting to add a duplicate ID will be rejected.
- Input is not extensively validated (e.g., entering non-numeric text for price/quantity/ID will raise an error).

## Possible Improvements

- Persist data to a file (CSV/JSON) or a database.
- Add input validation and error handling for invalid entries.
- Replace the raw list-based records with a data class or dictionary for clarity.
- Add unit tests for the core operations.
