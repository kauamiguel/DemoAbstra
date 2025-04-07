import abstra.forms as af
from abstra.tasks import send_task

# Set the background color to blue with 50% opacity
# Using rgba format where the last value (0.5) represents 50% opacity
af.set_background_color("rgba(0, 0, 255, 0.5)")

# Your form content
name = af.read("👋 Hello there! What is your name?")

# You can send tasks to the next stages of your workflow
send_task("greeting", {"name": name})

# Different kinds of input and output widgets are available
af.display(f"🎉 Welcome, {name}!")

af.display_markdown("Check out our [docs](https://abstra.io/docs/concepts/forms/) 📚")
