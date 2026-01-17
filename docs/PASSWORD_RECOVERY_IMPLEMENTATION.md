# Password Recovery & Complexity Implementation

## Overview
This document details the implementation of the "Forgot Password" functionality and the enforcement of password complexity standards across the application. The system allows users to request a password reset link via email (mocked), verifies a time-limited token, and securely updates their credentials. Additionally, strict password complexity rules are enforced on both the client and server sides.

## Security Standards

### Password Complexity
Passwords must meet the following criteria to be accepted:
- **Length**: Minimum 8 characters.
- **Uppercase**: At least one uppercase letter (`A-Z`).
- **Lowercase**: At least one lowercase letter (`a-z`).
- **Special/Digit**: At least one digit (`0-9`) or special character (`!@#$%^&*...`).

### Recovery Tokens
- **Format**: JWT (JSON Web Token).
- **Expiry**: 15 minutes.
- **Type**: Dedicated `password_reset` type claim to prevent misuse of other tokens (like access tokens) for resetting passwords.
- **Security**: Signed with the application's secret key.

## Backend Implementation (`/backend`)

### 1. API Endpoints (`app/api/v1/endpoints/auth.py`)
- **`POST /auth/password-recovery/{email}`**: 
  - Checks if the user exists (returns generic success message to prevent user enumeration).
  - Generates a reset token.
  - Triggers the mock email service.
- **`POST /auth/reset-password`**:
  - Accepts a `PasswordResetConfirm` schema (token + new password).
  - Validates the new password against complexity rules.
  - Verifies the token signature and expiry.
  - Updates the user's password hash in the database.

### 2. Schemas & Validation (`app/schemas/user.py`)
- **`validate_password_strength`**: A shared validator function used by `UserCreate` and `PasswordResetConfirm`.
- **Pydantic Models**: Custom validators raise `422 Unprocessable Entity` errors if passwords are too weak.

### 3. Security Utilities (`app/core/security.py`)
- **`create_password_reset_token`**: Generates the specific 15-minute JWT.
- **`verify_password_reset_token`**: Decodes the token and validates the `type` claim.

### 4. Email Service (`app/utils/email.py`)
- Currently uses a **Mock Implementation**.
- Instead of sending an actual email, the system prints the reset link to the server console (stdout).
- **Format**: `http://localhost:5173/reset-password?token=<JWT_TOKEN>`

## Frontend Implementation (`/frontend`)

### 1. UI Components
- **`views/AuthPage.vue`**: 
  - Added "Forgot Password?" toggle.
  - Implemented "Recovery Mode" form.
  - Added real-time password validation feedback (red borders) during signup.
- **`views/ResetPasswordPage.vue`**: 
  - New route: `/reset-password`.
  - Captures the token from the URL query parameters.
  - Validates password matching and complexity before submission.

### 2. State Management (`stores/auth.js`)
- **`recoverPassword(email)`**: Handles the API call to request a link.
- **`resetPassword(token, newPassword)`**: Handles the final reset API call.

### 3. Shared Utilities (`utils/validation.js`)
- **`validatePassword`**: A pure JavaScript function mirroring the backend regex rules. used for immediate user feedback.

## Testing

### Backend Tests (`backend/tests/test_auth.py`)
- **Test Coverage**:
  - Rejection of weak passwords during signup.
  - Successful token generation.
  - Full reset flow (Request -> Token -> Reset -> Login with new password).
  - Invalidation of old passwords after reset.

### End-to-End Tests (`frontend/e2e`)
- **`auth.spec.js`**: Verifies login, signup, and validation UI feedback (red borders).
- **`reset_password.spec.js`**: Verifies the recovery request flow and the reset page logic (token handling, password matching).

## How to Verify (Manual)

1. **Start Services**:
   - Backend: `uvicorn app.main:app --reload`
   - Frontend: `npm run dev`

2. **Request Reset**:
   - Go to `/login` -> Click "Forgot your password?".
   - Enter your email and submit.

3. **Get Token**:
   - Check the terminal running the **Backend**.
   - Look for `[MOCK EMAIL] Link: http://localhost:5173/reset-password?token=...`
   - Copy and paste that link into your browser.

4. **Reset**:
   - Enter a strong password (e.g., `StrongPass1!`).
   - Submit. You should be redirected to login.
