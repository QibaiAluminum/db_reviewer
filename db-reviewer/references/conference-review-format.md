# Conference Review Format

## Required Sections

If the venue form is not provided, use the following default review structure and check that all of
the following are present before finalizing:

1. Summary
2. Strengths
3. Weaknesses
4. Questions
5. Limitations
6. Scores

## Section Expectations

### Summary

- Keep this short. Three to five sentences is enough.
- State the method, the main claim, and the main empirical takeaway.
- Do not try to summarize every experiment or theorem.

### Strengths / Weaknesses

- Use numbered paragraphs, not bullet lists.
- Each numbered item should focus on one independent point.
- Do not reuse numbers or merge unrelated complaints into a single block.

### Questions

- Ask three to five questions.
- Separate critical questions from ablation or clarification suggestions.
- For each question, explain how the answer would affect the score or confidence.
- Prefer questions that force the authors to explain existing evidence over questions that only ask
  for entirely new experiments.

Suggested labels:

- `Critical:` answer needed to support the core claim
- `Suggestion:` useful but not review-determining

### Limitations

- Briefly judge whether the authors discuss limitations with enough honesty and specificity.

### Scores

Do not omit:

- Soundness
- Presentation
- Contribution
- Overall
- Confidence

If you internally reason about originality or significance, use that to calibrate contribution and
overall rather than adding extra score fields unless the venue explicitly asks for them.

## Venue Adaptation Rule

- If the user provides the official review form or score fields, mirror that structure exactly.
- If no form is provided, use the default structure above.
- Keep the section names generic unless the venue requires different labels.
- For database venues, place more weight on systems evidence, workload realism, and end-to-end
  evaluation.
- For ML venues with database or data-centric tracks, keep the same core structure but calibrate the
  technical concerns against method framing, statistical validity, and comparison fairness.

## Calibration Notes

- Strong assumptions plus existence-only theory usually cap soundness unless the empirical support
  is unusually strong.
- Experimental self-consistency with missing key ablations often lands between fair and good.
- Small synthetic experiments without real-world validation usually cap contribution.
- Clear writing and readable tables often justify a good presentation score even when the paper has
  technical weaknesses.
- A method can work empirically and still deserve a lower overall score if the theory framing is
  misleading or the evidence is incomplete.
