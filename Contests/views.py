from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseBadRequest
from .models import Contest, Problem
import markdown
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from datetime import datetime
from django.contrib import messages

# Create your views here.


# -1 means contest doesn't exist, 0 not started 1: started/past
def is_accessible(contest_id):
    try:
        contest = Contest.objects.get(id=contest_id)
        if contest.start_time > timezone.now():
            return 0
        else:
            return 1
    except Contest.DoesNotExist:
        return -1


def contest_detail(request, contest_id):
    is_access = is_accessible(contest_id)
    if is_access == 0:
        messages.error(request, "Contest is not started yet.")
        return redirect("contests")  # Redirect contests/<contest_id> page
    if is_access == -1:
        messages.error(request, "Contest doesn't exist")
        return redirect("contests")  # Redirect contests/<contest_id> page
    contest = get_object_or_404(Contest, id=contest_id)
    problems = contest.problems.all()
    rendered_problems = []
    is_past_contest = contest.is_past_contest
    for problem in problems:
        rendered_problems.append(
            {
                "title": problem.title,
                "id": str(problem.id).split("_")[-1],
                "difficulty": problem.difficulty,
                "tags": problem.tags.all(),
                "solved_by": problem.solved_by,
                "is_past_contest": is_past_contest,
            }
        )
    return render(
        request, "contest.html", {"contest": contest, "problems": rendered_problems}
    )


# contest_id is count of contest i.e {121}, code denotes which problem i.e. {A/C1 etc.} and problem_id is :{121_A/121_C1} unique for each problem
def problem(request, contest_id, code):
    is_access = is_accessible(contest_id)
    if is_access == 0:
        messages.error(request, "Contest is not started yet.")
        return redirect("contests")
    if is_access == -1:
        messages.error(request, "Problem doesn't exist")
        return redirect("contests")
    problem_id = f"{contest_id}_{code}"
    try:
        problem = Problem.objects.get(id=problem_id)
        markdown_content = problem.get_markdown_content()
        html_content = markdown.markdown(
            markdown_content, extensions=["extra", "smarty", "codehilite"]
        )
        return render(
            request, "problem.html", {"problem": problem, "html_content": html_content}
        )
    except Contest.DoesNotExist:
        messages.error(request, "Problem doesn't exist")
        return redirect(f"/contest/{contest_id}")


def contests(request):
    contests = Contest.objects.all()
    past_contests = []
    current_contest = []
    for contest in contests:
        if contest.is_past_contest:
            past_contests.append(
                {
                    "id": contest.id,
                    "name": contest.name,
                    "registrations": contest.registrations,
                    "start_time": contest.start_time,
                    "length": contest.length,
                    "is_past_contest": contest.is_past_contest,
                }
            )
        else:
            if is_accessible(contest.id):
                # contest.is_past_contest = 1
                past_contests.append(
                    {
                        "id": contest.id,
                        "name": contest.name,
                        "registrations": contest.registrations,
                        "start_time": contest.start_time,
                        "length": contest.length,
                        "is_past_contest": contest.is_past_contest,
                    }
                )
            else:
                current_contest.append(
                    {
                        "id": contest.id,
                        "name": contest.name,
                        "registrations": contest.registrations,
                        "start_time": contest.start_time,
                        "length": contest.length,
                        "is_past_contest": contest.is_past_contest,
                    }
                )
    return render(
        request,
        "contests.html",
        {
            "curr_contests": current_contest,
            "past_contests": past_contests,
            "is_timer": 0,
        },
    )


def contests_show(request, contest_id):
    is_access = is_accessible(contest_id)
    if is_access == -1:
        messages.error(request, "Contest doesn't exist")
        return redirect("contests")  # Redirect contests page
    contest = Contest.objects.get(id=contest_id)
    current_contest = []
    current_contest.append(
        {
            "id": contest.id,
            "name": contest.name,
            "registrations": contest.registrations,
            "start_time": contest.start_time,
            "length": contest.length,
            "is_past_contest": contest.is_past_contest,
        }
    )
    return render(
        request,
        "contests.html",
        {"curr_contests": current_contest, "is_timer": 1},
    )


@login_required
def submit_answer(request, contest_id, code):

    if request.method == "POST":
        answer = request.POST.get("answer")
        try:
            answer = float(answer)
            # Validate the answer and update the user's submission
            # ...
            messages.success(request, "Answer submitted successfully!")
            return redirect(f"/contest/{contest_id}/problem/{code}")
        except ValueError:
            messages.error(
                request, "Invalid answer format. Please enter a decimal value."
            )
            return redirect(f"/contest/{contest_id}/problem/{code}")
    return HttpResponseBadRequest()
