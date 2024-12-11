"""
This is calculator page view.
"""
from django.shortcuts import render
from WebsiteCreator.utils import date_utils


# Create your views here.
def calculator_view(request):
    print(request)
    if request.method == "POST":
        print(" method is POST")
        date1_str = request.POST['StartDateInput']
        date2_str = request.POST['EndDateInput']
        print(date1_str)
        print(date2_str)
        # Calculate difference
        util_obj = date_utils()
        response = util_obj.calculate_date_difference(date1_str, date2_str)

        # Display result
        print(f"The difference is {response['years']} years and {response['months']} months.")
        form = {'years': response['years'], 'months': response['months'], 'days': response['days']}

        # form = FileForm(request.POST, request.FILES)
        # if form.is_valid():
        #     uploaded_file = request.FILES['file']
        #     form.save()
        #     # handle_uploaded_file(uploaded_file)
        #     context = {'file_name': uploaded_file.name , "" : ""}
        #     return render(request, 'pages/upload_successful.html', context)
    else:
        print(" method is GET")
        form = {"form": "provide input"}
    # return render(request, "calculator_v1.html", form)
    return render(request, "calculator.html", form)
