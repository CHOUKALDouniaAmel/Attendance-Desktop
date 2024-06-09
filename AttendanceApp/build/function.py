import subprocess

def on_click(current_window, script_path):
   current_window.destroy()  # Close the current window
    
   # Run the new Python script
   subprocess.Popen(["python", script_path])
