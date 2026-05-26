# Release Plan — Version 1.0

## 1. Release Scope
- Feature A: User Login Module
- Feature B: Dashboard UI
- Feature C: API Integration

## 2. Change Requests
| CR ID | Description         | Priority | Status   |
|-------|---------------------|----------|----------|
| CR-01 | Add login page      | High     | Approved |
| CR-02 | Dashboard charts    | Medium   | Approved |
| CR-03 | Email notifications | Low      | Deferred |

## 3. Risk Assessment
| Risk                  | Likelihood | Impact | Mitigation                  |
|-----------------------|------------|--------|-----------------------------|
| DB connection failure | Medium     | High   | Use backup DB               |
| Login bug in prod     | Low        | High   | Extra QA testing            |
| Deployment downtime   | Low        | Medium | Schedule off-peak hours     |

## 4. Rollback Strategy
- Keep backup of current production database
- Maintain previous version for instant rollback
- Rollback command: git checkout v0.9
- Notify team if rollback is triggered
