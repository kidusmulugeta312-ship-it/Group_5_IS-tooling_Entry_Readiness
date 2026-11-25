# IS Software Tooling Gaps and Graduate Entry Readiness

Section 2, Group 5 — School of Information Science, Addis Ababa University
Research and Technical Writing for Information Systems
Instructor: Ermias Abebe (PhD)

## Project overview
This project investigates gaps between software tools covered in undergraduate Information Systems programs and tools required in local software firms and freelance work. It compares entry readiness across firm-employed graduates and freelancers. The original proposal is in `proposal/` (dated October 28, 2026).

## Current status
Repository starter prepared November 25, 2026 from the supplied proposal. The proposal is existing group work; additional instruments, templates, and code are AI-assisted drafts requiring group review. No pilot, participant recruitment, interviews, survey responses, statistical findings, or completed results are claimed. No historical commits have been recreated. The group must commit genuine subsequent work as it happens.

## Research questions
1. Which tool categories show the largest gaps between IS curriculum coverage and local workplace requirements?
2. How are tooling gaps associated with readiness and early performance in software firms compared with freelance work?

The original proposal uses impact language. A cross-sectional observational study should report associations, not establish causation.

## Folder structure
| Folder | Contents |
|---|---|
| proposal/ | Original proposal PDF, extracted text, and revision checklist |
| instruments/ | Draft questionnaire, interview guide, and consent text |
| pilot-study/ | Pilot protocol and blank feedback log |
| data/ | Header-only anonymized CSV template and data dictionary; no real responses |
| analysis/ | Runnable descriptive analysis script and analysis plan |
| report/ | Report outline; findings not yet available |
| presentation/ | Slide outline; results placeholders only |
| meeting-notes/ | Blank meeting template and contribution log |
| references/ | Proposal references, not independently verified |

## Group members and roles
Roles below are suggestions only; confirm or change them together before submission. Student IDs are intentionally omitted from this README; the original PDF contains them.

| Member | Proposed role — pending confirmation |
|---|---|
| Fikireselam Aragie | Project coordination and proposal integration |
| Kidus Mulugeta | Questionnaire and interview instrument coordination |
| Mahder Assefa | Pilot coordination and data stewardship |
| Nahom Daniel | Analysis scripts and reproducibility checks |
| Nathan Teshager | Report integration and presentation coordination |

All members should review the design, contribute genuine work, and review the final report.

## Software and datasets
- Git and GitHub: version history and collaboration.
- Google Forms: planned questionnaire collection, not yet created.
- Python 3.9+: supplied descriptive script (standard library only; no packages required).
- Optional spreadsheet/statistical software: to be selected and documented before inferential analysis.
- Dataset: `data/survey_anonymized_template.csv` is header-only, not collected or synthetic participant data.
- No external dataset or completed pilot dataset is included.

## Reproduce the descriptive analysis
1. Install Python 3.9 or later and extract or clone this repository.
2. Review `data/data-dictionary.md` and `analysis/analysis-plan.md`.
3. After consent and collection, produce a de-identified CSV using the exact template columns. Keep identifiable originals outside GitHub.
4. From the repository root run:
   `python analysis/analyze.py --input data/survey_anonymized_template.csv --output analysis/output`
   On Windows, `py` can replace `python` if necessary.
5. With the empty template, the program reports that no data exist and produces no findings.
6. With valid responses it writes `category_summary.csv` and `readiness_by_pathway.csv` into the output directory. Missing ratings are omitted; category counts are reported. Repeated rows per person represent tool categories, not independent participants.

The script implements descriptive summaries only. It does NOT perform regression, significance tests, thematic analysis, or causal estimation. Those require a reviewed design, sufficient data, and additional documented code. Outputs are ignored by Git by default to avoid accidental disclosure.

## Responsible data handling
Obtain instructor/institutional approval as applicable before recruitment. Use participant codes, not names, emails, phone numbers, client identities, or employer identifiers. Do not publish raw identifiable data, consent records, or interview recordings. The supplied original proposal PDF includes student names and IDs: obtain group agreement before making this repository public, or use an instructor-accessible private repository if permitted.

## Workflow and project evolution
Commit real changes as they occur: instrument revision, pilot feedback, approved instrument, cleaned-data documentation, analysis, report drafts, presentation. Use descriptive messages and keep actual meeting notes. Do not invent meetings, results, or backdated progress. See `SETUP_AND_SUBMISSION.md`.
