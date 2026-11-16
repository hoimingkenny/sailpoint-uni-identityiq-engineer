# IdentityIQ Custom Reports

English study notes for all eight numbered teaching modules, in the order shown in SailPoint University. The explanations are rewritten and reference the official course materials. The course is listed as three hours.

**Source depth:** these notes use the provided 75-page presentation deck and 39-page exercise guide. The course introduction's objectives, audience, prerequisites, lesson list and navigation slide were also inspected in the player. Full slide narration and interactive demonstrations were not transcribed or archived. The book provides rewritten study explanations; original slides, guide pages and diagrams are not reproduced. Open Course Files on SailPoint University for the original materials.

**Version context:** the exercise guide says its labs were developed and verified with IdentityIQ **8.1p1**. It carries 2021 notices, while the slides contain 2019/2020 material. These are the source course's examples, not a verified current product specification or support matrix.

[Exercise companion](practice-companion.html) · [Original presentation PDF](https://university.sailpoint.com/path/identity-security-engineer-identityiq/identityiq-custom-reports/424549) · [Original exercise guide](https://university.sailpoint.com/path/identity-security-engineer-identityiq/identityiq-custom-reports/424549) · [Coverage and gaps](coverage.json)

## 1. Course Introduction

### Audience and learning sequence

This course is intended for technical implementers who need to go beyond configuring an existing report. It moves from the report user's experience to the object definitions that implement it, then develops custom queries, output transformations, input forms and summary graphics.

The inspected introduction lists Essentials as a prerequisite and recommends Introduction and Rules, Scripts, and API. That background is useful because custom reports combine IdentityIQ objects, XML definitions and, in some areas, BeanShell/API logic. These notes do not assert that a registration rule has been satisfied or changed.

By the end of the course, the learner should be able to configure/preview/execute/schedule a report; identify the reporting TaskDefinition and its executor; distinguish Filter, Java and HQL data sources; define the returned data and columns; accept user parameters; transform display values with RenderScript; and add forms, a summary table and a chart.

### Training environment and workflow

The guide describes a preconfigured VM with representative identities, applications and a searchable Training Status extension. Its exercises progressively customize two examples: a User Details report and an Application report. A text editor and the IdentityIQ Console support controlled XML editing/import, while Debug Pages expose the resulting object relationships.

The guide's example software versions, file paths and credentials belong to that supplied training environment. The VM starter files referenced under `ReportsTraining` were not exported in this pass. Consult the official guide for their exact instructions and snippets.

No IdentityIQ report, schedule, capability or object was changed while preparing the study book. The separate Answer Key PDF was not used. The presentation handout begins with Module 2, so it has no matching introductory slide section; the unique introduction-player graphics are not separately exported here.

Related reference: [course environment and reference pages](practice-companion.html#practice-reference).

## 2. Configuring Reports

### Start with the user experience

Standard reports answer questions such as which accounts are uncorrelated, who belongs to application groups, which users hold capabilities and which identities are privileged. Intelligence → Reports is the entry point in the training UI. A report can also begin as an Advanced Analytics query saved for repeatable use.

Saving, previewing and executing are different operations. **Save** retains a configuration in My Reports. **Save and Preview** retains the configuration and shows a preview, including the first 20 detail rows in this course, without saving a reusable execution result. **Save and Execute** retains the configuration and runs it, producing a result that can be recalled later. A short preview is not evidence that the entire dataset contains only that many rows.

### Trace the objects behind the interface

IdentityIQ is a Java application whose persistent objects can be represented in XML. The reporting model uses several related objects rather than one file that means everything.

| User action or concept | Object | Meaning |
| --- | --- | --- |
| Select a standard report | Template TaskDefinition | Defines the report's reusable behavior and structure |
| Save a personal configuration | Configured TaskDefinition | Stores its parameters and a parent reference to the template |
| Set recurring execution | TaskSchedule | Specifies when the chosen TaskDefinition should run |
| Complete an execution | TaskResult | Records that run's output and execution information |

The template appears on Reports; a configured instance appears in its owner's My Reports; schedules appear on Scheduled Reports; results appear on Report Results. Results can be visible to other users with the appropriate report rights even if those users did not initiate that run. Ownership of a saved configuration and authorization to see report results are separate concepts.

The schedule stores the target report reference and cron-based timing. A scheduled run can therefore be traced from its TaskResult to the TaskSchedule and configured TaskDefinition, then back to the template. Inspecting these references is more informative than relying on report names alone.

### Exercise 1 study sequence

Explore the training identities and Training Status values. Save an identity query as a report, run the standard User Details report, configure a filtered lapsed-training instance and group its output by manager. Schedule the instance, then use Debug Pages to inspect the related TaskResult, TaskSchedule and TaskDefinition objects.

The filter can use a searchable extension even before that extension appears as a displayed output column. Adding a filter and adding a column are different requirements.

[Exercise 1 — report configuration and object flow](practice-companion.html#practice-1).

## 3. Report TaskDefinition Components

### The outer definition

A report is a specialized TaskDefinition. Its name, report type, template flag, executor, category/subtype, description, signature and required rights establish how IdentityIQ presents and runs it. The course identifies `LiveReport` as the type and `sailpoint.reporting.LiveReportExecutor` as the executor for these examples.

The **Signature** describes accepted inputs. **RequiredRights** references the SPRights needed to use the report. A capability is a collection of rights; it is not interchangeable with an SPRight simply because the training capability and right happen to share the name TRNG-Reporting.

### The nested LiveReport

| Component | Responsibility |
| --- | --- |
| DataSource | Retrieves report detail data |
| Columns / ReportColumnConfig | Defines available detail fields and the properties they use |
| ReportForm | Organizes the user-facing parameter input |
| ReportSummary | Defines an optional summary table |
| Chart | Defines an optional graphical summary |

A saved parameter instance can inherit the report behavior from its template. When changing a custom template, distinguish the definition being edited from previously saved instances and execution results. An old TaskResult is evidence of its completed run, not an automatically refreshed view of a newly edited template.

### Exercise 2 study sequence

Export a clean copy of User Details Report through the Console, rename it, assign the training category and add a column for Training Status. The original guide uses checkout with `-clean` before editing the exported XML. Review the new definition and its authorization, import it in the lab and inspect the output.

The guide then references the custom reporting SPRight in RequiredRights and assigns the corresponding capability to a training identity. This demonstrates authorization and shared result visibility. It was not performed on the user's system while preparing the notes.

[Exercise 2 — create a report and control access](practice-companion.html#practice-2).

## 4. Defining Report Contents

### Separate dataset, selected properties and conditions

The slides use a SQL analogy to explain report construction: selected columns correspond to ReportColumnConfig entries, the source corresponds to a SailPoint object/data source, and filtering corresponds to query criteria. This is a conceptual mapping, not an instruction to modify IdentityIQ database tables directly.

Three source approaches are presented:

- **Filter:** uses the SailPoint object/filter model and projection queries to retrieve the required properties.
- **Java:** delegates data retrieval to a compiled class implementing the reporting data-source interface.
- **HQL:** expresses a Hibernate query over persistent object names and their properties, rather than database table names.

The exercise guide spells the Java interface `sailpoint.reporting.datasource.JavaDataSource`; one slide uses a different capitalization. Use the exact deployed-version JavaDoc rather than copying a class name without checking it. The Java implementation and any compiled files referenced by the lab were not independently exported or executed for this book.

### Coordinate input with output

Signature and Form establish the report's input contract and its presentation. Columns define the detail grid. Summary and Chart communicate an aggregate view. These parts are related but not substitutes for one another: adding a form field does not automatically make it filter the data, and adding a detail column does not define a separate summary calculation.

For a column, distinguish the field identifier, display header and source property. The Application example selects name, authoritative status and owner name. A nested property such as owner.name expresses the required relationship in the source model rather than a new top-level application attribute.

An illustrative column fragment, based on the training example, is:

```xml
<ReportColumnConfig field="trainingStatus"
                    header="Training Status"
                    property="trainingStatus" />
```

It is a fragment to be placed inside the appropriate report structure, not a complete importable report.

### Exercise 3 study sequence

Inspect existing Java/HQL report definitions, then complete a new Filter report for Application objects. Define its name/category, source object/type, output properties and required right. Import and run the lab definition, then trace each visible output back to the XML that requested it.

[Exercise 3 — data-source types and an Application report](practice-companion.html#practice-3).

## 5. Custom Filter Report

### Choose the source object and fixed criteria

A Filter DataSource declares the object type being queried. The Query inside it can impose fixed criteria. For example, the non-authoritative Application report keeps only applications for which authoritative is false.

A rewritten fragment expressing that course example is:

```xml
<DataSource objectType="Application" type="Filter">
  <Query>authoritative==false</Query>
  <QueryParameters>
    <Parameter argument="appInput" property="id"/>
  </QueryParameters>
</DataSource>
```

The fixed condition and parameter condition are different parts of the report. Choosing an application in the input does not cancel the report's requirement that the application be non-authoritative.

### Connect parameters by name

A Signature input declares a parameter such as `appInput`. A QueryParameter with the same argument name maps that supplied value to the relevant source property, such as the Application ID. Keep the identifiers consistent across Signature, QueryParameters and any custom form field.

For study, the corresponding input fragment is:

```xml
<Signature>
  <Inputs>
    <Argument name="appInput" type="Application"/>
  </Inputs>
</Signature>
```

This Signature belongs at its intended TaskDefinition level; it is not nested inside DataSource merely because the fragments are shown next to one another in the notes.

### QueryScript for conditional query logic

The audit example uses QueryScript to examine an optional source-name input and add a case-insensitive prefix filter only when a meaningful value exists. The script returns the intended QueryOptions. This lets code translate a user input into query behavior beyond a direct property comparison.

Keep three questions separate: what objects qualify, what input values are accepted, and how those values alter the query. A dropdown can initially offer values that the fixed query would exclude; Module 7 shows how to constrain the selectable values as well.

### Exercise 4 study sequence

Copy the Application report, add the fixed non-authoritative Query and compare the returned dataset. Add matching Signature/QueryParameter entries, open the saved test instance and select a target application. Verify both the parameter section and the final output, then retain the report for the forms and rendering exercises.

[Exercise 4 — fixed and user-supplied filters](practice-companion.html#practice-4).

## 6. RenderScript

### Transform the displayed value

RenderScript runs BeanShell logic for a report column. It can turn stored values into readable labels, format identifiers or map codes to descriptions. The column's source property is supplied as `value`; the script returns what the user should see. This changes report presentation, not necessarily the underlying identity/application attribute.

The training example displays true Training Status as “Up to date” and false as “TRAINING EXPIRED.” Here is a rewritten fragment with an explicit unknown-value branch added for study:

```xml
<ReportColumnConfig field="trainingStatus"
                    header="Training Status"
                    property="trainingStatus">
  <RenderScript>
    <Source><![CDATA[
      String status = String.valueOf(value);
      if ("true".equalsIgnoreCase(status)) {
          return "Up to date";
      }
      if ("false".equalsIgnoreCase(status)) {
          return "TRAINING EXPIRED";
      }
      return "Unknown";
    ]]></Source>
  </RenderScript>
</ReportColumnConfig>
```

The added fallback avoids silently treating an absent/unrecognized value as either a completed or expired training record. The fragment is explanatory and was not imported or runtime-tested.

### Retrieve related information

The context argument makes API queries available when the displayed result depends on other objects. The Application report uses an application ID as the column property, counts identities with a Link on that application, and then counts the subset with expired training. That information is derived from identities/accounts, not simply read as a preexisting total on the Application object.

The course also mentions optional scriptArguments and sortExpression. Think through how displayed transformations affect sorting rather than assuming that a formatted label and its underlying raw value sort identically. When adapting percentage calculations, define what an application with zero relevant identities should display rather than dividing by zero.

Additional per-row queries can increase report cost. Apply the query/resource-management principles from Rules, Scripts, and API and measure representative workloads; a readable result is not sufficient evidence of scalable execution.

### Exercise 5 study sequence

Replace the Training Status column with its RenderScript version and compare the labels. Add the application columns that calculate identity counts and expired-training percentages, then inspect how the source application ID becomes each script's input. Verify the returned values as well as the visible labels.

[Exercise 5 — display transformations and related-object calculations](practice-companion.html#practice-5).

## 7. Report Forms

### Present the input contract clearly

A report form organizes the fields a user sees when configuring a report. Sections create logical groupings, and fields define labels, data types, cardinality, help text and allowed choices. A well-labeled input still needs to connect to the intended Signature and query parameter.

The training manager selector initially shows all identities and permits one selection. The exercise makes it multi-valued and filters the candidates by managerStatus, then separates Manager Selection and Training Status into distinct sections. Section labels and internal section names serve different purposes in the original editor.

### Constrain choices as well as results

The non-authoritative Application report's fixed Query already limits returned objects, but its original input selector can still offer authoritative applications. The custom Application form adds a filterString for non-authoritative applications, a clearer label/tooltip and multi-selection. Its field name remains aligned with `appInput`.

A report attaches the form through a ReportForm reference. An illustrative fragment has this shape:

```xml
<ReportForm>
  <Reference class="sailpoint.object.Form"
             name="Project-ApplicationReportForm"/>
</ReportForm>
```

This example name is a study placeholder; it is not a form created in the user's installation.

### Static and dynamic forms

A dynamic form can begin as a shell whose fields are populated by initialization logic. The standard User Details example discovers the installation's standard/extended identity attributes and builds suitable input fields. Seeing an empty section in the stored Form does not necessarily mean the user will see no fields at runtime.

When replacing that dynamic behavior with a fixed custom form, the guide coordinates the ReportForm reference, initialization-rule behavior, Signature and QueryParameters. Changing only one can leave a visually improved form disconnected from its query or still affected by the old initialization logic.

The guide notes that one supplied form is classified for editing through the UI; that editing choice is separate from the fact that the report references it as its parameter form.

[Exercise 6 — custom and dynamic report forms](practice-companion.html#practice-6).

## 8. Report Summary and Chart

### Summary is its own data contract

A summary gives an at-a-glance view of the report's detail data. Users can choose whether to include summary or detail sections. The summary may contain a two-column table, a chart or both.

ReportSummary obtains data through a script or rule that returns a map of named values. The LiveReportSummaryValue definitions identify which named entries to display. Match those names to the returned map: creating a value in the script without the corresponding display definition is not the same as presenting it in the report.

### Chart the intended grouping

A chart defines category, value and, where required, series. It may use the report's detail data or a separately supplied source. The original examples show uncorrelated accounts grouped by application, decisions counted by type and identity risk information.

Changing a chart from pie to column changes its presentation, not the meaning of the underlying aggregation. When a summary/chart uses a separate query, verify that it honors the intended report filters and uses the same population/denominator as the detail information it is supposed to summarize. This is a validation step to apply when adapting the example, not a claim that the handout independently proves those conditions for a new implementation.

### Exercise 7 study sequence

Run the standard identity-status and uncorrelated-account reports, inspect their summary sources and chart definition, then compare a changed chart type. Add the Application report's summary calculation and its named result entries. Attach the supplied chart data-source rule and inspect the categories, series and values in the resulting output.

The guide relies on preinstalled XML/text files in the training VM. Those starter files have not been separately archived; the companion summarizes their learning purpose and points back to the official guide.

[Exercise 7 — summary values and chart output](practice-companion.html#practice-7).

The numbered-module notes are complete at the handout-supported level. Full narration, animations, practical lab execution, external references and LMS completion remain separate from this offline study edition.
