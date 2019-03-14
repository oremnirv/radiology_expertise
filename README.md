# Radiology expertise exploration 
Extarct radiologist speciality features for future predictive modelling

## Background/Context

Radiology practice patterns -- physician caseloads and utilization with
respect to sub-specialty (e.g., knee, shoulder, cervical spine, lumbar spine,
etc.) -- are known to vary from physician to physician.
For example, the following table provides a scenario where two
radiologists appear to specialize in two procedures while a different two
radiologists appear to specialize in two different procedures.

- Table: Number of times a radiologist provided a specific procedure.

- Rows: Physician ID.

- Columns: Procedure ID.

|          |71020|72110|73060|76830|
|----------|----:|----:|----:|----:|
|1265413959| 100 | 200 |  10 |  20 |
|1255366340|  80 | 250 |  10 |  10 |
|1326089913|  40 |  40 | 140 | 150 |
|1871517128|  30 |  30 | 150 | 150 |

Another characteristic of radiology diagnostics that might be expected is that
some radiology physicians provide more accurate diagnoses than others.
What might be less expected is that variation in diagnostic accuracy is known
to be surprisingly large.
For example,
[a recent study published in the Spine Journal](http://www.thespinejournalonline.com/article/S1529-9430(16)31093-2/pdf)
demonstrated error rates of lumbar MRIs to be as high as 43%.

Identifying factors driving diagnostic accuracy -- a.k.a., feature
engineering -- is of  major importance.  For example, it
may be the case that a specialist who is well versed and experienced
with a particular radiology procedure will have improved diagnostic
accuracy with respect to that procedure.  Or, stated slightly more
formally, features `X` capturing specialization characteristics may
be predictive of diagnostic accuracy `Y`.

I limit my focus to just the process of
constructing practice pattern features `X` in isolation -- the data
will not contain or reference an explicit outcome `Y`.
From within such an unsupervised context. i.e., defining specializations and assigning
specialties to radiology physicians.

## Description of the data available

The data is an excerpt of the following table:
[Medicare Provider Utilization and Payment Data for the year 2016](https://data.cms.gov/use-agreement?id=utc4-f9xp&name=Medicare%20Provider%20Utilization%20and%20Payment%20Data:%20Physician%20and%20Other%20Supplier%20PUF%20CY2016).

The table is organized as follows:

- The primary index of the table is the tuple (`npi`, `hcpcs_code`); in the
  DynamoDB jargon, `npi` is the table's "partition key", whereas `hcpcs_code`
  is the table's "sort key".

  - The `npi` key is the National Provider Identifier, a unique identifier
    for physicians.

  - The `hcpcs_code` key represents medical procedures executed by the
    associated physician in the context of Medicare for the year 2016.

- The table also contains a `line_srvc_cnt` field that represents the total
  number of procedures that a `npi` has performed for a given `hcpcs_code`.

The `npis.pkl` file in the data folder (which has been serialized
using the `pickle` protocol 3) contains the set of NPIs that I  focus
on in my analysis.

You can find more information about the other fields of the
`Medicare2016Filtered` table
[here](https://data.cms.gov/use-agreement?id=utc4-f9xp&name=Medicare%20Provider%20Utilization%20and%20Payment%20Data:%20Physician%20and%20Other%20Supplier%20PUF%20CY2016).

For example:

- The `hcpcs_description` field contains the English description of the
  `hcpcs_code`.

- The `average_medicare_allowed_amt` field provides a proxy to
  "proportional effort required".

### Data Scope Limitations/Guidance

 `hcpcs_code` values not starting with "7" are not radiology
  codes.


## Goal

Define, on the basis of the data, what specializations are and subsequently,
to characterize radiology physicians with respect to these specialties.


Construct a tool that
(a) runs my analysis, and (b) makes the key analysis outputs readily
available as inputs for generic downstream processes.

## Results and insights

Please see pdf Report.


### Warnings

- In the raw data, all keys and attributes are recorded
  as strings.

- The special string `"NA"` indicates a missing value.

- Watch out for the presence of "|" (pipe) characters in the `line_srvc_cnt`
  field (and in the other table fields).




