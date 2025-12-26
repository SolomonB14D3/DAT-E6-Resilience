#!/bin/bash
# Synchronizes CITATION.bib with the Zenodo DOI 10.5281/zenodo.18051097
VERSION=$(grep "version:" CITATION.cff | awk '{print $2}' | tr -d '"')

cat << EOB > CITATION.bib
@software{DAT_E6_Resilience_2025,
  author = {Bryan Lab},
  title = {DAT-E6-Resilience: A Computational Framework for DAT 2.0},
  version = {${VERSION}},
  doi = {10.5281/zenodo.18051097},
  url = {https://github.com/SolomonB14D3/DAT-E6-Resilience},
  year = {2025}
}
EOB
echo "✅ CITATION.bib synchronized with Zenodo DOI."
