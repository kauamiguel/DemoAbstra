from abstra.compat import use_legacy_threads
"""
Calling the use_legacy_threads function allows using
the legacy threads in versions > 3.0.0
https://abstra.io/docs/guides/use-legacy-threads/

The new way of using workflows is with tasks. Learn more
at https://abstra.io/docs/concepts/tasks/ and contact us
on any issues during your migration
"""
use_legacy_threads("forms")

from typing import List, Union

import abstra.ai as ai
import abstra.forms as af
from abstra.tasks import send_task
from abstra_internals.widgets.response_types import FileResponse

af.display("Hello my friend")
af.display("Hello again")

### 📌 Abstra Forms is the easiest way to create dynamic forms that allow users to interact with your Python script.

# 💡 Use read functions to receive input types, like multiple choice, text, boolean, and more (check the docs for the full list):
best_movie = af.read_multiple_choice(
    "What is the best movie ever made?",
    options=[
        "Die Hard",
        "Devil Wears Prada",
        "Weekend at Bernie's",
        "American Psycho",
        "Legally Blond",
        "Wall-E",
        "Threat Level: Midnight",
        "Wolf of wall street"
    ],
)

# 💡 Use Python to control logic and the user interactions:
if best_movie == "Threat Level: Midnight":
    af.display("*Michael Scarn theme song plays* Congratulations! You're a genius.")
elif best_movie == "Die Hard":
    af.display("Yep, that's the one. Passed the vibe check.")
else:
    af.display(
        "Nope. The correct answer was 'Die Hard'. Not off to a great start here."
    )

# 💡 Explore more input widgets like read_toggle to get a True/False response:
interview_opt_in = af.read_checkbox(
    "Do you agree to participate in a interview with Prison Mike?", required=False
)

# 💡 Or even read_camera function to prompt the user to submit a photo:
object_photo = af.read_camera(
    "Quick, take a photo of the object on your left. Do it now! 📸"
)


def process_photo(photo: Union[FileResponse, List[FileResponse]]) -> FileResponse:
    if isinstance(photo, list):
        if len(photo) > 0:
            return photo[0]
        else:
            exit("No photo was submitted.")
    else:
        return photo


### 📌 Abstra AI is a powerful tool that allows you to prompt an AI model to extract data from images, generate text and more

# 💡 Use the prompt function to send your prompt, attach files, add instructions and specify the response format:
generated_joke = ai.prompt(
    [
        "Write the punchline that Michael Scott from Dunder Mifflin would say if he saw this object on someone's desk in their office. Make sure the joke includes a quirky, slightly deprecating derogatory observation.",
        process_photo(object_photo),
    ],
    instructions="Only the punchline, and keep it office-friendly!",
)

rating = af.read_rating(f"Rate this joke's funniness: {generated_joke}", char="🤡")

### 📌 Abstra Workflows is a powerful tool that allows you to store and share data between different stages of your workflow

# 💡 Use the send_task function to send data to be used in the next stages:
send_task(
    "data_collector",
    {
        "best_movie": best_movie,
        "interview_opt_in": interview_opt_in,
        "rating": rating,
    },
)
