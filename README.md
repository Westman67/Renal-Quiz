# Renal Picture Quiz

The reviewed bank uses 62 manual lecture captures from R1, R2, R4, R5, R6, R7, R8, and R9. It has 95 questions from 38 scored image families. Nineteen captures remain teaching references or alternate annotated views, including two R6 and two R7 H&E crops whose resolution, clipping, or labels prevent fair scoring. Coverage of each lecture remains partial.

## Open locally

Double-click `Start Quiz.command`. Keep its terminal window open while studying. Close it with Control-C when finished.

The launcher uses Python 3 and opens `http://127.0.0.1:8783`. No package installation or internet connection is required when Python is available. If that port is busy, run `python3 scripts/serve.py --port 8766 --open` from this app folder. Do not open `index.html` directly with a file URL.

## Study

Select Learn for immediate feedback or Exam for feedback only after finishing. Back and Next preserve drafts and locked answers. You may skip questions. Unanswered items are reported separately. Use 1–4 to choose, Enter to submit or advance, and Z or the image controls to zoom. Drag a zoomed image to pan. Every new question starts fitted to its frame.

Mode and session length use selectable boxes. Lecture boxes allow one lecture or a mixed selection as the bank grows. The Start button shows the actual available session size, even when the requested length is larger. Endless practice labels the pool size rather than promising a finite session.

Menu preferences are remembered in this browser separately from progress. On mobile, practice controls come first and the question appears above its image. Full image is available before answering, but displays only the safe quiz version until feedback is available. The teaching original remains hidden during an unfinished Exam.

The home screen's Lecture coverage summary distinguishes tested topics from known missing coverage. Expand each lecture to see its gaps. This is not a mastery score or a claim that every listed topic is covered exhaustively.

The Keanne Button changes an incorrect locked attempt to correct without changing your selection or adding an attempt. The correction gets its own visual treatment. Previously incorrect uses the latest result, not a lifetime miss count.

Unseen uses shared source history. Questions from the same visual are related, not independent unseen images. Sessions rotate source groups before showing another question from the same image when alternatives remain. Endless practice repeats the selected pool with source-aware ordering. Small filtered pools may necessarily repeat a source consecutively.

Use Your progress to export, import, or reset browser-local data. Export before changing browsers, clearing storage, or moving from a local address to a hosted address. Nothing is sent to a server. Imports replace local progress only after confirmation.

## Upload yourself

The `dist` folder is a self-contained static site. Upload its contents as the site files, with `index.html` at the site root. Relative asset paths support a repository subdirectory. No API keys, backend, package install, or build service are required for the finished site. No upload or repository creation has been performed for you.

Only upload the app or `dist`, not the enclosing Picture Quiz library. Before making the site public, confirm that you have permission to redistribute the course images. Redistribution permission has not been verified. This app contains original teaching copies as well as masked or cropped quiz images.

Client-side answer hiding is a study-interface feature, not security. Someone inspecting the static data can see the answer keys.

## Validate or rebuild

Node.js is needed only for development tests and building the static upload folder.

```sh
npm test
npm run build
```

There are no JavaScript dependencies to install. `scripts/validate_bank.py` validates the source/question contract. `scripts/verify_images.py` additionally validates hashes, formats, and exact unchanged pixels outside approved masks or crops. Run it with `--source` pointing to the `Renal/Manual` root.

`scripts/build_bank.py` and `scripts/write_questions.py` reproduce the original R1 pilot only; they are retained for provenance and must not be run over this mixed bank. The earlier mixed-bank recipe is `scripts/rebuild_existing.py`; do not rerun it over this later bank. The append-only recipes are `scripts/add_r6.py`, `scripts/add_r7.py`, `scripts/add_r8.py`, `scripts/add_r5_r8_new_captures.py`, and `scripts/add_r9_course_grounded.py`, with explicit full-size reviews in `scripts/review_r6.py` and `scripts/review_r7.py`. These scripts verify source hashes and create app-local derivatives. No script extracts new PDF images or edits source captures.

## Add future lectures

Keep new screenshots in a separate manual lecture folder. Request the quiz-maker workflow for that lecture and approve its prompt. Append validated sources/questions with stable IDs. Preserve existing IDs and browser-storage version so prior progress remains compatible. Do not replace the existing bank with a lecture-only bank.

Lecture-selection boxes appear automatically from question collection values. Add a source-backed entry to `data/coverage.json` for each audited lecture. Lectures without an entry are explicitly shown as not yet audited rather than assumed complete.

## Review and provenance

Source review includes all 62 originals and local reviewer decisions. Learner flags can be resolved and deliberately reopened. Export decisions to guide a future correction build. Decisions do not auto-activate unvalidated images.

`reports/preflight-audit.md` describes selection and limitations. `data/source-manifest.json` preserves hashes, source-slide citations, grouping, and reproducible edit coordinates. `data/question-bank.json` contains option-aligned rationales and citations. No web sources or invented clinical cases were used. The R4 resistance table has 16 distinct masked-arrow questions from one shared source group, not 16 independent photos. The two R6 SEM views share one source group, and the mitochondria EM supports separate yellow-arrow and red-arrow questions.

Educational use only. Not clinical guidance.

The R7 import uses six distinct questions from three scored EM captures. Both arrow colors in the collecting-duct TEM, both cell populations in the starred surface EM, and two separately visible distal-tubule EM features are tested. Two labeled or soft H&E captures remain Source review references.

The R8 import uses one complete manual flowchart and eleven separate safe masks for renal autoregulation, RAAS, baroreflex, ADH, thirst, and ANP targets. All eleven questions share one source group. The original capture is preserved, and no unprovided R8 picture or clinical measurement was invented.

## R5–R8 added-photo import, 2026-10-05

Twenty-four new filenames were reviewed. One renamed R6 H&E image was byte-identical to a pre-existing reference, leaving 23 new physical sources. Eighteen new captures are scored with 22 additional visual questions, and five remain references. Original manual captures were not edited. R5 and R6 transporter/feedback diagrams, R7 cell mechanisms, and R8 hormone diagrams now supplement the earlier EM and flowchart bank. Multiple independently identifiable targets were tested separately where supported. The R6 clipped-axis TF/P graph and four R7 text-only cards were not forced into scored picture questions. Existing question IDs and browser progress remain compatible. Full lecture coverage is not claimed.

## R9 course-grounded addendum, 2026-10-05

Four manual R9 PNGs were visually matched to the user-supplied R9 RLS. Three scored captures support four dedicated questions on the unmeasured-anion band, fixed-acid widening of the gap, and two proximal glutamine/ammonium/bicarbonate pathways. The two anion-gap pictures share a source group. The fourth, a thin text-only chart, remains a teaching reference. Existing IDs and local progress remain compatible. Two pre-existing R8 Part 5 transcript citations were corrected from nonexistent page 3 to page 2. No source capture was edited, and no internet source was used.
