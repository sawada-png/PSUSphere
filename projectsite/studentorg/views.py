from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Organization, College, Program, Student, OrgMember
from .forms import OrganizationForm, CollegeForm, ProgramForm, StudentForm, OrgMemberForm


class HomePageView(ListView):
    model = Organization
    context_object_name = "home"
    template_name = "home.html"


class OrganizationList(ListView):
    model = Organization
    context_object_name = "organization"
    template_name = "org_list.html"
    paginate_by = 5


class OrganizationCreateView(CreateView):
    model = Organization
    form_class = OrganizationForm
    template_name = "org_form.html"
    success_url = reverse_lazy("organization-list")


class OrganizationUpdateView(UpdateView):
    model = Organization
    form_class = OrganizationForm
    template_name = "org_form.html"
    success_url = reverse_lazy("organization-list")


class OrganizationDeleteView(DeleteView):
    model = Organization
    template_name = "org_del.html"
    success_url = reverse_lazy("organization-list")


class CollegeListView(ListView):
    model = College
    template_name = "college_list.html"


class CollegeCreateView(CreateView):
    model = College
    form_class = CollegeForm
    template_name = "college_form.html"
    success_url = reverse_lazy("college-list")


class CollegeUpdateView(UpdateView):
    model = College
    form_class = CollegeForm
    template_name = "college_form.html"
    success_url = reverse_lazy("college-list")


class CollegeDeleteView(DeleteView):
    model = College
    template_name = "college_del.html"
    success_url = reverse_lazy("college-list")


class ProgramListView(ListView):
    model = Program
    template_name = "program_list.html"


class ProgramCreateView(CreateView):
    model = Program
    form_class = ProgramForm
    template_name = "program_form.html"
    success_url = reverse_lazy("program-list")


class ProgramUpdateView(UpdateView):
    model = Program
    form_class = ProgramForm
    template_name = "program_form.html"
    success_url = reverse_lazy("program-list")


class ProgramDeleteView(DeleteView):
    model = Program
    template_name = "program_del.html"
    success_url = reverse_lazy("program-list")


class StudentListView(ListView):
    model = Student
    template_name = "student_list.html"


class StudentCreateView(CreateView):
    model = Student
    form_class = StudentForm
    template_name = "student_form.html"
    success_url = reverse_lazy("student-list")


class StudentUpdateView(UpdateView):
    model = Student
    form_class = StudentForm
    template_name = "student_form.html"
    success_url = reverse_lazy("student-list")


class StudentDeleteView(DeleteView):
    model = Student
    template_name = "student_del.html"
    success_url = reverse_lazy("student-list")


class OrgMemberListView(ListView):
    model = OrgMember
    template_name = "orgmember_list.html"


class OrgMemberCreateView(CreateView):
    model = OrgMember
    form_class = OrgMemberForm
    template_name = "orgmember_form.html"
    success_url = reverse_lazy("orgmember-list")


class OrgMemberUpdateView(UpdateView):
    model = OrgMember
    form_class = OrgMemberForm
    template_name = "orgmember_form.html"
    success_url = reverse_lazy("orgmember-list")


class OrgMemberDeleteView(DeleteView):
    model = OrgMember
    template_name = "orgmember_del.html"
    success_url = reverse_lazy("orgmember-list")