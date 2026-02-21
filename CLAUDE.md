# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Workspace Overview

This is a multi-project workspace (not a single git repo at root). Projects span React Native, Flutter/Dart, Python, vanilla JS, and Bash. Domain focus is electrical engineering education and NEC compliance tools. Development happens on **Termux (Android)** — no native build toolchain (Xcode/Android Studio) is available.

## Key Projects

### Turbo-Repos/Electrician — React Native + Expo calculator app
The main active project. See `Turbo-Repos/Electrician/CLAUDE.md` for detailed architecture and conventions (three-layer pattern, navigation, theme system, adding calculators).

```bash
cd Turbo-Repos/Electrician
npm install
npx expo start          # Dev server
npm test                # All Jest tests
npm test -- tests/ohmsLaw.test.js  # Single test
npm test -- --coverage  # Coverage
```

### sovereign-circuit-academy/vader-academy-app — Flutter mobile app
NEC codes, conduit bending, load calculator. Uses Riverpod for state management, feature-first architecture under `lib/features/`.

```bash
cd sovereign-circuit-academy/vader-academy-app
flutter pub get
flutter run
flutter test
```

### sovereign-circuit-academy — Python tools
Standalone Python scripts for NEC compliance calculations. Dependencies: pandas, matplotlib.

```bash
python3 sovereign-circuit-academy/imperial_load_audit_v3.py
python3 sovereign-circuit-academy/box_fill_calculator.py
python3 sovereign-circuit-academy/manual_j_thermal.py
```

### Todolite — Vanilla JS to-do app
No dependencies or build step. Open `index.html` directly.

### Turbo-Repos/DEATHSTAR — Bash CLI tool suite
Shell scripts, main executable is `deathstar`.

## Repository Management

23 repos deployed to GitHub under [@Turbo-the-tech-dev](https://github.com/Turbo-the-tech-dev). See `MASTER-INDEX.md` for the full catalog. Push and cleanup scripts:

```bash
/root/push_all_repos.sh        # Push all repos to GitHub
/root/cleanup_local_repos.sh   # Delete local copies after push
```

## Conventions

- Conventional commits: `feat:`, `fix:`, `docs:`, etc.
- Each sub-project has its own git repo — always `cd` into the project before running git commands
- Electrician app: utility functions must be pure (no React imports in `src/utils/`), tests use CommonJS `require()`
