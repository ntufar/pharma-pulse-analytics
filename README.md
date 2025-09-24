# PharmaPulse Analytics Platform - Gemini CLI Agent Workspace

This repository serves as the operational root for a Gemini CLI agent, specifically configured to manage the development lifecycle of the **PharmaPulse Analytics Platform**. It encapsulates all necessary configurations, scripts, and documentation for the agent to effectively create, plan, implement, and maintain features for the platform.

## Project Overview

The PharmaPulse Analytics Platform is a Commercial Data Platform (CDP) designed to provide comprehensive analytics and insights for pharmaceutical sales operations. This workspace facilitates the agent-driven development of this platform, demonstrating modern data stack architecture, migration management, and best practices for data governance and user management.

## Features & Capabilities of the Gemini CLI Agent

Within this workspace, the Gemini CLI agent is equipped to:

*   **Manage Project Constitution:** Define and enforce core principles, governance, and development standards.
*   **Create Feature Specifications:** Generate detailed `spec.md` files from natural language descriptions or existing PRDs.
*   **Plan Implementations:** Develop comprehensive `plan.md` documents, outlining technical approaches, data models, and contracts.
*   **Generate Tasks:** Break down implementation plans into actionable, dependency-ordered tasks in `tasks.md`.
*   **Analyze & Clarify:** Perform consistency checks across artifacts and identify ambiguities in specifications.
*   **Execute Implementations:** Drive the development process by executing defined tasks.

## Project Structure

*   `.gemini/`: Contains command definitions (TOML files) that guide the agent's actions, such as `analyze`, `implement`, `plan`, and `specify`.

*   `.specify/`: Holds agent-specific memory, scripts, and templates.
    *   `memory/`: Stores important agent-specific documents, like `constitution.md`, which outlines the project's core principles and governance.
    *   `scripts/bash/`: Contains bash scripts for agent setup, feature creation, and context updates.
    *   `templates/`: Provides templates for various agent outputs and documents (e.g., `plan-template.md`, `spec-template.md`, `tasks-template.md`).

*   `docs/`: Intended for project-specific documentation, including the Product Requirement Document (`PRD.md`) for the PharmaPulse Analytics Platform.

*   `specs/`: This directory will contain subdirectories for each feature, with each subdirectory holding its `spec.md`, `plan.md`, `tasks.md`, and other design artifacts.

## Getting Started

### Prerequisites

*   **Git:** For version control.
*   **Gemini CLI:** The command-line interface for interacting with the Gemini agent.

### Cloning the Repository

```bash
git clone https://github.com/ntufar/pharma-pulse-analytics.git
cd pharma-pulse-analytics
```

### Initial Setup

Ensure you are on the `master` branch or the desired base branch.

```bash
git checkout master
```

## Usage

Interact with the Gemini CLI agent using the `/` commands. The agent will guide you through the development process.

### Common Commands

*   `/specify <feature description>`: Create a new feature specification. For example, to create a spec from `docs/PRD.md`:
    ```
    /specify <content of docs/PRD.md>
    ```
    *(Note: The agent expects the actual content of the PRD, not just the filename.)*

*   `/plan`: Generate an implementation plan based on an existing feature specification.

*   `/clarify`: Identify and resolve ambiguities in a feature specification.

*   `/constitution`: View or update the project's governing principles.

## Contributing

Follow the established project constitution and development workflow. Ensure all changes adhere to code quality and testing standards.

## License

[TODO: Add license information here]