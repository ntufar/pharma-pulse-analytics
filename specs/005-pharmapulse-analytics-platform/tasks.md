# Tasks: PharmaPulse Analytics Platform

**Input**: Design documents from `/specs/005-pharmapulse-analytics-platform/`
**Prerequisites**: plan.md (required), research.md, data-model.md, contracts/

## Execution Flow (main)
```
1. Load plan.md from feature directory
   → If not found: ERROR "No implementation plan found"
   → Extract: tech stack, libraries, structure
2. Load optional design documents:
   → data-model.md: Extract entities → model tasks
   → contracts/: Each file → contract test task
   → research.md: Extract decisions → setup tasks
3. Generate tasks by category:
   → Setup: project init, dependencies, linting
   → Tests: contract tests, integration tests
   → Core: models, services, CLI commands
   → Integration: DB, middleware, logging
   → Polish: unit tests, performance, docs
4. Apply task rules:
   → Different files = mark [P] for parallel
   → Same file = sequential (no [P])
   → Tests before implementation (TDD)
5. Number tasks sequentially (T001, T002...)
6. Generate dependency graph
7. Create parallel execution examples
8. Validate task completeness:
   → All contracts have tests?
   → All entities have models?
   → All endpoints implemented?
9. Return: SUCCESS (tasks ready for execution)
```

## Format: `[ID] [P?] Description`
- **[P]**: Can run in parallel (different files, no dependencies)
- Include exact file paths in descriptions

## Path Conventions
- **Single project**: `src/`, `tests/` at repository root
- **Web app**: `backend/src/`, `frontend/src/`
- **Mobile**: `api/src/`, `ios/src/` or `android/src/`
- Paths shown below assume single project - adjust based on plan.md structure

## Phase 3.1: Setup
- [X] T001 Create project structure (backend/, frontend/ directories)
- [X] T002 Initialize Python backend project with dependencies (Snowflake, dbt Core, Dagster, AWS, PostgreSQL) - *Note: psycopg2-binary installation failed due to macOS Seatbelt permissions.*
- [X] T003 Initialize JavaScript/TypeScript frontend project with dependencies (React, Streamlit)
- [X] T004 [P] Configure linting and formatting for backend (e.g., Black, Flake8) in `backend/`
- [X] T005 [P] Configure linting and formatting for frontend (e.g., ESLint, Prettier) in `frontend/`
- [X] T006 Research and set up Python testing frameworks (unit, integration, E2E) in `backend/`
- [X] T007 Research and set up JavaScript/TypeScript testing frameworks (unit, integration, E2E) in `frontend/` - *Note: Playwright installation failed due to macOS Seatbelt permissions.*

## Phase 3.2: Tests First (TDD) ⚠️ MUST COMPLETE BEFORE 3.3
**CRITICAL: These tests MUST be written and MUST FAIL before ANY implementation**
- [X] T008 [P] Contract test `customers.yaml` API in `backend/tests/contract/test_customers_api.py`
- [X] T009 [P] Contract test `products.yaml` API in `backend/tests/contract/test_products_api.py`
- [X] T010 [P] Contract test `sales_transactions.yaml` API in `backend/tests/contract/test_sales_transactions_api.py`
- [X] T011 [P] Contract test `users.yaml` API in `backend/tests/contract/test_users_api.py`
- [X] T012 [P] Integration test UC-001: Territory Sales Performance in `backend/tests/integration/test_territory_sales.py`
- [X] T013 [P] Integration test UC-002: Product Analytics in `backend/tests/integration/test_product_analytics.py`
- [X] T014 [P] Integration test UC-003: Market Intelligence in `backend/tests/integration/test_market_intelligence.py`
- [X] T015 [P] Integration test UC-004: Sales Forecasting in `backend/tests/integration/test_sales_forecasting.py`
- [X] T016 [P] Integration test UC-005: Regulatory Compliance Reporting in `backend/tests/integration/test_regulatory_compliance.py`
- [X] T017 [P] Integration test Data Ingestion & Freshness in `backend/tests/integration/test_data_ingestion.py`
- [X] T018 [P] Integration test User Management in `backend/tests/integration/test_user_management.py`
- [X] T019 [P] Integration test API Access in `backend/tests/integration/test_api_access.py`

