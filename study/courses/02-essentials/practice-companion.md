# IdentityIQ Essentials — Practice Companion

Original English guide pages grouped by exercise, with rewritten learning summaries. This companion preserves all 257 PDF pages, including reference pages and the appendix. It is not an answer key or a record of completed exercises. All actions described are for study in the supplied training VM; no VM, identity, access, logging or authentication changes were performed while preparing this book.

The source guide uses printed page numbers that restart at section boundaries. Captions below identify the **continuous PDF page number**, which can be used in the original handout.

## Training environment and course reference

Original cover, notices, contents, VM environment, shortcuts and keyboard notes. The displayed software versions and example credentials belong to this supplied training environment.

Related modules: 1, 4, 6. Source: [exercise-guide PDF pages 1–8](handouts/exercise-guide.pdf#page=1).

![Original English exercise guide, PDF page 1](images/exercise-001.png)

![Original English exercise guide, PDF page 2](images/exercise-002.png)

![Original English exercise guide, PDF page 3](images/exercise-003.png)

![Original English exercise guide, PDF page 4](images/exercise-004.png)

![Original English exercise guide, PDF page 5](images/exercise-005.png)

![Original English exercise guide, PDF page 6](images/exercise-006.png)

![Original English exercise guide, PDF page 7](images/exercise-007.png)

![Original English exercise guide, PDF page 8](images/exercise-008.png)

## Exercise 1.1 — Configure IdentityIQ

Confirm version and installation; explore the UI; redirect training email; configure work-item archives, retention and auditing; verify the intended audit evidence.

Related modules: 4, 5, 6. Source: [exercise-guide PDF pages 9–17](handouts/exercise-guide.pdf#page=9).

### 1. Confirm the installed version

Open the VM's IIQ Console shortcut, or open a terminal in the training installation's `WEB-INF/bin` directory and run `./iiq console -j`. The guide says `-j` enables command-history navigation. At the prompt, use `about` to inspect the version, patch and build, then `quit` to exit.

The exercise starts from the preinstalled environment. It does not require deleting the database or performing a manual installation first.

### 2. Explore the browser interface

Use the VM's IdentityIQ bookmark or the training URL and the credentials provided for that training environment. Explore the administrator's menus, Quicklink cards and dashboard widgets. The exercise asks the learner to identify the available menus and identity sections; these notes leave those checks for the learner rather than supplying an answer key.

Review the Quicklink categories for assigned work, access management and identity management. Open **Identities → Identity Warehouse**, then inspect the initial administrator's Identity Cube and its Application Accounts section. The gear menu provides product settings, help opens documentation, the notification indicator leads to assigned work, and the user menu includes preferences and logout.

### 3. Redirect training emails to a file

In **Gear → Global Settings → IdentityIQ Configuration → Email Settings**, the guide uses **Redirect to File**, with `/home/spadmin/logs/iiq_email.log` as the file and `iga@example.com` as the default sender. The purpose is to inspect generated notifications during development without delivering messages to real users. The same configuration area also contains email-template and SMTP-related settings.

### 4. Archive completed work items

Under **Work Items**, the exercise selects Approval, Form and Manual Action as work-item types to archive. A work item is an assigned unit of work; archiving preserves a historical representation after completion. The guide notes that multi-selection can depend on keyboard behavior in the hosted VM.

### 5. Configure training retention and transaction logging

Under **Miscellaneous**, the guide uses the following values for its exercise:

| Training configuration | Value |
| --- | --- |
| Snapshot deletion | 365 days |
| Task-result deletion | 90 days |
| Certification archiving | 720 days |
| Certification archive deletion | 1080 days |
| Syslog-event deletion | 30 days |
| Provisioning transaction maximum log level | Success |
| Provisioning transaction-event deletion | 90 days |

These are exercise values, not general retention recommendations. The guide specifically says Success is selected for training and mentions Retry or Failure as typical production logging choices in its context. Retention needs to reflect the deployment's own history and operational requirements. Save the configuration after reviewing the complete page.

### 6. Review and test audit configuration

Navigate to **Gear → Global Settings → Audit Configuration**. The guide reviews default actions such as lifecycle events, incorrect challenge-question answers and the start of an access request. It then has the learner enable Login Failure, Import File and Email Sent auditing, review the other available tabs and save.

The validation sequence is to sign out, make a deliberately unsuccessful login in the training VM, sign back in correctly, and search **Intelligence → Advanced Analytics → Audit**. Sorting by newest date should let the learner locate the failed-login event. This links configuration to observable evidence rather than treating the checkbox as the entire test.

For hosted-VM multi-selection difficulties, the guide describes using the VM's on-screen keyboard to hold Ctrl, making the selections, then releasing Ctrl and closing the keyboard.


![Original English exercise guide, PDF page 9](images/exercise-009.png)

![Original English exercise guide, PDF page 10](images/exercise-010.png)

![Original English exercise guide, PDF page 11](images/exercise-011.png)

![Original English exercise guide, PDF page 12](images/exercise-012.png)

![Original English exercise guide, PDF page 13](images/exercise-013.png)

![Original English exercise guide, PDF page 14](images/exercise-014.png)

![Original English exercise guide, PDF page 15](images/exercise-015.png)

![Original English exercise guide, PDF page 16](images/exercise-016.png)

![Original English exercise guide, PDF page 17](images/exercise-017.png)

## Exercise 1.2 — Create Identity Cubes

Define employee and contractor file applications; discover/review schemas; configure filtering/merging, classification and the training creation rule; aggregate and verify the cubes.

Related modules: 7. Source: [exercise-guide PDF pages 18–33](handouts/exercise-guide.pdf#page=18).

![Original English exercise guide, PDF page 18](images/exercise-018.png)

![Original English exercise guide, PDF page 19](images/exercise-019.png)

![Original English exercise guide, PDF page 20](images/exercise-020.png)

![Original English exercise guide, PDF page 21](images/exercise-021.png)

![Original English exercise guide, PDF page 22](images/exercise-022.png)

![Original English exercise guide, PDF page 23](images/exercise-023.png)

![Original English exercise guide, PDF page 24](images/exercise-024.png)

![Original English exercise guide, PDF page 25](images/exercise-025.png)

![Original English exercise guide, PDF page 26](images/exercise-026.png)

![Original English exercise guide, PDF page 27](images/exercise-027.png)

![Original English exercise guide, PDF page 28](images/exercise-028.png)

![Original English exercise guide, PDF page 29](images/exercise-029.png)

![Original English exercise guide, PDF page 30](images/exercise-030.png)

![Original English exercise guide, PDF page 31](images/exercise-031.png)

![Original English exercise guide, PDF page 32](images/exercise-032.png)

![Original English exercise guide, PDF page 33](images/exercise-033.png)

## Exercise 1.3 — Populate Identity Cubes

Map standard/extended attributes, establish account and manager correlation, refresh identities, configure display fields and investigate data quality.

Related modules: 8. Source: [exercise-guide PDF pages 34–47](handouts/exercise-guide.pdf#page=34).

![Original English exercise guide, PDF page 34](images/exercise-034.png)

![Original English exercise guide, PDF page 35](images/exercise-035.png)

![Original English exercise guide, PDF page 36](images/exercise-036.png)

![Original English exercise guide, PDF page 37](images/exercise-037.png)

![Original English exercise guide, PDF page 38](images/exercise-038.png)

![Original English exercise guide, PDF page 39](images/exercise-039.png)

![Original English exercise guide, PDF page 40](images/exercise-040.png)

![Original English exercise guide, PDF page 41](images/exercise-041.png)

![Original English exercise guide, PDF page 42](images/exercise-042.png)

![Original English exercise guide, PDF page 43](images/exercise-043.png)

![Original English exercise guide, PDF page 44](images/exercise-044.png)

![Original English exercise guide, PDF page 45](images/exercise-045.png)

![Original English exercise guide, PDF page 46](images/exercise-046.png)

![Original English exercise guide, PDF page 47](images/exercise-047.png)

## Exercise 1.4 — Organize Identities

Create populations and group factories, establish workgroups and capabilities, configure notification ownership and verify the intended administrative access.

Related modules: 9, 10. Source: [exercise-guide PDF pages 48–60](handouts/exercise-guide.pdf#page=48).

![Original English exercise guide, PDF page 48](images/exercise-048.png)

![Original English exercise guide, PDF page 49](images/exercise-049.png)

![Original English exercise guide, PDF page 50](images/exercise-050.png)

![Original English exercise guide, PDF page 51](images/exercise-051.png)

![Original English exercise guide, PDF page 52](images/exercise-052.png)

![Original English exercise guide, PDF page 53](images/exercise-053.png)

![Original English exercise guide, PDF page 54](images/exercise-054.png)

![Original English exercise guide, PDF page 55](images/exercise-055.png)

![Original English exercise guide, PDF page 56](images/exercise-056.png)

![Original English exercise guide, PDF page 57](images/exercise-057.png)

![Original English exercise guide, PDF page 58](images/exercise-058.png)

![Original English exercise guide, PDF page 59](images/exercise-059.png)

![Original English exercise guide, PDF page 60](images/exercise-060.png)

## Exercise 1.5 — Define LDAP Application

Define and preview LDAP accounts/groups, test connector reads, set correlation and the email source, aggregate and inspect linked accounts and catalog entries.

Related modules: 11, 12, 13. Source: [exercise-guide PDF pages 61–74](handouts/exercise-guide.pdf#page=61).

![Original English exercise guide, PDF page 61](images/exercise-061.png)

![Original English exercise guide, PDF page 62](images/exercise-062.png)

![Original English exercise guide, PDF page 63](images/exercise-063.png)

![Original English exercise guide, PDF page 64](images/exercise-064.png)

![Original English exercise guide, PDF page 65](images/exercise-065.png)

![Original English exercise guide, PDF page 66](images/exercise-066.png)

![Original English exercise guide, PDF page 67](images/exercise-067.png)

![Original English exercise guide, PDF page 68](images/exercise-068.png)

![Original English exercise guide, PDF page 69](images/exercise-069.png)

![Original English exercise guide, PDF page 70](images/exercise-070.png)

![Original English exercise guide, PDF page 71](images/exercise-071.png)

![Original English exercise guide, PDF page 72](images/exercise-072.png)

![Original English exercise guide, PDF page 73](images/exercise-073.png)

![Original English exercise guide, PDF page 74](images/exercise-074.png)

## Exercise 1.6 — Enable Pass-Through Authentication

Configure the training LDAP pass-through path, test sign-in and study the related forgot-password exercise. These settings were not applied by the agent.

Related modules: 9. Source: [exercise-guide PDF pages 75–79](handouts/exercise-guide.pdf#page=75).

![Original English exercise guide, PDF page 75](images/exercise-075.png)

![Original English exercise guide, PDF page 76](images/exercise-076.png)

![Original English exercise guide, PDF page 77](images/exercise-077.png)

![Original English exercise guide, PDF page 78](images/exercise-078.png)

![Original English exercise guide, PDF page 79](images/exercise-079.png)

## Section Two — overview and contents

Reference page numbering for the business-application, task-sequencing and data-maintenance exercises.

Related modules: 11, 13, 14. Source: [exercise-guide PDF pages 80–81](handouts/exercise-guide.pdf#page=80).

![Original English exercise guide, PDF page 80](images/exercise-080.png)

![Original English exercise guide, PDF page 81](images/exercise-081.png)

## Exercise 2.1 — Define Business Applications

Configure Time Tracking and Chat, import other definitions, update ownership/account mappings and UI display, then configure Rapid Setup account interpretation.

Related modules: 11, 13. Source: [exercise-guide PDF pages 82–93](handouts/exercise-guide.pdf#page=82).

![Original English exercise guide, PDF page 82](images/exercise-082.png)

![Original English exercise guide, PDF page 83](images/exercise-083.png)

![Original English exercise guide, PDF page 84](images/exercise-084.png)

![Original English exercise guide, PDF page 85](images/exercise-085.png)

![Original English exercise guide, PDF page 86](images/exercise-086.png)

![Original English exercise guide, PDF page 87](images/exercise-087.png)

![Original English exercise guide, PDF page 88](images/exercise-088.png)

![Original English exercise guide, PDF page 89](images/exercise-089.png)

![Original English exercise guide, PDF page 90](images/exercise-090.png)

![Original English exercise guide, PDF page 91](images/exercise-091.png)

![Original English exercise guide, PDF page 92](images/exercise-092.png)

![Original English exercise guide, PDF page 93](images/exercise-093.png)

## Exercise 2.2 — Aggregation and Refresh Tasks

Build and schedule a sequential task, observe active/scheduled/completed results, target a refresh with query criteria and inspect an identity report.

Related modules: 13, 15. Source: [exercise-guide PDF pages 94–103](handouts/exercise-guide.pdf#page=94).

![Original English exercise guide, PDF page 94](images/exercise-094.png)

![Original English exercise guide, PDF page 95](images/exercise-095.png)

![Original English exercise guide, PDF page 96](images/exercise-096.png)

![Original English exercise guide, PDF page 97](images/exercise-097.png)

![Original English exercise guide, PDF page 98](images/exercise-098.png)

![Original English exercise guide, PDF page 99](images/exercise-099.png)

![Original English exercise guide, PDF page 100](images/exercise-100.png)

![Original English exercise guide, PDF page 101](images/exercise-101.png)

![Original English exercise guide, PDF page 102](images/exercise-102.png)

![Original English exercise guide, PDF page 103](images/exercise-103.png)

## Exercise 2.3 — Uncorrelated Accounts and Data Maintenance

Report and investigate unmatched accounts, correlate verified owners, prune empty cubes, and export/edit/import entitlement metadata.

Related modules: 12, 14. Source: [exercise-guide PDF pages 104–111](handouts/exercise-guide.pdf#page=104).

![Original English exercise guide, PDF page 104](images/exercise-104.png)

![Original English exercise guide, PDF page 105](images/exercise-105.png)

![Original English exercise guide, PDF page 106](images/exercise-106.png)

![Original English exercise guide, PDF page 107](images/exercise-107.png)

![Original English exercise guide, PDF page 108](images/exercise-108.png)

![Original English exercise guide, PDF page 109](images/exercise-109.png)

![Original English exercise guide, PDF page 110](images/exercise-110.png)

![Original English exercise guide, PDF page 111](images/exercise-111.png)

## Section Three — overview and contents

Reference pages for operations, diagnostics, policies, certification and roles.

Related modules: 15, 16, 17, 18, 19, 20. Source: [exercise-guide PDF pages 112–113](handouts/exercise-guide.pdf#page=112).

![Original English exercise guide, PDF page 112](images/exercise-112.png)

![Original English exercise guide, PDF page 113](images/exercise-113.png)

## Exercise 3.1 — Task Management Options

Compare delta processing, run-rule and maintenance tasks, test failure notification and inspect the Administrator Console. Disruptive service-stop steps are original training instructions only.

Related modules: 15. Source: [exercise-guide PDF pages 114–123](handouts/exercise-guide.pdf#page=114).

![Original English exercise guide, PDF page 114](images/exercise-114.png)

![Original English exercise guide, PDF page 115](images/exercise-115.png)

![Original English exercise guide, PDF page 116](images/exercise-116.png)

![Original English exercise guide, PDF page 117](images/exercise-117.png)

![Original English exercise guide, PDF page 118](images/exercise-118.png)

![Original English exercise guide, PDF page 119](images/exercise-119.png)

![Original English exercise guide, PDF page 120](images/exercise-120.png)

![Original English exercise guide, PDF page 121](images/exercise-121.png)

![Original English exercise guide, PDF page 122](images/exercise-122.png)

![Original English exercise guide, PDF page 123](images/exercise-123.png)

## Exercise 3.2 — Explore Log4j

Enable focused trace/debug logging in the lab, run a known task, inspect output and compare Rapid Setup logger settings.

Related modules: 16. Source: [exercise-guide PDF pages 124–127](handouts/exercise-guide.pdf#page=124).

![Original English exercise guide, PDF page 124](images/exercise-124.png)

![Original English exercise guide, PDF page 125](images/exercise-125.png)

![Original English exercise guide, PDF page 126](images/exercise-126.png)

![Original English exercise guide, PDF page 127](images/exercise-127.png)

## Exercise 3.3 — Debug and Console

Inspect debug views and object XML, create/test a training rule, explore help and commands and study object export/import portability.

Related modules: 17. Source: [exercise-guide PDF pages 128–137](handouts/exercise-guide.pdf#page=128).

![Original English exercise guide, PDF page 128](images/exercise-128.png)

![Original English exercise guide, PDF page 129](images/exercise-129.png)

![Original English exercise guide, PDF page 130](images/exercise-130.png)

![Original English exercise guide, PDF page 131](images/exercise-131.png)

![Original English exercise guide, PDF page 132](images/exercise-132.png)

![Original English exercise guide, PDF page 133](images/exercise-133.png)

![Original English exercise guide, PDF page 134](images/exercise-134.png)

![Original English exercise guide, PDF page 135](images/exercise-135.png)

![Original English exercise guide, PDF page 136](images/exercise-136.png)

![Original English exercise guide, PDF page 137](images/exercise-137.png)

## Exercise 3.4 — Define Policies

Define and simulate the entitlement SoD policy, enable checking and inspect violations, work items, notifications and troubleshooting checks.

Related modules: 18. Source: [exercise-guide PDF pages 138–143](handouts/exercise-guide.pdf#page=138).

![Original English exercise guide, PDF page 138](images/exercise-138.png)

![Original English exercise guide, PDF page 139](images/exercise-139.png)

![Original English exercise guide, PDF page 140](images/exercise-140.png)

![Original English exercise guide, PDF page 141](images/exercise-141.png)

![Original English exercise guide, PDF page 142](images/exercise-142.png)

![Original English exercise guide, PDF page 143](images/exercise-143.png)

## Exercise 3.5 — Certify Access

Generate and inspect a staged targeted campaign, activate it, study reviewer/workgroup decisions and sign-off, and observe maintenance-driven state changes.

Related modules: 19. Source: [exercise-guide PDF pages 144–151](handouts/exercise-guide.pdf#page=144).

![Original English exercise guide, PDF page 144](images/exercise-144.png)

![Original English exercise guide, PDF page 145](images/exercise-145.png)

![Original English exercise guide, PDF page 146](images/exercise-146.png)

![Original English exercise guide, PDF page 147](images/exercise-147.png)

![Original English exercise guide, PDF page 148](images/exercise-148.png)

![Original English exercise guide, PDF page 149](images/exercise-149.png)

![Original English exercise guide, PDF page 150](images/exercise-150.png)

![Original English exercise guide, PDF page 151](images/exercise-151.png)

## Exercise 3.6 — Business, IT and Birthright Roles

Inspect role relationships, refresh assignment/detection, review provisioning evidence and define joiner birthright access.

Related modules: 20. Source: [exercise-guide PDF pages 152–160](handouts/exercise-guide.pdf#page=152).

![Original English exercise guide, PDF page 152](images/exercise-152.png)

![Original English exercise guide, PDF page 153](images/exercise-153.png)

![Original English exercise guide, PDF page 154](images/exercise-154.png)

![Original English exercise guide, PDF page 155](images/exercise-155.png)

![Original English exercise guide, PDF page 156](images/exercise-156.png)

![Original English exercise guide, PDF page 157](images/exercise-157.png)

![Original English exercise guide, PDF page 158](images/exercise-158.png)

![Original English exercise guide, PDF page 159](images/exercise-159.png)

![Original English exercise guide, PDF page 160](images/exercise-160.png)

## Section Four — overview and contents

Reference pages for provisioning configuration, lifecycle events and user-driven changes.

Related modules: 21, 23, 25, 26, 27, 28, 29, 30. Source: [exercise-guide PDF pages 161–163](handouts/exercise-guide.pdf#page=161).

![Original English exercise guide, PDF page 161](images/exercise-161.png)

![Original English exercise guide, PDF page 162](images/exercise-162.png)

![Original English exercise guide, PDF page 163](images/exercise-163.png)

## Exercise 4.1 — Prepare Applications for Provisioning

Review and update LDAP create-account fields; import policies; attach JDBC provisioning rules and inspect supporting dependencies.

Related modules: 21. Source: [exercise-guide PDF pages 164–170](handouts/exercise-guide.pdf#page=164).

![Original English exercise guide, PDF page 164](images/exercise-164.png)

![Original English exercise guide, PDF page 165](images/exercise-165.png)

![Original English exercise guide, PDF page 166](images/exercise-166.png)

![Original English exercise guide, PDF page 167](images/exercise-167.png)

![Original English exercise guide, PDF page 168](images/exercise-168.png)

![Original English exercise guide, PDF page 169](images/exercise-169.png)

![Original English exercise guide, PDF page 170](images/exercise-170.png)

## Exercise 4.2 — Joiner Lifecycle Event

Customize training notifications, enable global and per-application joiner behavior, add sample source records, aggregate/process events and verify requests, transactions, identities, audits and emails.

Related modules: 23, 24. Source: [exercise-guide PDF pages 171–182](handouts/exercise-guide.pdf#page=171).

![Original English exercise guide, PDF page 171](images/exercise-171.png)

![Original English exercise guide, PDF page 172](images/exercise-172.png)

![Original English exercise guide, PDF page 173](images/exercise-173.png)

![Original English exercise guide, PDF page 174](images/exercise-174.png)

![Original English exercise guide, PDF page 175](images/exercise-175.png)

![Original English exercise guide, PDF page 176](images/exercise-176.png)

![Original English exercise guide, PDF page 177](images/exercise-177.png)

![Original English exercise guide, PDF page 178](images/exercise-178.png)

![Original English exercise guide, PDF page 179](images/exercise-179.png)

![Original English exercise guide, PDF page 180](images/exercise-180.png)

![Original English exercise guide, PDF page 181](images/exercise-181.png)

![Original English exercise guide, PDF page 182](images/exercise-182.png)

## Exercise 4.3 — Mover Lifecycle Event

Define trigger and certification behavior, change the training identity data, inspect the staged review and request/audit evidence, then return diagnostic logging to its intended state.

Related modules: 23, 24. Source: [exercise-guide PDF pages 183–191](handouts/exercise-guide.pdf#page=183).

![Original English exercise guide, PDF page 183](images/exercise-183.png)

![Original English exercise guide, PDF page 184](images/exercise-184.png)

![Original English exercise guide, PDF page 185](images/exercise-185.png)

![Original English exercise guide, PDF page 186](images/exercise-186.png)

![Original English exercise guide, PDF page 187](images/exercise-187.png)

![Original English exercise guide, PDF page 188](images/exercise-188.png)

![Original English exercise guide, PDF page 189](images/exercise-189.png)

![Original English exercise guide, PDF page 190](images/exercise-190.png)

![Original English exercise guide, PDF page 191](images/exercise-191.png)

## Exercise 4.4 — Configure Access Requests

Update requestability; clone/configure the approval workflow; select it for LCM; configure Quicklink Population permissions and search behavior.

Related modules: 25, 26, 27. Source: [exercise-guide PDF pages 192–199](handouts/exercise-guide.pdf#page=192).

![Original English exercise guide, PDF page 192](images/exercise-192.png)

![Original English exercise guide, PDF page 193](images/exercise-193.png)

![Original English exercise guide, PDF page 194](images/exercise-194.png)

![Original English exercise guide, PDF page 195](images/exercise-195.png)

![Original English exercise guide, PDF page 196](images/exercise-196.png)

![Original English exercise guide, PDF page 197](images/exercise-197.png)

![Original English exercise guide, PDF page 198](images/exercise-198.png)

![Original English exercise guide, PDF page 199](images/exercise-199.png)

## Exercise 4.5 — Test Access Requests and Attachments

Follow VPN request approvals, target confirmation and maintenance; study retry behavior during a training outage, preventive policies, optional roles and PDF attachment evidence.

Related modules: 22, 26, 27. Source: [exercise-guide PDF pages 200–219](handouts/exercise-guide.pdf#page=200).

![Original English exercise guide, PDF page 200](images/exercise-200.png)

![Original English exercise guide, PDF page 201](images/exercise-201.png)

![Original English exercise guide, PDF page 202](images/exercise-202.png)

![Original English exercise guide, PDF page 203](images/exercise-203.png)

![Original English exercise guide, PDF page 204](images/exercise-204.png)

![Original English exercise guide, PDF page 205](images/exercise-205.png)

![Original English exercise guide, PDF page 206](images/exercise-206.png)

![Original English exercise guide, PDF page 207](images/exercise-207.png)

![Original English exercise guide, PDF page 208](images/exercise-208.png)

![Original English exercise guide, PDF page 209](images/exercise-209.png)

![Original English exercise guide, PDF page 210](images/exercise-210.png)

![Original English exercise guide, PDF page 211](images/exercise-211.png)

![Original English exercise guide, PDF page 212](images/exercise-212.png)

![Original English exercise guide, PDF page 213](images/exercise-213.png)

![Original English exercise guide, PDF page 214](images/exercise-214.png)

![Original English exercise guide, PDF page 215](images/exercise-215.png)

![Original English exercise guide, PDF page 216](images/exercise-216.png)

![Original English exercise guide, PDF page 217](images/exercise-217.png)

![Original English exercise guide, PDF page 218](images/exercise-218.png)

![Original English exercise guide, PDF page 219](images/exercise-219.png)

## Exercise 4.7 — Create Identity Provisioning Policy

Compare default and configured forms, import the supplied identity provisioning policy and inspect the created identity/event. The presentation preview calls this Exercise 6; this guide labels it 4.7.

Related modules: 28. Source: [exercise-guide PDF pages 220–225](handouts/exercise-guide.pdf#page=220).

![Original English exercise guide, PDF page 220](images/exercise-220.png)

![Original English exercise guide, PDF page 221](images/exercise-221.png)

![Original English exercise guide, PDF page 222](images/exercise-222.png)

![Original English exercise guide, PDF page 223](images/exercise-223.png)

![Original English exercise guide, PDF page 224](images/exercise-224.png)

![Original English exercise guide, PDF page 225](images/exercise-225.png)

## Exercise 4.8 — Attribute Synchronization

Add email target mappings, inspect source/account values, run a synchronization refresh and investigate the resulting manual work item.

Related modules: 29. Source: [exercise-guide PDF pages 226–229](handouts/exercise-guide.pdf#page=226).

![Original English exercise guide, PDF page 226](images/exercise-226.png)

![Original English exercise guide, PDF page 227](images/exercise-227.png)

![Original English exercise guide, PDF page 228](images/exercise-228.png)

![Original English exercise guide, PDF page 229](images/exercise-229.png)

## Exercise 4.9 — Leaver and Immediate Termination

Configure global/per-application leaver behavior, study the inactive-source transition and its results, then compare immediate termination. No account was terminated while preparing the book.

Related modules: 23, 30. Source: [exercise-guide PDF pages 230–239](handouts/exercise-guide.pdf#page=230).

![Original English exercise guide, PDF page 230](images/exercise-230.png)

![Original English exercise guide, PDF page 231](images/exercise-231.png)

![Original English exercise guide, PDF page 232](images/exercise-232.png)

![Original English exercise guide, PDF page 233](images/exercise-233.png)

![Original English exercise guide, PDF page 234](images/exercise-234.png)

![Original English exercise guide, PDF page 235](images/exercise-235.png)

![Original English exercise guide, PDF page 236](images/exercise-236.png)

![Original English exercise guide, PDF page 237](images/exercise-237.png)

![Original English exercise guide, PDF page 238](images/exercise-238.png)

![Original English exercise guide, PDF page 239](images/exercise-239.png)

## Appendix — synonyms, Linux, installation and lab tools

The original appendix contains terminology, basic commands, manual installation/patch/e-fix procedures, target-side provisioning verification and Lab Reset instructions. These pages are retained; their commands were not executed or independently validated for another environment.

Related modules: 6, 17, 31, 32, 33. Source: [exercise-guide PDF pages 240–257](handouts/exercise-guide.pdf#page=240).

![Original English exercise guide, PDF page 240](images/exercise-240.png)

![Original English exercise guide, PDF page 241](images/exercise-241.png)

![Original English exercise guide, PDF page 242](images/exercise-242.png)

![Original English exercise guide, PDF page 243](images/exercise-243.png)

![Original English exercise guide, PDF page 244](images/exercise-244.png)

![Original English exercise guide, PDF page 245](images/exercise-245.png)

![Original English exercise guide, PDF page 246](images/exercise-246.png)

![Original English exercise guide, PDF page 247](images/exercise-247.png)

![Original English exercise guide, PDF page 248](images/exercise-248.png)

![Original English exercise guide, PDF page 249](images/exercise-249.png)

![Original English exercise guide, PDF page 250](images/exercise-250.png)

![Original English exercise guide, PDF page 251](images/exercise-251.png)

![Original English exercise guide, PDF page 252](images/exercise-252.png)

![Original English exercise guide, PDF page 253](images/exercise-253.png)

![Original English exercise guide, PDF page 254](images/exercise-254.png)

![Original English exercise guide, PDF page 255](images/exercise-255.png)

![Original English exercise guide, PDF page 256](images/exercise-256.png)

![Original English exercise guide, PDF page 257](images/exercise-257.png)

