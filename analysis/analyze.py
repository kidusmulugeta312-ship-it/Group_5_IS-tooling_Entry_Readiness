"""Descriptive analysis of a reviewed graduate-only, de-identified survey CSV."""
import argparse
import csv
from collections import defaultdict
from pathlib import Path
from statistics import mean

CATEGORIES = ('version_control', 'containers', 'ci_cd', 'cloud_deployment', 'frameworks', 'agile_tracking')
RATINGS = ('curriculum_exposure', 'current_proficiency', 'required_proficiency', 'workplace_importance', 'readiness_1', 'readiness_2', 'readiness_3', 'readiness_4')
FIELDS = ('respondent_id', 'pathway', 'tool_category') + RATINGS

def run():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', required=True)
    parser.add_argument('--output', default='analysis/output')
    args = parser.parse_args()
    with open(args.input, newline='', encoding='utf-8-sig') as handle:
        reader = csv.DictReader(handle)
        if not set(FIELDS).issubset(reader.fieldnames or []):
            raise ValueError('Missing required columns. See data dictionary.')
        rows = list(reader)
    if not rows:
        print('No responses found. No analysis results were generated.')
        return
    groups, people, seen = defaultdict(list), {}, set()
    for line, row in enumerate(rows, 2):
        rid, pathway, category = (row[k].strip() for k in FIELDS[:3])
        if not rid or pathway not in ('firm', 'freelance', 'hybrid', 'not_working') or category not in CATEGORIES:
            raise ValueError(f'Invalid identifier, pathway, or category at line {line}')
        if (rid, category) in seen:
            raise ValueError(f'Duplicate respondent/category at line {line}')
        seen.add((rid, category))
        for name in RATINGS:
            value = row[name].strip()
            if value and value not in ('1', '2', '3', '4', '5'):
                raise ValueError(f'Invalid rating {name} at line {line}')
            row[name] = int(value) if value else None
        readiness = tuple(row[f'readiness_{i}'] for i in range(1, 5))
        record = (pathway, readiness)
        if rid in people and people[rid] != record:
            raise ValueError(f'Inconsistent pathway or readiness for {rid}')
        people[rid] = record
        groups[category].append(row)
    output = Path(args.output)
    output.mkdir(parents=True, exist_ok=True)
    summaries = []
    for category, items in groups.items():
        gaps = [r['required_proficiency'] - r['current_proficiency'] for r in items if r['required_proficiency'] is not None and r['current_proficiency'] is not None]
        importance = [r['workplace_importance'] for r in items if r['workplace_importance'] is not None]
        exposure = [r['curriculum_exposure'] for r in items if r['curriculum_exposure'] is not None]
        summaries.append({'tool_category': category, 'n_rows': len(items), 'n_gap_pairs': len(gaps), 'mean_current_gap': mean(gaps) if gaps else '', 'n_exposure': len(exposure), 'mean_exposure': mean(exposure) if exposure else '', 'n_importance': len(importance), 'importance_rii': sum(importance)/(5*len(importance)) if importance else ''})
    summaries.sort(key=lambda r: (r['mean_current_gap'] == '', -r['mean_current_gap'] if r['mean_current_gap'] != '' else 0))
    def write(name, records):
        with (output/name).open('w', newline='', encoding='utf-8') as handle:
            writer = csv.DictWriter(handle, fieldnames=list(records[0]))
            writer.writeheader()
            writer.writerows(records)
    write('category_summary.csv', summaries)
    readiness_groups = []
    for pathway in ('firm', 'freelance', 'hybrid', 'not_working'):
        members = [scores for p, scores in people.values() if p == pathway]
        scores = [mean(s) for s in members if all(v is not None for v in s)]
        readiness_groups.append({'pathway': pathway, 'n_respondents': len(members), 'n_complete_readiness': len(scores), 'mean_provisional_readiness': mean(scores) if scores else ''})
    write('readiness_by_pathway.csv', readiness_groups)
    print(f'Processed {len(people)} unique respondents and {len(rows)} category rows. Descriptive outputs: {output}')

if __name__ == '__main__':
    run()