## Phase 3.3: Core Implementation (ONLY after tests are failing)
- [X] T020 [P] Implement `SalesTransaction` model in `backend/src/models/sales_transaction.py`
- [X] T021 [P] Implement `Product` model in `backend/src/models/product.py`
- [X] T022 [P] Implement `Territory` model in `backend/src/models/territory.py`
- [X] T023 [P] Implement `Customer` model in `backend/src/models/customer.py`
- [X] T024 Implement `CustomerService` (CRUD) in `backend/src/services/customer_service.py`
- [X] T025 Implement `ProductService` (CRUD) in `backend/src/services/product_service.py`
- [X] T026 Implement `SalesTransactionService` (CRUD) in `backend/src/services/sales_transaction_service.py`
- [X] T027 Implement `UserService` (CRUD) in `backend/src/services/user_service.py`
- [X] T028 Implement Customer API endpoints (`/customers`, `/customers/{id}`) in `backend/src/api/customers.py`
- [X] T029 Implement Product API endpoints (`/products`, `/products/{id}`) in `backend/src/api/products.py`
- [X] T030 Implement Sales Transaction API endpoints (`/sales-transactions`, `/sales-transactions/{id}`) in `backend/src/api/sales_transactions.py`
- [X] T031 Implement User API endpoints (`/users`, `/users/{id}`) in `backend/src/api/users.py`

## Phase 3.4: Integration
- [X] T032 Configure database connection for backend (Snowflake/PostgreSQL)
- [X] T033 Implement authentication middleware
- [X] T034 Implement request/response logging
- [X] T035 Configure CORS and security headers
- [ ] T036 Integrate frontend with Customer API
- [ ] T037 Integrate frontend with Product API
- [ ] T038 Integrate frontend with Sales Transaction API
- [ ] T039 Integrate frontend with User API

## Phase 3.5: Polish
- [ ] T040 [P] Write unit tests for `SalesTransaction` model in `backend/tests/unit/test_sales_transaction_model.py`
- [ ] T041 [P] Write unit tests for `Product` model in `backend/tests/unit/test_product_model.py`
- [ ] T042 [P] Write unit tests for `Territory` model in `backend/tests/unit/test_territory_model.py`
- [ ] T043 [P] Write unit tests for `Customer` model in `backend/tests/unit/test_customer_model.py`
- [ ] T044 [P] Write unit tests for `CustomerService` in `backend/tests/unit/test_customer_service.py`
- [ ] T045 [P] Write unit tests for `ProductService` in `backend/tests/unit/test_product_service.py`
- [ ] T046 [P] Write unit tests for `SalesTransactionService` in `backend/tests/unit/test_sales_transaction_service.py`
- [ ] T047 [P] Write unit tests for `UserService` in `backend/tests/unit/test_user_service.py`
- [ ] T048 Performance testing and optimization
- [ ] T049 [P] Update API documentation (e.g., Swagger UI generation)
- [ ] T050 [P] Update user-facing documentation (e.g., `docs/PRD.md` or new user guide)
- [ ] T051 Run quickstart scenarios (`quickstart.md`) for final validation

## Dependencies
- T001-T007 (Setup) must complete before T008-T051.
- T008-T019 (Tests First) must complete and fail before T020-T031 (Core Implementation).
- T020-T023 (Models) block T024-T027 (Services) and T040-T043 (Model Unit Tests).
- T024-T027 (Services) block T028-T031 (API Endpoints) and T044-T047 (Service Unit Tests).
- T028-T031 (API Endpoints) block T036-T039 (Frontend Integration).
- T032 (DB Connection) blocks T024-T027 (Services).
- T033 (Auth Middleware) blocks T028-T031 (API Endpoints) and T036-T039 (Frontend Integration).
- T034 (Logging) and T035 (CORS/Security) can run in parallel with other implementation tasks but should ideally be in place before extensive testing.
- T036-T039 (Frontend Integration) block T051 (Quickstart Scenarios).
- T040-T047 (Unit Tests) can run in parallel with each other once their respective models/services are implemented.
- T048-T050 (Polish) can run in parallel with each other but should ideally be done after core implementation and initial integration.
- T051 (Quickstart Scenarios) is the final validation step.

