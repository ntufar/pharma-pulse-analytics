# PharmaPulse Analytics Platform

This repository contains the **PharmaPulse Analytics Platform**, a Commercial Data Platform (CDP) designed to provide comprehensive analytics and insights for pharmaceutical sales operations. It encapsulates all necessary configurations, scripts, and documentation for the platform's development lifecycle.

## Project Overview

The PharmaPulse Analytics Platform is a Commercial Data Platform (CDP) designed to provide comprehensive analytics and insights for pharmaceutical sales operations. This workspace facilitates the agent-driven development of this platform, demonstrating modern data stack architecture, migration management, and best practices for data governance and user management.

## Development Workflow & Artifacts

Within this workspace, the development workflow supports:

*   **Project Constitution:** Core principles, governance, and development standards are defined and enforced.
*   **Feature Specifications:** Detailed `spec.md` files are created from natural language descriptions or existing PRDs.
*   **Implementation Plans:** Comprehensive `plan.md` documents are developed, outlining technical approaches, data models, and contracts.
*   **Task Generation:** Implementation plans are broken down into actionable, dependency-ordered tasks in `tasks.md`.
*   **Analysis & Clarification:** Consistency checks are performed across artifacts, and ambiguities in specifications are identified.
*   **Implementation Execution:** The development process is driven by executing defined tasks.

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

This repository supports a structured development workflow. Key artifacts and processes are managed through specific commands or tools.

### Common Workflow Steps

*   **Feature Specification Creation:** To create a new feature specification from a PRD, provide the content of your PRD to the relevant tool or command. For example, using `docs/PRD.md`:
    ```
    <tool_or_command> <content of docs/PRD.md>
    ```
    *(Note: The tool/command expects the actual content of the PRD, not just the filename.)*

*   **Implementation Planning:** Generate an implementation plan based on an existing feature specification.

*   **Ambiguity Resolution:** Identify and resolve ambiguities in a feature specification.

*   **Project Constitution Management:** View or update the project's governing principles.

## Contributing

Follow the established project constitution and development workflow. Ensure all changes adhere to code quality and testing standards.

## License

[TODO: Add license information here]