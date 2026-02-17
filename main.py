from pyscript import display, document

# team registration
def check_requirements(e):

    registration = document.querySelector("input[name='reg_status']:checked").value
    medical_clearance = document.querySelector("input[name='med']:checked").value
    grade_level = document.getElementById("grade-level").value
    section = document.getElementById("section").value

    green_hornets = ["1. Dela Cruz", "2. Santos", "3. Reyes", "4. Bautista", "5. Garcia", "6. Mendoza", "7. Torres", "8. Ramos", "9. Flores", "10. Gonzales", "11. Aquino", "12. Navarro", "13. Castillo", "14. Morales", "15. Herrera", "16. Valdez", "17. Jimenez", "18. Cruz", "19. Fernandez", "20. Vargas", "21. Dominguez", "22. Salazar", "23. Aguilar", "24. Santiago", "25. Mercado"]
    red_bulldogs = ["1. Villanueva", "2. Cabrera", "3. Padilla", "4. Soriano", "5. Fajardo", "6. Alonzo", "7. Espinoza", "8. Robles", "9. Ventura", "10. Ponce", "11. Galang", "12. Manalo", "13. Macapagal", "14. Villamor", "15. Ong", "16. Tan", "17. Go", "18. Lim", "19. Sy", "20. Chua", "21. Uy", "22. Del Rosario", "23. Lucero", "24. Cuenca", "25. Evangelista"]
    blue_bears = ["1. Arceo", "2. Arellano", "3. Balagtas", "4. Banuelos", "5. Beltran", "6. Bonifacio", "7. Briones", "8. Caballero", "9. Cardenas", "10. Carpio", "11. Casimiro", "12. Celis", "13. Collado", "14. Cortez", "15. De Guzman", "16. De Leon", "17. Delos Santos", "18. Esguerra", "19. Estrella", "20. Ferrer", "21. Fontanilla", "22. Fortun", "23. Fuentes", "24. Gatchalian", "25. Gregorio"]
    yellow_tigers = ["1. Hilario", "2. Ibarra", "3. Ignacio", "4. Jacinto", "5. Lacsamana", "6. Ledesma", "7. Llamas", "8. Lopez", "9. Luna", "10. Macaraeg", "11. Malabanan", "12. Mangahas", "13. Marquez", "14. Matias", "15. Montemayor", "16. Natividad", "17. Ocampo", "18. Palacios", "19. Pangilinan", "20. Quinto", "21. Recto", "22. Regalado", "23. Samonte", "24. Sarmiento", "25. Yabut"]

    document.getElementById("team").innerHTML = ' '
    document.getElementById("team_photo").innerHTML = ' '
    document.getElementById("player_list").innerHTML = ' '

    if (grade_level == "g7" or grade_level == "g8" or grade_level == "g9" or  grade_level == "g10") and section == "e" and registration == "yes" and medical_clearance == "yes":
        display(f"You are part of the", target='team')
        document.getElementById("team_photo").innerHTML = "<img src='green_hornets.jpeg' height='300px' width='325px'>"
        for g in green_hornets:
            display(g, target='player_list')
    elif (grade_level == "g7" or grade_level == "g8" or grade_level == "g9" or  grade_level == "g10") and section == "r" and registration == "yes" and medical_clearance == "yes":
        display(f"You are part of the", target='team')
        document.getElementById("team_photo").innerHTML = "<img src='red_bulldogs.jpeg' height='300px' width='310px'>"
        for r in red_bulldogs:
            display(r, target='player_list')
    elif (grade_level == "g7" or grade_level == "g8" or grade_level == "g9" or  grade_level == "g10") and section == "s" and registration == "yes" and medical_clearance == "yes":
        display(f"You are part of the", target='team')
        document.getElementById("team_photo").innerHTML = "<img src='blue_bears.jpg' height='300px' width='325px'>"
        for b in blue_bears:
            display(b, target='player_list')
    elif (grade_level == "g7" or grade_level == "g8" or grade_level == "g9" or  grade_level == "g10") and section == "t" and registration == "yes" and medical_clearance == "yes":
        display(f"You are part of the", target='team')
        document.getElementById("team_photo").innerHTML = "<img src='yellow_tigers.jpeg' height='300px' width='325px'>"
        for y in yellow_tigers:
            display(y, target='player_list')
    else:
        document.getElementById("team_photo").innerHTML = "You are not qualified to participate in the OBMC Intramurals."

# sign up page
def acc_creation(e):
    document.getElementById('authorization').innerHTML = ' '

    username = document.getElementById('un').value
    password = document.getElementById('pw').value

    if not len(username) >= 7:
        display(f'Your username must contain at least 7 characters', target='authorization')
    elif password.isalpha():
          display(f'Your password must contain at least one number', target='authorization')
    elif password.isdigit():
            display(f'Your password must contain at least one letter', target='authorization')
    elif len(password) <= 10:
            display(f'Your password must contain at least 10 characters long', target='authorization')
    else:
        display(f'Account created', target='authorization')