## Parallel Example
```
# Launch T004-T005 together:
Task: "Configure linting and formatting for backend (e.g., Black, Flake8) in `backend/`"
Task: "Configure linting and formatting for frontend (e.g., ESLint, Prettier) in `frontend/`"

# Launch T008-T011 together (Contract Tests):
Task: "Contract test `customers.yaml` API in `backend/tests/contract/test_customers_api.py`"
Task: "Contract test `products.yaml` API in `backend/tests/contract/test_products_api.py`"
Task: "Contract test `sales_transactions.yaml` API in `backend/tests/contract/test_sales_transactions_api.py`"
Task: "Contract test `users.yaml` API in `backend/tests/contract/test_users_api.py`"

# Launch T012-T019 together (Integration Tests):
Task: "Integration test UC-001: Territory Sales Performance in `backend/tests/integration/test_territory_sales.py`"
Task: "Integration test UC-002: Product Analytics in `backend/tests/integration/test_product_analytics.py`"
Task: "Integration test UC-003: Market Intelligence in `backend/tests/integration/test_market_intelligence.py`"
Task: "Integration test UC-004: Sales Forecasting in `backend/tests/integration/test_sales_forecasting.py`"
Task: "Integration test UC-005: Regulatory Compliance Reporting in `backend/tests/integration/test_regulatory_compliance.py`"
Task: "Integration test Data Ingestion & Freshness in `backend/tests/integration/test_data_ingestion.py`"
Task: "Integration test User Management in `backend/tests/integration/test_user_management.py`"
Task: "Integration test API Access in `backend/tests/integration/test_api_access.py`"

# Launch T020-T023 together (Model Implementation):
Task: "Implement `SalesTransaction` model in `backend/src/models/sales_transaction.py`"
Task: "Implement `Product` model in `backend/src/models/product.py`"
Task: "Implement `Territory` model in `backend/src/models/territory.py`"
Task: "Implement `Customer` model in `backend/src/models/customer.py`"

# Launch T040-T043 together (Model Unit Tests):
Task: "Write unit tests for `SalesTransaction` model in `backend/tests/unit/test_sales_transaction_model.py`"
Task: "Write unit tests for `Product` model in `backend/tests/unit/test_product_model.py`"
Task: "Write unit tests for `Territory` model in `backend/tests/unit/test_territory_model.py`"
Task: "Write unit tests for `Customer` model in `backend/tests/unit/test_customer_model.py`"

# Launch T044-T047 together (Service Unit Tests):
Task: "Write unit tests for `CustomerService` in `backend/tests/unit/test_customer_service.py`"
Task: "Write unit tests for `ProductService` in `backend/tests/unit/test_product_service.py`"
Task: "Write unit tests for `SalesTransactionService` in `backend/tests/unit/test_sales_transaction_service.py`"
Task: "Write unit tests for `UserService` in `backend/tests/unit/test_user_service.py`"

# Launch T049-T050 together (Documentation):
Task: "Update API documentation (e.g., Swagger UI generation)"
Task: "Update user-facing documentation (e.g., `docs/PRD.md` or new user guide)"
```

## Notes
- [P] tasks = different files, no dependencies
- Verify tests fail before implementing
- Commit after each task
- Avoid: vague tasks, same file conflicts

## Task Generation Rules
*Applied during main() execution*

1. **From Contracts**:
   - Each contract file → contract test task [P]
   - Each endpoint → implementation task
   
2. **From Data Model**:
   - Each entity → model creation task [P]
   - Relationships → service layer tasks
   
3. **From User Stories**:
   - Each story → integration test [P]
   - Quickstart scenarios → validation tasks

4. **Ordering**:
   - Setup → Tests → Models → Services → Endpoints → Polish
   - Dependencies block parallel execution

## Validation Checklist
*GATE: Checked by main() before returning*

- [X] All contracts have corresponding tests
- [X] All entities have model tasks
- [X] All tests come before implementation
- [X] Parallel tasks truly independent
- [X] Each task specifies exact file path
- [X] No task modifies same file as another [P] task