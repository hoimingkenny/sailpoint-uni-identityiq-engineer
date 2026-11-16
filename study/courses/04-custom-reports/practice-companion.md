# Custom Reports — Exercise Study Companion

Rewritten learning sequences for seven exercises, with source page references. Use the official exercise guide in [SailPoint Course Files](https://university.sailpoint.com/path/identity-security-engineer-identityiq/identityiq-custom-reports/424549) for exact lab instructions, screenshots and starter-file requirements. Original guide pages are not included. These are study explanations, not completed lab actions.

## Course environment and reference

Original cover, notices, contents and VM instructions. The guide identifies IdentityIQ 8.1p1 and a preconfigured training system. These are historical training values, not a current support matrix. No VM was launched or configured.

Related modules: 1. [Original guide PDF pages 1–6](https://university.sailpoint.com/path/identity-security-engineer-identityiq/identityiq-custom-reports/424549).



## Exercise 1 — Explore Report Configuration

1. Inspect the sample identities and their searchable Training Status extension.
2. Run an Advanced Analytics identity query with the selected fields, then save it as a named report.
3. Execute the standard User Details template and inspect the persisted result and export options.
4. Save a lapsed-training instance, compare preview with complete execution, and group the results by manager.
5. Schedule the configured instance to run now and weekly in the lab.
6. In Debug Pages, trace TaskResult to its schedule and TaskDefinition, then inspect the configured definition's parameters and parent template.

The original pages contain the exact training names/values and questions. No report was run, created, scheduled or exported from a live IdentityIQ system during preparation.

Related modules: 2. [Original guide PDF pages 7–14](https://university.sailpoint.com/path/identity-security-engineer-identityiq/identityiq-custom-reports/424549).



## Exercise 2 — Create a Custom Report and Control Access

1. Use the Console checkout command with the clean option to export the existing User Details TaskDefinition.
2. Edit the file externally, change the report name/category and add the Training Status column.
3. Import the lab definition, find it under the new category and inspect the output.
4. Study how RequiredRights references the custom reporting SPRight and how a capability conveys that right.
5. Test the intended training identity's report visibility and the visibility of results created by another user.

The guide uses the same name for the custom capability and SPRight for convenience; they remain different object types. No capability was assigned while building the book.

Related modules: 3. [Original guide PDF pages 15–18](https://university.sailpoint.com/path/identity-security-engineer-identityiq/identityiq-custom-reports/424549).



## Exercise 3 — Data Sources and an Application Filter Report

1. Inspect standard reports that reference compiled Java data-source classes.
2. Inspect the Account Group Membership Totals HQL source and its Query, QueryScript, QueryParameters and Signature.
3. Complete the supplied Filter report XML for Application objects, adding the name/category, source type, name/authoritative/owner.name columns and report right.
4. Import and run the lab report, then relate each displayed property back to the source definition.

HQL queries object names/properties through Hibernate; its syntax resemblance to SQL does not make it a direct database-table query. The compiled classes and VM starter XML were not exported or executed here.

Related modules: 4. [Original guide PDF pages 19–22](https://university.sailpoint.com/path/identity-security-engineer-identityiq/identityiq-custom-reports/424549).



## Exercise 4 — Fixed Filters and User Parameters

1. Copy the Application report and add the fixed authoritative==false query.
2. Run a saved test instance to establish what the fixed condition returns.
3. Add the appInput Signature argument and a matching QueryParameter mapped to the application ID.
4. Reimport the changed template, reopen the configured instance, select a target application and verify the resulting dataset.
5. Observe that the selector can still show authoritative applications even though the query excludes them; the custom-form exercise later improves the selectable values.

The Signature and QueryParameter names must agree. Filtering output and filtering input choices are separate configuration tasks.

Related modules: 5. [Original guide PDF pages 23–25](https://university.sailpoint.com/path/identity-security-engineer-identityiq/identityiq-custom-reports/424549).



## Exercise 5 — RenderScript

1. Complete the Training Status label transformation, replacing raw true/false values with the intended business labels.
2. Put the script in the existing column's RenderScript/Source structure, save a renamed report and compare its visible results.
3. Inspect the two additional Application-report column definitions. Their source property becomes each script's value argument.
4. Follow the identity-count query restricted to Links on the selected application and the additional expired-training condition.
5. Add the columns, run the lab report and inspect the counts/percentage.

The guide has a closing-tag typo near the paste instruction (`</Column>` versus the surrounding Columns collection); preserve well-formed XML and the intended element nesting. The calculations derive identity information through context, not a preexisting total on the Application itself.

Related modules: 6. [Original guide PDF pages 26–29](https://university.sailpoint.com/path/identity-security-engineer-identityiq/identityiq-custom-reports/424549).



## Exercise 6 — Report Forms

1. Import the supplied User Details report with a static custom form and examine the initial selector behavior.
2. Edit the Manager Selection label, make the manager field multi-valued, restrict candidates with managerStatus, and separate Training Status into its own section.
3. Define the custom Application form with a clear label, tooltip, multi-selection and a non-authoritative filterString. Keep the field name aligned with appInput.
4. Attach the Form through the report's ReportForm reference and verify both the selector and query output.
5. Inspect the standard User Details shell form and its initialization rule, which generates standard/extended-attribute fields dynamically.
6. When replacing dynamic behavior, coordinate ReportForm, InitializationRule, Signature and QueryParameters rather than changing only the appearance.

No Form or TaskDefinition was imported or edited on the user's systems for these notes.

Related modules: 7. [Original guide PDF pages 30–35](https://university.sailpoint.com/path/identity-security-engineer-identityiq/identityiq-custom-reports/424549).



## Exercise 7 — Report Charts and Summaries

1. Run the training Identity Status Summary report and inspect the map returned by its summary source and the matching LiveReportSummaryValue names.
2. Inspect Uncorrelated Accounts and compare its detail grid, summary and chart source.
3. Study changing the existing chart from pie to column and verify what changed in presentation.
4. Add the Application-report summary map with total identities, expired identities and the formatted percentage.
5. Inspect the supplied chart data-source rule and identify its series, category and values before attaching it to the report.
6. Run the updated lab report and compare the summary/chart totals to their intended population.

These are study steps, not completed reporting or review actions. Check the guide's occasionally inconsistent file spelling against the actual VM files.

Related modules: 8. [Original guide PDF pages 36–38](https://university.sailpoint.com/path/identity-security-engineer-identityiq/identityiq-custom-reports/424549).



## Appendix — terminology and Linux commands

Consult the original guide appendix for its UI/internal terminology cross-reference and Linux command reference. That appendix is not reproduced here; no commands were executed against the training VM.

Related modules: 1, 3, 4. [Original guide PDF pages 39–39](https://university.sailpoint.com/path/identity-security-engineer-identityiq/identityiq-custom-reports/424549).

