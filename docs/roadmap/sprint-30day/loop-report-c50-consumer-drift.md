# Consumer-drift audit: lap-schemas Pydantic vs ADR-005

**Auditor**: review-loop reviewer (c129 paused-window side-task).
**Date**: 2026-04-26.
**Scope**: ADR-005 §§5.1–5.7 (the 7 canonical coaching objects + their nested types) compared against the Pydantic v2 source-of-truth in `lap-schemas/python/src/lap_schemas/v1/`.
**Method**: field-by-field comparison; report only, no edits.

---

## Summary of CRITICAL findings

**Zero CRITICAL findings.** The Pydantic models in `lap-schemas/python/src/lap_schemas/v1/` faithfully implement ADR-005 §§5.1–5.7 with no missing fields, no wrong types, no wrong nullability, and no wrong enum literals.

This is the OPPOSITE of self-consistent AI drift. Where the audit expected to find quietly-introduced fields, dropped requirements, or enum re-namings — none exist. In several places the Pydantic is *tighter* than the ADR (e.g., the ADR comment `# 0-1` becomes `Field(ge=0, le=1)` enforcement at the schema layer).

## Summary of MINOR findings (7)

| # | Finding | Severity | Where |
|---|---|---|---|
| M1 | Tuple-vs-list collection representation | MINOR | All 7 objects with collection fields |
| M2 | `SessionContext` referenced but never field-spec'd in ADR-005 | MINOR (doc gap) | §5.3 ActionPrescription |
| M3 | `CohortDef` referenced but never field-spec'd in ADR-005 | MINOR (doc gap) | §5.6 DriverBenchmarkProfile |
| M4 | `TargetEvent` referenced but never field-spec'd in ADR-005 | MINOR (doc gap) | §5.7 DriverReadinessState |
| M5 | `cohort_size: must be >= 20 to publish` is a business rule in the ADR comment, not encoded as a field constraint | MINOR (defensible) | §5.6 DriverBenchmarkProfile |
| M6 | `DivergencePoint.track_distance_m: # or corner tag` — Pydantic chose float-only, dropping the corner-tag alternative | MINOR (ADR ambiguous) | §5.5 nested |
| M7 | Pydantic adds `Field(ge=, le=)` bounds where ADR has only `# 0-1` / `# 0-100` comments | MINOR (positive add-on) | Throughout |

---

## §5.1 — DriverProgressSnapshot + SkillDimension

### `DriverProgressSnapshot`

| Field | ADR-005 spec | Pydantic in lap-schemas | Match? | Severity |
|---|---|---|---|---|
| `id` | `UUID7` | `UUID7` | ✓ | OK |
| `driver_id` | `UUID7` | `UUID7` | ✓ | OK |
| `captured_at` | `datetime` | `datetime` | ✓ | OK |
| `window` | `Literal["session","week","month","rolling_30d"]` | `ProgressWindow = Literal[same 4 values]` | ✓ | OK |
| `window_start` | `datetime` | `datetime` | ✓ | OK |
| `window_end` | `datetime` | `datetime` | ✓ | OK |
| `braking` | `SkillDimension` | `SkillDimension` | ✓ | OK |
| `throttle_pickup` | `SkillDimension` | `SkillDimension` | ✓ | OK |
| `minimum_speed` | `SkillDimension` | `SkillDimension` | ✓ | OK |
| `line_consistency` | `SkillDimension` | `SkillDimension` | ✓ | OK |
| `tire_management` | `SkillDimension` | `SkillDimension` | ✓ | OK |
| `racecraft` | `SkillDimension` | `SkillDimension` | ✓ | OK |
| `fatigue_consistency` | `SkillDimension` | `SkillDimension` | ✓ | OK |
| `strategy_execution` | `SkillDimension` | `SkillDimension` | ✓ | OK |
| `setup_sensitivity` | `SkillDimension` | `SkillDimension` | ✓ | OK |
| `adaptation` | `SkillDimension` | `SkillDimension` | ✓ | OK |
| `overall_score` | `float  # weighted composite` | `float = Field(ge=0, le=100)` | ✓ + bound add-on | OK (M7) |
| `overall_confidence` | `float  # 0-1` | `float = Field(ge=0, le=1)` | ✓ + bound add-on | OK (M7) |
| `percentile_vs_cohort` | `Optional[float]  # null until cohort exists` | `float \| None = Field(default=None, ge=0, le=1)` | ✓ + bound add-on | OK (M7) |
| `generated_by` | `str  # version of scoring engine` | `str` | ✓ | OK |

### `SkillDimension` (nested)

