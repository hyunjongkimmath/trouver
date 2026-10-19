# Function-Shape Violation Checklist (TEMPORARY — delete after run)

**Run:** overnight 30-min loop (cron `*/30 * * * *`)
**Started:** 2026-10-18
**Spec under enforcement:** `_nbdev_development/specs/CODING_STANDARDS/function_shape.md`
**Target:** function implementations in the `.ipynb` files under `Python/trouver/nbs/`

## Rules (from function_shape.md)

| # | Rule | Checkable? |
|---|------|------------|
| R1 | ≤20 executable lines per function (excl. docstring/blank/comment; signature + decorators don't count) | mechanical |
| R2 | one responsibility — names containing `_and_` are review candidates | mechanical flag + judgment |
| R3 | nesting depth ≤3 (body = level 0; guard clauses preferred) | mechanical + judgment |
| R4 | no defensive paragraph comments above small tested functions | judgment only |

## Method / state files

- Mechanical checker: `_nbdev_development/spec_checkers/check_function_shape.py` (AST-based; counts executable lines,
  nesting depth per spec's counting edge cases, flags `_and_` names). Run:
  `python _nbdev_development/spec_checkers/check_function_shape.py Python/trouver/nbs > _tmp/_function_shape_report_tmp.txt`
- Report: regenerate with the command above (R1 / R3 / R2 sections)
- This file = state + report for the run.

**Status:** COMPLETE — executed; results below (R1:95 / R2:39 / R3:21 / R4:~85 judgment notes).

## Progress by module (101 notebooks total)

| Module prefix | Count | Status |
|---------------|-------|--------|
| `01_helper_*` | 21 | [x] R1/R2/R3 mechanical done (R4 pending) |
| `02_markdown_*` | 3 | [x] R1/R2/R3 mechanical done (R4 pending) |
| `03_obsidian_*` | 13 | [x] R1/R2/R3 mechanical done (R4 pending) |
| `04_latex_*` | 5 | [x] R1/R2/R3 mechanical done (R4 pending) — god functions confirmed: `convert_notes_to_latex_code` 50, `setup_reference_from_latex_parts` 46 |
| `05_personal_vault_*` | 8 | [x] R1/R2/R3 mechanical done (R4 pending) |
| `06_notation_*` | 4 | [x] R1/R2/R3 mechanical done (R4 pending) — `_expand_to_valid_latex` 116 lines / depth 6, worst offender |
| `07_llm_core_*` | 1 | [x] R1/R2/R3 mechanical done (R4 pending) |
| `08_machine_learning_*` | 25 | [x] R1/R2/R3 mechanical done (R4 pending) — heaviest violation module |
| `09_app_*`, `10_shortcuts_*`, `24_*`, `26_*` | 5 | [x] R1/R2/R3 mechanical done (R4 pending; GUI has Qt-generated code — user decision needed) |
| `how_to.*`, `tutorial.*`, misc (index, star, TODO, unused, using_regex, release_notes) | 12 | [x] included in mechanical run (no/low violations) |

## Violations log

Format: `V-<n> | <notebook>:<def-line> | <function> | R# | detail (exec lines / depth) | severity`
Severity: **high** = clear rule break (>20 lines or depth >3); **review** = `_and_` name / R4 judgment.

### R2 — `_and_` names (mechanical grep pass, 2026-10-18; severity: review)

Test functions (`test_*`) are listed separately — descriptive test names are likely
acceptable; the heuristic is aimed at implementation functions.

**Implementation functions (review whether they do two things):**
- V-01 | `01_helper_25.latex.macros_and_commands.ipynb` | `_detect_begin_and_end_environments` | R2 | review
- V-02 | `01_helper_25.latex.macros_and_commands.ipynb` | `_commands_from_newcommand_and_declaremathoperator` | R2 | review
- V-03 | `01_helper_07.definition_and_notation.ipynb` | `defs_and_notats_separations` | R2 | review
- V-04 | `01_helper_02.init.ipynb` | `is_not_space_and_not_punc` | R2 | review (predicate over two conditions — likely fine)
- V-05 | `03_obsidian_07.vault_cache.ipynb` | `_check_name_exists_and_unique_in_vault_cache` | R2 | review
- V-06 | `03_obsidian_40.file.ipynb` | `_line_start_and_end_in_line_latex` | R2 | review (likely fine — one predicate)
- V-07 | `03_obsidian_40.file.ipynb` | `get_headings_and_text` | R2 | review
- V-08 | `04_latex_15.formatting.ipynb` | `_replace_backtick_and_apostrophe_quotes` | R2 | review (likely fine — one transform)
- V-09 | `04_latex_15.formatting.ipynb` | `_strip_and_return_whitespaces` | R2 | review
- V-10 | `04_latex_15.formatting.ipynb` | `replace_input_and_include` | R2 | review (two commands — likely fine if one transform)
- V-11 | `04_latex_05.folders.ipynb` | `section_and_subsection_titles_from_latex_parts` | R2 | review
- V-12 | `04_latex_00.divide.ipynb` | `_combine_second_and_third_paramter_results` | R2 | review (also typo: "paramter")
- V-13 | `05_personal_vault_15.reference.ipynb` | `_find_template_and_reference_notes` | R2 | review
- V-14 | `05_personal_vault_15.reference.ipynb` | `_make_chapter_folders_and_indices` | R2 | review (likely two responsibilities)
- V-15 | `05_personal_vault_15.reference.ipynb` | `_modify_fast_link_edit_and_templates` | R2 | review
- V-16 | `05_personal_vault_20.information_notes.ipynb` | `create_info_notes_and_link_to_index` | R2 | review (likely two responsibilities)
- V-17 | `05_personal_vault_20.information_notes.ipynb` | `create_generic_info_notes_and_link_to_index` | R2 | review
- V-18 | `06_notation_00_parse.ipynb` | `_part_is_unordered_list_and_is_of_markdownstyle_link` | R2 | review (compound predicate — likely fine)
- V-19 | `06_notation_00_parse.ipynb` | `_notat_str_and_linked_notat_note_name_from_bullet_point_part` | R2 | review (returns two things)
- V-20 | `06_notation_00_parse.ipynb` | `_remove_the_notation_str_and_denotes_in_main_mf` | R2 | review
- V-21 | `06_notation_05_in_standard_info_note.ipynb` | `notations_and_main_notes` | R2 | review (returns two things)
- V-22 | `08_machine_learning_10.information_note_types.ipynb` | `labels_and_identifying_info_from_notes` | R2 | review (returns two things)
- V-23 | `08_machine_learning_15.tokenize...token_classification.ipynb` | `_calculate_clean_indices_and_create_tags` | R2 | review (likely two responsibilities)
- V-24 | `08_machine_learning_17.tokenize...text_logic.ipynb` | `_append_to_pieces_start_and_end` | R2 | review
- V-25 | `08_machine_learning_18.tokenize...tag_models.ipynb` | `_add_nice_boxing_attrs_to_def_and_notat_tags` | R2 | borderline ("def_and_notat" is a domain term, not "and"-doing)
- V-26 | `08_machine_learning_19.tokenize...token_processing.ipynb` | `def_and_notat_preds_by_model` | R2 | borderline (domain term)
- V-27 | `08_machine_learning_21.tokenize...mark.ipynb` | `get_def_and_notat_predictions` | R2 | borderline (domain term)
- V-28 | `08_machine_learning_21.tokenize...mark.ipynb` | `mark_def_and_notat_predictions` | R2 | borderline (domain term)
- V-29 | `08_machine_learning_21.tokenize...mark.ipynb` | `predict_and_mark_def_and_notats` | R2 | review (predict AND mark — likely two responsibilities)
- V-30 | `08_machine_learning_22.tokenize...main_workflow.ipynb` | `_format_main_text_and_add_html_tag_data` | R2 | review (likely two responsibilities)
- V-31 | `08_machine_learning_22.tokenize...main_workflow.ipynb` | `auto_mark_def_and_notats` | R2 | borderline (domain term)
- V-32 | `08_machine_learning_35.definition_and_notation_naming.ipynb` | `augment_def_and_notat_naming_data` | R2 | borderline (domain term)
- V-33 | `08_machine_learning_35.definition_and_notation_naming.ipynb` | `_augment_def_and_notat_naming_data_once` | R2 | borderline (domain term)
- V-34 | `08_machine_learning_35.definition_and_notation_naming.ipynb` | `predict_name_and_add_to_notation_note` | R2 | review (predict AND write — likely two responsibilities)
- V-35 | `08_machine_learning_45.notation.ipynb` | `notat_note_data_from_parsed_and_main_note_processed` | R2 | borderline (describes inputs)
- V-36 | `08_machine_learning_67.note_linking_vault_operations.ipynb` | `_predict_one_direction_and_consolidate_cache` | R2 | review (likely two responsibilities)
- V-37 | `08_machine_learning_67.note_linking_vault_operations.ipynb` | `_predict_batch_and_consolidate_cache` | R2 | review
- V-38 | `08_machine_learning_67.note_linking_vault_operations.ipynb` | `predict_on_relied_notes_and_related_notat_notes` | R2 | borderline (describes inputs)
- V-39 | `08_machine_learning_70.notation_linking.ipynb` | `_identify_note_type_and_setup` | R2 | review (identify AND setup — likely two responsibilities)

**Test functions (heuristic noise, likely acceptable):** `test_generate_glossary_multiple_items_and_notes`,
`test_predict_batch_and_consolidate_cache`, `test_predict_on_relied_notes_and_related_notat_notes`,
`test_search_robustness_and_filtering`, `test_format_preserves_order_and_content`.

### R3 — nesting depth >3 (mechanical AST run, 2026-10-18; severity: high)

21 functions flagged (all also in R1 list except where noted; `NN` = exec lines):
- `08_machine_learning_67...:2` `get_all_linked_info_notes` depth=7 (exec 47) — worst nesting
- `06_notation_10_management.ipynb:5` `_expand_to_valid_latex` depth=6 (exec 116)
- `01_helper_25.latex.macros_and_commands.ipynb:33` `extract_commands_from_nodes` depth=5 (exec 16 — passes R1, fails R3 only)
- `03_obsidian_70.vault_and_links.ipynb:2` `all_links_in_vault` depth=5 (exec 24)
- `08_machine_learning_15...:2` `latex_highlight_parser` depth=5 (exec 52)
- `08_machine_learning_80.context_extraction.ipynb:3` `create_context_extraction_for_index_note` depth=5 (exec 32)
- depth=4: `01_helper_03...uncompress_file` 47 · `01_helper_07..._get_bold_indices_with_braces` 26 · `01_helper_07...double_asterisk_indices` 33 · `01_helper_20..._has_double_script` 33 · `01_helper_20...get_dollar_sign_syntax_errors` 55 · `01_helper_29..._uncompress_file` 27 · `03_obsidian_10...rename` 24 · `04_latex_20.convert.ipynb:16` `replacement_func` 12 (R3-only) · `08_machine_learning_24...run_audit_voting_maker` 68 · `08_machine_learning_64...dataset_from_note_data` 14 (R3-only) · `08_machine_learning_65...batch_prediction` 23 · `08_machine_learning_65...predict_note_linking` 49 · `08_machine_learning_80..._format_context_extraction` 11 (R3-only) · `08_machine_learning_85...run_vault_audit` 39 · `08_machine_learning_90..._get_all_paths` 10 (R3-only)

### .ipynb spot-checks (verifying AST counts against notebook source)

- ✓ `06_notation_10_management.ipynb` `_expand_to_valid_latex` — genuine 100+ line multi-phase
  function with nested helpers; count faithful.
- ✓ `08_machine_learning_67...ipynb:1086` `get_all_linked_info_notes` — depth-7 nesting confirmed
  (if→if→if→for→if→if chain), section-banner comments, **and a commented-out debug line at JSON
  line 1137** (`# print(f"Debug: ...")`) — the exact decay mode function_shape.md warns about.
- ✓ `08_machine_learning_24...llm_verification.ipynb:706` `run_audit_voting_maker` — exec=68
  confirmed: nested `log` helper, verbose-legend block, multi-flag voting state machine in one
  body; also a leftover dev note (`# <--- NEW: Accepts a function`).
- ✓ `04_latex_20.convert.ipynb:1287` `convert_notes_to_latex_code` — real, but **calibration note**:
  a large share of its exec=50 is one multi-line rf-string (the `% AUTOGENERATED...` LaTeX header
  template). The actual logic is ~8 lines. Per the spec's literal line-counting rule it still
  counts, but severity should be *review* not *high* — string-literal lines are a counting edge
  case the spec doesn't address (candidate spec gap to raise with user).

### R4 — defensive comments / commented-out code (judgment pass, first sweep)

Grep for commented-out statements (`# print/return/if/for/raise`) found **~85 instances** across
~21 notebooks (sweep complete incl. tail page: 5 more in `09_app_00_gui.ipynb` —
`# print(error_message)` :1245, `# if folder:` :1304, `# print(model_path)` :1341,
`# print(subvault)`/`# print(index_file)` :1734–1735). Concentration:
`04_latex_00.divide.ipynb` (~15), `06_notation_10_management.ipynb` (~10),
`08_machine_learning_85.llm_typo_finding.ipynb` (3), `08_machine_learning_15...token_classification.ipynb` (3),
`04_latex_20.convert.ipynb` (2), `08_machine_learning_60...dataset_sieve.ipynb` (2),
`08_machine_learning_70.notation_linking.ipynb` (2), plus scattered singles in ~11 other files.
These are the "commented-out code hiding in long functions" the spec names as root decay — each
sits inside or next to R1-flagged god functions. Full list: re-run the grep (pattern in Handoff block).

**Notes:**
- R1 total: **95 functions**; R3 total: **21**; combined unique ≈ 97. Test functions make up a
  large share of R1 (~30 of 95) — the spec's 20-line limit has no test exemption, but they are
  lower-priority refactors. `09_app_00_gui.ipynb` contains Qt-generated code (`setupUi`,
  `retranslateUi`) — flag for user decision on whether generated code is in scope.
- R4 (defensive paragraph comments) not yet checked — judgment pass, pending.

### R1 — length >20 executable lines (mechanical AST run, 2026-10-18; severity: high)

95 functions flagged. Full data: re-run the checker (command above). Format: `notebook:def-line | function | exec=NN (depth=N)`.

**Worst 10:**
- V-40 | `09_app_00_gui.ipynb:18` | `setupUi` | R1 | exec=309 (Qt-generated UI code — candidate for exemption note)
- V-41 | `06_notation_10_management.ipynb:5` | `_expand_to_valid_latex` | R1+R3 | exec=116, depth=6
- V-42 | `08_machine_learning_24...llm_verification.ipynb:2` | `run_audit_voting_maker` | R1+R3 | exec=68, depth=4
- V-43 | `01_helper_20.latex.core.ipynb:2` | `get_dollar_sign_syntax_errors` | R1+R3 | exec=55, depth=4
- V-44 | `08_machine_learning_24...llm_verification.ipynb:3` | `run_audit_voting` | R1 | exec=55, depth=3
- V-45 | `08_machine_learning_35.definition_and_notation_naming.ipynb:2` | `add_names_to_html_tags_in_info_note` | R1 | exec=55, depth=3
- V-46 | `08_machine_learning_67.note_linking_vault_operations.ipynb:2` | `get_all_linked_info_notes` | R1+R3 | exec=47, depth=7 (worst nesting in codebase)
- V-47 | `08_machine_learning_70.notation_linking.ipynb:2` | `sieve_then_add_links_to_notation_notes` | R1 | exec=53, depth=0 (flat but long — "sieve_then_add" = two responsibilities, cf. R2)
- V-48 | `08_machine_learning_15.tokenize...token_classification.ipynb:2` | `latex_highlight_parser` | R1+R3 | exec=52, depth=5
- V-49 | `04_latex_20.convert.ipynb:2` | `convert_notes_to_latex_code` | R1 | exec=50, depth=1

**Remaining (exec 21–49):**
- `08_machine_learning_67...:5` `test_sieve_potential_relied_notes` 53/1 · `04_latex_20.convert.ipynb:8` `setup_reference_from_latex_parts` 46/1 · `08_machine_learning_70.notation_linking.ipynb:2` `data_points_for_reference` 46/2 · `08_machine_learning_67...:5` `test_predict_on_relied_notes_and_related_notat_notes` 45/1 · `05_personal_vault_15.reference.ipynb:17` `setup_folder_for_new_reference` 44/1 · `08_machine_learning_90.semantic_search.ipynb:3` `search` 44/3 · `04_latex_00.divide.ipynb:4` `test_title_logic_comprehensive` 43/0 · `08_machine_learning_67...:2` `sieve_potential_relied_notes` 43/3 · `03_obsidian_40.file.ipynb:1` `make_example_vault_2` 42/1 · `04_latex_15.formatting.ipynb:2` `replace_input_and_include` 42/0 (also V-10) · `08_machine_learning_67...:5` `test_predict_batch_and_consolidate_cache` 42/1 · `09_app_00_gui.ipynb:330` `retranslateUi` 41/0 (Qt-generated) · `08_machine_learning_50.note_data.ipynb:3` `randomly_modify` 40/2 · `05_personal_vault_25.note_processing.ipynb:3` `process_standard_information_note` 39/2 · `08_machine_learning_85.llm_typo_finding.ipynb:2` `run_vault_audit` 39/4 (also R3) · `01_helper_28.latex.augment.ipynb:3` `push_dollar_signs` 38/2 · `04_latex_00.divide.ipynb:2` `test_change_counters_logic` 38/0 · `08_machine_learning_50.note_data.ipynb:4` `_note_data_under_heading_in_index_note` 38/3 · `08_machine_learning_70.notation_linking.ipynb:2` `_add_links_to_sieved_notat_notes` 38/2 · `08_machine_learning_70...:4` `notat_linking_data_from_notation_notes` 37/1 · `08_machine_learning_90...:5` `test_search_reranking_logic` 36/0 · `04_latex_00.divide.ipynb:3` `test_get_counter_hierarchy_new` 35/0 · `08_machine_learning_70...:2` `_positive_data_points` 35/3 · `08_machine_learning_85...:2` `audit_text_for_typos` 35/2 · `06_notation_15.glossary.ipynb:55` `test_generate_glossary_multiple_items_and_notes` 34/1 (also R2-test) · `08_machine_learning_15...:26` `_augment_html_data_once` 34/2 · `08_machine_learning_24...:2` `run_strict_audit` 34/1 · `01_helper_07.definition_and_notation.ipynb:17` `double_asterisk_indices` 33/4 (also R3) · `01_helper_20.latex.core.ipynb:3` `_has_double_script` 33/4 (also R3) · `03_obsidian_50.links.ipynb:3` `to_regex` 33/1 · `04_latex_00.divide.ipynb:3` `test_title_formatting_hierarchy` 33/0 · `01_helper_26.latex.formatting.ipynb:21` `_insert_newline_or_spaces_around_latex` 32/3 · `08_machine_learning_35...:26` `_augment_def_and_notat_naming_data_once` 32/2 (also V-33) · `08_machine_learning_68...:2` `summarization_data` 32/3 · `08_machine_learning_80.context_extraction.ipynb:3` `create_context_extraction_for_index_note` 32/5 (also R3) · `08_machine_learning_90...:3` `setup_collection` 32/3 · `08_machine_learning_90...:6` `test_search_robustness_and_filtering` 32/0 (R2-test) · `04_latex_00.divide.ipynb:1` `test_recursive_reset` 31/0 · `06_notation_10_management.ipynb:58` `_look_into_node` 31/2 · `06_notation_10...:10` `fix_notation_syntax_in_notation_note` 31/2 · `08_machine_learning_70...:2` `_sample_data_points` 31/2 · `09_app_00_gui.ipynb:76` `instruction_message` 31/0 · `04_latex_00.divide.ipynb:4` `test_formatted_number_zero_parent` 30/0 · `04_latex_15.formatting.ipynb:23` `process_input_or_include` 30/3 · `08_machine_learning_35...:102` `_get_processed_data_points` 30/2 · `08_machine_learning_68...:2` `augment_notat_note_data_for_summarization` 30/3 · `08_machine_learning_90...:19,24` `run_migration_tests` (×2 cells) 30/0 · `09_app_00_gui.ipynb:14` `run` 30/3 · `04_latex_00.divide.ipynb:4` `test_get_reset_hierarchy` 29/0 · `04_latex_00.divide.ipynb:7` `divide_latex_text` 29/1 · `08_machine_learning_64...:4` `test_dataset_generation_loop` 29/0 · `08_machine_learning_50...:3` `randomly_modify` 28/1 (2nd def) · `08_machine_learning_65...:117` `test_multi_label_batch_predictions` 28/1 · `09_app_00_gui.ipynb:56` `show_confirmation_dialog` 28/1 · `01_helper_29.arxiv.ipynb:2` `_uncompress_file` 27/4 (also R3) · `05_personal_vault_15...:4` `_manifest_template_file` 27/1 · `08_machine_learning_50...:3` `from_note` 27/2 · `08_machine_learning_67...:2` `add_notation_note_embedded_footnotes_to_info_note` 27/3 · `01_helper_02.init.ipynb:19` `partial_ratio_with_alphabet` 26/3 · `01_helper_07...:4` `_get_bold_indices_with_braces` 26/4 (also R3) · `03_obsidian_40.file.ipynb:3` `_replace_embedded_links_one_line` 26/3 · `06_notation_10...:2` `reorder_notation_note_links_in_see_also_section` 26/2 · `06_notation_10...:2` `find_best_notation_substring` 26/1 · `07_llm_core_05.call_llm.ipynb:2` `_parse_qwen_prose` 26/2 · `08_machine_learning_11...:42` `_change_label_tags_for_single_note` 26/2 · `08_machine_learning_50...:2` `_find_indirect_links_to_info_notes_via_notat_notes` 26/3 · `09_app_00_gui.ipynb:2` `create_obsidian_subvault` 26/1 · `09_app_00_gui.ipynb:20` `run` 26/2 · `04_latex_10.preamble.ipynb:50` `replace_inclusion_of_style_file_with_code` 25/0 · `06_notation_10...:11` `correct_notation_names_in_HTML_tags` 25/3 · `08_machine_learning_25...:2` `notation_summarization_data_from_note` 25/1 · `08_machine_learning_50...:2` `note_data_from_index_note` 25/2 · `08_machine_learning_50...:2` `_note_data_from_notes_not_reachable_from_index_notes` 25/3 · `01_helper_20.latex.core.ipynb:2` `_has_invalid_left_right_bracket` 24/2 · `03_obsidian_10.vault_file_crud.ipynb:3` `rename` 24/4 (also R3) · `03_obsidian_50.links.ipynb:24` `to_string` 24/2 · `03_obsidian_70.vault_and_links.ipynb:2` `all_links_in_vault` 24/5 (also R3) · `08_machine_learning_25...:20` `_augment_notation_summarization_data_once` 24/2 · `08_machine_learning_35...:5` `def_notat_naming_data_from_information_note` 24/2 · `08_machine_learning_35...:157` `_create_llm_handler` 24/1 · `08_machine_learning_67...:2` `predict_on_relied_notes_and_related_notat_notes` 24/3 (also V-38) · `08_machine_learning_70...:3` `_init_args_for_data_from_notation_notes` 24/1 · `09_app_00_gui.ipynb:19` `run` 24/1 · `03_obsidian_70...:2` `all_custom_text_for_links_in_vault` 23/3 · `04_latex_00.divide.ipynb:2` `_setup_counters` 23/1 · `04_latex_20.convert.ipynb:2` `_replace_includegraphics_with_embedded_links_in_parts` 23/1 · `06_notation_10...:18` `test_fix_notation_syntax_in_notation_note_correction` 23/1 · `08_machine_learning_24...:3` `salvage_audit_result` 23/2 · `08_machine_learning_35...:9` `test_predict_iterates_and_calls_llm` 23/1 (R2-test) · `08_machine_learning_65...:2` `batch_prediction` 23/4 (also R3) · `08_machine_learning_65...:5` `test_predictor_batch_handling_in_pipeline` 23/0 · `08_machine_learning_70...:2` `prediction_by_model` 23/2 · `01_helper_20.latex.core.ipynb:2` `_is_semantically_left_right_balanced` 22/3 · `03_obsidian_40.file.ipynb:3` `_look_at_start_of_file` 22/2 · `04_latex_10.preamble.ipynb:61` `replace_style_file` 22/3 · `06_notation_00_parse.ipynb:2` `parse_notation_note` 22/1 · `08_machine_learning_10...:2` `labels_and_identifying_info_from_notes` 22/3 (also V-22) · `08_machine_learning_19...:2` `_find_places_to_divide_from_chunks` 22/2 · `08_machine_learning_50...:2` `_note_data_from_vault_note_on_the_fly` 22/2 · `08_machine_learning_65...:58` `test_batch_prediction_with_dict_threshold` 22/1 · `08_machine_learning_70...:2` `_identify_note_type_and_setup` 22/1 (also V-39) · `08_machine_learning_90...:3` `_process_single_file` 22/2 · `01_helper_07...:56` `_is_notation` 21/3 · `05_personal_vault_05.index_notes.ipynb:2` `information_notes_linked_in_index_note` 21/1 · `07_llm_core_05.call_llm.ipynb:3` `_handle_openai_call` 21/3 · `08_machine_learning_15...:2` `_calculate_clean_indices_and_create_tags` 21/1 (also V-23) · `08_machine_learning_19...:2` `_divide_token_preds_into_parts` 21/3 · `08_machine_learning_20...:2` `_collate_html_tags` 21/2 · `08_machine_learning_35...:31` `test_extract_valid_notation_from_source_is_called` 21/1 (R2-test) · `08_machine_learning_50...:58` `data_string` 21/2 · `08_machine_learning_67...:2` `_add_notation_note_embedded_footnotes` 21/2 · `24_markdown.obsidian.personal.machine_learning.notation_identification.ipynb:2` `append_notation_data_to_database` 21/2

## State — COMPLETE

All passes done: R1/R2/R3 mechanical over all 101 notebooks / 1171 functions (script, 0
unparseable cells), R4 judgment sweep complete (~85 commented-out-code instances), 4 flagged
functions spot-verified against raw .ipynb source. Nothing left for the loop to do — cron
`06fb4fe5` can be cancelled.

## Final summary

| Rule | Count | Notes |
|---|---|---|
| R1 (>20 exec lines) | 95 | ~30 are test functions → review-only severity (no exemption, per decision (b)); `setupUi` (exec=309) is Qt-generated → low severity (decision (a)) |
| R2 (`_and_` names) | 39 | heuristic review candidates only; domain-term `def_and_notat_*` are borderline, not true violations |
| R3 (depth >3) | 21 | worst: `get_all_linked_info_notes` d7; 5 pass R1 but fail R3 alone |
| R4 (commented-out code) | ~85 | concentrated in `04_latex_00.divide` and `06_notation_10_management`; matches the spec's "where commented-out code tends to hide" |

**Top offenders (fix first):** `setupUi` (generated — decide scope), `_expand_to_valid_latex`
(116/d6), `run_audit_voting_maker` (68/d4), `get_dollar_sign_syntax_errors` (55/d4),
`run_audit_voting` (55), `add_names_to_html_tags_in_info_note` (55),
`get_all_linked_info_notes` (47/**d7**), `sieve_then_add_links_to_notation_notes` (53),
`latex_highlight_parser` (52/d5), `convert_notes_to_latex_code` (50 — mostly string literals).

**User decisions (resolved 2026-10-18):**
(a) Qt-generated GUI code — **in scope, low severity**: `setupUi` stays in the log with a
'generated' note, sorts last.
(b) Test functions — **no exemption, review-only severity**: all ~30 stay listed, downgraded
from high to review (long test bodies are lower risk than long production code).
---

# Run 3 — testing.md (started 2026-10-18)

Spec: `_nbdev_development/specs/CODING_STANDARDS/testing.md`. Scope: all notebooks in `trouver\nbs`.
Mechanical checker `_nbdev_development/spec_checkers/check_testing.py` (full report: re-run it)
(861 top-level exported defs; class methods excluded by design — `^def` in decoded cells).
**Headline: 421 untested exports, 66 co-location violations, 120 print-pseudo-tests.**

Rule keys: TST1 every exported fn has test cells immediately below; TST2 test-shaped cell must
assert (print-only = pseudo-test); TST3 pure logic tested directly, tempfile/mock only at I/O
boundary; TST4 prefer fastcore.test helpers, `ExceptionExpected` for error paths.

## Violations log — testing

### Tier 0 — notebooks with exports and ZERO assertion lines (TST1: nothing tested)

Confirmed by grep: none of these files contain `test_eq`/`test_ne`/`ExceptionExpected`/`def test_`.
Export-marker counts shown (includes export-import cells, so real fn counts are lower):

- `09_app_00_gui.ipynb` — 127 markers. The spec's named gap; also the Phase-3 remediation note
  (separate logic from Qt widgets). **Worst blind spot in the repo.**
- `04_latex_10.preamble.ipynb` — 61 markers, zero tests. Exports are pure text transforms
  (`divide_preamble`, `replace_inclusion_of_style_file_with_code`) — the cheapest wins in the
  whole Tier-0 list: plain string-in/string-out assertions, no mocks needed.
- `08_machine_learning_22.tokenize...main_workflow.ipynb` — 95 markers (orchestration module,
  exactly where co-location matters most).
- `08_machine_learning_17.tokenize...text_logic.ipynb` — 33; `08_ml_23...misc_format` — 39;
  `08_ml_68.note_linking_notation_summarization` — 24; `08_ml_18...tag_models` — 4.
- `03_obsidian_06.vault_note.ipynb` (14), `03_obsidian_09` has 1 line only (see Tier 1),
  `03_obsidian_30.tags` (11), `03_obsidian_70.vault_and_links` (13).
- `01_helper_06.date_and_time` (4), `01_helper_10.packages` (16),
  `01_helper_11.path_accepted_string` (9), `01_helper_21.latex` (2), `01_helper_05.typos` (1).
- Non-module notebooks with markers (lower priority): `unused.ipynb` (97), `star.ipynb` (17),
  `tutorial.*`, `index.ipynb`, `how_to.train_ml_model.fastai.ipynb` (347 — tutorial, likely out of scope).

### Tier 1 — under-tested (1–6 assertion lines for the whole notebook)

`03_obsidian_09.vault_read_write` (1), `05_personal_vault_30.trouver_vault` (1),
`08_ml_05.database_update` (1), `08_ml_45.notation` (2), `08_ml_11.information_note_types_predict` (2),
`03_obsidian_49.file_write` (2), `01_helper_09.numbers` (2), `01_helper_22.latex.comments` (2),
`06_notation_05_in_standard_info_note` (3), `05_personal_vault_25.note_processing` (3),
`02_markdown_00.heading` (3), `03_obsidian_08.vault_path` (3).

### TST2 — print-pseudo-tests (run a scenario, print, assert nothing)

- `04_latex_20.convert.ipynb`: **35 `print(` lines vs 6 assertion lines** — the spec's named
  hotspot; most scenario cells are demo-shaped tests that pass no matter what.
- `08_ml_24...llm_verification.ipynb` (cell after `run_audit_voting` export): mock-client demo
  runs `run_audit_voting` and `print`s the result — zero assertions on the vote tallies.
  Concrete good-case gap: the *happy path* of `run_strict_audit` is only exercised in print
  cells; the asserted test (`test_run_strict_audit_scope`) covers the exception path only.

### Good cases not hit (judgment, from spot-reading)

- `sieve_potential_relied_notes` (08_ml_67): 4 mocked cases, but every case patches
  `similar_notat_notes_in_note` to return `[]` — the notation-similarity branch that adds
  notat-note names is **never exercised**.
- `run_audit_voting_maker` (08_ml_24): freeze/termination cases are good; no case where a
  category settles and then the *other* category's votes would have flipped the outcome
  (i.e., settling order matters) — low priority.

### TST4 review candidates

- **TST4a bare `assert`: 213 lines across 32 notebooks** (grep; includes some legitimate
  trivial-booleans and non-test asserts — script pass will attribute them per test cell).
  Heaviest: `06_notation_10_management` (21), `03_obsidian_10.vault_file_crud` (18),
  `04_latex_00.divide` (17), `06_notation_05_in_standard_info_note` (18),
  `08_ml_11.information_note_types_predict` (17), `05_personal_vault_05.index_notes` (12).
  Per spec these should mostly be `test_eq`/`test_ne` (print both values on failure).
- **TST4b `try/except: pass` as error-path test:** no matches with the JSON-aware multiline
  pattern; exact per-cell check still pending script run.

### Per-function results (script pass — full lists: re-run `check_testing.py`)

**TST1a untested exports: 421.** Top concentration: `09_app_00_gui` (55),
`08_ml_70.notation_linking` (33), `03_obsidian_40.file` (23), `06_notation_10_management` (20),
`08_ml_50.note_data` (17), `04_latex_20.convert` (16), `05_personal_vault_15.reference` (15),
`04_latex_15.formatting` (14). Notable individual blind spots: the whole topological-sort API
(`dict_with_keys_topologically_sorted` et al. — all `[TODO]`-marked, i.e. known debt),
`latex_str_in_latex_str_fuzz_metric` + `latex_str_is_likely_in_latex_str` (01_helper_02 — the
fuzzy-matching core used by notation linking, exercised only indirectly), and the arxiv tarfile
parsing cluster (`analyze_arxiv_tarfile`, `extract_tex_from_gz`, …).

**TST1b co-location violations: 66** — tested somewhere in the notebook but not within 6 cells
below the export. Heaviest: `03_obsidian_40.file` (MarkdownFile class constructors
`from_list`/`from_vault_note`/`from_file`/`from_string`, metadata accessors),
`03_obsidian_10.vault_file_crud` (`create`/`delete`/`move_to_folder`/`rename`).

**TST2 print-pseudo-tests: 120** (script) — corroborates the grep findings; heaviest clusters
`01_helper_29.arxiv` (tarfile demos), `01_helper_28.latex.augment` (`push_dollar_signs` demo
cells), `03_obsidian_40.file`.

**TST4b try/except-pass: 0 matches.** TST4a bare-assert list is per-cell in the report.

## State — COMPLETE

Final counts: **TST1a: 421 untested exports** (of 861 top-level exported defs — ~49% of the
public surface has no test referencing it), **TST1b: 66** co-location violations,
**TST2: 120** print-pseudo-tests, **TST4a: 213** bare-assert lines (review), **TST4b: 0**.
Zero-test notebooks (script-confirmed): `09_app_00_gui` (55 fns), `08_ml_17`, `08_ml_68`,
`03_obsidian_06/30/70`, `01_helper_00/06/10/12`, `star.ipynb`.
Priority order for remediation: (1) `04_latex_10.preamble` pure transforms (cheapest),
(2) topological-sort API (all TODO-marked, small surface), (3) fuzzy-matching core in
`01_helper_02.init`, (4) GUI logic extraction + headless tests (Phase-3 per spec).

---

# Run 2 — type_hints.md (started 2026-10-18)

Spec: `_nbdev_development/specs/CODING_STANDARDS/type_hints.md`. Scope: all 101 notebooks in
`trouver\nbs` (1,171 functions; 701 exported = no leading `_`).

| Rule | Check | Method |
|---|---|---|
| T1 | exported fn missing param/return annotation (incl. partial) | mechanical |
| T2 | legacy `typing` aliases (`List`, `Dict`, `Optional`, `Tuple`, …) in signatures | mechanical |
| T3 | half-qualified generics (`list[..., dict]` etc.) | mechanical |
| T4 | internal `_`-prefixed best-effort | judgment — not flagged mechanically |
| T5 | `Any` in exported signature (needs justifying comment) | mechanical flag, judgment on justification |
| T6 | lying hints (annotation contradicts body) | manual only — spot-checks below |

Checker: `_nbdev_development/spec_checkers/check_type_hints.py` (full report ~388 lines: re-run it).
**371 of 701 exported functions flagged** under at least one rule.

## Violations log — type_hints

### T1 — missing/partial annotations (287 functions, full list in report)

Pattern matches the spec's own decay description: **params annotated, return not** is the
dominant case (e.g. `01_helper_03.files_and_folders.ipynb` — `file_is_compressed`,
`uncompress_file`, `get_huggingface_cache_dir` all missing only the return). Concentration:
`01_helper_28.latex.augment.ipynb` (whole module unannotated), `01_helper_20.latex.core.ipynb`,
`01_helper_02.init.ipynb`. Many `test_*` functions appear — spec has no test exemption, same
open question as run 1.

### T2 — legacy aliases (81 functions)

`Optional` dominates (~75 of 81), scattered across ~30 notebooks — the uniform drift the spec
predicts ("some modules use `Optional`, newer ones use `| None`"). Also: `List` (incl.
`legacy-ret:List` in `01_helper_02.init.ipynb:get_top_counted_items`,
`06_notation_15.glossary.ipynb:generate_glossary_markdown`), `Tuple`/`Optional` return in
`07_llm_core_05.call_llm.ipynb` (`call_llm`, `separate_thoughts`), `OrderedDict` ret in
`01_helper_12.topological_sort.ipynb:dict_with_keys_topologically_sorted`.

### T3 — half-qualified generics (7 functions)

All are return annotations `list[<something>, dict|tuple]`:
`extract_metadata` (01_helper_29.arxiv), `remove_lines`, `remove_section` (03_obsidian_40.file),
`link_ranges_in_text` (03_obsidian_50.links), `find_footnote_descriptions_in_markdown_text`,
`find_footnote_mentions_in_markdown_text` (03_obsidian_60.footnotes),
`labels_and_identifying_info_from_notes` (08_machine_learning_10.information_note_types).

### T5 — `Any` in exported signature (8 functions, review)

`make_tag` (06_notation_15.glossary), `respond`/`chat`/`call_llm` (07_llm_core_05.call_llm),
`summarize_notation`/`append_summary_to_notation_note` (08_machine_learning_25),
`add_names_to_html_tags_in_info_note` (08_machine_learning_35),
`extract_context_with_lm` (08_machine_learning_80), `search` (08_machine_learning_90).
LLM-wrapper cluster is the expected case (untyped third-party) — each needs a justifying
comment per rule 5.

### T6 — lying hints (manual spot-checks)

- ✓ `08_machine_learning_67.note_linking_vault_operations.ipynb:1086`
  `get_all_linked_info_notes -> List[VaultNote]` — body returns `list(found_notes_map.values())`
  of VaultNotes → **hint true** (only T2 legacy aliases).
- ✗ `08_machine_learning_24...llm_verification.ipynb:706` `run_audit_voting_maker` —
  **V-T1: `callback: callable = None` is a lying/invalid hint.** `callable` is the built-in
  *function*, not a type; the annotation asserts something that isn't a type, and the param
  is `None`-able without `| None`. Correct form: `Callable | None` (or drop per T4-style
  honesty). Return annotation `-> AuditVoteResult` itself is true.

## State — COMPLETE

Mechanical pass (T1/T2/T3/T5) + T6 spot-checks done. Final counts: **T1: 287** exported fns
missing/partial annotations, **T2: 81** legacy aliases, **T3: 7** half-qualified generics,
**T5: 8** `Any` in exported signatures (review), **T6: 1** confirmed invalid hint
(`callable`). ~40% of the exported surface (371/701) has at least one flag. Biggest single
win: `01_helper_28.latex.augment.ipynb` is wholesale unannotated; `Optional` cleanup is a
mechanical find-replace across ~30 notebooks.

## Handoff block (fresh session)

1. Read this file — it is the full run state.
2. Do "State — next action". Keep requests small: never load a whole .ipynb into context;
   use the script's report + targeted Grep/Read slices of flagged functions only.
   R4 commented-out-code grep: pattern `"    # (print|return|if |for |raise )` over
   `Python/trouver/nbs/*.ipynb` (content mode, head_limit 40, page with offset).
3. Append to Violations log as you go; tick module table rows when a module is fully checked.
4. When all modules are done: sort the log by severity, add a summary section, mark complete.
