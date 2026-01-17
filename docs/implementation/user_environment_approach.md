# User Environment Implementation Approach

## Overview
This document outlines the phased approach for implementing the logged-in user environment for the 3D Print Website. It details the architectural decisions, implementation steps, and testing strategies for each phase to ensure a robust and secure user experience.

## Core Architecture Decisions
*   **Layout:** Sidebar Dashboard (Persistent sidebar with navigation: Dashboard, Orders, Settings).
*   **Data Migration:** Existing orders will be linked to users based on email matching via a database migration.
*   **Checkout Flow:** Guest checkout will be preserved; `user_id` on orders will remain nullable.

## Phased Implementation Plan

### Phase 1: Foundation (Identity & Security)
**Goal:** Establish secure authentication state management and the basic user dashboard structure.

#### Implementation Tasks
*   **Backend:**
    *   **Dependency:** Create `app/api/deps.py` to handle `get_current_user` dependency using JWT validation.
    *   **Endpoint:** Create `GET /api/v1/users/me` endpoint to retrieve the authenticated user's profile.
    *   **Router:** Register the `users` router in `app/api/v1/__init__.py`.
*   **Frontend:**
    *   **Store:** Update `AuthStore` (`stores/auth.js`) to fetch the real user profile from the backend upon login and page reload.
    *   **Routing:** Implement Vue Router Guards (`router.beforeEach`) to protect `/dashboard` and related routes.
    *   **UI:** Create a `UserDashboard` layout component with the sidebar navigation.
    *   **Navigation:** Update the main `Header` component to display a user dropdown (Profile, Logout) instead of the "Login" button when authenticated.

#### Testing Strategy
*   **Backend Unit Tests (`pytest`):**
    *   Test `get_current_user` with valid, invalid, and expired tokens.
    *   Test `GET /users/me` ensures it returns the correct user data.
*   **Frontend E2E Tests (`Playwright`):**
    *   **Auth State:** Verify that logging in persists the session state across reloads.
    *   **Protection:** Verify that accessing `/dashboard` without a token redirects to `/login`.
    *   **Navigation:** Verify the Header updates correctly upon login/logout.

### Phase 2: Order Integration (History)
**Goal:** Connect users to their purchase history, including past orders.

#### Implementation Tasks
*   **Database:**
    *   **Migration:** Create an Alembic migration to add a nullable `user_id` (ForeignKey to `users.id`) to the `orders` table.
    *   **Data Script:** Include a post-migration script to iterate through existing orders and link them to users where `order.customer_email` matches `user.email`.
*   **Backend:**
    *   **Model:** Update `Order` model and Pydantic schemas to include `user_id`.
    *   **Logic:** Update `OrderService.create_order` to accept and save `user_id` if the user is authenticated.
    *   **Endpoint:** Create `GET /api/v1/users/me/orders` to fetch the authenticated user's order history.
*   **Frontend:**
    *   **View:** Create an `OrderHistory` view within the dashboard.
    *   **Integration:** Fetch and display the list of orders from the new endpoint.

#### Testing Strategy
*   **Migration Tests:**
    *   Create a test database state with unlinked orders, run the migration, and verify they are correctly linked to users with matching emails.
*   **Backend Integration Tests:**
    *   Verify that orders created by a logged-in user have the `user_id` set.
    *   Verify that `GET /users/me/orders` only returns orders belonging to that user.
*   **Frontend E2E Tests:**
    *   Verify a user can see their past orders in the dashboard.

### Phase 3: Profile Management & Settings
**Goal:** Allow users to manage their account details and security.

#### Implementation Tasks
*   **Backend:**
    *   **Endpoint:** Create `PUT /api/v1/users/me` to update user details.
    *   **Logic:** Allow updates to `full_name` and `password`. ensure password changes are hashed correctly.
*   **Frontend:**
    *   **View:** Create a `Settings` view in the dashboard.
    *   **Form:** Implement a form for updating profile information and changing the password.

#### Testing Strategy
*   **Backend Unit Tests:**
    *   Test profile updates reflect in the database.
    *   Test password changes allow login with the new password and fail with the old one.
    *   Test validation (e.g., invalid email formats, weak passwords).
*   **Frontend E2E Tests:**
    *   Verify a user can update their name and see the change reflected in the UI immediately.
