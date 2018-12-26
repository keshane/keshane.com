from django.shortcuts import render
from .sudoku import Sudoku
import timeit


def sudoku(request):
    if request.method == "POST":
        sudoku_string = request.POST["sudoku_string"]
        # remove all whitespace
        sudoku_string = "".join(sudoku_string.split())
        data = {"sudoku_initial": request.POST["sudoku_string"]}
        try:
            solver = Sudoku(raw_text=sudoku_string)
            start_time = timeit.default_timer()
            solver.solve()
            end_time = timeit.default_timer()
            data["sudoku_solution"] = str(solver)
            execution_time = end_time - start_time
            execution_time *= 1000 # convert to milliseconds
            data["execution_time"] = str(execution_time)
        except ValueError as ex:
            data["input_errors"] = str(ex)

        return render(request, "projects/sudoku.html", data)
    else:
        return render(request, "projects/sudoku.html")


def projects(request):
    return render(request, "projects/projects.html")

