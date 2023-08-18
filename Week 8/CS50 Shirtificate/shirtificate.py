from fpdf import FPDF


class Shirtificate(FPDF):
    def header(self):
        self.set_font("Helvetica", "", 50)
        self.cell(0, 55, "CS50 Shirtificate", align="C")
    
    def create_shirtificate(self, name):
        # Page settings
        self.add_page()
        self.set_auto_page_break(auto=True, margin=15)
        self.set_margins(left=15, top=15, right=15)

        # Set font and color for the shirt text
        self.set_font("Helvetica", size=25)
        self.set_text_color(255, 255, 255)  # Black text
        
        # Add additional details, you can customize as needed
        self.cell(0, 10, name, align="C")

        # Add the shirt image centered horizontally
        self.image("shirtificate.png", x=10, y=70, w=190, h=190)

        # Add the user's name on the shirt image
        self.text(65, 140, name)


def main():
    # Get user's name
    name = input("Name: ")

    # Create and generate the shirtificate
    shirtificate = Shirtificate(orientation="P", unit="mm", format="A4")
    shirtificate.create_shirtificate(f"{name} took CS50")
    shirtificate.output("shirtificate.pdf")


if __name__ == "__main__":
    main()