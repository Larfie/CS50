"""
 Copyright (c) 2022, Ricardo Madeira
All rights reserved.

This source code is licensed under the BSD-style license found in the
LICENSE file in the root directory of this source tree.  
"""

from project import bmi_formula, creatinine_clearance_formula, chadsvasc_score_analysis, validate


def main():
    test_bmi()
    test_validate()
    test_creatinine_clearance()
    test_chadsvasc


def test_bmi():
    assert round(bmi_formula(64, 190), 1) == 17.7


def test_validate():
    assert validate("0.0") == False
    assert validate ("0") == False
    assert validate("-1") == False
    assert validate("23.5") == True
    assert validate("23") == True


def test_creatinine_clearance():
    assert round(creatinine_clearance_formula("male", 60, 75, 1), 0) == 83 
    assert round(creatinine_clearance_formula("female", 60, 75, 1), 0) == 71
 

def test_chadsvasc():
    assert chadsvasc_score_analysis(0, "male") == {"Risk": "Low", "Therapy": "No anticoagulant therapy"}
    assert chadsvasc_score_analysis(1, "female") == {"Risk": "Low", "Therapy": "No anticoagulant therapy"}
    assert chadsvasc_score_analysis(4, "male") == {"Risk": "High", "Therapy": "Oral anticoagulant is recommended"}


if __name__ == "__main__":
    main()
