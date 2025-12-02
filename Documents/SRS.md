## Software Requirements Specification (SRS) – Connect‑4‑RL

### 1. Introduction

#### 1.1 Purpose
This Software Requirements Specification (SRS) defines the functional and non-functional requirements for the Connect‑4‑RL system.  
It is intended to guide the design, implementation, and testing of the reinforcement learning engine, Django backend, and React frontend.

#### 1.2 Scope
Connect‑4‑RL is a web-based platform for playing the Connect 4 board game, featuring:
- **PvP** games between two human players.
- **PvE** games where a human plays against an RL-based AI agent.
- **Self-play** for a single user controlling both sides.

The system includes:
- A reinforcement learning engine for Connect 4.
- A Django backend providing APIs and real-time game management.
- A React frontend providing the user interface.

#### 1.3 Definitions and Abbreviations
- **RL**: Reinforcement Learning.
- **PvP**: Player vs Player (two human players).
- **PvE**: Player vs Environment (human vs AI).
- **SRS**: Software Requirements Specification.
- **WBS**: Work Breakdown Structure.

### 2. Overall Description

#### 2.1 Product Perspective
Connect‑4‑RL is a standalone web application. The RL engine, backend, and frontend are developed within the same project and deployed together.  
External dependencies include the database, web server, RL libraries (e.g., PyTorch/TensorFlow), and standard web development libraries.

#### 2.2 User Classes and Characteristics
- **Guest player**
  - Can start and play games without logging in.
  - Does not have persistent personal statistics.
- **Registered player**
  - Can log in, play games, and see personal statistics (games played, win/loss, winning rate).
- **Admin**
  - Has access to an admin dashboard to view access logs and basic analytics.

#### 2.3 Operating Environment
- Backend: Django application running on a server (Linux/Windows) with Python.
- Frontend: React application running in modern web browsers.
- Database: Relational database (e.g., SQLite/PostgreSQL) managed by Django.
- Deployment: Docker containers, orchestrated locally via Docker Compose or similar; optional remote deployment (e.g., VPS/cloud).

#### 2.4 Design and Implementation Constraints
- Frontend must be implemented using **React**.
- Backend must be implemented using **Django**.
- Game must use the standard Connect 4 board (6 rows × 7 columns).
- System is developed and maintained primarily by a single developer.

#### 2.5 Assumptions and Dependencies
- Users have access to a modern web browser and stable internet connection.
- Server resources are sufficient to support 5–10 concurrent games.
- External RL and web frameworks (e.g., PyTorch/TensorFlow, React, Django) are available.

### 3. Specific Requirements

#### 3.1 Functional Requirements

##### 3.1.1 RL Engine
- **FR‑RL‑01**: The system shall represent the Connect 4 board state and valid actions for use by RL algorithms.
- **FR‑RL‑02**: The system shall support at least one model-free RL method (e.g., Q-learning or similar) for training an agent.
- **FR‑RL‑03**: The system shall support at least one additional method (value-based, policy-based, or deep RL) where feasible.
- **FR‑RL‑04**: The system shall provide scripts or modules to train RL agents and save the resulting policies to disk.
- **FR‑RL‑05**: The system shall allow the backend to load a trained policy and request actions (moves) given the current board state.

##### 3.1.2 Game Management (Backend)
- **FR‑GM‑01**: The system shall allow creation of new games in self-play, PvP, or PvE mode.
- **FR‑GM‑02**: The system shall allow players to join existing public games or private games via an invite code.
- **FR‑GM‑03**: The system shall validate each move according to Connect 4 rules:
  - Correct column.
  - Gravity (discs stack from the bottom).
  - No moves allowed after the game has ended.
- **FR‑GM‑04**: The system shall determine and store the game result (win, loss, draw).
- **FR‑GM‑05**: The system shall maintain game state (board configuration, current player, move history).
- **FR‑GM‑06**: For PvE games, the system shall obtain AI moves from the RL engine and apply them to the game state.
- **FR‑GM‑07**: The system shall support at least 5–10 concurrent active games without significant errors or timeouts.

##### 3.1.3 Real-time Communication
- **FR‑RT‑01**: The system shall provide a real-time channel (e.g., WebSockets) for game updates between clients and server.
- **FR‑RT‑02**: The system shall send board state and game status updates to all players in the room when a move is made.
- **FR‑RT‑03**: The system shall allow a player who disconnects to reconnect to an ongoing PvP game within a defined timeout window.
- **FR‑RT‑04**: If chat is implemented, the system shall transmit chat messages in real time between players in the same room.

##### 3.1.4 User Accounts and Statistics
- **FR‑UA‑01**: The system shall optionally allow users to register and log in.
- **FR‑UA‑02**: The system shall associate games played while logged in with the corresponding user account.
- **FR‑UA‑03**: The system shall store, for each registered user:
  - Total number of games played.
  - Number of wins, losses, and draws.
- **FR‑UA‑04**: The system shall compute and display the user’s winning rate.

##### 3.1.5 Logging and Analytics
- **FR‑LA‑01**: The system shall record, for each access or game session, the IP address, username/nickname (if available), and timestamp.
- **FR‑LA‑02**: The system shall provide an admin view showing charts of game access over time.
- **FR‑LA‑03**: The system shall provide an admin view listing access and game logs.

##### 3.1.6 Frontend UI
- **FR‑UI‑01**: The frontend shall provide a visual Connect 4 board that reflects the current game state.
- **FR‑UI‑02**: The frontend shall display current player turn and game status (in progress, win, loss, draw).
- **FR‑UI‑03**: The frontend shall allow the user to initiate self-play, PvP, and PvE games.
- **FR‑UI‑04**: The frontend shall connect to the backend’s real-time channel and update the board automatically when moves occur.
- **FR‑UI‑05**: The frontend shall be responsive and usable on desktop, tablet, and phone screen sizes.
- **FR‑UI‑06**: If chat is implemented, the frontend shall display a chat panel for the current room.
- **FR‑UI‑07**: When the user is logged in, the frontend shall show basic statistics such as games played, wins/losses, and winning rate.

#### 3.2 Non-functional Requirements

##### 3.2.1 Performance
- **NFR‑P‑01**: The system should respond to user moves (including AI response) within a few seconds under normal load.
- **NFR‑P‑02**: The system should support at least 5–10 simultaneous games without noticeable lag on the target deployment environment.

##### 3.2.2 Security and Privacy
- **NFR‑S‑01**: User passwords (if implemented) shall be stored hashed and not in plain text.
- **NFR‑S‑02**: IP addresses and logs shall be stored securely and not exposed to other users via the UI.
- **NFR‑S‑03**: Administrative views shall only be accessible to authenticated admin users.

##### 3.2.3 Usability
- **NFR‑U‑01**: The UI shall provide clear feedback for invalid moves, connection issues, and game results.
- **NFR‑U‑02**: Core flows (start game, make moves, see result) shall be achievable without reading external documentation.
- **NFR‑U‑03**: The UI shall remain usable and readable on desktop, tablet, and phone.

##### 3.2.4 Maintainability
- **NFR‑M‑01**: The codebase shall be organized into clear modules for RL engine, backend, and frontend.
- **NFR‑M‑02**: Key components and APIs shall be documented with code comments or short README sections.
- **NFR‑M‑03**: Configuration values (e.g., database URLs, secrets) shall be externalized into environment variables or configuration files.

##### 3.2.5 Portability and Deployment
- **NFR‑D‑01**: The system shall be containerized using Docker for backend and frontend.
- **NFR‑D‑02**: The system shall include basic CI/CD configuration to build, test, and deploy containers to the chosen environment.


