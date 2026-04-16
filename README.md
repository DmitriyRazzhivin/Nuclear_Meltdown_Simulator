# Nuclear Meltdown Simulator

A real-time, object-oriented systems simulation designed to model the thermodynamics and radiation hazards of a pressurized water reactor (PWR). This project demonstrates the integration of multi-threaded physics calculations with a data-driven gameplay engine.

## ⚙️ Core Mechanics

* **Multithreaded Physics Engine**: A background thread simulates reactor decay and thermal accumulation in real-time.
* **Dynamic Thermodynamics**: Models the relationship between Temperature ($T$) and Pressure ($P$) using a simplified ideal gas law logic.
* **Radiation Dosimetry**: Tracks cumulative exposure in Millisieverts ($mSv$).
* **Gated Progression**: Implements access control logic based on player inventory and environmental requirements.

## 🛠 Technical Architecture

The project follows a modular, decoupled architecture to ensure scalability and maintainability:

* **`main.py`**: The central controller handling the primary execution loop and user interface.
* **`engine.py`**: The physics layer containing the `Reactor` class and concurrency logic.
* **`player.py`**: The state management layer for player coordinates, inventory, and health metrics.
* **`data.json`**: An externalized data store defining the world map, item locations, and environmental metadata.

## 📂 Project Structure

```text
├── main.py          # Entry point and command loop
├── engine.py        # Reactor simulation and background threading
├── player.py        # Player state and movement logic
├── data.json        # World map and room metadata
└── .gitignore       # Project exclusion rules
```

## 🚀 Technical Implementation Highlights

* **Concurrency & Real-Time Simulation**

The reactor core operates on a daemon thread, independent of user input. This ensures that the environmental threat escalates even while the user is stationary, forcing a "time-pressure" decision-making environment.

* **Data-Driven World Building**

By utilizing JSON for world-building, the logic is separated from the data. This allows for complex map expansions and balancing tweaks without modifying the underlying Python source code.

* **Inverse Square Logic (Work-in-Progress)**

The simulation is being updated to calculate radiation exposure based on the player’s Euclidean distance from the core coordinates, rather than static room values.