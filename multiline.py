# Triple-quoted f-strings for long templates
name    = "Sneha Reddy"
marks   = 91
grade   = "A+"
school  = "Delhi Public School"

certificate = f"""
===========================================
           CERTIFICATE OF MERIT
===========================================
This is to certify that

  Student Name : {name}
  School       : {school}
  Total Marks  : {marks}/100
  Grade        : {grade}

Congratulations on your {'outstanding' if marks >= 90 else 'excellent'} performance!
==========================================="""

print(certificate)
