from fpdf import FPDF
logo_file = "./cbse_logo.png"


# def draw_table():


def table_grade():
    dict_grades={

        'A+':['90% & Above','Excellent'],
        'A':['80 % - 89 %','Very Good'],
        'B':['70 % - 79 %','Good'],
        'C':['50 % - 69 %','Average'],
        'D':['40 % - 49','Satisfactory'],
        'E':['Bellow 40 %','UnSatisfactory'],
        
    }
    return  dict_grades

def table_grade_subject():
    dict_grades={

        'GK':['-','-','-','-'],
        'Theology':['A','B','C','B'],
        'Computer':['-','-','-','-'],
        'Art/Craft':['B/E','B/B','B/A','A/B'],
        'Converstion':['B','A','B','C'],
        
    }
    return  dict_grades

def table_total():
    dict_total={
        'Total Max Marks':[450,900,450,900,2700],
        'Total Marks Obtained':[306,515,268,528,1617],
        'Total Percentage':['68%',57.22,59.56,58.67,59.89],
    }
    return dict_total

def table_data():
    """
    
    Subject , 1st Assesment , Half Yearly , 2nd Assesment , Final , Total Marks , Percentage

    """
    dict_subject={
        'Subject':['1st Ass.','Half Yearly' , '2nd Ass.' , 'Final' , 'Total Marks' , '%'],
        'English I':[50,100,50,100,300,100],
        'English II':[50,100,50,100,300,100],
        'English S/D/R/W/R':[50,100,50,100,300,100],
        'Hindi I':[50,100,50,100,300,100],
        'Hindi II':[50,100,50,100,300,100],
        'Hindi S/D/R/W/R':[50,100,50,100,300,100],
        'Math':[50,100,50,100,300,100],
        'Science':[50,100,50,100,300,100],
        'Social Studies':[50,100,50,100,300,100],
        'Urdu':[50,100,50,100,300,100],
        'Urdu S/D/R/W/R':[50,100,50,100,300,100],
    }

    

    return dict_subject

