#  Federal Government Scholarship Eligibility Program
name = input("Enter your name: ")

citizenship = input("Are you a Nigerian?(Yes/No): ").strip().title()

if citizenship == "Yes":
    enrollment = input("Are you currently a full-time undergraduate student in Nigeria? (Yes/No): ").strip().title()
    if enrollment == "Yes":
        other_scholarships = input("Are you currently on any scholarship related to Oil and Gas industry? (Yes/No): ").strip().title()
        if other_scholarships == "No":
            academic_qualification = input("Do you have five distinctions (A's and B's) in relevant subsets in WASSCE (may/June) exams, including English and Mathematics? (Yes/No): ").strip().title()
            if academic_qualification == "Yes":
                # dept = input("What department are you?(Arts/Science/Commercial): ").title()
                dept = ""
                grade = []
                if dept != "Arts" or "Science" or "Commercial":
                    dept = input("What department are you?(Arts/Science/Commercial): ").title()
                    if dept == "Arts":
                        english = input("Kindly enter your grade for English: ").capitalize()
                        maths = input("Kindly enter your grade for Mathematics: ").capitalize()
                        gov = input("Kindly enter your grade for Government: ").capitalize()
                        lit_english = input("Kindly enter your grade for Literature-in-English: ").capitalize()
                        economics = input("Kindly enter your grade for Economics: ").capitalize()
                        grade.append(english)
                        grade.append(maths)
                        grade.append(gov)
                        grade.append(lit_english)
                        grade.append(economics)
                    elif dept == "Science":
                        english = input("Kindly enter your grade for English: ").capitalize()
                        maths = input("Kindly enter your grade for Mathematics: ").capitalize()
                        phs = input("Kindly enter your grade for Physics: ").capitalize()
                        chm = input("Kindly enter your grade for Chemistry: ").capitalize()
                        bio = input("Kindly enter your grade for Biology: ").capitalize()
                        grade.append(english)
                        grade.append(maths)
                        grade.append(phs)
                        grade.append(chm)
                        grade.append(bio)
                    elif dept == "Commercial":
                        english = input("Kindly enter your grade for English: ").capitalize()
                        maths = input("Kindly enter your grade for Mathematics: ").capitalize()
                        acc = input("Kindly enter your grade for Accounting: ").capitalize()
                        gov = input("Kindly enter your grade for Government: ").capitalize()
                        economics = input("Kindly enter your grade for Economics: ").capitalize()
                        grade.append(english)
                        grade.append(maths)
                        grade.append(acc)
                        grade.append(gov)
                        grade.append(economics)
                    else:
                        print("You entered the wrong details!")
                        
                    if set(grade) == {"A", "B"}:
                        print(f"Congratulation {name}! You are eligible for this scholarship")
                    else: 
                        print("Sorry, You did not meet the academic criteria therefore you're not eligible for the scholarship.")
                        
                else:
                    print("You entered the wrong details!")
            else:
                print("Sorry, You did not meet the scholarship criteria.")
                
        else:
            print("You can't be on another scholarship at the time of application.")
    else:
        print("Sorry, You must be a fulltime undergraduate at the time of application.")

else:
    print("You must be a Nigerian to qualify for this Scholarship!")