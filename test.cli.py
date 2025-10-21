from quickumls import QuickUMLS

matcher = QuickUMLS('/Users/pearsosj/umls/QuickUMLS.db');
text = "To provide funding and project support  to further develop and validate established biomarkers to meet clinical needs in Alzheimer's disease and related dementias. Priority focus: developing novel PET ligands for clinical trials, validating innovative MRI approaches in larger cohorts, and developing novel measures of functional activity such as EEG."
json = matcher.match(text, best_match=True, ignore_syntax=False)
print(json)
