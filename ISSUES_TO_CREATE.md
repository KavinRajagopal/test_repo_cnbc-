# Issues to Create for Testing

Create these 7 issues in your GitHub repository to test the automated test generation tool.

Go to: https://github.com/KavinRajagopal/test_repo_cnbc-/issues/new

---

## Issue #1: Calculator Division Tests

**Title:** Add comprehensive tests for calculator division

**Body:**
```markdown
Implement thorough testing for the calculator's division functionality including edge cases and error handling.

## Acceptance Criteria

- AC1: Division of positive numbers returns correct result
- AC2: Division by zero raises ValueError with appropriate message
- AC3: Division of negative numbers works correctly
- AC4: Division resulting in float is handled properly
- AC5: Division of zero by any number returns zero

## Related Files
- `src/calculator.py` - Calculator.divide() method

## Technical Notes
- Use pytest framework
- Use calculator fixture from conftest.py
- Follow test patterns in test_example.py
```

**Labels:** `needs-tests`, `automated-testing`

---

## Issue #2: Email Validation Tests

**Title:** Create comprehensive tests for email validation

**Body:**
```markdown
Add tests to validate the email validation function handles various email formats correctly.

## Acceptance Criteria

- AC1: Valid email formats pass validation (user@example.com)
- AC2: Invalid emails without @ symbol fail validation
- AC3: Emails without domain extension fail validation
- AC4: Emails with special characters in local part are handled correctly
- AC5: Empty string returns False
- AC6: Emails with multiple @ symbols fail validation
- AC7: Email with valid subdomains work (user@mail.example.com)

## Related Files
- `src/user.py` - validate_email() function

## Test Cases to Cover
**Valid:** john.doe@example.com, user+tag@domain.co.uk, test@sub.example.com
**Invalid:** @example.com, user@, user, user@@domain.com, "", user@domain
```

**Labels:** `needs-tests`, `validation`

---

## Issue #3: Password Validation Tests

**Title:** Test password validation requirements

**Body:**
```markdown
Create comprehensive tests to ensure password validation enforces all security requirements.

## Acceptance Criteria

- AC1: Password with 8+ characters, uppercase, and digit passes validation
- AC2: Password shorter than 8 characters fails
- AC3: Password without uppercase letter fails
- AC4: Password without digit fails
- AC5: Password meeting all requirements returns True
- AC6: Edge case: exactly 8 characters with requirements passes
- AC7: Empty string or None fails validation

## Related Files
- `src/user.py` - validate_password() function

## Security Requirements
- Minimum 8 characters
- At least 1 uppercase letter
- At least 1 digit
```

**Labels:** `needs-tests`, `security`, `validation`

---

## Issue #4: User Registration Tests

**Title:** Implement tests for user registration flow

**Body:**
```markdown
Test the complete user registration flow including validation, user creation, and error handling.

## Acceptance Criteria

- AC1: Valid registration creates a new user with correct attributes
- AC2: Registration with invalid email raises ValueError
- AC3: Registration with weak password raises ValueError
- AC4: Duplicate email registration raises ValueError with appropriate message
- AC5: Newly registered user is initially inactive (is_active=False)
- AC6: Registered user is stored in users dictionary with email as key
- AC7: Optional name parameter works correctly

## Related Files
- `src/auth.py` - AuthService.register() method
- `src/user.py` - User model

## Additional Context
Use the auth_service fixture from conftest.py for test isolation
```

**Labels:** `needs-tests`, `authentication`

---

## Issue #5: User Login Authentication Tests

**Title:** Add comprehensive user login tests

**Body:**
```markdown
Test user login functionality including success scenarios, authentication failures, and session management.

## Acceptance Criteria

- AC1: Valid credentials for active user return a session token
- AC2: Invalid email raises AuthenticationError
- AC3: Wrong password raises AuthenticationError with appropriate message
- AC4: Inactive user cannot login (raises AuthenticationError)
- AC5: Session token is stored in sessions dictionary
- AC6: Session token format is consistent and includes user email
- AC7: Multiple logins for same user create different sessions

## Related Files
- `src/auth.py` - AuthService.login() method

## Test Scenarios
- Happy path: activated user with correct credentials
- Edge cases: inactive user, wrong password, non-existent user, empty credentials
```

**Labels:** `needs-tests`, `authentication`, `security`

---

## Issue #6: User Logout Tests

**Title:** Test user logout and session cleanup

**Body:**
```markdown
Ensure logout properly cleans up user sessions and handles edge cases gracefully.

## Acceptance Criteria

- AC1: Logout removes session token from sessions dictionary
- AC2: Logout with valid token succeeds without errors
- AC3: Logout with invalid token doesn't raise error
- AC4: After logout, session token is no longer in sessions
- AC5: Multiple logouts with same token don't cause issues
- AC6: Logout doesn't affect other active sessions

## Related Files
- `src/auth.py` - AuthService.logout() method

## Additional Context
Test should verify session cleanup is complete and doesn't affect other users
```

**Labels:** `needs-tests`, `authentication`

---

## Issue #7: User Role Management Tests

**Title:** Test user role management and validation

**Body:**
```markdown
Test the user role assignment functionality including validation of valid roles.

## Acceptance Criteria

- AC1: New user defaults to "user" role
- AC2: set_role() accepts valid roles (user, admin, moderator)
- AC3: set_role() with invalid role raises ValueError
- AC4: Role changes are persisted correctly
- AC5: User can change roles multiple times
- AC6: Error message for invalid role includes valid options

## Related Files
- `src/user.py` - User.set_role() method

## Valid Roles
- user (default)
- admin
- moderator
```

**Labels:** `needs-tests`, `user-management`

---

## Quick Create Script (Optional)

If you have GitHub CLI installed, you can use this script to create all issues:

```bash
#!/bin/bash

gh issue create --title "Add comprehensive tests for calculator division" \
  --body-file issue1.md --label "needs-tests,automated-testing"

gh issue create --title "Create comprehensive tests for email validation" \
  --body-file issue2.md --label "needs-tests,validation"

gh issue create --title "Test password validation requirements" \
  --body-file issue3.md --label "needs-tests,security,validation"

gh issue create --title "Implement tests for user registration flow" \
  --body-file issue4.md --label "needs-tests,authentication"

gh issue create --title "Add comprehensive user login tests" \
  --body-file issue5.md --label "needs-tests,authentication,security"

gh issue create --title "Test user logout and session cleanup" \
  --body-file issue6.md --label "needs-tests,authentication"

gh issue create --title "Test user role management and validation" \
  --body-file issue7.md --label "needs-tests,user-management"
```

---

## Next Steps

1. Create each issue manually in GitHub (copy-paste from above)
2. Or save each body as separate files and use the GitHub CLI script
3. Update your test authoring tool `.env` file:
   ```
   GITHUB_REPO=KavinRajagopal/test_repo_cnbc-
   ```
4. Start generating tests!

```bash
curl -X POST http://localhost:8000/github/generate-tests \
  -H "Content-Type: application/json" \
  -d '{"issue_number": 1}'
```

