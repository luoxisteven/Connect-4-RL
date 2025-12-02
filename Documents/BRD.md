## Business Requirements Document – Connect‑4‑RL

### 1. Executive Summary
Connect‑4‑RL is a personal AI project that uses reinforcement learning (RL) to play the classic Connect 4 board game.  
The system will provide a web-based experience that supports:
- **PvP (Player vs Player)** games between two human players.
- **PvE (Player vs Environment)** games where a human plays against an AI agent.

The project combines:
- A set of RL algorithms trained to play Connect 4.
- A Django backend server that hosts games and exposes APIs.
- A React frontend that allows users to start and play games in the browser.

### 2. Business Objectives
- **Skill development**: Apply and deepen my knowledge of reinforcement learning, classical AI, and web development (React + Django).
- **Portfolio piece**: Create a demonstrable project that showcases my AI and software engineering abilities for future career opportunities.
- **Entertainment**: Build a fun and interactive game platform that I can use during my free time.

### 3. Scope

#### 3.1 In Scope
- **Reinforcement learning for Connect 4**
  - Implement and train multiple RL algorithms for Connect 4.
  - Save and load trained policies for later use in the game server.
- **Backend game server (Django)**
  - Provide APIs to create, join, and manage games.
  - Integrate trained RL policies to support PvE games.
  - Support multiple concurrent games (target: 5–10 concurrent games).
- **Web frontend (React)**
  - Provide a playable Connect 4 board in the browser.
  - Support self-play (one user controlling both sides), PvP, and PvE modes.
  - Provide winning rate for user who login
  - Responsive to Tablet and Phone
- **Full production-grade deployment**
  - Docker Images and Containers
  - DevOps pipelines

#### 3.2 Out of Scope (Initial Version)
- Advanced social features beyond basic chat (e.g., friends system, rankings, tournaments).

### 4. Functional Requirements

#### 4.1 Reinforcement Learning Engine
- **RL algorithms**
  - Support multiple RL approaches (at minimum):
    - Model-based methods.
    - Model-free methods.
    - Policy-based methods.
    - Value-based methods.
    - Deep reinforcement learning methods.
- **Training and policy management**
  - Provide scripts or modules to train RL agents on Connect 4.
  - Save trained policies to disk.
  - Load saved policies into the backend server for inference during PvE games.

#### 4.2 Game Server and Match Management (Backend)
- **Game sessions**
  - Create new games (self-play, PvP, PvE).
  - Join existing games via a public lobby or private invite code.
  - Maintain game state (board, current player, move history, game result).
- **Room types**
  - Public rooms that can be discovered and joined by other players.
  - Private rooms accessible only with an invite code.
- **Concurrency**
  - Support 5–10 active games running at the same time without noticeable performance degradation.
- **Connectivity**
  - Maintain continuous connection during a game (e.g., using WebSockets or long polling).
  - Allow players to reconnect and resume an existing PvP game if they disconnect accidentally (within a reasonable time window).
- **PvE integration**
  - When a game is PvE, the server must:
    - Call the RL policy to obtain the AI’s move.
    - Validate moves and update game state accordingly.

#### 4.3 User Accounts, Logging, and Analytics
- **Authentication (optional / basic)**
  - Allow users to play with or without logging in.
  - When logged in, associate game history with the user account.
- **Game records**
  - Store basic game results (win / loss / draw, game duration).
  - Allow users to see:
    - Number of games played.
    - Win / loss statistics.
- **Player metadata and access logs**
  - Record IP address, username (or nickname), and timestamp when users access or play games.
  - Provide an admin dashboard view that shows:
    - Charts of game access over time.
    - Logs of game access events.

#### 4.4 Web Frontend (React)
- **Game UI**
  - Display a clear and responsive Connect 4 board.
  - Show current player turn and game status (in progress, win, loss, draw).
  - Allow users to start:
    - Self-play games.
    - PvP games (public or private).
    - PvE games against the RL agent.
- **Connectivity and reliability**
  - Maintain a constant connection with the backend during games.
  - Allow users to restart a PvE game quickly from the UI.
  - Allow users to rejoin an existing PvP game if they accidentally close the page or lose connection (within a defined time).
- **Chat (nice-to-have)**
  - Optional in-game chat for players in the same room.

### 5. Non-functional Requirements

- **Performance**
  - The system should support at least 5–10 concurrent active games without significant latency.
  - Average move response time (including AI move) should be acceptable for real-time gameplay (e.g., typically under a few seconds).
- **Availability**
  - For a personal project, target “best-effort” availability, with the ability to restart the server easily if it fails.
- **Security and Privacy**
  - Store user credentials (if any) securely following standard practices.
  - Do not expose sensitive information (e.g., IP addresses) to other players in the UI.
- **Usability**
  - The UI should be simple, intuitive, and playable on desktop web browsers.
  - Provide clear feedback messages (e.g., invalid moves, connection lost, game over).
- **Maintainability**
  - Use clear code structure and documentation for the RL components, Django backend, and React frontend.
  - Separate concerns between training code, inference code, backend APIs, and frontend UI.

### 6. Constraints and Technology Stack
- **Frontend**: React.
- **Backend**: Django.
- **Game**: Connect 4 (6 rows × 7 columns standard board).
- **Developer**: Single developer (time and scope must remain manageable).
