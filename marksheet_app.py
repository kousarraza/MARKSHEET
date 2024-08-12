import streamlit as st


def calculate_grade(percentage):
    if percentage >= 90:
        return 'A+'
    elif percentage >= 80:
        return 'A'
    elif percentage >= 70:
        return 'B+'
    elif percentage >= 60:
        return 'B'
    elif percentage >= 50:
        return 'C+'
    elif percentage >= 40:
        return 'C'
    else:
        return 'F'

def get_remarks(grade):
    if grade == 'A+':
        return 'Excellent'
    elif grade == 'A':
        return 'Very Good'
    elif grade == 'B+':
        return 'Good'
    elif grade == 'B':
        return 'Above Average'
    elif grade == 'C+':
        return 'Average'
    elif grade == 'C':
        return 'Below Average'
    else:
        return 'Fail'

def main():
    st.title("Marksheet Generator")
    
    num_subjects = st.number_input("Enter number of subjects:", min_value=1, step=1)
    
    if num_subjects > 0:
        marks = []
        for i in range(num_subjects):
            mark = st.number_input(f"Enter marks for subject {i+1}:", min_value=0, max_value=100, step=1)
            marks.append(mark)
        
        if st.button("Calculate"):
            total_marks = sum(marks)
            percentage = total_marks / num_subjects
            grade = calculate_grade(percentage)
            remarks = get_remarks(grade)
            
            st.write(f"**Total Marks:** {total_marks}")
            st.write(f"**Percentage:** {percentage:.2f}%")
            st.write(f"**Grade:** {grade}")
            st.write(f"**Remarks:** {remarks}")
    
if __name__ == "__main__":
    main()
