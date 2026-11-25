# Analysis-ready data dictionary — draft
One row per graduate respondent per tool category. Exactly one row for each respondent/category combination. Six categories are planned: version_control, containers, ci_cd, cloud_deployment, frameworks, agile_tracking.
- respondent_id: random pseudonymous string; no identifying information.
- pathway: firm, freelance, hybrid, or not_working.
- tool_category: one of the six categories above.
- curriculum_exposure: integer 1–5; anchors in questionnaire.
- current_proficiency, required_proficiency: integer 1–5 using identical proficiency anchors.
- workplace_importance: integer 1–5.
- readiness_1 through readiness_4: integer 1–5. Repeat identical responses across a participant's category rows; script validates consistency. A descriptive composite is computed only when all four are answered.
- Missing / not applicable / cannot recall: blank cell. Never encode as 0 or 99.
The script uses graduate responses only. Keep student and practitioner modules in separate reviewed datasets; they are not implemented in this template. Contextual variables are not included in this minimal script and must be added with an updated dictionary and validation before regression.
