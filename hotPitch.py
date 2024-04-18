# WTF is going on 
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

# Function to draw hexagons for tech skills
def draw_hexagon(canvas, x, y, width):

    canvas.saveState()

    # draw a test line to confirm coord
    # canvas.line(x,y - width/2, x, y + width/2)

    canvas.translate(x, y)

    canvas.rotate(0)

    for _ in range(6):
        canvas.rotate(60)
        if _ == 0 or _ == 3:
            canvas.setStrokeColor("red")
        if _ == 1 or _ == 4:
            canvas.setStrokeColor("green")
        if _ == 2 or _ == 5:
            canvas.setStrokeColor("blue")

        canvas.line(-width/2, -width/4, 0, -width/2)
    canvas.restoreState()
    
# Function to draw ovals for soft skills
def draw_oval(canvas, x, y, width, height):
    canvas.saveState()
    canvas.translate(x, y)
    canvas.scale(width, height)
    canvas.arc(0, 0.5, 1, 0.5, 0, 360)
    canvas.restoreState()

# Function to draw balloons for goals
def draw_balloon(canvas, x, y, width, height):
    canvas.saveState()
    canvas.translate(x, y)
    canvas.scale(width, height)
    canvas.arc(0, 0, 1, -0.5, 0, 180)
    canvas.line(0, 1, 10, 1)
    canvas.restoreState()

# Function to generate the PDF
def generate_pdf(voice_input):
    print("top generate_pdf()\n")

    c = canvas.Canvas("hotPitch.pdf", pagesize=letter)

    print("after canvas  in generate_pdf()\n")

    # Parse voice input and draw elements
    tech_skills = voice_input["Tech Skills"]
    soft_skills = voice_input["Soft Skills"]
    goals = voice_input["Goals"]
    job_entries = voice_input["Job Entries"]

    # Draw tech skills
    x, y = 150, 700         # was 50, 700
    size = 40
    for skill, rating in tech_skills.items():
        draw_hexagon(c, x, y, size)
        c.drawString(x - 15, y - 15, f"{skill}: {rating}")
        x += 100

    # Draw soft skills
    x, y = 50, 600
    width, height = 40, 20
    for skill, rating in soft_skills.items():
        draw_oval(c, x, y, width, height)
        c.drawString(x - 20, y - 15, f"{skill}: {rating}")
        x += 120

    # Draw goals
    x, y = 50, 500
    width, height = 40, 30
    for goal in goals:
        draw_balloon(c, x, y, width, height)
        c.drawString(x - 20, y - 15, goal)
        x += 150

    # Draw job entries
    x, y = 50, 400
    for entry in job_entries[::-1]:  # Reverse to have most recent on top
        role, company, time_interval, accomplishment = entry
        c.drawString(x, y, f"{role} at {company} ({time_interval})")
        c.drawString(x, y - 15, f"- {accomplishment}")
        y -= 30

    c.save()

# Example usage
voice_input = {
    "Tech Skills": {"Python": 7, "JavaScript": 5, "C++": 6},
    "Soft Skills": {"Communication": 7, "Teamwork": 6, "Problem Solving": 6},
    "Goals": ["Learn AI technologies", "Obtain leadership role"],
    "Job Entries": [
        ("Software Engineer", "ABC Inc.", "2020-2022", "Developed new features"),
        ("Web Developer", "XYZ Corp.", "2018-2020", "Designed responsive websites"),
    ],
}

generate_pdf(voice_input)