| Field | ADR-005 spec | Pydantic | Match? | Severity |
|---|---|---|---|---|
| `score` | `float  # 0-100` | `float = Field(ge=0, le=100)` | ✓ + bound add-on | OK (M7) |
| `confidence` | `float  # 0-1, decays with time...` | `float = Field(ge=0, le=1)` | ✓ + bound add-on | OK (M7) |
| `trend_14d` | `Literal["up","flat","down","volatile"]` | `Trend14d = Literal[same 4]` | ✓ | OK |
| `last_evidence_session_id` | `Optional[UUID7]` | `UUID7 \| None = None` | ✓ | OK |
| `sample_count` | `int  # how many sessions fed this` | `int = Field(ge=0)` | ✓ + bound add-on | OK (M7) |

---

## §5.2 — WeaknessEpisode

### `WeaknessEpisode`

| Field | ADR-005 spec | Pydantic | Match? | Severity |
|---|---|---|---|---|
| `id` | `UUID7` | `UUID7` | ✓ | OK |
| `driver_id` | `UUID7` | `UUID7` | ✓ | OK |
| `category` | `WeaknessCategory  # enum: technique, consistency, setup_sensitivity, confidence, race_management, execution` | `WeaknessCategory = StrEnum(same 6 values)` | ✓ | OK |
| `subcategory` | `str  # "late_braking", etc.` | `str` | ✓ | OK |
| `corner_tag` | `Optional[str]  # "Spa/T1" or None` | `str \| None = None` | ✓ | OK |
| `environment_scope` | `list[EnvironmentTag]` | `tuple[EnvironmentTag, ...] = Field(default_factory=tuple)` | ✓ representation diff | MINOR (M1) |
| `first_observed_at` | `datetime` | `datetime` | ✓ | OK |
| `last_observed_at` | `datetime` | `datetime` | ✓ | OK |
| `recurrence_count` | `int` | `int = Field(ge=0)` | ✓ + bound add-on | OK (M7) |
| `sessions_affected` | `list[UUID7]  # capped at last 50` | `tuple[UUID7, ...] = Field(default_factory=tuple, max_length=50)` | ✓ representation diff + cap encoded | MINOR (M1) |
| `severity` | `Literal["low","medium","high"]` | `EpisodeSeverity = Literal[same 3]` | ✓ | OK |
| `confidence` | `float  # 0-1, decays...` | `float = Field(ge=0, le=1)` | ✓ + bound add-on | OK (M7) |
| `confidence_decay_per_day` | `float  # default 0.02` | `float = Field(default=0.02, ge=0)` | ✓ default encoded | OK |
| `status` | `Literal["open","improving","resolved","dormant"]` | `EpisodeStatus = Literal[same 4]` | ✓ | OK |
| `resolved_at` | `Optional[datetime]` | `datetime \| None = None` | ✓ | OK |
| `linked_prescriptions` | `list[UUID7]` | `tuple[UUID7, ...]` | ✓ representation diff | MINOR (M1) |
| `linked_insights` | `list[UUID7]` | `tuple[UUID7, ...]` | ✓ representation diff | MINOR (M1) |
| `library_rule_id` | `str` | `str` | ✓ | OK |

---

## §5.3 — ActionPrescription + SuccessCondition

### `ActionPrescription`

