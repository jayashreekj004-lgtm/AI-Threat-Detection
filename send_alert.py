import smtplib
import tkinter as tk
from tkinter import messagebox

sender_email = "abc@gmail.com"
app_password = "abcd dfhh dfrr"

receiver_email = "cfd@gmail.com"

try:
    # SMTP connect
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()

    # Login
    server.login(sender_email, app_password)

    # Message
    subject = "🚨 Alert Message"
    body = "Hey! This is a real-time alert from my project."

    message = f"Subject: {subject}\n\n{body}"

    # Send email
    server.sendmail(sender_email, receiver_email, message.encode('utf-8'))
    print("✅ Email Sent Successfully!")
    
    # Show GUI Alert
    root = tk.Tk()
    root.withdraw() # Hide the main window
    messagebox.showinfo("Alert", "✅ Email Alert Sent Successfully!")
    root.destroy()

    # Close
    server.quit()
except Exception as e:
    print(f"❌ Failed to send email: {e}")
    root = tk.Tk()
    root.withdraw()
    messagebox.showerror("Error", f"Failed to send email:\n{e}")
    root.destroy()
