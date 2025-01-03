# Wordle Solver

A Python project to create an algorithm that solves Wordle in the most efficient way possible.

## Table of Contents

- [Overview](#Overview)
- [Features](#Features)
- [Roadmap](#Planning-roadmap)
- [Prerequisites](#Prerequisites)
- [Installation](#installation)
- [Configuration](#configuration)

## Overview

Welcome to the Wordle Solver and Game project! This repository contains a Python implementation of the popular Wordle game, enhanced with a Discord bot interface and an advanced entropy-based algorithm to solve Wordle puzzles efficiently.

## Features

### 1. Wordle Game
- Fully functional Wordle game implemented in Python.
- User-friendly command-line interface for standalone gameplay.

### 2. Discord Bot Integration
- Play Wordle directly in your Discord server.
- Easy-to-use commands for starting and interacting with the game.

### 3. Algorithm v1
- Advanced algorithm that calculates entropy to identify the most optimal guesses.
- Can solve Wordle puzzles with high efficiency.

## Planning roadmap

- [x] Wordle Game
- [X] Export letter types
- [X] Filter words from data
- [X] Make algorithm for choosing words
    - [X] Using the feedback from main.py it will return a guess

    - [X] Impliment algorithm to guess
- [ ] Discord bot implementation

## Prerequisites

Before you begin, ensure you have met the following requirements:

- [Latest python version](https://www.python.org/downloads/) is installed on your machine
- [Visual Studio Code](https://code.visualstudio.com/download) is the recommended IDE for developing the discord bot
- VScode Python and Pylance Extension for the python environment
- [git](https://git-scm.com/downloads) and [Github Desktop](https://github.com/apps/desktop) for version control
- [pip](https://pip.pypa.io/en/stable/installation/) is installed for package management.
- Access to the discord bot application and token (Message harpoonz_ on discord)

## Installation

To set up the project, follow these steps:

1. **Fork the Repository:**
To contribute to this project or modify it for your use, first fork the repository:
- Navigate to the repository on GitHub.
- Click on the `Fork` button at the top right of the page to create a copy of the repository under your own GitHub account.
2. **Clone the repository:** 
```bash
git clone https://github.com/your_username/wordle_solver
```
3. **Navigate to the project directory:**
```bash
cd wordle_solver
```
4. **Install dependencies:**
```bash
pip install -r requirements.txt
```

## Configuration

1. **Create a `.env` File**

   In the root directory of the project, create a `.env` file to store your sensitive information like the Discord bot token and any API keys.

   ```
   DISCORD_TOKEN=your_discord_bot_token_here
   ```

2. **Configure Environment Variables**

   Ensure your `.env` file is correctly formatted and saved in the project’s root directory. The `.env` file should not be included in version control, as it contains sensitive information. Make sure your `.gitignore` file includes:

   ```
   .env
   ```

