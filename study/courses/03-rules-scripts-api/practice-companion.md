# Rules, Scripts, and API — Exercise Companion

Rewritten exercise instructions followed by all 37 original English guide pages. The pages preserve the exact examples, diagrams, screenshots and practice prompts. They are not evidence of a completed lab. No IdentityIQ objects, requests, capabilities, logs, services or reviews were changed while preparing the material.

## Course and exercise reference

The original guide cover, notices, contents and environment notes. Starter artifacts contain marked insertion points. The exercises assume the supplied training VM; their example passwords and software state are not instructions for other systems.

Related reader topics: 1. [Original guide PDF pages 1–5](handouts/exercise-guide.pdf#page=1).

![Original English exercise guide, PDF page 1](images/exercise-001.png)

![Original English exercise guide, PDF page 2](images/exercise-002.png)

![Original English exercise guide, PDF page 3](images/exercise-003.png)

![Original English exercise guide, PDF page 4](images/exercise-004.png)

![Original English exercise guide, PDF page 5](images/exercise-005.png)

## Exercise 1 — Explore and Execute Rules and Scripts

1. Inspect the HR Employees Creation rule's description, arguments and source before changing anything.
2. Examine the PRISM create-account policy's Login ID calculation. The exercise moves the reusable logic from an inline script into a named rule, then tests the request path and resulting account name.
3. Import the identity-lookup rule, inspect its XML in the Console and run it with the supplied argument-map file.
4. Import the utility library, inspect its manager-email function and the calling rule's ReferencedRules metadata, then rerun the lookup.
5. Create a Run Rule task with the intended rule/configuration. The guide's `identityName,Adam.Kennedy` value has no space after the comma.
6. The supplied task template needs a Returns entry so its result appears in Task Results. The argument name is `Result: `, including the trailing space. Preserve that exact training detail when following the original page.
7. Compare the returned task result with standard-output logging. Console standard output and web-application server standard output are different locations.

The guide explains that a task-provided argument map is nested under `config`; a Console-only rule can instead use a simpler direct map if its code and arguments file agree. These are study steps, not imports, approvals or account changes performed by the agent.

Related reader topics: 2. [Original guide PDF pages 6–14](handouts/exercise-guide.pdf#page=6).

![Original English exercise guide, PDF page 6](images/exercise-006.png)

![Original English exercise guide, PDF page 7](images/exercise-007.png)

![Original English exercise guide, PDF page 8](images/exercise-008.png)

![Original English exercise guide, PDF page 9](images/exercise-009.png)

![Original English exercise guide, PDF page 10](images/exercise-010.png)

![Original English exercise guide, PDF page 11](images/exercise-011.png)

![Original English exercise guide, PDF page 12](images/exercise-012.png)

![Original English exercise guide, PDF page 13](images/exercise-013.png)

![Original English exercise guide, PDF page 14](images/exercise-014.png)

## Exercise 2 — Using the API

1. Inspect the Application ownerContact extended attribute and the starter rule's existing loop over applications.
2. Use Application/SailPointObject JavaDoc to find the owner getter and Identity JavaDoc to find the email getter.
3. Set the application extension by attribute name, then use the standalone rule's supplied persistence/transaction structure.
4. Import/run the rule in the training environment and verify the application Details field rather than expecting every operation to return a visible dialog value.
5. In the Creation-rule activity, inspect the ResourceObject argument and apply the supplied department-dependent training logic.
6. Introduce the new employee records specified by the exercise, aggregate and compare the resulting User Rights tabs.

The Creation hook affects newly created identities in this scenario; re-running aggregation does not retroactively apply that same creation event to every existing identity. The example's administrator-capability assignment is an instructional lab scenario, not a general access-design recommendation. No capabilities were granted while preparing the notes.

Related reader topics: 3. [Original guide PDF pages 15–19](handouts/exercise-guide.pdf#page=15).

![Original English exercise guide, PDF page 15](images/exercise-015.png)

![Original English exercise guide, PDF page 16](images/exercise-016.png)

![Original English exercise guide, PDF page 17](images/exercise-017.png)

![Original English exercise guide, PDF page 18](images/exercise-018.png)

![Original English exercise guide, PDF page 19](images/exercise-019.png)

## Exercise 3 — SailPointContext, Searches and Filters

1. Verify the sample identity's original Accounting/London values.
2. Inspect the starter rule's QueryOptions and projection-properties variables.
3. Add the guide's explicit `qo.setCloneResults(true)` correction. The guide warns that this line is absent from the supplied solution.
4. Build department and location filters and combine them with AND, then add the result to QueryOptions.
5. Search for IDs using the matching overload and retrieve one Identity at a time by its identifier.
6. Follow the supplied rule's change/save/transaction structure in the lab, then confirm the intended identity change.

The exercise updates location directly to practice API calls; the guide says that a real organizational move would more typically arrive from HR. The study material does not execute this change.

Related reader topics: 4. [Original guide PDF pages 20–22](handouts/exercise-guide.pdf#page=20).

![Original English exercise guide, PDF page 20](images/exercise-020.png)

![Original English exercise guide, PDF page 21](images/exercise-021.png)

![Original English exercise guide, PDF page 22](images/exercise-022.png)

## Exercise 4 — Exploring IdentityIQ Objects

1. Inspect the supplied external-database connection and try/catch/finally structure.
2. Import the Custom class, create or look up the named regionCodes object, and populate its map from the external lookup rows.
3. Save/commit through the supplied standalone-rule structure and inspect the object's serialized XML. Reusing the named object avoids creating a fresh duplicate on every run.
4. Import the After Provisioning rule and email template, then attach the rule to LDAP in the training application definition.
5. Read ProvisioningResult status from the direct result argument or the plan-attached result as appropriate. The guide explicitly acknowledges an additional AccountRequest result location that its simplified code does not cover.
6. Test the successful request and notification path, then the guide's lab-only offline-service failure path, restoring LDAP afterward.

The requested change can succeed even if the After Provisioning notification rule fails. Diagnose target fulfillment and post-processing separately. No request, email, service stop or directory reset was performed for this book.

Related reader topics: 5. [Original guide PDF pages 23–29](handouts/exercise-guide.pdf#page=23).

![Original English exercise guide, PDF page 23](images/exercise-023.png)

![Original English exercise guide, PDF page 24](images/exercise-024.png)

![Original English exercise guide, PDF page 25](images/exercise-025.png)

![Original English exercise guide, PDF page 26](images/exercise-026.png)

![Original English exercise guide, PDF page 27](images/exercise-027.png)

![Original English exercise guide, PDF page 28](images/exercise-028.png)

![Original English exercise guide, PDF page 29](images/exercise-029.png)

## Exercise 5 — Common API Uses

1. Add regionCode to the account schema and create the identity attribute/source mapping required to preserve and promote it.
2. Attach the ResourceObject customization rule and use the previously created regionCodes Custom object as its lookup.
3. Aggregate and inspect the resulting identity data. The guide notes that the Identity Warehouse display also needs a UIConfig change before the new value appears there.
4. Inspect the manager-certification exclusion hook's entity, items and itemsToExclude arguments.
5. Evaluate the contractor condition and PRISM account presence, using the guide's IdentityService helper for account access rather than assuming every relationship should be traversed directly.
6. For this all-or-nothing example, move the excluded items into the exclusion collection and remove them from the review collection, preserving an exclusion reason.
7. Generate the lab campaign with saved exclusions and inspect the exclusions view.

Excluding all access for a person who has a PRISM account is different from excluding only PRISM-related access items. The latter needs more selective logic. The lesson preview's reference to a Custom object from Exercise 3 conflicts with the guide, which creates it in Exercise 4.

Related reader topics: 6. [Original guide PDF pages 30–34](handouts/exercise-guide.pdf#page=30).

![Original English exercise guide, PDF page 30](images/exercise-030.png)

![Original English exercise guide, PDF page 31](images/exercise-031.png)

![Original English exercise guide, PDF page 32](images/exercise-032.png)

![Original English exercise guide, PDF page 33](images/exercise-033.png)

![Original English exercise guide, PDF page 34](images/exercise-034.png)

## Exercise 6 — Best Practices and Performance

1. Create a uniquely named custom logger in the starter rule.
2. Add matching logger name/level entries to Log4j2 properties and use the custom logger for the provided debug messages.
3. Bracket each of the two query paths with distinct, matched Meter enter/exit names.
4. Import/run the training rule, inspect its log messages and use Debug Pages → Call Timings to inspect execution counts and timing statistics.
5. Optionally compare trace-level diagnostics, then restore an appropriate operating level.

The guide explicitly says the small lab and unequal query work do not prove a universal performance ranking. The purpose is to learn logging and metering, with cursor cleanup and decache examples, rather than publish a benchmark.

Related reader topics: 7. [Original guide PDF pages 35–37](handouts/exercise-guide.pdf#page=35).

![Original English exercise guide, PDF page 35](images/exercise-035.png)

![Original English exercise guide, PDF page 36](images/exercise-036.png)

![Original English exercise guide, PDF page 37](images/exercise-037.png)

