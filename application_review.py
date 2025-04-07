from abstra.compat import use_legacy_threads

"""
Calling the use_legacy_threads function allows using
the legacy threads in versions > 3.0.0
https://abstra.io/docs/guides/use-legacy-threads/

The new way of using workflows is with tasks. Learn more
at https://abstra.io/docs/concepts/tasks/ and contact us
on any issues during your migration
"""
use_legacy_threads("scripts")

from abstra.messages import send_email
from abstra.tasks import get_trigger_task, send_task

### Abstra Workflows is the easiest way to store and manage data across different parts of your workflow

# You can use the get_trigger_task function to get the task that triggered the script
task = get_trigger_task()
best_movie = task["best_movie"]
interview_opt_in = task["interview_opt_in"]
rating = task["rating"]

reasons = []

if best_movie != "Die Hard" and best_movie != "Threat Level: Midnight":
    reasons.append("Applicant does not have good cinematic taste.")

if not interview_opt_in:
    reasons.append(
        "Applicant refused to engage in a mandatory but voluntary interview with 'Prison Mike'."
    )

if rating != 5:
    reasons.append(
        "Applicant didn't laugh at Michael's joke, making Michael question his sense of humor."
    )

print(reasons)
### Abstra Messages is a built-in notification module that makes automating your processes much easier.

# Use send_email to send emails. All emails in development mode are sent to the editor's email (that's you!).
email = "kauamcm@email.com"  # this is a placeholder

if not reasons:
    send_email(
        email,
        title="Welcome to Dunder Mifflin!",
        message="Welcome to the team! You can now join as Secretary of the Assistant to the Regional Manager. \n\n See you Monday, \n\n Michael Scott - World's Best Boss.",
    )
else:
    reasons_text = "\n".join(reasons)
    print(reasons_text)
    send_email(
        email,
        title="Nope, Sorry!",
        message=f"Your application to work at Dunder Mifflin has been rejected. Here's why:\n {reasons_text} \n\n Sincerely Not Sorry, \n\n Michael Scott - World's Best Boss.",
    )

# Store the application response for future use:
if not reasons:
    send_task("approved", {})
else:
    send_task("rejected", {"reasons": reasons})

task.complete()
