from django.shortcuts import render
from .sudoku import Sudoku


def sudoku(request):
    if request.method == "POST":
        sudoku_string = request.POST["sudoku_string"]
        # remove all whitespace
        sudoku_string = "".join(sudoku_string.split())
        data = {"sudoku_initial": request.POST["sudoku_string"]}
        try:
            solver = Sudoku(raw_text=sudoku_string)
            solver.solve()
            data["sudoku_solution"] = str(solver)
        except ValueError as ex:
            data["input_errors"] = str(ex)

        return render(request, "projects/sudoku.html", data)
    else:
        return render(request, "projects/sudoku.html")


def projects(request):
    return render(request, "projects/projects.html")

