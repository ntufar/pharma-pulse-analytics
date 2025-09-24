# Gemini CLI Agent Project Root

This directory serves as the operational root for a Gemini CLI agent. It contains configurations, scripts, and templates that define the agent's behavior, commands, and project management processes.

## Key Directories

*   `.gemini/`: This directory contains command definitions (TOML files) that guide the agent's actions. These commands include functionalities like `analyze`, `implement`, `plan`, and `specify`, which are crucial for the agent's operation and interaction with projects.

*   `.specify/`: This directory holds agent-specific memory, scripts, and templates.
    *   `memory/`: Stores important agent-specific documents, such as `constitution.md`. This file outlines the project's core principles, governance, and operational guidelines that the agent adheres to.
    *   `scripts/bash/`: Contains bash scripts used for various agent-related tasks, including initial setup (`setup-plan.sh`), creating new features (`create-new-feature.sh`), checking prerequisites (`check-prerequisites.sh`), and updating the agent's context (`update-agent-context.sh`).
    *   `templates/`: Provides templates for various agent outputs and documents. Examples include `plan-template.md` (for project plans), `spec-template.md` (for specifications), and `tasks-template.md` (for task breakdowns).

*   `docs/`: This directory is intended for project-specific documentation. It may contain documents such as Product Requirement Documents (`PRD.md`), design documents, or other relevant project-related information.

## Usage

The files and directories within this project root are integral to the Gemini CLI agent's functionality. They enable the agent to:

*   **Understand its operational context:** By reading configuration files and memory documents.
*   **Execute commands:** Based on the definitions in `.gemini/commands`.
*   **Manage project documentation:** By utilizing templates and storing project-specific documents in `docs/`.
*   **Adhere to defined project principles:** As outlined in the `constitution.md`.

This setup allows the Gemini CLI agent to operate effectively, manage projects, and interact with users in a structured and consistent manner.