| Field | ADR-005 spec | Pydantic | Match? | Severity |
|---|---|---|---|---|
| `id` | `UUID7` | `UUID7` | ✓ | OK |
| `driver_id` | `UUID7` | `UUID7` | ✓ | OK |
| `weakness_episode_id` | `Optional[UUID7]` | `UUID7 \| None = None` | ✓ | OK |
| `created_at` | `datetime` | `datetime` | ✓ | OK |
| `priority` | `Literal["p0","p1","p2"]` | `PrescriptionPriority = Literal[same 3]` | ✓ | OK |
| `due_before_session_id` | `Optional[UUID7]` | `UUID7 \| None = None` | ✓ | OK |
| `valid_until` | `Optional[datetime]` | `datetime \| None = None` | ✓ | OK |
| `title` | `str` | `str` | ✓ | OK |
| `rationale` | `str` | `str` | ✓ | OK |
| `drill_template_id` | `Optional[str]` | `str \| None = None` | ✓ | OK |
| `expected_context` | `SessionContext` | `SessionContext` | ✓ type ref present | MINOR (M2 — ADR doesn't field-spec SessionContext) |
| `success_condition` | `SuccessCondition` | `SuccessCondition` | ✓ | OK |
| `status` | `Literal["proposed","accepted","in_progress","completed","skipped","expired"]` | `PrescriptionStatus = Literal[same 6]` | ✓ | OK |
| `accepted_at` | `Optional[datetime]` | `datetime \| None = None` | ✓ | OK |
| `outcome_id` | `Optional[UUID7]  # ActionOutcome` | `UUID7 \| None = None` | ✓ | OK |

### `SuccessCondition` (nested)

| Field | ADR-005 spec | Pydantic | Match? | Severity |
|---|---|---|---|---|
| `metric` | `str  # "t1_trail_brake_release_pct"` | `str` | ✓ | OK |
| `target_value` | `float` | `float` | ✓ | OK |
| `comparison` | `Literal["gte","lte","within_pct"]` | `Comparison = Literal[same 3]` | ✓ | OK |
| `target_pct` | `Optional[float]` | `float \| None = None` | ✓ | OK |
| `measurement_window` | `Literal["next_session","next_3_sessions","next_7_days"]` | `MeasurementWindow = Literal[same 3]` | ✓ | OK |

### `SessionContext` (referenced, NOT spec'd in ADR-005) — DOC GAP M2

ADR-005 §5.3 references `expected_context: SessionContext  # car+track+conditions to execute in` but does not define SessionContext field-by-field anywhere in the ADR. Pydantic implements:
- `car_id: UUID7`
- `track_id: UUID7`
- `track_layout: str`
- `environment_tag: EnvironmentTag | None = None`
- `conditions: str | None = None`

This is a doc gap, not a code drift. The Pydantic shape is reasonable for the use case ("car+track+conditions to execute in") but cannot be audited against ADR.

---

## §5.4 — ActionOutcome

| Field | ADR-005 spec | Pydantic | Match? | Severity |
|---|---|---|---|---|
| `id` | `UUID7` | `UUID7` | ✓ | OK |
| `prescription_id` | `UUID7` | `UUID7` | ✓ | OK |
| `measured_at` | `datetime` | `datetime` | ✓ | OK |
| `session_ids_measured` | `list[UUID7]` | `tuple[UUID7, ...]` | ✓ representation diff | MINOR (M1) |
| `success_condition_met` | `bool` | `bool` | ✓ | OK |
| `measured_value` | `float` | `float` | ✓ | OK |
| `delta_vs_baseline` | `float  # improvement vs pre-prescription` | `float` | ✓ | OK |
| `confidence_change` | `float  # how much WeaknessEpisode confidence moved` | `float` | ✓ | OK |
| `prescription_efficacy_score` | `float  # 0-1, feeds prescription_efficacy KPI` | `float = Field(ge=0, le=1)` | ✓ + bound add-on | OK (M7) |
| `notes` | `Optional[str]` | `str \| None = None` | ✓ | OK |

---

## §5.5 — TransferLink + DivergencePoint

### `TransferLink`

| Field | ADR-005 spec | Pydantic | Match? | Severity |
|---|---|---|---|---|
| `id` | `UUID7` | `UUID7` | ✓ | OK |
| `driver_id` | `UUID7` | `UUID7` | ✓ | OK |
| `created_at` | `datetime` | `datetime` | ✓ | OK |
| `created_by` | `Literal["user","auto"]` | `TransferCreatedBy = Literal[same 2]` | ✓ | OK |
| `session_pair` | `list[UUID7]  # usually 2: one sim, one real` | `tuple[UUID7, ...]` | ✓ representation diff | MINOR (M1) |
| `link_reason` | `Literal["same_track","event_prep","similar_car_class","manual"]` | `TransferLinkReason = Literal[same 4]` | ✓ | OK |
| `shape_match_score` | `float  # 0-1` | `float = Field(ge=0, le=1)` | ✓ + bound add-on | OK (M7) |
| `intensity_match_score` | `float  # 0-1` | `float = Field(ge=0, le=1)` | ✓ + bound add-on | OK (M7) |
| `divergence_points` | `list[DivergencePoint]` | `tuple[DivergencePoint, ...]` | ✓ representation diff | MINOR (M1) |
| `transferred_skills` | `list[str]` | `tuple[str, ...]` | ✓ representation diff | MINOR (M1) |
| `non_transferred_skills` | `list[str]` | `tuple[str, ...]` | ✓ representation diff | MINOR (M1) |
| `generated_report_id` | `Optional[UUID7]  # CoachingInsight summarizing` | `UUID7 \| None = None` | ✓ | OK |

### `DivergencePoint` (nested)

| Field | ADR-005 spec | Pydantic | Match? | Severity |
|---|---|---|---|---|
| `track_distance_m` | `float  # or corner tag` | `float = Field(ge=0)` | ✓ + bound; "or corner tag" alternative dropped | MINOR (M6 — ADR ambiguous) |
| `metric` | `str  # "brake_pressure_peak"` | `str` | ✓ | OK |
| `sim_value` | `float` | `float` | ✓ | OK |
| `real_value` | `float` | `float` | ✓ | OK |
| `divergence_type` | `Literal["shape","intensity","both"]` | `DivergenceType = Literal[same 3]` | ✓ | OK |

The ADR comment `# or corner tag` on `track_distance_m: float` suggests the field could also represent a corner tag (string) — i.e., a polymorphic distance-or-corner-name. Pydantic chose the simpler `float` shape. This is a deliberate disambiguation in absence of a clear ADR mandate; if the polymorphism was actually intended, the model would need union-typing or a separate field.

---

## §5.6 — DriverBenchmarkProfile + CohortDef

### `DriverBenchmarkProfile`

| Field | ADR-005 spec | Pydantic | Match? | Severity |
|---|---|---|---|---|
| `id` | `UUID7` | `UUID7` | ✓ | OK |
| `driver_id` | `UUID7` | `UUID7` | ✓ | OK |
| `generated_at` | `datetime` | `datetime` | ✓ | OK |
| `cohort_definition` | `CohortDef` | `CohortDef` | ✓ type ref present | MINOR (M3 — ADR doesn't field-spec CohortDef) |
| `cohort_size` | `int  # must be >= 20 for a percentile to publish` | `int = Field(ge=0)` | ✓ but business rule (>=20) not encoded | MINOR (M5) |
| `per_track_car_percentiles` | `dict[str, float]  # "spa/gt3-porsche" → 0.72` | `dict[str, float] = Field(default_factory=dict)` | ✓ | OK |
| `per_dimension_percentiles` | `dict[str, float]  # "braking" → 0.65` | `dict[str, float] = Field(default_factory=dict)` | ✓ | OK |
| `archetype` | `Optional[Literal["late_braker","smooth_flow","aggressive_exit","consistent_executor","adaptive_racecraft"]]` | `DriverArchetype \| None = None` (Literal[same 5]) | ✓ | OK |

### `CohortDef` (referenced, NOT spec'd in ADR-005) — DOC GAP M3

ADR-005 §5.6 references `cohort_definition: CohortDef` but does not define CohortDef field-by-field. Pydantic implements:
- `skill_level: str | None = None`
- `car_class: str | None = None`
- `track_id: UUID7 | None = None`
- `environment_tag: EnvironmentTag | None = None`
- `min_sessions: int = Field(default=5, ge=0)`

These are reasonable cohort-filter fields for the documented intent ("Percentiles vs cohort. Empty until we have cohort data — ADR-008") but cannot be audited against ADR-005.

---

## §5.7 — DriverReadinessState + TargetEvent

### `DriverReadinessState`

| Field | ADR-005 spec | Pydantic | Match? | Severity |
|---|---|---|---|---|
| `id` | `UUID7` | `UUID7` | ✓ | OK |
| `driver_id` | `UUID7` | `UUID7` | ✓ | OK |
| `target_event` | `Optional[TargetEvent]  # iRacing special / track day` | `TargetEvent \| None = None` | ✓ type ref present | MINOR (M4 — ADR doesn't field-spec TargetEvent) |
| `computed_at` | `datetime` | `datetime` | ✓ | OK |
| `readiness_score` | `float  # 0-100` | `float = Field(ge=0, le=100)` | ✓ + bound add-on | OK (M7) |
| `volume_input` | `float  # sessions in last N days` | `float` | ✓ | OK |
| `quality_input` | `float  # avg data_quality score` | `float` | ✓ | OK |
| `recency_input` | `float  # time since last relevant session` | `float` | ✓ | OK |
| `consistency_input` | `float  # lap-time consistency trend` | `float` | ✓ | OK |
| `unresolved_weaknesses_input` | `float  # count x severity` | `float` | ✓ | OK |
| `familiarity_input` | `float  # sessions on this track/car` | `float` | ✓ | OK |
| `event_pressure_input` | `float  # competitive weight of target` | `float` | ✓ | OK |
| `recovery_input` | `float  # time since last intense session` | `float` | ✓ | OK |
| `limiting_factor` | `str  # which input is lowest` | `str` | ✓ | OK |
| `likely_gain_area` | `str  # which weakness moves score most` | `str` | ✓ | OK |
| `recommended_sessions_before_event` | `int` | `int = Field(ge=0)` | ✓ + bound add-on | OK (M7) |

### `TargetEvent` (referenced, NOT spec'd in ADR-005) — DOC GAP M4

ADR-005 §5.7 references `target_event: Optional[TargetEvent]` but does not define TargetEvent field-by-field. Pydantic implements:
- `id: UUID7`
- `name: str`
- `kind: TargetEventKind = Literal["sim_event", "real_track_day", "real_race", "real_test"]`
- `starts_at: datetime`
- `ends_at: datetime | None = None`
- `track_id: UUID7 | None = None`
- `car_id: UUID7 | None = None`
- `competitive_weight: float = Field(ge=0, le=1)`
- `notes: str | None = None`

Reasonable shape but cannot be audited.

---

## Recommended fix path

### CRITICAL fixes

**None.** No CRITICAL findings detected.

### MINOR follow-ups (all optional, none blocking router phase)

**M1 — tuple-vs-list collection representation**
- *Path*: keep as-is. Tuple choice is justified by `model_config = ConfigDict(frozen=True, extra="forbid")` — frozen models with mutable list fields are an anti-pattern. JSON serialization is identical (both → JSON array). Downstream codegen (TS / Swift / Kotlin) all emit `Array<T>` or equivalent regardless. **Recommend: amend the ADR comment to read `tuple[X]` for consistency, or leave silent and accept the Pydantic refinement.**

**M2 — SessionContext doc gap (§5.3)**
- *Path*: amend ADR-005 by adding a `SessionContext` subsection (parallel to §5.1's SkillDimension) with the 5 fields the Pydantic already encodes. Code is not wrong — doc is incomplete.

**M3 — CohortDef doc gap (§5.6)**
- *Path*: amend ADR-005 by adding a `CohortDef` subsection. Same reasoning as M2.

**M4 — TargetEvent doc gap (§5.7)**
- *Path*: amend ADR-005 by adding a `TargetEvent` subsection. Same reasoning as M2.

**M5 — `cohort_size >= 20` business rule unencoded**
- *Path*: leave field constraint as `ge=0`. The "≥20 to publish" rule belongs in the API/computation layer (e.g., the percentile-publish service should refuse to expose percentiles when `cohort_size < 20`), not at the model level. A row in the DB with `cohort_size=15` is a legitimate snapshot of insufficient cohort, not an invalid model. **Recommend: add a short comment in `driver_benchmark_profile.py` referencing the publish-rule for future readers.**

**M6 — DivergencePoint "or corner tag" alternative dropped**
- *Path*: amend ADR-005 to remove the ambiguous comment, since Pydantic chose float. If polymorphism is later wanted, a new ADR can introduce `track_distance_m: float | None` + `corner_tag: str | None` with at-least-one validation.

**M7 — Pydantic adds `Field(ge=, le=)` bounds where ADR has only `# 0-1` / `# 0-100` comments**
- *Path*: keep as-is. The Pydantic enforcement is a positive add-on that elevates ADR-comment-level invariants to schema-validation-level. **No action; consider this a strength.**

---

## Auditor's bottom line

The Pydantic source-of-truth in `lap-schemas/python/src/lap_schemas/v1/` is in **good shape vs. ADR-005**. The 7 canonical objects are present, fields match, types match, enums match (including `WeaknessCategory`, `EpisodeSeverity`, `EpisodeStatus`, `PrescriptionPriority`, `PrescriptionStatus`, `Comparison`, `MeasurementWindow`, `TransferCreatedBy`, `TransferLinkReason`, `DivergenceType`, `DriverArchetype`, `Trend14d`, `ProgressWindow`). Constraint refinements (`ge=`, `le=`, `max_length=`) tighten the contract beyond what the ADR's English comments require, which is desirable for the source-of-truth role.

The MINOR findings group into two patterns:
1. **Pydantic chose tighter shapes than ADR mandated** (frozen tuples, validated bounds, capped lengths) — these are improvements, not drift.
2. **ADR-005 references three nested types (`SessionContext`, `CohortDef`, `TargetEvent`) without defining their fields** — this is an ADR documentation completeness issue, not a Pydantic problem. The Pydantic implementations of these types are reasonable but unauditable against the ADR until the ADR gains those subsections.

If you adopt the recommended path (amend ADR-005 to add the 3 missing nested-type subsections, optionally tighten the `# or corner tag` comment), then a re-audit would find exactly zero MINOR findings as well — full conformance.

**No code changes recommended. Optional ADR amendments to close 3 doc gaps.**

---

*Generated by review-loop reviewer during c129 paused window. No commits or edits to Pydantic files were performed.*
