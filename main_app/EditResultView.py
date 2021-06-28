from django.shortcuts import get_object_or_404, render, redirect
from django.views import View
from django.contrib import messages
from .models import Subject, Staff, Student, StudentResult
from .forms import EditResultForm
from django.urls import reverse


class EditResultView(View):
    def get(self, request, *args, **kwargs):
        resultForm = EditResultForm()
        staff = get_object_or_404(Staff, admin=request.user)
        resultForm.fields['subject'].queryset = Subject.objects.filter(staff=staff)
        context = {
            'form': resultForm,
            'page_title': "Edit Student's Result"
        }
        return render(request, "staff_template/edit_student_result.html", context)

    def post(self, request, *args, **kwargs):
        form = EditResultForm(request.POST)
        context = {'form': form, 'page_title': "Edit Student's Result"}
        if form.is_valid():
            try:
                student = form.cleaned_data.get('student')
                subject = form.cleaned_data.get('subject')
                first_test = form.cleaned_data.get('first_test')
                second_test = form.cleaned_data.get('second_test')
                third_test = form.cleaned_data.get('third_test')
                exam = form.cleaned_data.get('exam')
                total = form.cleaned_data.get('total')
                class_average = form.cleaned_data.get('class_average')
                highest_in_class = form.cleaned_data.get('highest_in_class')
                lowest_in_class  = form.cleaned_data.get('lowest_in_class')
                position = form.cleaned_data.get('position')
                grade = form.cleaned_data.get('grade')
                remark = form.cleaned_data.get('remark')
                # Validating
                result = StudentResult.objects.get(student=student, subject=subject)
                result.exam = exam
                result.first_test = first_test
                result.second_test = second_test
                result.third_test = third_test
                result.total = total
                result.class_average = class_average
                result.highest_in_class = highest_in_class
                result.lowest_in_class = lowest_in_class
                result.position = position
                result.grade = grade
                result.total = total
                result.remark = remark
                result.save()
                messages.success(request, "Result Updated")
                return redirect(reverse('edit_student_result'))
            except Exception as e:
                messages.warning(request, "Result Could Not Be Updated")
        else:
            messages.warning(request, "Result Could Not Be Updated")
        return render(request, "staff_template/edit_student_result.html", context)