def create_table_pdf(output_filename="report_card.pdf"):
    pdf = FPDF(format='A4')  # Creates a PDF object with A4 page size
    pdf.add_page()  # Adds a new page to the PDF

    # TOP Section Start Images and School Name 

    pdf.set_font("Arial", size=20)  # Sets the font to Arial, size 12
    pdf.image(logo_file, x=10, y=10, w=40,h=40) #try to add image
    pdf.image(logo_file, x=160, y=10, w=40,h=40) #try to add image   
    pdf.ln()              # Move to the next line (default line height)
    # pdf.write(10,"Mohd Numan") # Write text to the PDF
    # pdf.set_x(60)
    pdf.cell(180,10,"Aligarh Public School",align='C')
    pdf.set_font("Arial", size=12) 

    
    pdf.ln() 
    # pdf.set_x(60)
    pdf.cell(180,8,"90/209, Bewis Compound, Bans Mandi,",align='C')

    pdf.ln() 
    # pdf.set_x(60)
    pdf.cell(180,8,"Kanpur-208001, Uttar Pradesh, India",align='C')

    pdf.ln()   
    # pdf.set_x(60)
    pdf.cell(185,8,"Email : Aligarhpublicschool@rediffmail.com",align='C')
    

    pdf.ln()   
    pdf.ln() 
    pdf.ln()   
    pdf.ln() 


    # TOP Section Start Images and School Name 
    



    pdf.set_font("Arial", size=18) 
    pdf.cell(185,8,"Progress Report",align='C')
    pdf.ln()
    pdf.cell(185,8,"2023-2024",align='C')
    pdf.ln()
    pdf.ln()
    pdf.ln()
    pdf.ln()
    pdf.ln()
    pdf.ln()


    # Student Intro

    pdf.set_font("Arial", size=12) 


    pdf.set_draw_color(0, 0, 0)



    student_info={
        'Name':'',
        'Class':'',
        'Roll No.':'',
        'Adm. No':'',
        'Date Of Birth':'',
        'Father Name':'',
        'Address':'',
        'Mobile 1':'',
        'Mobile 2':'',
    }

    for i in student_info:

    
        pdf.cell(40, 10, txt=F"  {i}", border=1, align='L', fill=False)
        pdf.cell(100, 10, txt="  Mister Villain", border=1, align='L', fill=False)
        pdf.ln()


    pdf.ln()
    pdf.ln()
    pdf.ln()
    pdf.ln()

    pdf.add_page()


    # Table Header
    header = ["Subject Name", "Test - 1", "Test - 2", "Test - 3", "Exam", "Total Marks"]
    col_widths = [40, 20, 20, 20, 20, 25]  # Manually sets column widths in mm
    row_height = 10  # Sets the height of each row in mm

    pdf.set_fill_color(238,238,238)  # Sets the fill color for cells (light blue)
    # pdf.set_fill_color(0, 255, 0)  # Green
    # pdf.set_text_color(255, 0, 0) # Red
    pdf.set_draw_color(0, 0, 0)  # Sets the border color for cells (black)
    # x_start = pdf.get_x()  # Gets the current x position (left edge)
    # print(x_start)
    x_start= 10
    # Loop to create header cells
    pdf.cell(40,row_height,txt=' ',border=1,align='C')
    pdf.cell(105, row_height, txt='First Year', border=1, align='C', fill=True)
    pdf.ln()
    for i, col in enumerate(header):
        pdf.cell(col_widths[i], row_height, txt=col, border=1, align='C', fill=True)
    pdf.ln()  # Moves to the next line after the header

    # Table Rows
    data = [  # Sample table data
        ["English", 78.50, 82.75, 90.00, 88.20, 339.45],
        ["Math", 92.20, 85.50, 78.90, 95.00, 351.60],
        ["Science", 80.00, 75.00, 88.00, 70.00, 313.00],
        ["Social Studies", 70.50, 80.25, 75.60, 85.00, 311.35],
        ["Computer", 95.00, 90.50, 88.00, 92.75, 366.25],
    ]

    pdf.set_fill_color(255, 255, 255)  # Sets the fill color for data rows (white)

    # Loop to create data rows
    for row in data:
        pdf.set_x(x_start)  # Resets the x position at the beginning of each row
        for i, item in enumerate(row):
            # print(item)
            if isinstance(item, float):
                item = f"{item:.2f}"  # Formats float values to 2 decimal places
            pdf.cell(col_widths[i], row_height, txt=str(item), border=1, align='C', fill=False)
        pdf.ln()  # Moves to the next line after each row





    # 3rd Page
    pdf.add_page()
    print(table_data())
    dict_table=table_data()
    pdf.set_font("Arial", size=10) 
    pdf.set_fill_color(200, 220, 255) 
    for sub,marks in dict_table.items():
        print(sub,end=' ')
        fill_color=False
        if sub == 'Subject':
            fill_color=True
        pdf.cell(35, 10, txt=F' {sub}', border=1, align='L', fill=True)
        for i in marks:
            print(i,end=' ')
            pdf.cell(20, 10, txt=F' {i}', border=1, align='C', fill=fill_color)
        print()
        pdf.ln()

    
    pdf.ln()
    dict_table=table_total()
    for sub,marks in dict_table.items():
        print(sub,end=' ')
        fill_color=False
        if sub == 'Total Max Marks':
            fill_color=True
        pdf.cell(40, 10, txt=F' {sub}', border=1, align='L', fill=True)
        for i in marks:
            print(i,end=' ')
            pdf.cell(23, 10, txt=F' {i}', border=1, align='C', fill=fill_color)
        print()
        pdf.ln()



    pdf.ln()

    dict_table=table_grade()
    pdf.cell(80, 10, txt=F' Marks / Grade', border=1, align='C', fill=True)
    pdf.ln()
    for sub,marks in dict_table.items():

        print(sub,end=' ')
        fill_color=False
        if sub == 'Total Max Marks':
            fill_color=True
        pdf.cell(20, 10, txt=F' {sub}', border=1, align='L', fill=True)
        for i in marks:
            print(i,end=' ')
            pdf.cell(30, 10, txt=F' {i}', border=1, align='L', fill=fill_color)
        print()
        pdf.ln()



    # 4rd Page
    pdf.add_page()
    pdf.ln()
    dict_table=table_grade_subject()
    pdf.set_draw_color(0, 0, 0) 
    pdf.cell(90, 10, txt=F' Grade Subject', border=1, align='C', fill=True)
    pdf.ln()
    for sub,marks in dict_table.items():

        print(sub,end=' ')
        fill_color=False
        if sub == 'Total Max Marks':
            fill_color=True
        pdf.cell(30, 10, txt=F' {sub}', border=1, align='L', fill=True)
        for i in marks:
            print(i,end=' ')
            pdf.cell(15, 10, txt=F' {i}', border=1, align='C', fill=fill_color)
        print()
        pdf.ln()


    pdf.output(output_filename)  # Saves the PDF to the specified filename
    print('PDF Created')

if __name__ == "__main__":
    create_table_pdf()  # Calls the function to create the PDF
    print("PDF generated successfully!")